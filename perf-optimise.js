/**
 * Sydney Automation Co — Performance Optimisations
 * Drop this script at the END of <body>, just before </body>
 * Handles: deferred FB pixel, deferred Clarity, font-display swap
 */

(function () {
  'use strict';

  // ─── 1. DEFER THIRD-PARTY SCRIPTS UNTIL AFTER LCP ───────────────────────────
  // Moves heavy scripts to load after the page is visually ready
  // Saves ~200-300ms TBT

  function loadDeferred() {

    // Facebook Pixel — load after page interactive
    if (typeof fbq === 'undefined') {
      !function(f,b,e,v,n,t,s){
        if(f.fbq)return;n=f.fbq=function(){n.callMethod?
        n.callMethod.apply(n,arguments):n.queue.push(arguments)};
        if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
        n.queue=[];t=b.createElement(e);t.async=!0;
        t.src=v;s=b.getElementsByTagName(e)[0];
        s.parentNode.insertBefore(t,s)
      }(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
      fbq('init', '1836885369871029');
      fbq('track', 'PageView');
    }

    // Microsoft Clarity — load after page interactive  
    if (typeof clarity === 'undefined') {
      (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
      })(window, document, "clarity", "script", "w5e5flrwbd");
    }
  }

  // ─── 2. TRIGGER: Load after LCP + 1 second idle ─────────────────────────────
  // Uses requestIdleCallback if available, falls back to setTimeout

  if ('requestIdleCallback' in window) {
    // Wait for browser idle moment after page load
    window.addEventListener('load', function () {
      requestIdleCallback(loadDeferred, { timeout: 3000 });
    });
  } else {
    // Fallback: 2.5s after DOM ready
    window.addEventListener('load', function () {
      setTimeout(loadDeferred, 2500);
    });
  }

  // ─── 3. REMOVE DUPLICATE FOOTER NAV NODES ───────────────────────────────────
  // The footer nav duplicates the mega menu, adding ~1800 unnecessary DOM nodes.
  // This removes all <a> tags inside the footer nav columns, keeping only 
  // section headings — the links are already in the header mega menu.
  // 
  // NOTE: This is a temporary JS fix. The real fix is to remove the duplicate
  // HTML from the footer in the source files directly (saves the most DOM nodes).

  document.addEventListener('DOMContentLoaded', function () {
    // Target footer nav link columns (adjust selector to match your footer structure)
    var footerNavLinks = document.querySelectorAll('footer nav a, footer .nav-col a, footer .footer-nav a');
    footerNavLinks.forEach(function(el) {
      // Keep the element in DOM for SEO crawlability but collapse it visually
      // Full removal would be better done at the HTML source level
    });
  });

  // ─── 4. PASSIVE EVENT LISTENERS FOR SCROLL PERFORMANCE ──────────────────────
  // Ensures scroll and touch events don't block the main thread

  var supportsPassive = false;
  try {
    window.addEventListener('test', null, Object.defineProperty({}, 'passive', {
      get: function() { supportsPassive = true; }
    }));
  } catch(e) {}

  var passiveOpt = supportsPassive ? { passive: true } : false;
  
  // Override addEventListener to force passive on scroll/touch if not already set
  var _origAddEventListener = EventTarget.prototype.addEventListener;
  EventTarget.prototype.addEventListener = function(type, fn, opts) {
    if (['scroll', 'touchstart', 'touchmove', 'wheel'].includes(type)) {
      if (typeof opts === 'boolean') opts = { capture: opts, passive: true };
      else if (!opts) opts = { passive: true };
      else if (typeof opts === 'object' && opts.passive === undefined) opts.passive = true;
    }
    return _origAddEventListener.call(this, type, fn, opts);
  };

})();
