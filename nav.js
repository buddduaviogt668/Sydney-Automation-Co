(function(){
    document.querySelectorAll('.nav-dd').forEach(function(dd){
      var trigger = dd.querySelector('.nav-dd-trigger');
      if (!trigger) return;
      trigger.addEventListener('click', function(e){
        e.stopPropagation();
        e.stopImmediatePropagation();
        var isOpen = dd.classList.contains('open');
        document.querySelectorAll('.nav-dd.open').forEach(function(d){d.classList.remove('open');});
        if(!isOpen) dd.classList.add('open');
      }, true);
    });
    document.addEventListener('click', function(){
      document.querySelectorAll('.nav-dd.open').forEach(function(d){d.classList.remove('open');});
    });
    var ham = document.getElementById('hamburger');
    var mob = document.getElementById('mobNav');
    if(ham && mob){
      ham.addEventListener('click', function(e){
        e.stopPropagation();
        ham.classList.toggle('open');
        mob.classList.toggle('open');
      }, true);
      mob.addEventListener('click', function(e){e.stopPropagation();});
      document.addEventListener('click', function(){
        mob.classList.remove('open');
        ham.classList.remove('open');
      });
    }
    var path = window.location.pathname.replace(/\/$/, '') || '/';
    document.querySelectorAll('nav a, .mob-nav a').forEach(function(a){
      var href = a.getAttribute('href');
      if(href === path || (path === '' && href === '/')) a.classList.add('active');
    });
  })();
  