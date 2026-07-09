/* ABC OS — shared hub-screen renderer (driven by body[data-hub]) */
(function () {
  // restore theme chosen on the dashboard
  const theme = localStorage.getItem('abc-theme') || 'dark';
  document.documentElement.classList.toggle('dark', theme === 'dark');

  const HUBS = {
    community: { c: '#E57373', eyebrow: "L'ASSEMBLÉE", title: 'Community', ico: 'groups',
      search: 'Rechercher discussions et membres',
      tabs: [['Feed', null], ['Co-ops', null], ['Events', '3']] },
    learn: { c: '#13ec13', eyebrow: 'CULTIVER LE SAVOIR', title: 'Learn Hub', ico: 'school',
      search: 'Rechercher cours & sujets',
      tabs: [['Mes cours', null], ['Parcours', null], ['Certificats', null]] },
    build: { c: '#3b82f6', eyebrow: 'BÂTIR ENSEMBLE', title: 'Build Hub', ico: 'construction',
      search: 'Rechercher projets & outils',
      tabs: [['Mes projets', null], ['Outils coop', null]] },
    brand: { c: '#FFC72C', eyebrow: 'VOTRE IDENTITÉ COLLECTIVE', title: 'Brand Hub', ico: 'verified',
      search: 'Rechercher modèles & assets',
      tabs: [['Story', null], ['Reach', null], ['Impact', null]] },
  };

  const key = document.body.dataset.hub;
  const H = HUBS[key];
  document.documentElement.style.setProperty('--c', H.c);

  const av = (i, c) => `<div class="avatar" style="background:${c};width:30px;height:30px;font-size:11px">${i}</div>`;

  function gauge(score, size, stroke) {
    const r = (size - stroke) / 2, cx = size / 2, gap = 0.16, arc = 1 - gap;
    const circ = 2 * Math.PI * r, dash = circ * arc, filled = dash * (score / 100), rot = 90 + gap * 180;
    return `<div class="gauge" style="width:${size}px;height:${size}px">
      <svg width="${size}" height="${size}" viewBox="0 0 ${size} ${size}" style="transform:rotate(${rot}deg)">
        <defs><linearGradient id="hg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#008080"/><stop offset="1" stop-color="#13ec13"/></linearGradient></defs>
        <circle cx="${cx}" cy="${cx}" r="${r}" fill="none" stroke="var(--line-strong)" stroke-width="${stroke}" stroke-linecap="round" stroke-dasharray="${dash} ${circ}"/>
        <circle cx="${cx}" cy="${cx}" r="${r}" fill="none" stroke="url(#hg)" stroke-width="${stroke}" stroke-linecap="round" stroke-dasharray="${filled} ${circ}"/>
      </svg>
      <div class="val"><div><b style="font-size:${size*.36}px">${score}</b><s>/ 100</s></div></div></div>`;
  }

  /* ---- per-hub content ---- */
  const CONTENT = {
    community: `
      <div class="hsec"><div class="hd"><h2>Fil de l'assemblée</h2><button class="more">Tout voir</button></div>
        <div class="hcard">
          <div style="display:flex;gap:11px;align-items:center">
            ${av('KP', '#E57373')}
            <div><div style="font-weight:700;font-size:14px">Kaelan Patel</div><div style="font-size:12px;color:var(--ink-faint)">il y a 2 h · Lagos, NG</div></div>
            <span class="material-symbols-outlined" style="margin-left:auto;color:var(--ink-faint)">more_horiz</span>
          </div>
          <p style="margin:12px 0 0;font-size:14px;line-height:1.5">Je cherche des conseils pour enregistrer une coopérative au Nigéria — quelqu'un a déjà fait la démarche ? Quelles sont les étapes clés&nbsp;?</p>
          <div style="display:flex;gap:8px;margin-top:12px"><span class="pill" style="background:color-mix(in srgb,var(--secondary) 16%,transparent);color:var(--secondary)">#Legal</span><span class="pill" style="background:color-mix(in srgb,var(--secondary) 16%,transparent);color:var(--secondary)">#Startup</span></div>
          <div style="display:flex;gap:18px;margin-top:13px;color:var(--ink-faint);font-size:13px;font-weight:600">
            <span style="display:flex;align-items:center;gap:5px"><span class="material-symbols-outlined" style="font-size:19px">favorite</span>24</span>
            <span style="display:flex;align-items:center;gap:5px"><span class="material-symbols-outlined" style="font-size:19px">chat_bubble</span>8</span>
            <span style="display:flex;align-items:center;gap:5px"><span class="material-symbols-outlined" style="font-size:19px">share</span></span>
          </div>
        </div>
      </div>
      <div class="hsec"><div class="hcard">
          <div style="display:flex;gap:11px;align-items:center">
            ${av('FD', '#00796B')}
            <div><div style="font-weight:700;font-size:14px">Fatou Diallo</div><div style="font-size:12px;color:var(--ink-faint)">il y a 5 h · Dakar, SN</div></div>
          </div>
          <p style="margin:12px 0 0;font-size:14px;line-height:1.5">Notre coopérative de teinture lance une formation indigo le mois prochain — places limitées&nbsp;!</p>
        </div></div>`,
    learn: `
      <div class="hsec"><div class="hd"><h2>Mes cours</h2><button class="more">Tout voir</button></div>
        <div class="bigcourse">
          <div class="ph"><span class="material-symbols-outlined">layers</span></div>
          <div class="bd">
            <div class="eyebrow" style="color:var(--c)">FONDATIONS</div>
            <h3 style="margin:6px 0 12px;font-size:20px;font-weight:700">Architect Principles</h3>
            <div class="bar"><span style="width:60%;background:var(--c)"></span></div>
            <div style="display:flex;justify-content:space-between;margin-top:8px;font-size:12.5px;color:var(--ink-soft)"><span>Module 4 / 7</span><b style="color:var(--c)">60%</b></div>
          </div>
        </div>
      </div>
      <div class="hsec"><div class="hcard" style="display:flex;align-items:center;gap:13px">
        <div style="width:46px;height:46px;border-radius:13px;display:grid;place-items:center;background:color-mix(in srgb,var(--c) 18%,transparent);color:var(--c)"><span class="material-symbols-outlined">balance</span></div>
        <div style="flex:1"><div style="font-weight:700;font-size:14px">Gouvernance coopérative</div><div style="font-size:12px;color:var(--ink-soft)">Module 2 / 5 · 35%</div></div>
        <span class="material-symbols-outlined" style="color:var(--ink-faint)">chevron_right</span>
      </div></div>`,
    build: `
      <div class="hsec"><div class="hcard" style="padding:0;overflow:hidden">
        <div style="padding:15px 15px 0"><span class="pill" style="background:color-mix(in srgb,var(--build-green,#13ec13) 18%,transparent);color:#13ec13"><span style="width:7px;height:7px;border-radius:999px;background:#13ec13"></span>EN COURS</span></div>
        <div style="padding:14px 15px 0"><h3 style="margin:0;font-size:22px;font-weight:700">Solaris Agri-Coop</h3><p style="margin:5px 0 0;font-size:13px;color:var(--ink-soft)">Agriculture coopérative solaire · Kenya</p></div>
        <div style="padding:16px 15px 16px">
          <div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:7px"><b>Progression des jalons</b><b style="color:var(--c)">3 / 5</b></div>
          <div class="bar"><span style="width:60%;background:var(--c)"></span></div>
          <div class="stack" style="margin-top:14px">${av('KP', '#3b82f6')}${av('FD', '#13ec13')}${av('NJ', '#FFC72C')}<div class="avatar" style="background:var(--card-2);color:var(--ink-soft);width:30px;height:30px;font-size:11px">+2</div></div>
        </div>
      </div></div>
      <div class="hsec"><div class="hd"><h2>Prochains jalons</h2></div>
        <div class="hcard" style="display:flex;align-items:center;gap:13px">
          <div style="width:42px;height:42px;border-radius:13px;display:grid;place-items:center;background:color-mix(in srgb,var(--c) 18%,transparent);color:var(--c)"><span class="material-symbols-outlined">water_drop</span></div>
          <div style="flex:1"><div style="font-weight:700;font-size:14px">Irrigation solaire</div><div style="font-size:12px;color:var(--ink-soft)">Échéance demain · 2 tâches</div></div>
          <span class="pill" style="background:color-mix(in srgb,#E06B5B 20%,transparent);color:#E06B5B">Demain</span>
        </div>
      </div>`,
    brand: `
      <div class="hsec" style="text-align:center;padding-top:24px">
        <div class="eyebrow" style="color:var(--c);letter-spacing:.2em">BRAND IMPACT</div>
        <div style="display:grid;place-items:center;margin:14px 0 6px">${gauge(85, 168, 14)}</div>
        <div class="pill" style="background:color-mix(in srgb,#13ec13 16%,transparent);color:#13ec13;margin-top:4px"><span class="material-symbols-outlined" style="font-size:15px">trending_up</span>+6 cette semaine</div>
        <p style="margin:14px auto 0;max-width:260px;font-size:13.5px;color:var(--ink-soft);line-height:1.5">Résonance actuelle de votre communauté. Croissance régulière.</p>
      </div>
      <div class="segtabs" style="justify-content:center"><button class="on">Story</button><button>Reach</button><button>Impact</button></div>
      <div class="hsec"><div class="hcard" style="display:flex;align-items:center;gap:13px">
        <div style="width:46px;height:46px;border-radius:13px;display:grid;place-items:center;background:color-mix(in srgb,var(--c) 18%,transparent);color:var(--c)"><span class="material-symbols-outlined">auto_stories</span></div>
        <div style="flex:1"><div style="font-weight:700;font-size:14px">Renforcer la brand story</div><div style="font-size:12px;color:var(--ink-soft)">2 sections manquantes · +4 impact</div></div>
        <span class="material-symbols-outlined" style="color:var(--ink-faint)">chevron_right</span>
      </div></div>`,
  };

  const navItem = (k) => {
    const meta = { community: ['groups', 'Community'], learn: ['school', 'Learn'], build: ['construction', 'Build'], brand: ['verified', 'Brand'] }[k];
    return `<a href="${k}.html" class="${k === key ? 'on' : ''}"><span class="material-symbols-outlined">${meta[0]}</span>${meta[1]}</a>`;
  };

  document.getElementById('scroll').innerHTML = `
    <div class="appbar">
      <button class="icbtn backbtn" onclick="location.href='../ABC OS Dashboard.html'" aria-label="Retour au dashboard"><span class="material-symbols-outlined">arrow_back</span></button>
      <div style="margin-left:4px;font-weight:700;font-size:15px">${H.title}</div>
      <button class="icbtn" style="margin-left:auto" aria-label="Réglages"><span class="material-symbols-outlined">tune</span></button>
    </div>
    <div class="hubhead">
      <div class="eyebrow">${H.eyebrow}</div>
      <h1>${H.title}</h1>
    </div>
    <div class="search"><span class="material-symbols-outlined">search</span>${H.search}…</div>
    <div class="segtabs">${H.tabs.map((t, i) => `<button class="${i === 0 ? 'on' : ''}">${t[0]}${t[1] ? `<span class="b">${t[1]}</span>` : ''}</button>`).join('')}</div>
    ${CONTENT[key]}`;

  document.getElementById('nav').innerHTML = ['community', 'learn', 'build', 'brand'].map(navItem).join('');
})();
