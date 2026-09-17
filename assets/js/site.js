/* Pulso Studios - site behaviour (vanilla, no dependencies) */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasIO = 'IntersectionObserver' in window;

  /* ── About text: wrap words so they can light up while reading ── */
  var about = document.querySelector('.about-text');
  if (about && !reduce) {
    var words = about.textContent.trim().split(/\s+/);
    about.textContent = '';
    words.forEach(function (word, i) {
      var span = document.createElement('span');
      span.className = 'w';
      span.style.setProperty('--w', i);
      span.textContent = word;
      about.appendChild(span);
      about.appendChild(document.createTextNode(' '));
    });
  }

  /* ── Scroll reveals ── */
  var targets = document.querySelectorAll('[data-reveal], [data-wipe], .about-text');
  if (hasIO && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        io.unobserve(entry.target);
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -8% 0px' });
    targets.forEach(function (el) { io.observe(el); });
  } else {
    targets.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ── Nav: mark the section in view ── */
  var navLinks = document.querySelectorAll('.nav-section a');
  if (hasIO && navLinks.length) {
    var byId = {};
    navLinks.forEach(function (a) { byId[a.getAttribute('href').split('#')[1]] = a; });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var link = byId[entry.target.id];
        if (!link) return;
        if (entry.isIntersecting) {
          navLinks.forEach(function (a) { a.removeAttribute('aria-current'); });
          link.setAttribute('aria-current', 'true');
        } else {
          link.removeAttribute('aria-current');
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    Object.keys(byId).forEach(function (id) {
      var section = document.getElementById(id);
      if (section) spy.observe(section);
    });
  }

  /* ── Hero: the pulse leans toward the pointer (desktop only) ── */
  var hero = document.getElementById('hero');
  var pulse = document.querySelector('.pulse');
  if (hero && pulse && !reduce && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    var frame = 0;
    hero.addEventListener('pointermove', function (e) {
      if (frame) return;
      frame = requestAnimationFrame(function () {
        frame = 0;
        var r = hero.getBoundingClientRect();
        pulse.style.setProperty('--px', ((e.clientX - r.left) / r.width - 0.5) * 48 + 'px');
        pulse.style.setProperty('--py', ((e.clientY - r.top) / r.height - 0.5) * 48 + 'px');
      });
    });
    hero.addEventListener('pointerleave', function () {
      pulse.style.setProperty('--px', '0px');
      pulse.style.setProperty('--py', '0px');
    });
  }

  /* ── Artwork: leans a few degrees toward the pointer (desktop only) ── */
  if (!reduce && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    document.querySelectorAll('.project-media').forEach(function (media) {
      var raf = 0;
      media.addEventListener('pointermove', function (e) {
        if (raf) return;
        raf = requestAnimationFrame(function () {
          raf = 0;
          var r = media.getBoundingClientRect();
          var x = (e.clientX - r.left) / r.width - 0.5;
          var y = (e.clientY - r.top) / r.height - 0.5;
          var MAX_TILT = 3.5; /* degrees at the very edge of the cover */
          media.style.setProperty('--ry', (x * 2 * MAX_TILT).toFixed(2) + 'deg');
          media.style.setProperty('--rx', (y * -2 * MAX_TILT).toFixed(2) + 'deg');
        });
      });
      media.addEventListener('pointerleave', function () {
        media.style.setProperty('--rx', '0deg');
        media.style.setProperty('--ry', '0deg');
      });
    });
  }

  /* ── FAQ accordion (one open at a time; all answers stay in the DOM for search engines) ── */
  var triggers = document.querySelectorAll('.faq-trigger');
  function setOpen(trigger, open) {
    var panel = document.getElementById(trigger.getAttribute('aria-controls'));
    trigger.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (panel) panel.classList.toggle('is-open', open);
  }
  triggers.forEach(function (trigger, i) {
    setOpen(trigger, i === 0);
    trigger.addEventListener('click', function () {
      var willOpen = trigger.getAttribute('aria-expanded') !== 'true';
      triggers.forEach(function (t) { setOpen(t, false); });
      setOpen(trigger, willOpen);
    });
  });

  /* ── Contact form: opens the visitor's mail client (no backend) ── */
  var form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = document.getElementById('contactStatus');
      var data = new FormData(form);
      var name = data.get('name');
      var email = data.get('email');
      var message = data.get('message');
      var subject = encodeURIComponent((form.dataset.subject || 'New message from') + ' ' + name);
      var body = encodeURIComponent('Name: ' + name + '\nEmail: ' + email + '\n\n' + message);
      window.location.href = 'mailto:contact@pulso-studios.com?subject=' + subject + '&body=' + body;
      if (status) {
        status.textContent = form.dataset.opening || 'Opening your mail client...';
        setTimeout(function () { status.textContent = ''; form.reset(); }, 4000);
      }
    });
  }

  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
