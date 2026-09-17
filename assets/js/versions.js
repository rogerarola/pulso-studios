/* Pulso Studios - showcase pages: optional password gate + audio player (vanilla) */
(function () {
  'use strict';

  /* ── Gate (config lives in the page: window.PULSO_GATE) ── */
  var cfg = window.PULSO_GATE || { enabled: false };
  var root = document.documentElement;
  var gateForm = document.getElementById('gateForm');
  if (cfg.enabled && gateForm) {
    var pass = document.getElementById('gatePass');
    var gateError = document.getElementById('gateError');
    gateForm.addEventListener('submit', function (e) {
      e.preventDefault();
      if (pass.value === cfg.password) {
        try { sessionStorage.setItem('psv_ok', '1'); } catch (err) {}
        root.classList.remove('gated');
      } else {
        gateError.textContent = gateForm.dataset.wrong || 'Wrong password';
        pass.value = '';
        pass.focus();
      }
    });
  }

  /* ── Player ── */
  var tracks = Array.prototype.slice.call(document.querySelectorAll('.track'));
  var list = document.querySelector('.tracks');
  var labels = list ? list.dataset : {};

  function fmt(seconds) {
    if (!isFinite(seconds)) return '0:00';
    var s = Math.max(0, Math.round(seconds));
    return Math.floor(s / 60) + ':' + ('0' + (s % 60)).slice(-2);
  }

  tracks.forEach(function (row, index) {
    var audio = row.querySelector('audio');
    var button = row.querySelector('.track-play');
    var seek = row.querySelector('.track-seek');
    var current = row.querySelector('.track-current');
    var error = row.querySelector('.track-error');
    var title = row.querySelector('.track-title').textContent;
    var total = parseFloat(row.dataset.duration) || 0;
    var dragging = false;

    function paint(time) {
      var length = audio.duration && isFinite(audio.duration) ? audio.duration : total;
      var pct = length ? Math.min(100, (time / length) * 100) : 0;
      seek.value = pct;
      seek.style.setProperty('--p', pct + '%');
      seek.setAttribute('aria-valuetext', fmt(time));
      current.textContent = fmt(time);
      row.classList.toggle('has-progress', time > 0);
    }

    function setState(state) {
      row.classList.toggle('is-playing', state === 'playing');
      row.classList.toggle('is-loading', state === 'loading');
      button.setAttribute('aria-label', (state === 'playing' ? labels.pause : labels.play) + ' ' + title);
    }
    setState('idle');

    button.addEventListener('click', function () {
      if (audio.paused) {
        error.textContent = '';
        setState('loading');
        var started = audio.play();
        if (started && started.catch) started.catch(function () {});
      } else {
        audio.pause();
      }
    });

    audio.addEventListener('play', function () {
      tracks.forEach(function (other) {
        var a = other.querySelector('audio');
        if (a !== audio) a.pause();
      });
    });
    audio.addEventListener('playing', function () { setState('playing'); });
    audio.addEventListener('waiting', function () { if (!audio.paused) setState('loading'); });
    audio.addEventListener('pause', function () { setState('idle'); });
    audio.addEventListener('timeupdate', function () { if (!dragging) paint(audio.currentTime); });
    audio.addEventListener('ended', function () {
      audio.currentTime = 0;
      paint(0);
      var next = tracks[index + 1];
      if (next) next.querySelector('.track-play').click();
    });
    audio.addEventListener('error', function () {
      setState('idle');
      error.textContent = labels.error || '';
    });

    seek.addEventListener('input', function () {
      dragging = true;
      var length = audio.duration && isFinite(audio.duration) ? audio.duration : total;
      var time = (seek.value / 100) * length;
      seek.style.setProperty('--p', seek.value + '%');
      current.textContent = fmt(time);
    });
    seek.addEventListener('change', function () {
      var length = audio.duration && isFinite(audio.duration) ? audio.duration : total;
      var time = (seek.value / 100) * length;
      dragging = false;
      if (audio.readyState > 0) {
        audio.currentTime = time;
      } else {
        audio.addEventListener('loadedmetadata', function once() {
          audio.removeEventListener('loadedmetadata', once);
          audio.currentTime = time;
        });
        audio.load();
      }
      paint(time);
    });
  });
})();
