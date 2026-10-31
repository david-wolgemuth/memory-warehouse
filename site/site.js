(() => {
  const data = JSON.parse(document.getElementById('records').textContent);
  const frames = [...document.querySelectorAll('iframe[data-frame]')];
  let step = 0;
  let paused = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const pause = document.getElementById('pause');
  const status = document.getElementById('rotation-status');
  function render() {
    for (const frame of frames) {
      const entries = data[frame.dataset.frame];
      if (!entries.length) continue;
      const offset = Number(frame.dataset.offset || 0);
      const index = ((step + offset) % entries.length + entries.length) % entries.length;
      if (frame.getAttribute('src') !== entries[index].url) frame.src = entries[index].url;
    }
  }
  function updatePause() {
    pause.textContent = paused ? '▶ RESUME' : 'Ⅱ PAUSE';
    pause.setAttribute('aria-pressed', String(paused));
    status.textContent = paused ? 'ROTATION PAUSED' : 'ROTATING EVERY 12 SECONDS';
  }
  document.getElementById('previous').addEventListener('click', () => { step--; render(); });
  document.getElementById('next').addEventListener('click', () => { step++; render(); });
  pause.addEventListener('click', () => { paused = !paused; updatePause(); });
  setInterval(() => { if (!paused && !document.hidden) { step++; render(); } }, 12000);
  updatePause();
})();
