const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const files = fs.readdirSync('out').filter(f => f.endsWith('.html'));
  for (const vw of [1280, 390]) for (const f of files) {
    const p = await b.newPage({ viewport: { width: vw, height: 900 } }); const errs = [];
    p.on('console', m => { if (m.type() === 'error') errs.push(m.text().slice(0, 160)); }); p.on('pageerror', e => errs.push('PAGEERR ' + e.message.slice(0, 160)));
    await p.route('https://cdn.jsdelivr.net/npm/three@0.170.0/**', r => { const u = r.request().url().split('three@0.170.0/')[1]; r.fulfill({ path: process.cwd() + '/node_modules/three/' + u, contentType: 'text/javascript' }); });
    await p.route('https://fonts.googleapis.com/**', r => r.fulfill({ body: '', contentType: 'text/css' }));
    await p.goto('file://' + process.cwd() + '/out/' + f); await p.waitForTimeout(vw === 1280 ? 2500 : 1200);
    const r = await p.evaluate(async () => {
      const q = s => Array.from(document.querySelectorAll(s));
      const oa = document.querySelector('#openAll'); if (oa) oa.click();
      // 모든 슬라이더를 최소·최대로 움직여 NaN 확인
      let bad = [];
      for (const i of q('.sim input[type=range], .dash input[type=range]')) { for (const v of [i.min, i.max, i.defaultValue]) { i.value = v; i.dispatchEvent(new Event('input')); } }
      for (const bt of q('.sim .group .bt')) bt.click();
      for (const el of q('.sim, .dash')) { const t = el.innerText; if (/NaN|undefined|Infinity/.test(t)) bad.push((el.dataset.sim || 'dash') + ':' + (t.match(/.{0,30}(NaN|undefined|Infinity).{0,20}/) || [''])[0].replace(/\n/g, ' ')); }
      const rv = document.querySelector('.reveal'); let duel = '';
      if (rv) { rv.click(); await new Promise(r => setTimeout(r, 200)); duel = (document.querySelector('.result .say[data-who=moa] p') || {}).textContent || ''; }
      const over = document.documentElement.scrollWidth - window.innerWidth;
      const wide = over > 1 ? q('body *').filter(e => e.getBoundingClientRect().right > window.innerWidth + 1 && !e.closest('.tw, .cwrap, .tower')).slice(0, 3).map(e => e.tagName + '.' + e.className) : [];
      const noimg = q('img[data-img]').filter(i => !i.src || i.naturalWidth === 0).length;
      const empty = q('.sim').filter(e => !e.children.length).length;
      return { over, wide, noimg, empty, bad, duel, quiz: q('.quiz .qi').length, tw: !!document.querySelector('.tw-cv canvas') };
    });
    console.log(vw, f.padEnd(30), 'over', r.over, r.wide.join(','), 'noimg', r.noimg, 'emptysim', r.empty, 'quiz', r.quiz, '3d', r.tw, r.duel, r.bad.length ? 'BAD ' + r.bad.join(' | ') : '', errs.length ? 'ERR ' + errs.slice(0, 3).join(' | ') : '');
    await p.close();
  }
  await b.close();
})();
