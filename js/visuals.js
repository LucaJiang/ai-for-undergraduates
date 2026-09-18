/* Original decorative SVG icons; all information also appears in nearby text. */
(function () {
  'use strict';
  const paths = Object.freeze({
    book: 'M3 5Q7 3 12 6Q17 3 21 5V20Q17 18 12 21Q7 18 3 20ZM12 6V21',
    files: 'M7 3H16L21 8V21H7ZM16 3V8H21M3 6V18M10 12H18M10 16H17',
    pen: 'M4 20L5 15L16 4Q18 2 20 4Q22 6 20 8L9 19ZM14 6L18 10M4 20H20',
    chat: 'M4 4H20V16H10L4 21ZM8 8H16M8 12H14',
    users: 'M9 9A3 3 0 1 0 9 3A3 3 0 0 0 9 9M3 21V17Q3 12 9 12Q15 12 15 17V21M17 4Q22 5 20 9M18 13Q22 14 22 18V21',
    target: 'M21 12A9 9 0 1 1 12 3M17 12A5 5 0 1 1 12 7M12 12L21 3M17 3H21V7',
    layers: 'M3 7L12 3L21 7L12 11ZM3 12L12 16L21 12M3 17L12 21L21 17',
    lightbulb: 'M8 15Q3 11 6 6Q8 3 12 3Q16 3 18 6Q21 11 16 15V18H8ZM9 22H15M12 10V17',
    clock: 'M21 12A9 9 0 1 1 3 12A9 9 0 0 1 21 12M12 6V12L16 15',
    mic: 'M8 6A4 4 0 0 1 16 6V11A4 4 0 0 1 8 11ZM5 10V12A7 7 0 0 0 19 12V10M12 19V22M8 22H16',
    play: 'M21 12A9 9 0 1 1 3 12A9 9 0 0 1 21 12M10 8L16 12L10 16Z',
    sliders: 'M4 5H20M4 12H20M4 19H20M8 2V8M16 9V15M10 16V22',
    search: 'M16 10A6 6 0 1 1 4 10A6 6 0 0 1 16 10M14 15L21 22',
    check: 'M3 12L9 18L21 5',
    math: 'M17 4H5L12 12L5 20H17M19 9H22M19 14H22',
    chart: 'M3 3V21H22M6 16L11 10L15 13L21 5M17 5H21V9',
    link: 'M9 15L15 9M8 12L5 15A3 3 0 0 0 9 19L12 16M12 8L15 5A3 3 0 0 1 19 9L16 12',
    shield: 'M12 2L21 6V12Q20 18 12 22Q4 18 3 12V6ZM8 12L11 15L17 9',
    face: 'M3 8V3H8M16 3H21V8M21 16V21H16M8 21H3V16M8 9H8.1M16 9H16.1M12 10V14H14M8 16Q12 19 16 16',
    board: 'M3 3H21V21H3ZM9 3V21M15 3V21M3 9H21M3 15H21M11 9A2 2 0 1 1 7 9A2 2 0 0 1 11 9M17 15A2 2 0 1 1 13 15A2 2 0 0 1 17 15',
    medal: 'M7 3L11 10M17 3L13 10M6 3H3L8 12M18 3H21L16 12M18 16A6 6 0 1 1 6 16A6 6 0 0 1 18 16M12 13V19M10 14L12 13',
    compass: 'M21 12A9 9 0 1 1 3 12A9 9 0 0 1 21 12M15 8L13 14L8 16L10 10Z',
    heart: 'M12 21L4 13Q0 8 4 4Q8 1 12 6Q16 1 20 4Q24 8 20 13Z'
  });
  window.initWorkshopVisuals = function () {
    const ns = 'http://www.w3.org/2000/svg';
    document.querySelectorAll('.reveal [data-icon]').forEach(host => {
      const d = paths[host.dataset.icon];
      if (!d || host.querySelector('svg')) return;
      host.setAttribute('aria-hidden', 'true');
      const svg = document.createElementNS(ns, 'svg');
      svg.setAttribute('viewBox', '0 0 24 24');
      svg.setAttribute('fill', 'none');
      svg.setAttribute('stroke', 'currentColor');
      svg.setAttribute('stroke-width', '1.65');
      svg.setAttribute('stroke-linecap', 'round');
      svg.setAttribute('stroke-linejoin', 'round');
      svg.setAttribute('focusable', 'false');
      const path = document.createElementNS(ns, 'path');
      path.setAttribute('d', d); svg.append(path); host.append(svg);
    });
    window.Reveal?.layout();
  };
})();
