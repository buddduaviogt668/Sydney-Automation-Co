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
    #sac-lead-panel{position:fixed;right:0;top:0;height:100%;width:min(500px,100%);background:#0e1f3d;color:#f0f4ff;z-index:1001;transform:translateX(100%);transition:transform .25s ease;overflow:auto;padding:28px 24px 40px;box-shadow:-12px 0 36px rgba(0,0,0,.3);font-family:'Barlow',sans-serif}
    #sac-lead-backdrop.open #sac-lead-panel{transform:translateX(0)}
    .sac-lead-close{float:right;background:transparent;border:0;color:#a8c0e0;font-size:30px;line-height:1;cursor:pointer}
    .sac-lead-kicker{display:inline-block;color:#f07020;font-weight:800;letter-spacing:1px;text-transform:uppercase;font-size:12px;margin:8px 0 8px}
    #sac-lead-panel h2{font:800 32px 'Barlow Condensed',sans-serif;margin:0 42px 10px 0;color:#fff}
    #sac-lead-panel p{color:#a8c0e0;line-height:1.6;margin:0 0 18px}
    .sac-lead-step{display:none}.sac-lead-step.active{display:block}
    .sac-path-grid{display:grid;gap:10px;margin:18px 0}
    .sac-path{display:flex;align-items:center;text-align:left;width:100%;background:#132647;color:#fff;border:1px solid #2a4a80;border-radius:10px;padding:15px;cursor:pointer;transition:border-color .18s,background .18s,transform .18s}
    .sac-path:hover{background:#18345f;border-color:#f07020;transform:translateY(-1px)}
    .sac-path strong{display:block;font:800 18px 'Barlow Condensed',sans-serif;margin-bottom:3px}.sac-path span{display:block;color:#a8c0e0;font-size:13px;line-height:1.35}
    .sac-path-icon{width:34px;height:34px;border-radius:50%;background:#f07020;color:#fff;display:inline-flex;align-items:center;justify-content:center;font-weight:900;margin-right:12px;flex:0 0 auto}
    .sac-lead-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
    .sac-lead-field{margin-bottom:12px}.sac-lead-field.full{grid-column:1/-1}
    .sac-lead-field label{display:block;color:#a8c0e0;font-size:13px;font-weight:700;margin-bottom:6px}
    .sac-lead-field input,.sac-lead-field select,.sac-lead-field textarea{box-sizing:border-box;width:100%;background:#132647;color:#f0f4ff;border:1px solid #2a4a80;border-radius:8px;padding:12px;font:15px 'Barlow',sans-serif}
    .sac-lead-field textarea{min-height:92px;resize:vertical}
    .sac-lead-actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:8px}.sac-lead-submit{background:#f07020;color:#fff;border:0;border-radius:8px;padding:13px 18px;font-weight:800;cursor:pointer}.sac-lead-submit[disabled]{opacity:.6;cursor:wait}
    .sac-lead-alt{display:inline-flex;align-items:center;color:#f0f4ff;border:1px solid #2a4a80;border-radius:8px;padding:12px 15px;text-decoration:none;font-weight:700}
    .sac-lead-back{background:none;border:0;color:#a8c0e0;text-decoration:underline;padding:0;cursor:pointer;font:600 14px 'Barlow',sans-serif;margin-bottom:16px}
    .sac-lead-note{font-size:12px!important;margin-top:14px!important;color:#8fa8cb!important}.sac-lead-success{background:#132647;border:1px solid #2a4a80;border-radius:10px;padding:18px;margin-top:16px}.sac-lead-error{color:#ffbf9d!important;background:rgba(240,112,32,.12);border:1px solid rgba(240,112,32,.35);border-radius:8px;padding:12px;margin-top:12px;font-size:14px!important}
    .sac-lead-honeypot{position:absolute;left:-10000px;width:1px;height:1px;overflow:hidden}
    @media(max-width:600px){#sac-lead-trigger{font-size:14px;padding:12px 15px}.sac-lead-grid{grid-template-columns:1fr}.sac-lead-field.full{grid-column:auto}#sac-lead-panel{padding:22px 18px 34px}}
  `;
  document.head.appendChild(css);

  var wrapper = document.createElement('div');
  wrapper.innerHTML = `
    <button id="sac-lead-trigger" type="button" aria-haspopup="dialog">Send project details</button>
    <div id="sac-lead-backdrop" role="presentation">
      <aside id="sac-lead-panel" role="dialog" aria-modal="true" aria-labelledby="sac-lead-title">
        <button class="sac-lead-close" type="button" aria-label="Close enquiry form">×</button>
        <span class="sac-lead-kicker">Sydney Automation Co.</span>
        <h2 id="sac-lead-title">What do you need help with?</h2>
        <p id="sac-lead-intro">Choose the closest path and we’ll ask only for the details needed to direct you to the fastest useful next step.</p>
        <div id="sac-lead-choice" class="sac-lead-step active">
          <div class="sac-path-grid">
            <button class="sac-path" type="button" data-path="urgent"><span class="sac-path-icon">!</span><span><strong>Urgent Sydney fault</strong><span>C-Bus or Dynalite not working in Greater Sydney.</span></span></button>
            <button class="sac-path" type="button" data-path="remote"><span class="sac-path-icon">↗</span><span><strong>National remote programming</strong><span>Programming, commissioning or diagnosis from interstate.</span></span></button>
            <button class="sac-path" type="button" data-path="commercial"><span class="sac-path-icon">▦</span><span><strong>Commercial lighting project</strong><span>DALI, RAPIX, emergency lighting or controls.</span></span></button>
            <button class="sac-path" type="button" data-path="facilities"><span class="sac-path-icon">⌂</span><span><strong>Car-park, strata or maintenance</strong><span>Repairs, upgrades, assessments or service contracts.</span></span></button>
            <button class="sac-path" type="button" data-path="smart_home"><span class="sac-path-icon">⌘</span><span><strong>Premium Smart Home Package</strong><span>C-Bus or Dynalite planning for a new or existing home.</span></span></button>
          </div>
          <p class="sac-lead-note">Urgent faults are best handled by phone: <a href="tel:+61422469739" style="color:#fff;font-weight:800">0422 469 739</a>.</p>
        </div>
        <div id="sac-lead-form-step" class="sac-lead-step">
          <button id="sac-lead-back" class="sac-lead-back" type="button">← Choose a different path</button>
          <p id="sac-lead-path-summary" style="color:#fff;font-weight:700"></p>
          <form id="sac-lead-form">
            <input type="text" name="website" class="sac-lead-honeypot" tabindex="-1" autocomplete="off">
            <input type="hidden" name="path" id="sac-lead-path">
            <div class="sac-lead-grid">
              <div class="sac-lead-field"><label for="sac-lead-name">Name</label><input id="sac-lead-name" name="name" autocomplete="name" required></div>
              <div class="sac-lead-field"><label for="sac-lead-phone">Phone</label><input id="sac-lead-phone" name="phone" type="tel" autocomplete="tel"></div>
              <div class="sac-lead-field"><label for="sac-lead-email">Email</label><input id="sac-lead-email" name="email" type="email" autocomplete="email"></div>
              <div class="sac-lead-field"><label for="sac-lead-location">Suburb / state</label><input id="sac-lead-location" name="location" autocomplete="address-level2" placeholder="e.g. Brisbane, Menai"></div>
              <div class="sac-lead-field full"><label for="sac-lead-system">System or platform</label><select id="sac-lead-system" name="system"><option value="">Choose if known</option><option>Clipsal C-Bus</option><option>Signify Dynalite</option><option>RAPIX / DALI</option><option>KNX</option><option>BMS / building management</option><option>Industrial / PLC</option><option>Not sure</option></select></div>
              <div class="sac-lead-field"><label for="sac-lead-urgency">Timing</label><select id="sac-lead-urgency" name="urgency"><option value="">When do you need help?</option><option>System currently down</option><option>This week</option><option>Planning / quote</option><option>Not sure</option></select></div>
              <div class="sac-lead-field"><label for="sac-lead-contact">Preferred contact</label><select id="sac-lead-contact" name="contactPreference"><option value="">Choose one</option><option>Phone call</option><option>Email</option><option>Either</option></select></div>
              <div class="sac-lead-field full"><label for="sac-lead-message">Briefly describe the issue or project</label><textarea id="sac-lead-message" name="message" placeholder="What is happening, what platform is involved and what outcome do you need?"></textarea></div>
            </div>
            <div class="sac-lead-actions"><button class="sac-lead-submit" type="submit">Request next step</button><a class="sac-lead-alt" href="tel:+61422469739">Call 0422 469 739</a></div>
            <p class="sac-lead-note">Your details are sent securely to Sydney Automation Co. and used only to respond to this enquiry. Urgent Sydney faults are best handled by phone.</p>
            <div id="sac-lead-result" aria-live="polite"></div>
          </form>
        </div>
      </aside>
    </div>`;
  document.body.appendChild(wrapper);

  var trigger = document.getElementById('sac-lead-trigger');
  var naturalTarget = document.querySelector('main a[href^="tel:"], .cta-band a[href^="tel:"], main a[href="/contact"], footer a[href="/contact"]');
  if (naturalTarget && naturalTarget.parentNode) {
    naturalTarget.insertAdjacentElement('afterend', trigger);
  } else {
    trigger.remove();
  }
  var backdrop = document.getElementById('sac-lead-backdrop');
  var close = backdrop.querySelector('.sac-lead-close');
  var choice = document.getElementById('sac-lead-choice');
  var formStep = document.getElementById('sac-lead-form-step');
  var form = document.getElementById('sac-lead-form');
  var result = document.getElementById('sac-lead-result');
  var title = document.getElementById('sac-lead-title');
  var intro = document.getElementById('sac-lead-intro');
  var summary = document.getElementById('sac-lead-path-summary');
  var pathField = document.getElementById('sac-lead-path');
  var storageKey = 'sacLeadDraftV2';
  var submissionKey = 'sacLeadSubmissionV1';
  var pathLabels = {
    urgent: 'Urgent Sydney C-Bus or Dynalite fault',
    remote: 'National remote programming or commissioning',
    commercial: 'Commercial DALI, RAPIX or emergency lighting',
    facilities: 'Car-park, strata or facilities lighting',
    smart_home: 'Premium Smart Home Package'
  };

  function track(name, params) { if (typeof window.gtag === 'function') window.gtag('event', name, params || {}); }
  function openLead(source) { backdrop.classList.add('open'); trigger.setAttribute('aria-expanded', 'true'); track('lead_drawer_open', {source: source || 'contextual_cta', page_location: location.pathname}); setTimeout(function(){ (choice.querySelector('.sac-path') || document.getElementById('sac-lead-name')).focus(); }, 40); }
  function closeLead() { backdrop.classList.remove('open'); trigger.setAttribute('aria-expanded', 'false'); }
  function saveDraft() { var data = {}; Array.prototype.forEach.call(form.elements, function(el){ if(el.name) data[el.name] = el.value; }); try { localStorage.setItem(storageKey, JSON.stringify(data)); } catch(e) {} }
  function restoreDraft() { try { var data = JSON.parse(localStorage.getItem(storageKey) || '{}'); Object.keys(data).forEach(function(key){ var el = form.elements[key]; if(el) el.value = data[key]; }); if(data.path && pathLabels[data.path]) showForm(data.path, true); } catch(e) {} }
  function showForm(path, restored) { pathField.value = path; summary.textContent = pathLabels[path]; choice.classList.remove('active'); formStep.classList.add('active'); title.textContent = path === 'urgent' ? 'Tell us about the fault' : 'Tell us about the project'; intro.textContent = path === 'urgent' ? 'Give us the essentials and call George if the system is currently down.' : 'A few useful details will help us direct your enquiry to the right next step.'; track('lead_path_selected', {lead_path:path, page_location:location.pathname, restored:!!restored}); setTimeout(function(){ document.getElementById('sac-lead-name').focus(); }, 40); }
  trigger.addEventListener('click', function(){ openLead('contextual_cta'); });
  close.addEventListener('click', closeLead);
  backdrop.addEventListener('click', function(e){ if(e.target === backdrop) closeLead(); });
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape') closeLead(); });
  Array.prototype.forEach.call(form.elements, function(el){ el.addEventListener('input', function(){ saveDraft(); if(el.name && el.value) track('lead_field_completed', {field:el.name, lead_path:pathField.value || 'unselected'}); }); });
  Array.prototype.forEach.call(choice.querySelectorAll('[data-path]'), function(button){ button.addEventListener('click', function(){ showForm(button.getAttribute('data-path'), false); }); });
  document.getElementById('sac-lead-back').addEventListener('click', function(){ formStep.classList.remove('active'); choice.classList.add('active'); title.textContent = 'What do you need help with?'; intro.textContent = 'Choose the closest path and we’ll ask only for the details needed to direct you to the fastest useful next step.'; });
  restoreDraft();
  form.addEventListener('submit', async function(e){
    e.preventDefault();
    var submit = form.querySelector('.sac-lead-submit');
    var data = {};
    Array.prototype.forEach.call(form.elements, function(el){ if(el.name) data[el.name] = el.value.trim(); });
    if(!data.phone && !data.email){ result.innerHTML = '<p class="sac-lead-error">Please provide a phone number or email so George can respond.</p>'; return; }
    submit.disabled = true; submit.textContent = 'Sending securely…'; result.innerHTML = ''; track('lead_form_started', {lead_path:data.path, page_location:location.pathname});
    try {
      var submissionId = (window.crypto && crypto.randomUUID) ? crypto.randomUUID() : String(Date.now()) + Math.random().toString(36).slice(2);
      var response = await fetch('/api/leads', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(Object.assign(data, {sourcePage: location.href, submissionId: submissionId}))});
      var payload = await response.json().catch(function(){ return {}; });
      if(!response.ok || !payload.ok) throw new Error(payload.error || 'submission_failed');
      try { localStorage.removeItem(storageKey); } catch(err) {}
      track('generate_lead', {lead_path:data.path, event_label:pathLabels[data.path] || data.path, page_location:location.pathname});
      result.innerHTML = '<div class="sac-lead-success"><strong>Details received.</strong><br>George will review your enquiry and respond with the most useful next step. If the matter is urgent, call <a href="tel:+61422469739" style="color:#fff;font-weight:800">0422 469 739</a>.</div>';
      form.reset(); pathField.value = data.path;
      submit.textContent = 'Sent';
    } catch(error) {
      track('lead_form_error', {lead_path:data.path, error:String(error.message || error), page_location:location.pathname});
      result.innerHTML = '<p class="sac-lead-error">We could not send the details just now. Please call <a href="tel:+61422469739" style="color:#fff;font-weight:800">0422 469 739</a> or email <a href="mailto:service@sydneyautomationco.com.au" style="color:#fff;font-weight:800">service@sydneyautomationco.com.au</a>.</p>';
      submit.disabled = false; submit.textContent = 'Try again';
    }
  });
})();
