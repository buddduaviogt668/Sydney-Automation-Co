(function () {
  'use strict';
  if (window.__sacLeadCaptureLoaded) return;
  window.__sacLeadCaptureLoaded = true;

  var css = document.createElement('style');
  css.textContent = `
    #sac-lead-trigger{display:inline-flex;align-items:center;justify-content:center;background:#f07020;color:#fff;border:0;border-radius:8px;padding:13px 18px;font:800 15px 'Barlow',sans-serif;box-shadow:0 6px 16px rgba(0,0,0,.2);cursor:pointer;transition:transform .2s,background .2s;margin:10px 8px 0 0;vertical-align:middle}
    #sac-lead-trigger:hover{background:#ff8533;transform:translateY(-1px)}
    #sac-lead-backdrop{position:fixed;inset:0;background:rgba(4,15,35,.68);z-index:1000;display:none}
    #sac-lead-backdrop.open{display:block}
    #sac-lead-panel{position:fixed;right:0;top:0;height:100%;width:min(470px,100%);background:#0e1f3d;color:#f0f4ff;z-index:1001;transform:translateX(100%);transition:transform .25s ease;overflow:auto;padding:28px 24px 40px;box-shadow:-12px 0 36px rgba(0,0,0,.3);font-family:'Barlow',sans-serif}
    #sac-lead-backdrop.open #sac-lead-panel{transform:translateX(0)}
    .sac-lead-close{float:right;background:transparent;border:0;color:#a8c0e0;font-size:30px;line-height:1;cursor:pointer}
    .sac-lead-kicker{display:inline-block;color:#f07020;font-weight:800;letter-spacing:1px;text-transform:uppercase;font-size:12px;margin:8px 0 8px}
    #sac-lead-panel h2{font:800 32px 'Barlow Condensed',sans-serif;margin:0 42px 10px 0;color:#fff}
    #sac-lead-panel p{color:#a8c0e0;line-height:1.6;margin:0 0 18px}
    .sac-lead-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
    .sac-lead-field{margin-bottom:12px}
    .sac-lead-field.full{grid-column:1/-1}
    .sac-lead-field label{display:block;color:#a8c0e0;font-size:13px;font-weight:700;margin-bottom:6px}
    .sac-lead-field input,.sac-lead-field select,.sac-lead-field textarea{box-sizing:border-box;width:100%;background:#132647;color:#f0f4ff;border:1px solid #2a4a80;border-radius:8px;padding:12px;font:15px 'Barlow',sans-serif}
    .sac-lead-field textarea{min-height:92px;resize:vertical}
    .sac-lead-actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:8px}
    .sac-lead-submit{background:#f07020;color:#fff;border:0;border-radius:8px;padding:13px 18px;font-weight:800;cursor:pointer}
    .sac-lead-alt{display:inline-flex;align-items:center;color:#f0f4ff;border:1px solid #2a4a80;border-radius:8px;padding:12px 15px;text-decoration:none;font-weight:700}
    .sac-lead-note{font-size:12px!important;margin-top:14px!important;color:#8fa8cb!important}
    .sac-lead-success{background:#132647;border:1px solid #2a4a80;border-radius:10px;padding:18px;margin-top:16px}
    @media(max-width:600px){#sac-lead-trigger{font-size:14px;padding:12px 15px}.sac-lead-grid{grid-template-columns:1fr}.sac-lead-field.full{grid-column:auto}#sac-lead-panel{padding:22px 18px 34px}}
  `;
  document.head.appendChild(css);

  function esc(value) {
    return String(value || '').replace(/[&<>"']/g, function (c) {
      return ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'})[c];
    });
  }

  var wrapper = document.createElement('div');
  wrapper.innerHTML = `
    <button id="sac-lead-trigger" type="button">Get a project plan</button>
    <div id="sac-lead-backdrop" role="presentation">
      <aside id="sac-lead-panel" role="dialog" aria-modal="true" aria-labelledby="sac-lead-title">
        <button class="sac-lead-close" type="button" aria-label="Close enquiry form">×</button>
        <span class="sac-lead-kicker">Sydney Automation Co.</span>
        <h2 id="sac-lead-title">Tell us what you need</h2>
        <p>Give us the platform, location and project type. We will direct you to the fastest useful next step.</p>
        <form id="sac-lead-form">
          <div class="sac-lead-grid">
            <div class="sac-lead-field"><label for="sac-lead-name">Name</label><input id="sac-lead-name" name="name" autocomplete="name" required></div>
            <div class="sac-lead-field"><label for="sac-lead-phone">Phone</label><input id="sac-lead-phone" name="phone" type="tel" autocomplete="tel" required></div>
            <div class="sac-lead-field"><label for="sac-lead-email">Email</label><input id="sac-lead-email" name="email" type="email" autocomplete="email" required></div>
            <div class="sac-lead-field"><label for="sac-lead-location">Suburb / state</label><input id="sac-lead-location" name="location" autocomplete="address-level2" placeholder="e.g. Brisbane, Menai"></div>
            <div class="sac-lead-field full"><label for="sac-lead-service">What do you need?</label><select id="sac-lead-service" name="service"><option value="">Choose one</option><option>Urgent C-Bus fault</option><option>Dynalite fault or programming</option><option>National remote programming</option><option>DALI / RAPIX / emergency lighting</option><option>Car-park or commercial lighting</option><option>Strata or facilities maintenance</option><option>Smart Home Package</option><option>Other project</option></select></div>
            <div class="sac-lead-field full"><label for="sac-lead-message">Briefly describe the issue or project</label><textarea id="sac-lead-message" name="message" placeholder="What is happening, what platform is involved and what outcome do you need?"></textarea></div>
          </div>
          <div class="sac-lead-actions"><button class="sac-lead-submit" type="submit">Send project details</button><a class="sac-lead-alt" href="tel:+61422469739">Call 0422 469 739</a></div>
          <p class="sac-lead-note">Your details are used to respond to this enquiry. Urgent Sydney faults are best handled by phone.</p>
          <div id="sac-lead-result" aria-live="polite"></div>
        </form>
      </aside>
    </div>`;
  document.body.appendChild(wrapper);

  var trigger = document.getElementById('sac-lead-trigger');
  var naturalTarget = document.querySelector('main a[href^="tel:"], .cta-band a[href^="tel:"], main a[href="/contact"], footer a[href="/contact"]');
  if (naturalTarget && naturalTarget.parentNode) {
    trigger.textContent = 'Send project details';
    trigger.setAttribute('aria-label', 'Send project details');
    naturalTarget.insertAdjacentElement('afterend', trigger);
  } else {
    trigger.remove();
  }
  var backdrop = document.getElementById('sac-lead-backdrop');
  var close = backdrop.querySelector('.sac-lead-close');
  var form = document.getElementById('sac-lead-form');
  var result = document.getElementById('sac-lead-result');
  var storageKey = 'sacLeadDraftV1';

  function track(name, params) {
    if (typeof window.gtag === 'function') window.gtag('event', name, params || {});
  }
  function openLead(source) {
    backdrop.classList.add('open');
    trigger.setAttribute('aria-expanded','true');
    track('lead_drawer_open', {source: source || 'floating_cta', page_location: location.pathname});
    var first = document.getElementById('sac-lead-name');
    if (first) setTimeout(function(){ first.focus(); }, 40);
  }
  function closeLead() {
    backdrop.classList.remove('open');
    trigger.setAttribute('aria-expanded','false');
  }
  function saveDraft() {
    var data = {};
    Array.prototype.forEach.call(form.elements, function (el) { if (el.name) data[el.name] = el.value; });
    try { localStorage.setItem(storageKey, JSON.stringify(data)); } catch(e) {}
  }
  function restoreDraft() {
    try {
      var data = JSON.parse(localStorage.getItem(storageKey) || '{}');
      Object.keys(data).forEach(function (key) { var el = form.elements[key]; if (el) el.value = data[key]; });
    } catch(e) {}
  }
  trigger.addEventListener('click', function(){ openLead('floating_cta'); });
  close.addEventListener('click', closeLead);
  backdrop.addEventListener('click', function(e){ if (e.target === backdrop) closeLead(); });
  document.addEventListener('keydown', function(e){ if (e.key === 'Escape') closeLead(); });
  Array.prototype.forEach.call(form.elements, function (el) { el.addEventListener('input', saveDraft); });
  restoreDraft();
  form.addEventListener('submit', function(e){
    e.preventDefault();
    var data = {};
    Array.prototype.forEach.call(form.elements, function (el) { if (el.name) data[el.name] = el.value.trim(); });
    var subject = 'SAC project enquiry — ' + (data.service || 'New enquiry');
    var body = ['Name: '+data.name,'Phone: '+data.phone,'Email: '+data.email,'Location: '+data.location,'Service: '+data.service,'Details: '+data.message,'Page: '+location.href].join('\n');
    track('generate_lead', {event_category:'lead_drawer', event_label:data.service || 'general', page_location:location.pathname});
    try { localStorage.removeItem(storageKey); } catch(err) {}
    result.innerHTML = '<div class="sac-lead-success"><strong>Details prepared.</strong><br>We are opening your email app with the project information. If it does not open, call 0422 469 739 or email service@sydneyautomationco.com.au.</div>';
    window.location.href = 'mailto:service@sydneyautomationco.com.au?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
  });
})();
