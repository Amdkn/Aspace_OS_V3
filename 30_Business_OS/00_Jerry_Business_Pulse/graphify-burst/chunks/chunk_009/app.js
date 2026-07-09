/* ============================================================
   ABC OS — Dashboard logic (data-driven, vanilla)
   ============================================================ */

const HUB = {
  community: { c: 'var(--community)',   ico: 'groups',       label: "L'ASSEMBLÉE",            name: 'Community', href: 'hubs/community.html' },
  learn:     { c: 'var(--learn-green)', ico: 'school',       label: 'CULTIVER LE SAVOIR',     name: 'Learn',     href: 'hubs/learn.html' },
  build:     { c: 'var(--build-blue)',  ico: 'construction', label: 'BÂTIR ENSEMBLE',         name: 'Build',     href: 'hubs/build.html' },
  brand:     { c: 'var(--brand-gold)',  ico: 'verified',     label: 'VOTRE IDENTITÉ COLLECTIVE', name: 'Brand',  href: 'hubs/brand.html' },
};

const DATA = {
  member: { name: 'Amara', full: 'Amara Okonkwo', initials: 'AO', tint: 'linear-gradient(150deg,#FFC72C,#E57373)' },
  coop: 'Umoja Weavers',
  place: 'Nairobi, Kenya',
  notifications: 4,
  pulse: {
    community: { count: '5 nouvelles', meta: '3 événements à venir · #Legal #Startup actifs' },
    learn:     { course: 'Architect Principles', pct: 60, meta: 'Module 4 / 7 · reprendre' },
    build:     { project: 'Solaris Agri-Coop', ms: 3, msTotal: 5, meta: 'Prochain : Irrigation solaire',
                 team: [['KP','#3b82f6'],['FD','#13ec13'],['NJ','#FFC72C'],['+2','#A45D5D']] },
    brand:     { score: 85, delta: 6 },
  },
  actions: [
    { hub: 'build',     t: 'Finaliser le milestone « Irrigation solaire »', d: 'Solaris Agri-Coop · 3/5 jalons', due: 'Demain', urgent: true },
    { hub: 'learn',     t: 'Terminer le module « Gouvernance coopérative »', d: 'Architect Principles · 60% complété', due: '12 min' },
    { hub: 'community', t: 'Répondre à la discussion #Legal #Startup', d: '2 mentions de Kaelan P. · Lagos', due: null },
    { hub: 'brand',     t: 'Renforcer votre Brand Story', d: '2 sections manquantes · +4 impact estimé', due: null },
  ],
  spotlight: {
    name: 'Umoja Weavers', tag: 'PROJET VEDETTE',
    desc: 'Collectif textile · teinture naturelle indigo', place: 'Nairobi, Kenya',
    ms: 4, msTotal: 6, pct: 67,
    team: [['AO','#FFC72C'],['ZW','#00796B'],['TM','#E57373'],['KN','#3b82f6'],['+7','#A45D5D']],
  },
  feed: [
    { who: 'Kaelan P.', av: ['KP','#E57373'], hub: 'community', what: 'a lancé une discussion', detail: 'Conseils pour enregistrer une coopérative au Nigéria', when: '2 h', place: 'Lagos, NG' },
    { who: 'Fatou D.',  av: ['FD','#00796B'], hub: 'learn', what: 'a terminé le module', detail: 'Design Thinking pour coopératives', when: '4 h', place: null },
    { who: 'Solaris Agri-Coop', av: ['SA','#3b82f6'], hub: 'build', what: 'jalon validé', detail: '« Étude de sol » approuvée par 4 membres', when: 'hier', place: 'Kenya' },
    { who: 'Brand Impact', av: ['BI','#FFC72C'], hub: 'brand', what: 'a progressé', detail: '+6 cette semaine — résonance en hausse', when: 'hier', place: null },
  ],
};

/* ---------- helpers ---------- */
const h = (s) => s; // identity tag
function av(initials, color, cls = '') {
  const isPlus = String(initials).startsWith('+');
  return `<div class="avatar av ${cls}" style="background:${isPlus ? 'var(--card-2)' : color};${isPlus ? 'color:var(--ink-soft);font-size:11px;' : ''}">${initials}</div>`;
}
function badgeIcon(hub) {
  const m = { community: 'forum', learn: 'school', build: 'construction', brand: 'auto_awesome' };
  return m[hub];
}

/* ---------- radial gauge SVG ---------- */
function gauge(score, size = 86, stroke = 9) {
  const r = (size - stroke) / 2;
  const cx = size / 2;
  const gap = 0.16;                  // bottom gap fraction
  const arc = 1 - gap;
  const circ = 2 * Math.PI * r;
  const dash = circ * arc;
  const filled = dash * (score / 100);
  const rot = 90 + gap * 180;        // rotate so gap sits at the bottom
  const id = 'g' + Math.random().toString(36).slice(2, 7);
  return `
  <div class="gauge" style="width:${size}px;height:${size}px">
    <svg width="${size}" height="${size}" viewBox="0 0 ${size} ${size}" style="transform:rotate(${rot}deg)">
      <defs><linearGradient id="${id}" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="var(--brand-teal)"/><stop offset="1" stop-color="var(--build-green)"/>
      </linearGradient></defs>
      <circle cx="${cx}" cy="${cx}" r="${r}" fill="none" stroke="var(--line-strong)" stroke-width="${stroke}" stroke-linecap="round" stroke-dasharray="${dash} ${circ}"/>
      <circle cx="${cx}" cy="${cx}" r="${r}" fill="none" stroke="url(#${id})" stroke-width="${stroke}" stroke-linecap="round" stroke-dasharray="${filled} ${circ}"/>
    </svg>
    <div class="val"><div><b>${score}</b><s>/ 100</s></div></div>
  </div>`;
}

/* ---------- pulse hub cards ---------- */
function hubCard(key) {
  const H = HUB[key], P = DATA.pulse[key];
  const base = `style="--c:${H.c}"`;
  let body = '';
  if (key === 'community') {
    body = `
      <div class="cnt"><span class="material-symbols-outlined" style="font-size:15px">forum</span>${P.count}</div>
      <h3>Community</h3>
      <div class="meta">${P.meta}</div>
      <div class="foot"><div class="pill" style="background:color-mix(in srgb,var(--c) 18%,transparent);color:var(--c)"><span class="material-symbols-outlined" style="font-size:15px">event</span>3 events</div></div>`;
  } else if (key === 'learn') {
    body = `
      <div class="cnt">${P.pct}%</div>
      <h3>Learn</h3>
      <div class="meta">${P.course}<br>${P.meta}</div>
      <div class="foot"><div class="bar"><span style="width:${P.pct}%;background:var(--c)"></span></div></div>`;
  } else if (key === 'build') {
    body = `
      <div class="cnt">${P.ms}/${P.msTotal}</div>
      <h3>Build</h3>
      <div class="meta">${P.project}<br>${P.meta}</div>
      <div class="foot stack">${P.team.map(t => av(t[0], t[1], 'av')).join('')}</div>`;
  } else {
    body = `
      <div class="cnt"><span class="material-symbols-outlined" style="font-size:15px">trending_up</span>+${P.delta}</div>
      <h3 style="margin-bottom:8px">Brand</h3>
      <div class="foot" style="padding-top:0;display:flex;align-items:center;gap:10px">
        ${gauge(P.score, 64, 7)}
        <div class="meta">Brand Impact<br>+${P.delta} cette semaine</div>
      </div>`;
  }
  const topIco = key === 'build'
    ? `<div class="ico">${P.team ? '' : ''}<span class="material-symbols-outlined">${H.ico}</span></div>`
    : `<div class="ico"><span class="material-symbols-outlined">${H.ico}</span></div>`;
  return `
  <a href="${H.href}" class="hub tap" ${base} aria-label="Ouvrir ${H.name}">
    <div class="top">${topIco}<span class="material-symbols-outlined chev" style="font-size:18px">north_east</span></div>
    ${body}
  </a>`;
}

/* ---------- action item ---------- */
function actionItem(a) {
  const H = HUB[a.hub];
  const dueHtml = a.due
    ? `<span class="due" style="background:${a.urgent ? 'color-mix(in srgb,var(--danger) 20%,transparent);color:var(--danger)' : 'color-mix(in srgb,var(--secondary) 18%,transparent);color:var(--secondary)'}">${a.due}</span>`
    : '';
  const detail = a.d.replace(/#(\w+)/g, '<span class="hashtag">#$1</span>');
  return `
  <button class="act tap" onclick="location.href='${H.href}'">
    <div class="tag" style="background:color-mix(in srgb,${H.c} 18%,transparent);color:${H.c}"><span class="material-symbols-outlined">${H.ico}</span></div>
    <div class="body"><div class="t">${a.t}</div><div class="d">${detail}</div></div>
    ${dueHtml}
    <span class="material-symbols-outlined chev">chevron_right</span>
  </button>`;
}

/* ---------- spotlight ---------- */
function spotlight() {
  const S = DATA.spotlight;
  return `
  <a class="spot tap" href="hubs/build.html" style="display:block">
    <div class="ph">
      <div class="grad-tag pill" style="background:rgba(0,0,0,.32);color:#FFD600;backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,.18)"><span class="material-symbols-outlined" style="font-size:14px">star</span>${S.tag}</div>
      <button class="like pill" aria-label="Suivre"><span class="material-symbols-outlined" style="font-size:16px">favorite</span></button>
      <div class="place"><span class="material-symbols-outlined" style="font-size:15px">location_on</span>${S.place}</div>
    </div>
    <div class="info">
      <h3>${S.name}</h3>
      <p>${S.desc}</p>
      <div class="row">
        <div style="flex:1;margin-right:16px">
          <div style="display:flex;justify-content:space-between;font-size:11.5px;margin-bottom:6px;color:rgba(251,243,228,.72)"><span>Milestones</span><b style="color:#fff">${S.ms} / ${S.msTotal}</b></div>
          <div class="bar"><span style="width:${S.pct}%;background:linear-gradient(90deg,var(--brand-gold),var(--build-green))"></span></div>
        </div>
        <div class="stack">${S.team.map(t => av(t[0], t[1], 'av')).join('')}</div>
      </div>
    </div>
  </a>`;
}

/* ---------- feed item ---------- */
function feedItem(f) {
  const H = HUB[f.hub];
  return `
  <div class="fi tap" onclick="location.href='${H.href}'">
    ${av(f.av[0], f.av[1], 'av')}
    <div class="badge" style="background:${H.c}"><span class="material-symbols-outlined">${badgeIcon(f.hub)}</span></div>
    <div class="ct">
      <div class="l"><b>${f.who}</b> ${f.what} — ${f.detail}</div>
      <div class="m"><span>${f.when}</span>${f.place ? '<span>·</span><span>' + f.place + '</span>' : ''}<span>·</span><span style="color:${H.c};font-weight:700">${H.name}</span></div>
    </div>
  </div>`;
}

/* ============ MOBILE RENDER ============ */
function renderMobile(state) {
  const greet = greeting();
  const sync = state === 'error'
    ? `<button class="syncpill off tap" id="m-sync"><span class="led"></span>Hors-ligne</button>`
    : `<button class="syncpill tap" id="m-sync"><span class="led"></span>Synchro</button>`;

  const header = `
    <div class="appbar">
      <div class="me">
        ${av(DATA.member.initials, DATA.member.tint, 'av')}
        <div class="hello"><div class="g">${greet}, bon retour</div><div class="coop"><span class="material-symbols-outlined">hub</span>${DATA.coop}</div></div>
      </div>
      <div class="right">
        ${sync}
        <button class="icbtn tap" aria-label="Notifications"><span class="material-symbols-outlined">notifications</span><span class="dot-badge"></span></button>
      </div>
    </div>
    <div class="hero">
      <div class="kick">L'OS <em>en main</em>,<br>tout le temps.</div>
      <div class="sub"><span class="material-symbols-outlined" style="font-size:16px;color:var(--secondary)">location_on</span>${DATA.member.full} · ${DATA.place}</div>
    </div>`;

  if (state === 'loading') return header + skeletonMobile();
  if (state === 'empty') return header + emptyMobile();

  const err = state === 'error' ? `
    <div class="errbar" style="margin-top:14px">
      <span class="material-symbols-outlined">cloud_off</span>
      <div><b>Synchronisation échouée</b><br><span style="color:var(--ink-soft)">Données du cache · 2 modifications en attente</span></div>
      <button onclick="window.__retry()">Réessayer</button>
    </div>` : '';

  return header + err + `
    <div class="sec">
      <div class="sechd"><h2>Pulse des hubs</h2><button class="more">Tout voir <span class="material-symbols-outlined" style="font-size:15px">chevron_right</span></button></div>
      <div class="pulse">${['community','learn','build','brand'].map(hubCard).join('')}</div>
    </div>

    <div class="sec">
      <div class="sechd"><h2>Aujourd'hui</h2><span class="more" style="color:var(--primary)">${DATA.actions.length} actions</span></div>
      <div class="actions">${DATA.actions.map(actionItem).join('')}</div>
    </div>

    <div class="sec">
      <div class="sechd"><h2>Spotlight coopérative</h2></div>
      ${spotlight()}
    </div>

    <div class="sec">
      <div class="sechd"><h2>Activité récente</h2><button class="more">Tout voir</button></div>
      <div class="feed">${DATA.feed.map(feedItem).join('')}</div>
    </div>`;
}

function skeletonMobile() {
  const card = `<div class="card" style="height:156px;padding:15px"><div class="skel" style="width:38px;height:38px;border-radius:12px"></div><div class="skel" style="width:60%;height:14px;margin-top:14px"></div><div class="skel" style="width:85%;height:10px;margin-top:10px"></div><div class="skel" style="width:70%;height:10px;margin-top:7px"></div></div>`;
  const row = `<div class="card" style="height:70px;display:flex;align-items:center;gap:13px;padding:14px"><div class="skel" style="width:42px;height:42px;border-radius:13px"></div><div style="flex:1"><div class="skel" style="width:80%;height:12px"></div><div class="skel" style="width:50%;height:10px;margin-top:8px"></div></div></div>`;
  return `
    <div class="sec"><div class="skel" style="width:140px;height:18px;margin-bottom:14px"></div>
      <div class="pulse">${card}${card}${card}${card}</div></div>
    <div class="sec"><div class="skel" style="width:110px;height:18px;margin-bottom:14px"></div>
      <div class="actions">${row}${row}${row}</div></div>`;
}

function emptyMobile() {
  return `
    <div class="sec"><div class="placeholder">
      <div class="big"><span class="material-symbols-outlined">rocket_launch</span></div>
      <h3>Bienvenue dans ABC OS</h3>
      <p>Votre coopérative <b>${DATA.coop}</b> démarre. Invitez vos membres et lancez votre premier projet pour faire vibrer les 4 hubs.</p>
      <button class="btn-primary tap" onclick="window.__seed()"><span class="material-symbols-outlined">group_add</span>Inviter des membres</button>
    </div></div>
    <div class="sec">
      <div class="pulse" style="opacity:.55">${['community','learn','build','brand'].map(k => {
        const H = HUB[k];
        return `<div class="hub" style="--c:${H.c};min-height:120px"><div class="top"><div class="ico"><span class="material-symbols-outlined">${H.ico}</span></div></div><h3>${H.name}</h3><div class="meta">Aucune activité</div></div>`;
      }).join('')}</div>
    </div>`;
}

/* ============ DESKTOP RENDER ============ */
function renderDesktop(state) {
  const greet = greeting();
  const sync = state === 'error'
    ? `<button class="syncpill off tap"><span class="led"></span>Hors-ligne · cache</button>`
    : `<button class="syncpill tap"><span class="led"></span>Synchronisé</button>`;

  const head = `
    <div class="deskhead">
      <div>
        <div class="kick">${greet} Amara,<br>l'OS <em>en main</em>.</div>
        <div class="sub"><span class="material-symbols-outlined" style="font-size:18px;color:var(--secondary)">hub</span>${DATA.coop} · ${DATA.place}</div>
      </div>
      <div class="right">
        ${sync}
        <button class="icbtn tap" aria-label="Notifications"><span class="material-symbols-outlined">notifications</span><span class="dot-badge"></span></button>
        <button class="btn-primary tap" style="margin-top:0"><span class="material-symbols-outlined">bolt</span>Action rapide</button>
      </div>
    </div>`;

  if (state === 'loading') return head + skeletonDesktop();
  if (state === 'empty') return head + `<div class="b-card">${emptyMobile()}</div>`;

  const err = state === 'error' ? `<div class="errbar" style="margin:0 0 18px"><span class="material-symbols-outlined">cloud_off</span><div><b>Synchronisation échouée</b> — données du cache · 2 modifications en attente</div><button onclick="window.__retry()">Réessayer</button></div>` : '';

  return head + err + `
    <div class="bento">
      <div class="b-pulse">${hubCard('community')}</div>
      <div class="b-pulse">${hubCard('learn')}</div>
      <div class="b-spot">
        <div style="margin-bottom:14px;display:flex;align-items:center;justify-content:space-between"><h3 style="margin:0;font-size:16px;font-weight:700">Spotlight coopérative</h3></div>
        ${spotlight()}
      </div>
      <div class="b-actions b-card">
        <div class="hd"><h3>Aujourd'hui · Next best action</h3><span class="more" style="color:var(--primary);font-weight:700">${DATA.actions.length}</span></div>
        <div class="actions">${DATA.actions.map(actionItem).join('')}</div>
      </div>
      <div class="b-pulse">${hubCard('build')}</div>
      <div class="b-pulse">${hubCard('brand')}</div>
      <div class="b-feed b-card">
        <div class="hd"><h3>Activité cross-hub</h3><button class="more">Tout voir</button></div>
        <div class="feed">${DATA.feed.map(feedItem).join('')}</div>
      </div>
    </div>`;
}

function skeletonDesktop() {
  const c = `<div class="b-card" style="height:200px"><div class="skel" style="width:40px;height:40px;border-radius:12px"></div><div class="skel" style="width:60%;height:16px;margin-top:18px"></div><div class="skel" style="width:80%;height:11px;margin-top:12px"></div></div>`;
  const big = `<div class="b-card" style="grid-column:span 2;grid-row:span 2;height:416px"><div class="skel" style="width:100%;height:140px;border-radius:14px"></div><div class="skel" style="width:50%;height:18px;margin-top:16px"></div><div class="skel" style="width:80%;height:12px;margin-top:10px"></div></div>`;
  return `<div class="bento">${c}${c}${big}${big}${c}${c}</div>`;
}

/* ---------- greeting by time ---------- */
function greeting() {
  const hr = new Date().getHours();
  if (hr < 12) return 'Bonjour';
  if (hr < 18) return 'Bon après-midi';
  return 'Bonsoir';
}

/* ============ STATE / CONTROLS ============ */
const App = {
  device: localStorage.getItem('abc-device') || 'mobile',
  theme: localStorage.getItem('abc-theme') || 'dark',
  state: 'ready',
};

function paint() {
  document.documentElement.classList.toggle('dark', App.theme === 'dark');
  document.body.className = 'view-' + App.device;
  document.getElementById('m-scroll').innerHTML = renderMobile(App.state);
  document.getElementById('d-main').innerHTML = renderDesktop(App.state);
  syncSeg('seg-device', 'v', App.device);
  syncSeg('seg-theme', 't', App.theme);
  syncSeg('seg-state', 's', App.state);
  wire();
}
function syncSeg(id, attr, val) {
  document.querySelectorAll('#' + id + ' button').forEach(b => b.classList.toggle('on', b.dataset[attr] === val));
}
function wire() {
  const fab = document.getElementById('m-fab');
  if (fab) fab.onclick = () => toast('Action rapide — choisir un hub');
  const sync = document.getElementById('m-sync');
  if (sync) sync.onclick = () => { App.state = App.state === 'error' ? 'ready' : 'error'; paint(); };
}
window.__retry = () => { App.state = 'loading'; paint(); setTimeout(() => { App.state = 'ready'; paint(); }, 1400); };
window.__seed = () => { App.state = 'loading'; paint(); setTimeout(() => { App.state = 'ready'; paint(); }, 1200); };

function toast(msg) {
  const t = document.createElement('div');
  t.textContent = msg;
  t.style.cssText = 'position:fixed;left:50%;bottom:82px;transform:translateX(-50%);background:var(--surface-dark);color:#FBF3E4;padding:11px 18px;border-radius:13px;font:600 13px/1 "Space Grotesk";z-index:60;box-shadow:0 12px 30px rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.12)';
  document.body.appendChild(t);
  setTimeout(() => t.remove(), 1800);
}

/* control dock listeners */
document.getElementById('seg-device').addEventListener('click', e => {
  const b = e.target.closest('button'); if (!b) return;
  App.device = b.dataset.v; localStorage.setItem('abc-device', App.device); paint();
});
document.getElementById('seg-theme').addEventListener('click', e => {
  const b = e.target.closest('button'); if (!b) return;
  App.theme = b.dataset.t; localStorage.setItem('abc-theme', App.theme); paint();
});
document.getElementById('seg-state').addEventListener('click', e => {
  const b = e.target.closest('button'); if (!b) return;
  App.state = b.dataset.s; paint();
});

paint();
