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

// Video controls. State is driven by the media element's own play/pause
// events rather than by the click handler, so the UI cannot drift out of
// sync if playback is stopped by anything other than the button.
(function () {
  document.querySelectorAll('.video-play-hint').forEach(function (btn) {
    var vid = document.getElementById(btn.getAttribute('data-video'));
    if (!vid) return;
    var wrap = vid.closest('.gallery-video');
    var title = btn.getAttribute('data-title') || 'video';
    var bar = wrap ? wrap.querySelector('.video-progress i') : null;

    function paint(playing) {
      if (wrap) wrap.classList.toggle('playing', playing);
      btn.setAttribute('aria-pressed', playing ? 'true' : 'false');
      btn.setAttribute('aria-label', (playing ? 'Pause video: ' : 'Play video: ') + title);
    }

    btn.addEventListener('click', function () {
      if (vid.paused) {
        // Only one clip at a time.
        document.querySelectorAll('.gallery-video video').forEach(function (v) {
          if (v !== vid && !v.paused) v.pause();
        });
        var p = vid.play();
        if (p && p.catch) p.catch(function () { paint(false); });
      } else {
        vid.pause();
      }
    });

    vid.addEventListener('play', function () { paint(true); });
    vid.addEventListener('pause', function () { paint(false); });
    vid.addEventListener('ended', function () { paint(false); });
    vid.addEventListener('timeupdate', function () {
      if (bar && vid.duration) bar.style.width = (vid.currentTime / vid.duration * 100) + '%';
    });
  });

  // Escape stops whatever is playing.
  document.addEventListener('keydown', function (ev) {
    if (ev.key !== 'Escape') return;
    document.querySelectorAll('.gallery-video video').forEach(function (v) {
      if (!v.paused) v.pause();
    });
  });

  // Pause anything scrolled out of view.
  if ('IntersectionObserver' in window) {
    var vo = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting && !en.target.paused) en.target.pause();
      });
    }, { threshold: 0.15 });
    document.querySelectorAll('.gallery-video video').forEach(function (v) { vo.observe(v); });
  }
})();
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

// Booking form: async submit so the customer stays on the page.
(function () {
  var form = document.getElementById('bookingForm');
  if (!form || !form.getAttribute('action')) return;
  var status = document.getElementById('cf-status');
  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var name = form.querySelector('#cf-name');
    var phone = form.querySelector('#cf-phone');
    if (!name.value.trim() || !phone.value.trim()) {
      status.textContent = 'Please add your name and mobile number.';
      status.style.color = '#e8a020';
      return;
    }
    var btn = form.querySelector('button[type=submit]');
    btn.disabled = true;
    status.style.color = '';
    status.textContent = 'Sending...';
    fetch(form.getAttribute('action'), {
      method: 'POST',
      body: new FormData(form),
      headers: { Accept: 'application/json' }
    }).then(function (r) {
      if (!r.ok) throw new Error('bad status');
      form.reset();
      status.style.color = '#e8a020';
      status.textContent = 'Thanks — we have your request and will be in touch shortly.';
    }).catch(function () {
      status.style.color = '#e8a020';
      status.textContent = 'Something went wrong. Please call or text 414-286-1609 instead.';
    }).finally(function () { btn.disabled = false; });
  });
})();
