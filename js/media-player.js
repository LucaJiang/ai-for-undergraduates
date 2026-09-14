/* Presenter-selected files stay in this browser. Never upload or persist media. */
(function () {
  'use strict';
  const files = new Map();
  let dialog;
  function stages() { return Array.from(document.querySelectorAll('.video-stage[data-video]')); }
  function stopAll() {
    stages().forEach(box => {
      box.querySelectorAll('video').forEach(v => { v.pause(); v.removeAttribute('src'); v.load(); v.remove(); });
      box.querySelectorAll('iframe,.play-again,.video-error').forEach(el => el.remove());
      delete box.dataset.loaded;
    });
  }
  function showError(box, text) {
    box.querySelectorAll('iframe,video,.play-again,.video-error').forEach(el => el.remove());
    delete box.dataset.loaded;
    const p = document.createElement('div'); p.className = 'video-error'; p.textContent = text; box.append(p);
  }
  function play(box) {
    stopAll();
    const start = Number(box.dataset.start), end = Number(box.dataset.end);
    if (!Number.isFinite(start) || !Number.isFinite(end) || end <= start) return;
    const selected = files.get(box.dataset.video);
    if (!selected) {
      const frame = document.createElement('iframe');
      const query = new URLSearchParams({start:String(start),end:String(end),autoplay:'1',rel:'0',playsinline:'1',enablejsapi:'1'});
      if (location.protocol !== 'file:') query.set('origin',location.origin);
      frame.src = 'https://www.youtube.com/embed/' + box.dataset.video + '?' + query;
      frame.title = box.querySelector('p').textContent + ' excerpt';
      frame.allow = 'autoplay; encrypted-media; picture-in-picture'; frame.allowFullscreen = true;
      frame.referrerPolicy = 'strict-origin-when-cross-origin'; box.dataset.loaded = 'true'; box.append(frame);
      return;
    }
    const video = document.createElement('video'); video.controls = true; video.playsInline = true; video.preload = 'metadata';
    video.src = selected.url; box.dataset.loaded = 'true'; box.append(video);
    const begin = selected.trimmed ? 0 : start;
    let finish = selected.trimmed ? end - start : end;
    const replay = document.createElement('button'); replay.className = 'play-again'; replay.type = 'button'; replay.textContent = 'Replay excerpt'; replay.hidden = true; box.append(replay);
    video.addEventListener('loadedmetadata', () => {
      if (!Number.isFinite(video.duration) || video.duration <= begin) { showError(box,'The file does not contain this time range. Check Video setup.'); return; }
      finish = Math.min(finish,video.duration);
      video.currentTime = begin;
      video.play().catch(() => { /* Browser requires another click: native Play remains available. */ });
    }, {once:true});
    video.addEventListener('timeupdate', () => { if(video.currentTime >= finish) { video.pause(); replay.hidden = false; } });
    video.addEventListener('play', () => { if(video.currentTime >= finish || video.currentTime < begin) video.currentTime = begin; replay.hidden = true; });
    video.addEventListener('seeking', () => { if(video.currentTime < begin) video.currentTime = begin; if(video.currentTime > finish) { video.pause(); video.currentTime = finish; replay.hidden = false; } });
    video.addEventListener('ended', () => { replay.hidden = false; });
    video.addEventListener('error', () => showError(box,'This file could not be played. Choose another file or use the YouTube link.'));
    replay.addEventListener('click', () => { video.currentTime = begin; replay.hidden = true; video.play().catch(() => {}); });
  }
  function setup() {
    if (!dialog) {
      dialog = document.createElement('dialog'); dialog.className = 'media-settings'; dialog.setAttribute('aria-label','Presenter video setup');
      const h = document.createElement('h2'); h.textContent = 'Presenter video setup';
      const p = document.createElement('p'); p.textContent = 'Choose video files you have permission to use. Files stay on this device and must be selected again after reloading. Full recordings use the source timestamps; trimmed excerpts start at zero. Leaving a slide stops playback.';
      dialog.append(h,p);
      stages().forEach(box => {
        const row = document.createElement('div'); row.className = 'media-row';
        const label = document.createElement('label'); label.textContent = box.querySelector('p').textContent + ' (' + box.dataset.start + '–' + box.dataset.end + ' seconds)';
        const input = document.createElement('input'); input.type = 'file'; input.accept = 'video/*'; label.append(input);
        const select = document.createElement('select'); select.setAttribute('aria-label','Video file type');
        [['full','Full source video'],['trimmed','Already trimmed excerpt']].forEach(([value,text]) => { const opt = document.createElement('option'); opt.value = value; opt.textContent = text; select.append(opt); });
        const status = document.createElement('p'); status.className = 'media-status'; status.textContent = 'YouTube embed';
        const clear = document.createElement('button'); clear.type = 'button'; clear.textContent = 'Use YouTube instead';
        input.addEventListener('change', () => {
          const file = input.files[0]; if(!file) return;
          stopAll(); const previous = files.get(box.dataset.video); if(previous) URL.revokeObjectURL(previous.url);
          files.set(box.dataset.video,{url:URL.createObjectURL(file),trimmed:select.value==='trimmed'}); status.textContent = file.name;
        });
        select.addEventListener('change', () => { const entry=files.get(box.dataset.video); if(entry) { stopAll(); entry.trimmed=select.value==='trimmed'; } });
        clear.addEventListener('click', () => { stopAll(); const entry=files.get(box.dataset.video); if(entry) URL.revokeObjectURL(entry.url); files.delete(box.dataset.video); input.value=''; status.textContent='YouTube embed'; });
        row.append(label,select,status,clear); dialog.append(row);
      });
      const close = document.createElement('button'); close.type='button'; close.textContent='Close setup'; close.addEventListener('click',()=>dialog.close()); dialog.append(close); document.body.append(dialog);
    }
    stopAll(); dialog.showModal();
  }
  // Capture avoids invoking the legacy bubbling embed handler as well.
  document.addEventListener('click', event => {
    const button = event.target.closest?.('.play-clip');
    if(button) { event.preventDefault(); event.stopImmediatePropagation(); play(button.closest('.video-stage')); }
  }, true);
  document.addEventListener('keydown', event => {
    if(event.key.toLowerCase()==='v' && !event.ctrlKey && !event.metaKey && !event.altKey && !event.target.closest('input,textarea,select,[contenteditable]')) {
      event.preventDefault(); event.stopImmediatePropagation(); if(dialog?.open) dialog.close(); else setup();
    }
  }, true);
  document.addEventListener('visibilitychange',()=>{
    if(document.hidden) { document.querySelectorAll('.video-stage video').forEach(v=>v.pause()); document.querySelectorAll('.video-stage iframe').forEach(f=>f.contentWindow?.postMessage(JSON.stringify({event:'command',func:'pauseVideo',args:[]}),'https://www.youtube.com')); }
  });
  window.addEventListener('pagehide',()=>{ stopAll(); files.forEach(entry=>URL.revokeObjectURL(entry.url)); files.clear(); });
  window.initWorkshopMedia = function () {
    Reveal.on('slidechanged',stopAll); Reveal.on('overviewshown',stopAll);
    if(new URLSearchParams(location.search).get('presenter')==='1') { const button=document.createElement('button'); button.type='button'; button.textContent='Video setup'; button.addEventListener('click',setup); document.querySelector('.deck-nav').append(button); }
  };
})();
