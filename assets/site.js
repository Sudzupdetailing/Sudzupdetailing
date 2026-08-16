// Sudz Up Detailing — shared behaviour
(function () {
  var toggle = document.getElementById('navToggle');
  var links = document.getElementById('navLinks');
  if (toggle && links) {
    toggle.addEventListener('click', function () { links.classList.toggle('open'); });
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { links.classList.remove('open'); });
    });
  }

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
