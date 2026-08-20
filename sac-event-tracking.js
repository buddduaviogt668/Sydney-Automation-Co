(function () {
  'use strict';
  if (window.__sacEventTrackingLoaded) return;
  window.__sacEventTrackingLoaded = true;

  function sendEvent(name, params) {
    if (typeof window.gtag !== 'function') return;
    window.gtag('event', name, Object.assign({
      page_path: window.location.pathname,
      page_title: document.title,
      page_location: window.location.href
    }, params || {}));
  }

  function textOf(element) {
    return (element.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 120);
  }

  function classifyLink(link) {
    var href = (link.getAttribute('href') || '').toLowerCase();
    var label = textOf(link).toLowerCase();

    if (href.indexOf('tel:') === 0) return { name: 'phone_click', type: 'phone' };
    if (href.indexOf('mailto:') === 0) return { name: 'email_click', type: 'email' };
    if (href.indexOf('wa.me') !== -1 || href.indexOf('whatsapp') !== -1) return { name: 'whatsapp_click', type: 'whatsapp' };
    if (href === '/book-service' || label.indexOf('book') !== -1 || label.indexOf('technician') !== -1) return { name: 'booking_click', type: 'booking' };
    if (href === '/contact' || label.indexOf('quote') !== -1 || label.indexOf('enquir') !== -1 || label.indexOf('assessment') !== -1 || label.indexOf('project details') !== -1) return { name: 'quote_click', type: 'quote' };
    return null;
  }

  document.addEventListener('click', function (event) {
    var link = event.target.closest ? event.target.closest('a') : null;
    if (!link) return;
    var classified = classifyLink(link);
    if (!classified) return;
    sendEvent(classified.name, {
      cta_type: classified.type,
      cta_text: textOf(link),
      destination: link.getAttribute('href') || ''
    });
  }, true);

  document.addEventListener('submit', function (event) {
    var form = event.target;
    if (!form || form.tagName !== 'FORM') return;
    sendEvent('form_submit', {
      form_id: form.id || 'unidentified_form',
      form_action: form.getAttribute('action') || window.location.pathname
    });
  }, true);
})();
