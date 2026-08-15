const buckets = new Map();

const PATH_LABELS = {
  urgent: 'Urgent Sydney C-Bus or Dynalite fault',
  remote: 'National remote programming or commissioning',
  commercial: 'Commercial DALI, RAPIX or emergency lighting',
  facilities: 'Car-park, strata or facilities lighting',
  smart_home: 'Premium Smart Home Package',
};

function clean(value, max = 2000) {
  return String(value || '').replace(/[<>]/g, '').trim().slice(0, max);
}

function json(res, status, payload) {
  res.status(status).setHeader('Content-Type', 'application/json; charset=utf-8').end(JSON.stringify(payload));
}

function allowedOrigin(req) {
  const origin = req.headers.origin;
  const host = req.headers.host || '';
  if (!origin) return true;
  try {
    const url = new URL(origin);
    return url.hostname === host.split(':')[0] || url.hostname.endsWith('.vercel.app') || url.hostname === 'localhost' || url.hostname === '127.0.0.1';
  } catch (error) {
    return false;
  }
}

module.exports = async function handler(req, res) {
  if (req.method === 'OPTIONS') return res.status(204).end();
  if (req.method !== 'POST') return json(res, 405, { ok: false, error: 'method_not_allowed' });
  if (!allowedOrigin(req)) return json(res, 403, { ok: false, error: 'origin_not_allowed' });

  const ip = String(req.headers['x-forwarded-for'] || req.socket?.remoteAddress || 'unknown').split(',')[0].trim();
  const now = Date.now();
  const recent = (buckets.get(ip) || []).filter((time) => now - time < 10 * 60 * 1000);
  if (recent.length >= 5) return json(res, 429, { ok: false, error: 'rate_limited' });
  recent.push(now);
  buckets.set(ip, recent);

  const body = req.body || {};
  if (clean(body.website, 200)) return json(res, 200, { ok: true, id: 'accepted' });

  const path = clean(body.path, 40);
  const name = clean(body.name, 120);
  const phone = clean(body.phone, 80);
  const email = clean(body.email, 160);
  const location = clean(body.location, 160);
  const message = clean(body.message, 3000);
  const sourcePage = clean(body.sourcePage, 500);
  const contactPreference = clean(body.contactPreference, 40);

  if (!PATH_LABELS[path] || !name || (!phone && !email)) {
    return json(res, 400, { ok: false, error: 'missing_required_details' });
  }
  if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return json(res, 400, { ok: false, error: 'invalid_email' });
  }

  const apiKey = process.env.RESEND_API_KEY;
  const from = process.env.LEAD_FROM_EMAIL;
  const to = process.env.LEAD_TO_EMAIL || 'service@sydneyautomationco.com.au';
  const subject = `SAC lead — ${PATH_LABELS[path]} — ${name}`;
  const text = [
    'New Sydney Automation Co. website enquiry',
    '',
    `Lead path: ${PATH_LABELS[path]}`,
    `Name: ${name}`,
    `Phone: ${phone || 'Not supplied'}`,
    `Email: ${email || 'Not supplied'}`,
    `Location: ${location || 'Not supplied'}`,
    `Preferred contact: ${contactPreference || 'Not supplied'}`,
    `Details: ${message || 'Not supplied'}`,
    `Source page: ${sourcePage || 'Not supplied'}`,
    `Received: ${new Date().toISOString()}`,
  ].join('\\n');

  try {
    const jobSystemUrl = process.env.JOB_SYSTEM_URL;
    const jobSystemToken = process.env.JOB_SYSTEM_INGEST_TOKEN;
    if (jobSystemUrl && jobSystemToken) {
      const jobResponse = await fetch(`${jobSystemUrl.replace(/\/$/, '')}/api/leads`, {
        method: 'POST',
        headers: { Authorization: `Bearer ${jobSystemToken}`, 'Content-Type': 'application/json' },
        body: JSON.stringify({ path, name, phone, email, location, contactPreference, message, sourcePage, submissionId: clean(body.submissionId, 120) }),
      });
      const jobResult = await jobResponse.json().catch(() => ({}));
      if (jobResponse.ok && jobResult.ok) return json(res, 200, { ok: true, id: jobResult.id, provider: 'job-system' });
      console.error('Job-system lead delivery failed', jobResponse.status, jobResult);
    }

    if (apiKey && from) {
      const response = await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: { Authorization: `Bearer ${apiKey}`, 'Content-Type': 'application/json' },
        body: JSON.stringify({ from, to: [to], reply_to: email || undefined, subject, text }),
      });
      const result = await response.json().catch(() => ({}));
      if (!response.ok) {
        console.error('Resend lead delivery failed', response.status, result);
        return json(res, 502, { ok: false, error: 'lead_delivery_failed' });
      }
      return json(res, 200, { ok: true, id: result.id || 'accepted', provider: 'resend' });
    }

    const formSubmit = await fetch(`https://formsubmit.co/ajax/${encodeURIComponent(to)}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify({
        name,
        phone,
        email,
        location,
        path: PATH_LABELS[path],
        contactPreference,
        message,
        sourcePage,
        _subject: subject,
        _template: 'table',
        _honey: clean(body.website, 200),
      }),
    });
    const formResult = await formSubmit.json().catch(() => ({}));
    if (!formSubmit.ok || formResult.success === false) {
      console.error('FormSubmit lead delivery failed', formSubmit.status, formResult);
      return json(res, 502, { ok: false, error: 'lead_delivery_failed' });
    }
    return json(res, 200, { ok: true, id: 'accepted', provider: 'formsubmit' });
  } catch (error) {
    console.error('Lead delivery exception', error);
    return json(res, 502, { ok: false, error: 'lead_delivery_failed' });
  }
};
