// Sydney Automation Co - Deferred Third-Party Script Loader
// Loads FB Pixel and Microsoft Clarity after page is interactive

window.addEventListener('load', function() {
  // Defer to next idle period if supported, otherwise slight delay
  var load = window.requestIdleCallback
    ? function(fn) { requestIdleCallback(fn, { timeout: 3000 }); }
    : function(fn) { setTimeout(fn, 2000); };

  load(function() {

    // Facebook Pixel
    !function(f,b,e,v,n,t,s){
      if(f.fbq)return;
      n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};
      if(!f._fbq)f._fbq=n;
      n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];
      t=b.createElement(e);t.async=!0;t.src=v;
      s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)
    }(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', '1836885369871029');
    fbq('track', 'PageView');

    // Microsoft Clarity
    (function(c,l,a,r,i,t,y){
      c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window,document,"clarity","script","w5e5flrwbd");

  });
});
