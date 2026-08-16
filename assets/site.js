// Sudz Up Detailing - shared behaviour
(function () {
  var MOBILE = '(max-width: 980px)';
  var isMobile = function () { return window.matchMedia(MOBILE).matches; };

  var toggle = document.getElementById('navToggle');
  var links  = document.getElementById('navLinks');
  var menus  = [].slice.call(document.querySelectorAll('.has-menu'));

  function closeMenus(except) {
    menus.forEach(function (li) {
      if (li === except) return;
      li.classList.remove('open');
      var b = li.querySelector('.nav-top');
      if (b) b.setAttribute('aria-expanded', 'false');
    });
  }

  function closeNav() {
    if (!links) return;
    links.classList.remove('open');
    if (toggle) toggle.setAttribute('aria-expanded', 'false');
    closeMenus(null);
  }

  if (toggle && links) {
    toggle.addEventListener('click', function (ev) {
      ev.stopPropagation();
      var open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (!open) closeMenus(null);
    });
  }

  // Open state is JS-driven so Escape can always win. CSS hover-opening made
  // that impossible: the pointer resting on the trigger kept the panel up.
  var hoverEnabled = true;

  function setMenu(li, open) {
    li.classList.toggle('open', open);
    var b = li.querySelector('.nav-top');
    if (b) b.setAttribute('aria-expanded', open ? 'true' : 'false');
  }

  menus.forEach(function (li) {
    var btn = li.querySelector('.nav-top');
    if (!btn) return;

    btn.addEventListener('click', function (ev) {
      ev.stopPropagation();
      closeMenus(li);
      if (isMobile()) {
        // Accordion: tapping the same row again collapses it.
        setMenu(li, !li.classList.contains('open'));
      } else {
        // Desktop: pointerenter has usually opened this already, so a click
        // must not toggle it shut. Clicking only ever opens; the pointer
        // leaving (or Escape) closes.
        setMenu(li, true);
      }
    });

    // Desktop pointer behaviour. Guarded so touch taps do not double-fire.
    li.addEventListener('pointerenter', function (ev) {
      if (ev.pointerType === 'touch' || isMobile() || !hoverEnabled) return;
      closeMenus(li);
      setMenu(li, true);
    });
    li.addEventListener('pointerleave', function (ev) {
      if (ev.pointerType === 'touch' || isMobile()) return;
      setMenu(li, false);
      hoverEnabled = true;   // re-arm once the pointer actually leaves
    });
  });

  // Navigating away via any nav link should collapse the panel first.
  if (links) {
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { closeNav(); });
    });
  }

  document.addEventListener('click', function (ev) {
    if (links && links.contains(ev.target)) return;
    if (toggle && toggle.contains(ev.target)) return;
    closeMenus(null);
    if (isMobile()) closeNav();
  });

  document.addEventListener('keydown', function (ev) {
    if (ev.key !== 'Escape') return;
    var openLi = document.querySelector('.has-menu.open');
    closeNav();
    // Suppress hover-reopen until the pointer leaves, otherwise a pointer
    // still resting on the trigger would immediately reopen the panel.
    hoverEnabled = false;
    if (openLi) {
      var b = openLi.querySelector('.nav-top');
      if (b) b.focus();
    } else if (toggle && isMobile()) {
      toggle.focus();
    }
  });

  // Crossing the breakpoint must not strand an open mobile panel on desktop.
  var mq = window.matchMedia(MOBILE);
  var onChange = function () { closeNav(); };
  if (mq.addEventListener) mq.addEventListener('change', onChange);
  else if (mq.addListener) mq.addListener(onChange);

  if ('IntersectionObserver' in window) {
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (en, i) {
        if (en.isIntersecting) {
          setTimeout(function () { en.target.classList.add('visible'); }, i * 70);
          obs.unobserve(en.target);
        }
      });
    }, { threshold: 0.1 });
    document.querySelectorAll('.fade-up').forEach(function (el) { obs.observe(el); });
  } else {
    document.querySelectorAll('.fade-up').forEach(function (el) { el.classList.add('visible'); });
  }

  document.querySelectorAll('.faq-q').forEach(function (btn, i) {
    if (i === 0) {
      btn.closest('.faq-item').classList.add('open');
      btn.setAttribute('aria-expanded', 'true');
    }
    btn.addEventListener('click', function () {
      var item = btn.closest('.faq-item');
      var open = item.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
})();

var lastFocus = null;
function toggleVideo(vidId, wrapId) {
  var vid = document.getElementById(vidId), wrap = document.getElementById(wrapId);
  if (!vid || !wrap) return;
  if (vid.paused) {
    document.querySelectorAll('.gallery-video video').forEach(function (v) {
      if (v !== vid && !v.paused) { v.pause(); v.closest('.gallery-video').classList.remove('playing'); }
    });
    vid.play().catch(function () {});
    wrap.classList.add('playing');
  } else {
    vid.pause();
    wrap.classList.remove('playing');
  }
}
function openLightbox(src, alt) {
  var lb = document.getElementById('lightbox'), im = document.getElementById('lightboxImg');
  if (!lb || !im) return;
  lastFocus = document.activeElement;
  im.src = src;
  im.alt = alt || 'Auto detailing work by Sudz Up Detailing, Hartford WI';
  lb.classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeLightbox(ev) {
  var lb = document.getElementById('lightbox');
  if (!lb) return;
  if (!ev || ev.target === lb || (ev.target.classList && ev.target.classList.contains('lightbox-close'))) {
    lb.classList.remove('open');
    document.getElementById('lightboxImg').src = '';
    document.body.style.overflow = '';
    if (lastFocus) { lastFocus.focus(); lastFocus = null; }
  }
}
document.addEventListener('keydown', function (ev) {
  if (ev.key === 'Escape') closeLightbox({ target: document.getElementById('lightbox') });
});
