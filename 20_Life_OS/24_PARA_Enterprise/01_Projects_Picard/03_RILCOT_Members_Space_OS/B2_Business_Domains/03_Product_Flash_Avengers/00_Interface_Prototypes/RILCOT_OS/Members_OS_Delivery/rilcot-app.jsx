/* RILCOT Members OS — unified Landing + Dashboard */

const { useState, useEffect, useRef, useMemo } = React;

/* ---------- Lucide icon helper (renders SVG as React children) ---------- */
function toPascal(s) {
  return s.split(/[-_]/).map(p => p ? p[0].toUpperCase() + p.slice(1) : '').join('');
}
function getLucideNode(name) {
  if (!window.lucide || !window.lucide.icons) return null;
  // try kebab name first, then PascalCase, then lower
  const icons = window.lucide.icons;
  return icons[name] || icons[toPascal(name)] || icons[name.toLowerCase()] || null;
}
const KEBAB_TO_CAMEL_SVG = {
  "stroke-width": "strokeWidth",
  "stroke-linecap": "strokeLinecap",
  "stroke-linejoin": "strokeLinejoin",
  "stroke-dasharray": "strokeDasharray",
  "stroke-dashoffset": "strokeDashoffset",
  "fill-rule": "fillRule",
  "clip-rule": "clipRule",
  "fill-opacity": "fillOpacity",
  "stroke-opacity": "strokeOpacity",
  "stop-color": "stopColor",
  "stop-opacity": "stopOpacity",
  "text-anchor": "textAnchor",
  "font-family": "fontFamily",
  "font-size": "fontSize",
  "font-weight": "fontWeight",
};
function svgAttrsToReact(attrs) {
  const out = {};
  for (const [k, v] of Object.entries(attrs || {})) {
    if (k === "class") out.className = v;
    else if (KEBAB_TO_CAMEL_SVG[k]) out[KEBAB_TO_CAMEL_SVG[k]] = v;
    else out[k] = v;
  }
  return out;
}
function renderLucideChildren(children) {
  if (!Array.isArray(children)) return null;
  return children.map((child, i) => {
    if (!Array.isArray(child)) return null;
    const [tag, props = {}] = child;
    return React.createElement(tag, { key: i, ...svgAttrsToReact(props) });
  });
}
function Icon({ name, className = "w-5 h-5", strokeWidth = 1.75 }) {
  const node = getLucideNode(name);
  // node shape: [tag, attrs, children] OR { toSvg, ... } depending on UMD version
  if (!node) {
    return <span className={className} aria-hidden="true" />;
  }
  // Array form
  if (Array.isArray(node)) {
    const [, attrs = {}, children = []] = node;
    const svgProps = { ...svgAttrsToReact(attrs), className, strokeWidth, "aria-hidden": "true" };
    return <svg {...svgProps}>{renderLucideChildren(children)}</svg>;
  }
  // Object with .toSvg (older versions)
  if (node && typeof node === 'object' && Array.isArray(node.children) && node.attrs) {
    const svgProps = { ...svgAttrsToReact(node.attrs), className, strokeWidth, "aria-hidden": "true" };
    return <svg {...svgProps}>{renderLucideChildren(node.children)}</svg>;
  }
  return <span className={className} aria-hidden="true" />;
}

/* ---------- SDG / ODD palette (UN colors) ---------- */
const SDG = {
  1: { c: "#E5243B", t: "Pas de pauvreté" },
  2: { c: "#DDA63A", t: "Faim zéro" },
  3: { c: "#4C9F38", t: "Bonne santé" },
  4: { c: "#C5192D", t: "Éducation" },
  5: { c: "#FF3A21", t: "Égalité genres" },
  6: { c: "#26BDE2", t: "Eau propre" },
  7: { c: "#FCC30B", t: "Énergie" },
  8: { c: "#A21942", t: "Travail décent" },
  9: { c: "#FD6925", t: "Innovation" },
  10:{ c: "#DD1367", t: "Inégalités" },
  11:{ c: "#FD9D24", t: "Villes durables" },
  12:{ c: "#BF8B2E", t: "Consommation" },
  13:{ c: "#3F7E44", t: "Climat" },
  14:{ c: "#0A97D9", t: "Vie aquatique" },
  15:{ c: "#56C02B", t: "Vie terrestre" },
  16:{ c: "#00689D", t: "Paix & Justice" },
  17:{ c: "#19486A", t: "Partenariats" },
};

function SdgBadge({ n, size = "sm" }) {
  const s = SDG[n]; if (!s) return null;
  const sz = size === "lg" ? "w-9 h-9 text-[11px]" : "w-7 h-7 text-[10px]";
  return (
    <span title={`ODD ${n} — ${s.t}`}
      style={{ background: s.c }}
      className={`${sz} rounded-md inline-flex items-center justify-center font-sans font-bold text-white tracking-tight ring-1 ring-black/5`}>
      {n}
    </span>
  );
}

/* ---------- Tiny logo ---------- */
function RilcotMark({ className = "w-8 h-8" }) {
  return (
    <svg viewBox="0 0 40 40" className={className} aria-label="RILCOT">
      <circle cx="20" cy="20" r="18.5" fill="#FAFAF9" stroke="#064E3B" strokeWidth="1.2"/>
      <circle cx="20" cy="20" r="12" fill="none" stroke="#064E3B" strokeWidth="0.8" strokeDasharray="1.5 2.5"/>
      <path d="M20 6 L23 20 L20 34 L17 20 Z" fill="#064E3B"/>
      <path d="M6 20 L20 17 L34 20 L20 23 Z" fill="#9A3412" opacity="0.9"/>
      <circle cx="20" cy="20" r="2.2" fill="#FAFAF9" stroke="#064E3B" strokeWidth="1.2"/>
    </svg>
  );
}

/* =====================================================
   TOP NAVIGATION (shared)
====================================================== */
function TopNav({ view, setView }) {
  return (
    <header className="sticky top-0 z-40 bg-cream/85 backdrop-blur-md border-b border-line">
      <div className="max-w-[1400px] mx-auto px-5 lg:px-8 h-16 flex items-center gap-6">
        <button onClick={() => setView("landing")} className="flex items-center gap-2.5 group">
          <RilcotMark className="w-9 h-9 transition-transform group-hover:rotate-12" />
          <div className="leading-none">
            <div className="font-display text-[17px] font-bold text-forest-900 tracking-tight">RILCOT</div>
            <div className="text-[10px] uppercase tracking-[0.18em] text-ink-500 mt-0.5 font-sans font-medium">Members OS</div>
          </div>
        </button>

        {/* Tab switcher */}
        <div className="hidden md:flex items-center bg-cream-warm/60 rounded-lg p-1 ml-2 border border-line/70">
          {[
            { id: "landing",   label: "Vitrine",       icon: "globe" },
            { id: "os",        label: "RILCOT OS",     icon: "compass" },
            { id: "dashboard", label: "Member Space",  icon: "layout-dashboard" },
          ].map(t => (
            <button key={t.id} onClick={() => setView(t.id)}
              className={`relative px-3.5 py-1.5 rounded-md text-sm font-sans font-medium flex items-center gap-1.5 transition-all
                ${view === t.id ? "bg-white text-forest-900 tab-active" : "text-ink-700 hover:text-forest-900"}`}>
              <Icon name={t.icon} className="w-4 h-4" />
              {t.label}
            </button>
          ))}
        </div>

        <div className="flex-1" />

        {/* Right utilities */}
        <div className="hidden lg:flex items-center gap-1.5 text-sm text-ink-700">
          <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-forest-50 text-forest-800 font-sans font-medium text-xs">
            <span className="w-1.5 h-1.5 rounded-full bg-forest-600 pulse-dot" />
            AG Ordinaire — 14 juin
          </span>
        </div>

        <div className="hidden md:flex items-center gap-2 pl-3 ml-1 border-l border-line">
          <button className="w-9 h-9 rounded-md hover:bg-cream-warm/70 flex items-center justify-center text-ink-700"><Icon name="search" className="w-4 h-4" /></button>
          <button className="w-9 h-9 rounded-md hover:bg-cream-warm/70 flex items-center justify-center text-ink-700 relative">
            <Icon name="bell" className="w-4 h-4" />
            <span className="absolute top-1.5 right-1.5 w-1.5 h-1.5 bg-terra-600 rounded-full" />
          </button>
          <div className="w-9 h-9 rounded-full bg-gradient-to-br from-forest-800 to-forest-950 flex items-center justify-center text-white font-sans font-semibold text-xs ring-2 ring-cream">AT</div>
        </div>

        {/* Mobile tabs */}
        <div className="md:hidden flex items-center bg-cream-warm/60 rounded-lg p-1 border border-line/70">
          {[
            { id: "landing",   icon: "globe" },
            { id: "os",        icon: "compass" },
            { id: "dashboard", icon: "layout-dashboard" },
          ].map(t => (
            <button key={t.id} onClick={() => setView(t.id)}
              className={`px-2.5 py-1.5 rounded-md ${view === t.id ? "bg-white tab-active text-forest-900" : "text-ink-500"}`}>
              <Icon name={t.icon} className="w-4 h-4" />
            </button>
          ))}
        </div>
      </div>
    </header>
  );
}

/* =====================================================
   LANDING PAGE  (Front-stage / Vitrine)
====================================================== */
function Landing({ setView }) {
  return (
    <main className="min-h-screen">

      {/* ===== HERO ===== */}
      <section className="relative hero-pattern overflow-hidden">
        <div className="absolute inset-0 grain opacity-60 pointer-events-none" />
        <div className="absolute -right-32 top-10 w-[460px] h-[460px] rounded-full compass-ring opacity-70 pointer-events-none hidden lg:block" />
        <div className="absolute -right-16 top-32 w-[300px] h-[300px] rounded-full border border-forest-900/15 pointer-events-none hidden lg:block" />

        <div className="max-w-[1400px] mx-auto px-5 lg:px-8 pt-14 lg:pt-24 pb-20 lg:pb-32 relative">
          {/* Eyebrow */}
          <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/70 border border-line text-xs font-sans font-medium text-forest-900 tracking-wide shadow-soft-sm">
            <span className="w-1.5 h-1.5 rounded-full bg-terra-600" />
            Réseau Institutionnel — Édition 2026
            <span className="text-ink-400">·</span>
            <span className="text-ink-500">Cohorte VII ouverte</span>
          </div>

          <div className="mt-7 grid lg:grid-cols-12 gap-10 lg:gap-14 items-end">
            <div className="lg:col-span-7">
              <h1 className="font-display text-[44px] sm:text-[62px] lg:text-[78px] leading-[0.95] tracking-[-0.02em] text-forest-950">
                Forger l'Avenir<br/>
                du <span className="italic font-medium text-terra-700">Leadership</span> Africain.
              </h1>
              <p className="mt-7 text-lg lg:text-xl text-ink-700 max-w-xl leading-relaxed font-body">
                Catalyser le changement éthique et transformationnel à travers le continent.
                Une boussole pour les bâtisseurs d'institutions, les jeunes leaders et les entrepreneurs engagés.
              </p>

              <div className="mt-9 flex flex-wrap items-center gap-3">
                <button className="group h-12 px-6 rounded-lg bg-forest-900 hover:bg-forest-950 text-white font-sans font-semibold text-[15px] flex items-center gap-2 shadow-soft-md transition">
                  Devenez Membre
                  <Icon name="arrow-up-right" className="w-4 h-4 transition-transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
                </button>
                <button className="h-12 px-6 rounded-lg bg-white hover:bg-cream-warm/60 border border-line text-forest-900 font-sans font-semibold text-[15px] flex items-center gap-2 transition">
                  <Icon name="compass" className="w-4 h-4 text-terra-700" />
                  Découvrir nos piliers
                </button>
                <button onClick={() => setView("dashboard")}
                  className="h-12 px-4 rounded-lg text-ink-700 hover:text-forest-900 font-sans font-medium text-[15px] flex items-center gap-1.5 transition">
                  Entrer dans le Member OS
                  <Icon name="chevron-right" className="w-4 h-4" />
                </button>
              </div>

              {/* trust strip */}
              <div className="mt-12 flex items-center gap-6 lg:gap-9 text-ink-500 text-xs font-sans uppercase tracking-[0.16em]">
                <span>Avec</span>
                <span className="text-ink-700 font-semibold">UA — CIEFFA</span>
                <span className="text-line">·</span>
                <span className="text-ink-700 font-semibold">PNUD</span>
                <span className="text-line">·</span>
                <span className="text-ink-700 font-semibold hidden sm:inline">CAMES</span>
                <span className="text-line hidden sm:inline">·</span>
                <span className="text-ink-700 font-semibold hidden md:inline">AfDB Academy</span>
              </div>
            </div>

            {/* Side card — Live indicators */}
            <div className="lg:col-span-5">
              <div className="bg-white rounded-2xl border border-line shadow-soft-lg p-6 lg:p-7">
                <div className="flex items-center justify-between">
                  <div>
                    <div className="text-[11px] uppercase tracking-[0.18em] text-ink-500 font-sans font-semibold">Télémétrie publique</div>
                    <div className="font-display text-2xl text-forest-950 mt-1">L'impact en temps réel</div>
                  </div>
                  <div className="text-[10px] font-mono text-ink-500 inline-flex items-center gap-1.5">
                    <span className="w-1.5 h-1.5 rounded-full bg-forest-600 pulse-dot" /> LIVE
                  </div>
                </div>

                <div className="mt-6 grid grid-cols-2 gap-3">
                  <Stat label="Membres actifs"        value="1 204" delta="+5.2%" tone="forest"/>
                  <Stat label="Projets ouverts"       value="28"    delta="+3"    tone="terra"/>
                  <Stat label="Pays représentés"      value="34"    delta="+2"    tone="forest" muted/>
                  <Stat label="Bénéficiaires"         value="412k"  delta="+18%"  tone="terra"  muted/>
                </div>

                <div className="mt-6 pt-5 border-t border-line">
                  <div className="text-[11px] uppercase tracking-[0.18em] text-ink-500 font-sans font-semibold mb-3">ODD prioritaires 2026</div>
                  <div className="flex flex-wrap gap-1.5">
                    {[4,5,8,9,11,13,16,17].map(n => <SdgBadge key={n} n={n} />)}
                  </div>
                </div>

                <div className="mt-5 flex items-center justify-between text-xs text-ink-500 font-sans">
                  <span>Audit trimestriel · Q1 2026</span>
                  <a className="text-forest-800 font-semibold inline-flex items-center gap-1 hover:gap-1.5 transition-all" href="#">
                    Rapport <Icon name="arrow-right" className="w-3.5 h-3.5" />
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="stripe-divider" />
      </section>

      {/* ===== 4 PILIERS ===== */}
      <section className="max-w-[1400px] mx-auto px-5 lg:px-8 py-20 lg:py-28">
        <div className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-6 mb-12">
          <div>
            <div className="text-[11px] uppercase tracking-[0.2em] text-terra-700 font-sans font-bold mb-3">04 · Architecture d'action</div>
            <h2 className="font-display text-4xl lg:text-5xl text-forest-950 tracking-tight leading-[1.05] max-w-2xl">
              Les quatre piliers <span className="italic text-terra-700">structurants</span>.
            </h2>
          </div>
          <p className="text-ink-700 max-w-md font-body leading-relaxed">
            Chaque action menée par le réseau s'inscrit dans l'un de ces quatre piliers,
            avec des protocoles de mesure et de redevabilité partagés.
          </p>
        </div>

        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4 lg:gap-5">
          <Pilier
            num="01"
            icon="scale"
            title="Gouvernance Éthique"
            text="Cadres, chartes et observatoires de l'intégrité institutionnelle."
            metric="14 chartes adoptées"
            tone="forest"
            sdg={[16, 17]}
          />
          <Pilier
            num="02"
            icon="graduation-cap"
            title="Leadership des Jeunes"
            text="Académies, mentorat et résidences de transformation pour la relève."
            metric="640 alumni · 6 cohortes"
            tone="terra"
            sdg={[4, 5]}
          />
          <Pilier
            num="03"
            icon="lightbulb"
            title="Entrepreneuriat Durable"
            text="Incubation, finance patiente et chaînes de valeur africaines."
            metric="92 startups · €4,2M déployés"
            tone="forest"
            sdg={[8, 9]}
          />
          <Pilier
            num="04"
            icon="users"
            title="Engagement Communautaire"
            text="Ancrage territorial, dialogues citoyens et résilience locale."
            metric="34 pays · 210 communes"
            tone="terra"
            sdg={[11, 13]}
          />
        </div>
      </section>

      {/* ===== METHOD STRIP ===== */}
      <section className="bg-forest-950 text-cream relative overflow-hidden">
        <div className="absolute -left-32 -bottom-32 w-[400px] h-[400px] rounded-full bg-terra-700/20 blur-3xl" />
        <div className="absolute right-0 top-0 w-[300px] h-[300px] rounded-full bg-forest-700/30 blur-3xl" />
        <div className="max-w-[1400px] mx-auto px-5 lg:px-8 py-20 lg:py-24 relative">
          <div className="grid lg:grid-cols-12 gap-10">
            <div className="lg:col-span-5">
              <div className="text-[11px] uppercase tracking-[0.2em] text-terra-200 font-sans font-bold mb-3">La méthode RILCOT</div>
              <h2 className="font-display text-4xl lg:text-5xl tracking-tight leading-[1.05]">
                Une boussole, pas un<br/>simple <span className="italic">programme</span>.
              </h2>
              <p className="mt-6 text-cream/80 leading-relaxed max-w-md">
                Trois cycles annuels alignés sur les rituels de gouvernance,
                avec une exécution mesurée trimestre par trimestre, en pleine transparence.
              </p>
            </div>
            <div className="lg:col-span-7 grid sm:grid-cols-3 gap-px bg-forest-800/60 rounded-xl overflow-hidden">
              {[
                { n: "I",   t: "Diagnostic & Cadrage",    d: "Audit éthique, cartographie d'acteurs, contrat d'engagement.", w: "Janv. — Mars" },
                { n: "II",  t: "Exécution & Cohortes",    d: "Mise en œuvre par les chapitres territoriaux et les commissions.", w: "Avr. — Sept." },
                { n: "III", t: "Redevabilité & Forum",    d: "Indicateurs ODD publiés, AG ordinaire, restitution citoyenne.",  w: "Oct. — Déc." },
              ].map(s => (
                <div key={s.n} className="bg-forest-950 p-6 lg:p-7">
                  <div className="font-display text-3xl text-terra-200 italic">Cycle {s.n}</div>
                  <div className="font-sans font-semibold mt-3 text-cream">{s.t}</div>
                  <div className="text-sm text-cream/70 mt-2 leading-relaxed font-body">{s.d}</div>
                  <div className="mt-5 text-[11px] uppercase tracking-[0.18em] text-cream/50 font-sans font-medium">{s.w}</div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* ===== JOIN / FOOTER LITE ===== */}
      <section className="max-w-[1400px] mx-auto px-5 lg:px-8 py-20 lg:py-24">
        <div className="grid lg:grid-cols-12 gap-8 items-center">
          <div className="lg:col-span-7">
            <h3 className="font-display text-3xl lg:text-4xl text-forest-950 tracking-tight leading-[1.1]">
              Rejoindre la cohorte VII <span className="italic text-terra-700">— ouverture le 1<sup>er</sup> juillet.</span>
            </h3>
            <p className="mt-4 text-ink-700 max-w-xl">
              Trois parcours d'entrée : Académie Jeunes Leaders, Chapitre Territorial, et Cercle des Institutions Partenaires.
            </p>
          </div>
          <div className="lg:col-span-5 flex flex-wrap gap-3 lg:justify-end">
            <button className="h-12 px-6 rounded-lg bg-forest-900 hover:bg-forest-950 text-white font-sans font-semibold text-[15px] flex items-center gap-2 shadow-soft-md transition">
              Postuler à la cohorte VII
              <Icon name="send" className="w-4 h-4" />
            </button>
            <button onClick={() => setView("dashboard")} className="h-12 px-6 rounded-lg border border-line bg-white hover:bg-cream-warm/60 text-forest-900 font-sans font-semibold text-[15px] flex items-center gap-2 transition">
              Espace Membres
              <Icon name="log-in" className="w-4 h-4" />
            </button>
          </div>
        </div>

        <div className="mt-16 pt-8 border-t border-line flex flex-col md:flex-row md:items-center md:justify-between gap-4 text-sm text-ink-500 font-sans">
          <div className="flex items-center gap-2.5">
            <RilcotMark className="w-7 h-7" />
            <span className="text-ink-700 font-semibold">RILCOT</span>
            <span>· Réseau Institutionnel pour le Leadership Communautaire et la Transformation</span>
          </div>
          <div className="flex items-center gap-5">
            <a className="hover:text-forest-900">Charte éthique</a>
            <a className="hover:text-forest-900">Gouvernance</a>
            <a className="hover:text-forest-900">Presse</a>
            <a className="hover:text-forest-900">Contact</a>
          </div>
        </div>
      </section>
    </main>
  );
}

/* ---------- Landing sub-components ---------- */
function Stat({ label, value, delta, tone = "forest", muted = false }) {
  const tones = {
    forest: "text-forest-800 bg-forest-50",
    terra:  "text-terra-700 bg-terra-50",
  };
  return (
    <div className={`p-3 rounded-lg ${muted ? "bg-cream-warm/40" : "bg-cream"} border border-line/70`}>
      <div className="text-[11px] uppercase tracking-[0.14em] text-ink-500 font-sans font-medium">{label}</div>
      <div className="mt-1.5 flex items-baseline gap-2">
        <div className="font-display text-[26px] text-forest-950 leading-none num">{value}</div>
        <span className={`text-[10px] px-1.5 py-0.5 rounded-md font-sans font-semibold ${tones[tone]}`}>{delta}</span>
      </div>
    </div>
  );
}

function Pilier({ num, icon, title, text, metric, tone = "forest", sdg = [] }) {
  const accent = tone === "forest" ? "text-forest-900" : "text-terra-700";
  const dot    = tone === "forest" ? "bg-forest-900" : "bg-terra-700";
  return (
    <div className="group bg-white rounded-xl border border-line p-6 lg:p-7 shadow-soft-sm hover:shadow-soft-lg hover:-translate-y-0.5 transition-all duration-300 relative overflow-hidden">
      <div className={`absolute left-0 top-0 w-1 h-0 ${dot} group-hover:h-full transition-all duration-500`} />
      <div className="flex items-start justify-between">
        <div className={`w-11 h-11 rounded-lg flex items-center justify-center ${tone === "forest" ? "bg-forest-50 text-forest-900" : "bg-terra-50 text-terra-700"}`}>
          <Icon name={icon} className="w-5 h-5" strokeWidth={1.6} />
        </div>
        <span className="font-mono text-[11px] text-ink-400">{num}</span>
      </div>
      <h3 className={`mt-5 font-display text-2xl ${accent} tracking-tight`}>{title}</h3>
      <p className="mt-2.5 text-sm text-ink-700 leading-relaxed font-body">{text}</p>

      <div className="mt-6 pt-4 border-t border-line/70 flex items-center justify-between">
        <div className="text-xs font-sans font-semibold text-ink-700 num">{metric}</div>
        <div className="flex gap-1">{sdg.map(n => <SdgBadge key={n} n={n} />)}</div>
      </div>
    </div>
  );
}

/* =====================================================
   DASHBOARD  (Back-stage / Member OS)
====================================================== */
const SIDEBAR = [
  { id: "home",    label: "Accueil",                icon: "home" },
  { id: "people",  label: "Annuaire & Communauté",  icon: "users-round" },
  { id: "projects",label: "Projets & Impact",       icon: "rocket" },
  { id: "gov",     label: "Gouvernance",            icon: "landmark" },
  { id: "univ",    label: "Réseau Universités",     icon: "graduation-cap" },
];

function Dashboard({ setView }) {
  const [active, setActive] = useState("home");
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className="flex min-h-[calc(100vh-64px)]">
      {/* ===== SIDEBAR ===== */}
      <aside className={`fixed lg:static inset-y-0 left-0 z-30 w-[260px] bg-white border-r border-line flex-col
        ${sidebarOpen ? "flex" : "hidden lg:flex"} top-16 lg:top-auto`}>
        <div className="p-5 border-b border-line">
          <div className="text-[10px] uppercase tracking-[0.18em] text-ink-500 font-sans font-semibold mb-3">Chapitre</div>
          <button className="w-full flex items-center gap-2.5 p-2.5 rounded-lg hover:bg-cream-warm/60 transition group">
            <div className="w-8 h-8 rounded-md bg-gradient-to-br from-forest-800 to-forest-950 text-white flex items-center justify-center font-sans font-bold text-xs">CI</div>
            <div className="flex-1 text-left">
              <div className="font-sans font-semibold text-sm text-forest-950">Côte d'Ivoire — Abidjan</div>
              <div className="text-[11px] text-ink-500">86 membres actifs</div>
            </div>
            <Icon name="chevrons-up-down" className="w-4 h-4 text-ink-400" />
          </button>
        </div>

        <nav className="flex-1 p-3 space-y-0.5">
          {SIDEBAR.map(item => {
            const isActive = active === item.id;
            return (
              <button key={item.id} onClick={() => { setActive(item.id); setSidebarOpen(false); }}
                className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-[14px] font-sans font-medium transition-all group relative
                  ${isActive
                    ? "bg-forest-50 text-forest-900"
                    : "text-ink-700 hover:bg-cream-warm/60 hover:text-forest-900"}`}>
                {isActive && <span className="absolute left-0 top-1.5 bottom-1.5 w-[3px] bg-forest-900 rounded-r-full" />}
                <Icon name={item.icon} className={`w-[18px] h-[18px] ${isActive ? "text-forest-900" : "text-ink-500 group-hover:text-forest-800"}`} />
                <span className="flex-1 text-left">{item.label}</span>
                {item.id === "projects" && <span className="text-[10px] font-mono text-terra-700 bg-terra-50 px-1.5 py-0.5 rounded">28</span>}
                {item.id === "gov" && <span className="w-1.5 h-1.5 rounded-full bg-terra-600 pulse-dot" />}
              </button>
            );
          })}

          <div className="pt-5 mt-3 border-t border-line">
            <div className="px-3 text-[10px] uppercase tracking-[0.18em] text-ink-400 font-sans font-semibold mb-1.5">Commissions</div>
            {[
              { l: "Éthique & Audit",   i: "shield-check" },
              { l: "Finances",          i: "wallet" },
              { l: "Communication",     i: "megaphone" },
            ].map(c => (
              <button key={c.l} className="w-full flex items-center gap-3 px-3 py-2 rounded-lg text-[13px] text-ink-700 hover:bg-cream-warm/60 hover:text-forest-900 transition">
                <Icon name={c.i} className="w-4 h-4 text-ink-400" />
                {c.l}
              </button>
            ))}
          </div>
        </nav>

        <div className="p-4 border-t border-line">
          <div className="rounded-lg bg-gradient-to-br from-forest-900 to-forest-950 p-4 text-cream relative overflow-hidden">
            <div className="absolute -right-6 -top-6 w-20 h-20 rounded-full bg-terra-600/30 blur-2xl" />
            <div className="font-display text-[15px] text-cream leading-tight">Boussole Q2</div>
            <div className="text-[11px] text-cream/70 mt-1">Auto-évaluation mensuelle</div>
            <button className="mt-3 text-[11px] inline-flex items-center gap-1 bg-cream text-forest-950 px-2.5 py-1 rounded-md font-sans font-semibold">
              Démarrer <Icon name="arrow-right" className="w-3 h-3" />
            </button>
          </div>
        </div>
      </aside>

      {/* ===== MAIN ===== */}
      <div className="flex-1 min-w-0">
        {/* Mobile sidebar toggle */}
        <div className="lg:hidden px-5 pt-4">
          <button onClick={() => setSidebarOpen(s => !s)}
            className="inline-flex items-center gap-2 px-3 py-2 rounded-lg border border-line bg-white text-sm text-ink-700 shadow-soft-sm">
            <Icon name={sidebarOpen ? "x" : "menu"} className="w-4 h-4" />
            {sidebarOpen ? "Fermer" : "Menu OS"}
          </button>
        </div>

        {active === "home"     && <HomeView/>}
        {active === "people"   && <PlaceholderView title="Annuaire & Communauté" icon="users-round" />}
        {active === "projects" && <ProjectsView/>}
        {active === "gov"      && <GovView/>}
        {active === "univ"     && <PlaceholderView title="Réseau Universités" icon="graduation-cap" />}
      </div>
    </div>
  );
}

/* ---------- HOME view (the main dashboard) ---------- */
function HomeView() {
  return (
    <div className="p-5 lg:p-8 max-w-[1180px] mx-auto">
      {/* Welcome / breadcrumb */}
      <div className="flex flex-col md:flex-row md:items-end md:justify-between gap-5 mb-8">
        <div>
          <div className="flex items-center gap-2 text-[11px] uppercase tracking-[0.18em] text-ink-500 font-sans font-semibold">
            <Icon name="home" className="w-3 h-3" />
            Member OS · Accueil
            <span className="text-line">/</span>
            <span className="text-forest-800">Mardi 18 mai · S20</span>
          </div>
          <h1 className="mt-3 font-display text-3xl lg:text-[40px] text-forest-950 tracking-tight leading-tight">
            Bienvenue sur RILCOT&nbsp;OS, <span className="italic text-terra-700">Aïcha</span>.
          </h1>
          <p className="mt-2 text-ink-700 max-w-xl font-body">
            Trois rituels cette semaine, deux signatures de gouvernance en attente, et un nouveau jalon ODD à célébrer.
          </p>
        </div>
        <div className="flex flex-wrap items-center gap-2.5">
          <button className="h-10 px-4 rounded-lg bg-forest-900 hover:bg-forest-950 text-white font-sans font-semibold text-sm flex items-center gap-2 shadow-soft-sm transition">
            <Icon name="plus" className="w-4 h-4" />
            Proposer un projet
          </button>
          <button className="h-10 px-4 rounded-lg bg-white border border-line hover:bg-cream-warm/60 text-forest-900 font-sans font-semibold text-sm flex items-center gap-2 transition">
            <Icon name="calendar-days" className="w-4 h-4 text-terra-700" />
            Voir l'Agenda
          </button>
        </div>
      </div>

      {/* ===== KPI Telemetry ===== */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-3 lg:gap-4 mb-10">
        <KpiCard label="Membres actifs"        value="1 204" delta="+5.2%" trend="up"
          spark={[8,11,9,13,12,15,14,17,16,19,18,22]}  icon="users-round" tone="forest"
          sub="86 nouveaux ce trimestre"/>
        <KpiCard label="Exécution budgétaire"  value="76%"   delta="+4 pts" trend="up"
          ring={76} icon="wallet" tone="terra"
          sub="€2,1M sur €2,76M engagés"/>
        <KpiCard label="Projets en cours"      value="28"    delta="+3" trend="up"
          spark={[3,5,4,6,5,7,6,8,7,9,8,11]} icon="rocket" tone="forest"
          sub="6 en phase d'audit final"/>
        <KpiCard label="Score d'intégrité"     value="A−"    delta="stable" trend="flat"
          ring={92} icon="shield-check" tone="terra" sub="Audit indépendant CIE"/>
      </div>

      {/* ===== Portefeuille + Agenda ===== */}
      <div className="grid lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 space-y-6">
          <SectionHeader
            kicker="Portefeuille"
            title="Projets prioritaires"
            sub="Sélection commission éthique · Q2 2026"
            cta="Voir les 28 projets"
          />
          <div className="grid md:grid-cols-2 gap-4">
            <ProjectCard
              code="α-24"
              status="En exécution"
              statusTone="forest"
              title="Programme Alpha 2024"
              desc="Académie panafricaine pour 240 jeunes leaders, 3 cohortes synchronisées."
              lead={{ name: "Dr. Mariama Diop", role: "Lead — Dakar", initials: "MD" }}
              progress={68}
              beneficiaries="240 leaders"
              budget="€480 000"
              sdg={[4,5,8]}
              tone="forest"
              chapter="Pan-africain"
            />
            <ProjectCard
              code="ε-18"
              status="Phase pilote"
              statusTone="terra"
              title="Initiative Eau Propre"
              desc="Forages solaires & gouvernance villageoise dans 18 communes du Sahel."
              lead={{ name: "Boubacar Touré", role: "Lead — Mopti", initials: "BT" }}
              progress={42}
              beneficiaries="34 200 hab."
              budget="€720 000"
              sdg={[6,11,13]}
              tone="terra"
              chapter="Sahel"
            />
            <ProjectCard
              code="κ-07"
              status="Audit final"
              statusTone="forest"
              title="Charte d'Intégrité Locale"
              desc="Codes éthiques pour 12 collectivités, signature publique au Forum d'octobre."
              lead={{ name: "Aïssatou Ba", role: "Lead — Kigali", initials: "AB" }}
              progress={91}
              beneficiaries="12 collectivités"
              budget="€140 000"
              sdg={[16,17]}
              tone="forest"
              chapter="Afrique de l'Est"
            />
            <ProjectCard
              code="ω-02"
              status="Cadrage"
              statusTone="muted"
              title="Boussole Entrepreneuriale"
              desc="Finance patiente & mentorat pour 60 PME dirigées par des femmes."
              lead={{ name: "Linda Mwangi", role: "Lead — Nairobi", initials: "LM" }}
              progress={18}
              beneficiaries="60 PME"
              budget="€310 000"
              sdg={[5,8,9]}
              tone="terra"
              chapter="Afrique de l'Est"
            />
          </div>
        </div>

        {/* Agenda */}
        <div className="space-y-6">
          <SectionHeader
            kicker="Rituels"
            title="Agenda & Gouvernance"
            sub="Prochains 14 jours"
            cta="Calendrier"
          />
          <AgendaList/>
          <PulseCard/>
        </div>
      </div>

      {/* ===== Network band ===== */}
      <div className="mt-12 bg-white border border-line rounded-xl p-6 lg:p-7 shadow-soft-sm">
        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-5">
          <div>
            <div className="text-[11px] uppercase tracking-[0.18em] text-ink-500 font-sans font-semibold">Réseau · 34 chapitres</div>
            <h3 className="font-display text-2xl text-forest-950 mt-1">Pouls des chapitres territoriaux</h3>
          </div>
          <div className="flex items-center gap-2 text-xs font-sans">
            <span className="inline-flex items-center gap-1.5 px-2 py-1 rounded bg-forest-50 text-forest-800 font-semibold"><span className="w-1.5 h-1.5 bg-forest-600 rounded-full" /> Actif</span>
            <span className="inline-flex items-center gap-1.5 px-2 py-1 rounded bg-terra-50 text-terra-700 font-semibold"><span className="w-1.5 h-1.5 bg-terra-600 rounded-full" /> Sous suivi</span>
            <span className="inline-flex items-center gap-1.5 px-2 py-1 rounded bg-cream-warm/60 text-ink-500 font-semibold"><span className="w-1.5 h-1.5 bg-ink-300 rounded-full" /> En cadrage</span>
          </div>
        </div>

        <div className="mt-5 grid grid-cols-3 sm:grid-cols-5 lg:grid-cols-8 gap-2">
          {[
            ["Dakar","forest"],["Abidjan","forest"],["Bamako","terra"],["Cotonou","forest"],
            ["Lomé","muted"],["Niamey","terra"],["Yaoundé","forest"],["Libreville","muted"],
            ["Kinshasa","forest"],["Kigali","forest"],["Nairobi","forest"],["Addis","terra"],
            ["Tunis","forest"],["Rabat","forest"],["Maputo","muted"],["Le Cap","forest"],
          ].map(([city,tone]) => (
            <div key={city} className={`p-3 rounded-lg border text-xs font-sans
              ${tone === "forest" ? "bg-forest-50/60 border-forest-100 text-forest-900" :
                tone === "terra"  ? "bg-terra-50/60 border-terra-100 text-terra-800" :
                "bg-cream-warm/40 border-line text-ink-500"}`}>
              <div className="font-semibold">{city}</div>
              <div className="num text-[11px] opacity-80 mt-0.5">{Math.round(Math.random()*60+12)} m.</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

/* ---------- Section header ---------- */
function SectionHeader({ kicker, title, sub, cta }) {
  return (
    <div className="flex items-end justify-between gap-3">
      <div>
        <div className="text-[11px] uppercase tracking-[0.18em] text-terra-700 font-sans font-bold">{kicker}</div>
        <div className="font-display text-2xl text-forest-950 mt-1 leading-tight">{title}</div>
        {sub && <div className="text-xs text-ink-500 mt-0.5 font-sans">{sub}</div>}
      </div>
      {cta && <button className="text-xs font-sans font-semibold text-forest-900 hover:text-forest-700 inline-flex items-center gap-1">{cta}<Icon name="arrow-right" className="w-3.5 h-3.5"/></button>}
    </div>
  );
}

/* ---------- KPI Card ---------- */
function KpiCard({ label, value, delta, trend, spark, ring, icon, tone="forest", sub }) {
  const iconBg = tone === "forest" ? "bg-forest-50 text-forest-800" : "bg-terra-50 text-terra-700";
  const trendStyles = {
    up:   "bg-forest-50 text-forest-800",
    down: "bg-terra-50  text-terra-700",
    flat: "bg-cream-warm/60 text-ink-500"
  };
  return (
    <div className="group bg-white border border-line rounded-xl p-5 shadow-soft-sm hover:shadow-soft-md transition-all hover:-translate-y-0.5">
      <div className="flex items-start justify-between">
        <div className={`w-9 h-9 rounded-lg flex items-center justify-center ${iconBg}`}>
          <Icon name={icon} className="w-4 h-4" />
        </div>
        <span className={`inline-flex items-center gap-1 text-[10px] font-sans font-semibold px-1.5 py-0.5 rounded ${trendStyles[trend]}`}>
          <Icon name={trend === "up" ? "trending-up" : trend === "down" ? "trending-down" : "minus"} className="w-2.5 h-2.5"/>
          {delta}
        </span>
      </div>
      <div className="mt-4 text-[11px] uppercase tracking-[0.14em] text-ink-500 font-sans font-medium">{label}</div>
      <div className="mt-1.5 flex items-end gap-3">
        <div className="font-display text-[34px] text-forest-950 leading-none num">{value}</div>
        {spark && <Spark data={spark} tone={tone}/>}
        {ring != null && <Ring pct={ring} tone={tone}/>}
      </div>
      {sub && <div className="mt-3 pt-3 border-t border-line/70 text-[11px] text-ink-500 font-body">{sub}</div>}
    </div>
  );
}

function Spark({ data, tone="forest" }) {
  const w = 92, h = 30, pad = 2;
  const min = Math.min(...data), max = Math.max(...data);
  const sx = (i) => pad + (i*(w-2*pad))/(data.length-1);
  const sy = (v) => h - pad - ((v-min)/(max-min || 1))*(h-2*pad);
  const d = data.map((v,i) => `${i?'L':'M'}${sx(i).toFixed(1)},${sy(v).toFixed(1)}`).join(' ');
  const stroke = tone === "forest" ? "#064E3B" : "#9A3412";
  const fill   = tone === "forest" ? "rgba(6,78,59,0.08)" : "rgba(154,52,18,0.08)";
  return (
    <svg width={w} height={h} className="ml-auto">
      <path d={`${d} L${(w-pad).toFixed(1)},${h-pad} L${pad},${h-pad}Z`} fill={fill}/>
      <path d={d} fill="none" stroke={stroke} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
      <circle cx={sx(data.length-1)} cy={sy(data[data.length-1])} r="2.2" fill={stroke}/>
    </svg>
  );
}

function Ring({ pct, tone="forest" }) {
  const r = 13, c = 2*Math.PI*r;
  const stroke = tone === "forest" ? "#064E3B" : "#9A3412";
  return (
    <svg width="36" height="36" className="ml-auto -mr-1">
      <circle cx="18" cy="18" r={r} fill="none" stroke="#EAE6DD" strokeWidth="3"/>
      <circle cx="18" cy="18" r={r} fill="none" stroke={stroke} strokeWidth="3"
        strokeDasharray={c} strokeDashoffset={c*(1-pct/100)}
        strokeLinecap="round" transform="rotate(-90 18 18)"/>
      <text x="18" y="21" textAnchor="middle" fontSize="9" fontFamily="Inter" fontWeight="600" fill="#1B1B18">{pct}</text>
    </svg>
  );
}

/* ---------- Project Card ---------- */
function ProjectCard({ code, status, statusTone, title, desc, lead, progress, beneficiaries, budget, sdg, tone, chapter }) {
  const statusStyles = {
    forest: "bg-forest-50 text-forest-800 border-forest-100",
    terra:  "bg-terra-50  text-terra-700 border-terra-100",
    muted:  "bg-cream-warm/60 text-ink-500 border-line"
  };
  const barColor = tone === "forest" ? "bg-forest-800" : "bg-terra-600";

  return (
    <div className="group bg-white border border-line rounded-xl p-5 shadow-soft-sm hover:shadow-soft-md hover:-translate-y-0.5 transition-all relative overflow-hidden">
      <div className={`absolute right-0 top-0 w-32 h-32 rounded-full blur-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-500
        ${tone === "forest" ? "bg-forest-100" : "bg-terra-100"}`}/>

      <div className="flex items-center justify-between relative">
        <div className="flex items-center gap-2">
          <span className="font-mono text-[11px] text-ink-400">{code}</span>
          <span className={`text-[10px] uppercase tracking-[0.14em] font-sans font-semibold px-2 py-0.5 rounded border ${statusStyles[statusTone]}`}>{status}</span>
        </div>
        <button className="w-7 h-7 rounded-md text-ink-400 hover:text-forest-900 hover:bg-cream-warm/60 flex items-center justify-center transition">
          <Icon name="more-horizontal" className="w-4 h-4"/>
        </button>
      </div>

      <h3 className="mt-3 font-display text-xl text-forest-950 leading-tight">{title}</h3>
      <p className="mt-1.5 text-sm text-ink-700 leading-relaxed font-body line-clamp-2">{desc}</p>

      {/* Lead */}
      <div className="mt-4 flex items-center gap-2.5">
        <div className={`w-8 h-8 rounded-full flex items-center justify-center text-white text-[11px] font-sans font-bold
          ${tone === "forest" ? "bg-gradient-to-br from-forest-800 to-forest-950" : "bg-gradient-to-br from-terra-600 to-terra-800"}`}>
          {lead.initials}
        </div>
        <div className="leading-tight">
          <div className="text-[13px] font-sans font-semibold text-ink-900">{lead.name}</div>
          <div className="text-[11px] text-ink-500">{lead.role}</div>
        </div>
        <div className="ml-auto text-[10px] text-ink-400 font-mono uppercase">{chapter}</div>
      </div>

      {/* Progress */}
      <div className="mt-4">
        <div className="flex items-center justify-between text-[11px] font-sans">
          <span className="text-ink-500 uppercase tracking-[0.14em] font-medium">Avancement</span>
          <span className="font-semibold text-forest-950 num">{progress}%</span>
        </div>
        <div className="mt-1.5 h-1.5 rounded-full bg-line/70 overflow-hidden">
          <div className={`h-full ${barColor} rounded-full transition-all duration-700`} style={{width: `${progress}%`}} />
        </div>
      </div>

      {/* Footer meta */}
      <div className="mt-4 pt-4 border-t border-line/70 flex items-center justify-between gap-3">
        <div className="flex items-center gap-4 text-[11px] font-sans">
          <div>
            <div className="text-ink-500 uppercase tracking-[0.14em]">Bénéficiaires</div>
            <div className="font-semibold text-ink-900 num mt-0.5">{beneficiaries}</div>
          </div>
          <div className="w-px h-7 bg-line"/>
          <div>
            <div className="text-ink-500 uppercase tracking-[0.14em]">Budget</div>
            <div className="font-semibold text-ink-900 num mt-0.5">{budget}</div>
          </div>
        </div>
        <div className="flex gap-1 flex-shrink-0">
          {sdg.map(n => <SdgBadge key={n} n={n}/>)}
        </div>
      </div>
    </div>
  );
}

/* ---------- Agenda list ---------- */
const AGENDA = [
  { kind: "AG",     title: "Assemblée Générale Ordinaire", date: "14 juin",  time: "09:30 — 17:00", place: "Dakar · Hybride", attendees: 248, tone: "forest", icon: "landmark", urgent: true },
  { kind: "Pulse",  title: "Weekly Pulse — Chapitre Abidjan", date: "Jeudi 22", time: "18:00 — 19:00", place: "Visioconférence", attendees: 32,  tone: "terra",  icon: "activity" },
  { kind: "Comité", title: "Comité de pilotage · Sahel", date: "27 mai",   time: "10:00 — 12:30", place: "Bamako",          attendees: 14,  tone: "forest", icon: "users-round" },
  { kind: "Forum",  title: "Restitution citoyenne — Q1",  date: "5 juin",   time: "16:00 — 18:00", place: "Cotonou",         attendees: 96,  tone: "terra",  icon: "megaphone" },
];

function AgendaList() {
  return (
    <div className="bg-white border border-line rounded-xl shadow-soft-sm overflow-hidden divide-y divide-line/70">
      {AGENDA.map((e, i) => (
        <div key={i} className="group p-4 hover:bg-cream-warm/40 transition-colors cursor-pointer relative">
          {e.urgent && <span className="absolute left-0 top-0 bottom-0 w-[3px] bg-terra-600"/>}
          <div className="flex items-start gap-3">
            <div className={`w-10 h-10 rounded-lg flex flex-col items-center justify-center flex-shrink-0
              ${e.tone === "forest" ? "bg-forest-50 text-forest-900" : "bg-terra-50 text-terra-700"}`}>
              <Icon name={e.icon} className="w-4 h-4" strokeWidth={1.7}/>
            </div>
            <div className="flex-1 min-w-0">
              <div className="flex items-center gap-2">
                <span className={`text-[10px] uppercase tracking-[0.14em] font-sans font-semibold
                  ${e.tone === "forest" ? "text-forest-700" : "text-terra-700"}`}>{e.kind}</span>
                {e.urgent && <span className="text-[10px] px-1.5 py-0.5 rounded bg-terra-600 text-white font-sans font-semibold tracking-wide">PRIORITAIRE</span>}
              </div>
              <div className="font-sans font-semibold text-[14px] text-forest-950 mt-0.5 leading-tight">{e.title}</div>
              <div className="mt-1.5 flex items-center gap-3 text-[11px] text-ink-500 font-sans">
                <span className="inline-flex items-center gap-1"><Icon name="calendar" className="w-3 h-3"/> <span className="num">{e.date}</span></span>
                <span className="inline-flex items-center gap-1"><Icon name="clock" className="w-3 h-3"/> <span className="num">{e.time}</span></span>
              </div>
              <div className="mt-1 flex items-center gap-3 text-[11px] text-ink-500 font-sans">
                <span className="inline-flex items-center gap-1"><Icon name="map-pin" className="w-3 h-3"/>{e.place}</span>
                <span className="inline-flex items-center gap-1"><Icon name="users" className="w-3 h-3"/><span className="num">{e.attendees}</span></span>
              </div>
            </div>
            <Icon name="chevron-right" className="w-4 h-4 text-ink-300 group-hover:text-forest-900 group-hover:translate-x-0.5 transition-all flex-shrink-0 mt-1"/>
          </div>
        </div>
      ))}
    </div>
  );
}

/* ---------- Pulse / motivational card ---------- */
function PulseCard() {
  return (
    <div className="bg-gradient-to-br from-cream-warm/80 to-terra-50/40 border border-line rounded-xl p-5 relative overflow-hidden">
      <div className="absolute -right-10 -top-10 w-32 h-32 rounded-full compass-ring opacity-50"/>
      <div className="relative">
        <div className="text-[10px] uppercase tracking-[0.18em] text-terra-700 font-sans font-bold">Quote du jour</div>
        <p className="mt-3 font-display text-lg text-forest-950 leading-snug italic">
          « Le leadership éthique n'est pas une posture, c'est une discipline quotidienne. »
        </p>
        <div className="mt-4 flex items-center gap-2 text-[11px] text-ink-500 font-sans">
          <div className="w-6 h-6 rounded-full bg-forest-900 text-cream flex items-center justify-center text-[9px] font-bold">FK</div>
          Felwine Kabou · Forum 2025
        </div>
      </div>
    </div>
  );
}

/* ---------- Projects view (drill-down) ---------- */
function ProjectsView() {
  return (
    <div className="p-5 lg:p-8 max-w-[1180px] mx-auto">
      <div className="mb-8">
        <div className="text-[11px] uppercase tracking-[0.18em] text-ink-500 font-sans font-semibold flex items-center gap-2">
          <Icon name="rocket" className="w-3 h-3"/> Member OS · Projets & Impact
        </div>
        <h1 className="mt-3 font-display text-[40px] text-forest-950 tracking-tight">Portefeuille complet</h1>
        <p className="mt-2 text-ink-700 font-body max-w-xl">28 projets actifs · €4,2M déployés · 412 000 bénéficiaires touchés.</p>
      </div>

      <div className="flex flex-wrap items-center gap-2 mb-6">
        {["Tous","En exécution","Audit final","Cadrage","Phase pilote"].map((f,i) => (
          <button key={f} className={`px-3.5 py-1.5 rounded-md text-sm font-sans font-medium border transition
            ${i===0 ? "bg-forest-900 text-white border-forest-900" : "bg-white text-ink-700 border-line hover:bg-cream-warm/60"}`}>{f}</button>
        ))}
        <div className="ml-auto flex items-center gap-2 text-sm">
          <button className="px-3 py-1.5 rounded-md bg-white border border-line text-ink-700 inline-flex items-center gap-1.5">
            <Icon name="sliders-horizontal" className="w-4 h-4"/>Filtrer
          </button>
        </div>
      </div>

      <div className="grid md:grid-cols-2 xl:grid-cols-3 gap-4">
        <ProjectCard code="α-24" status="En exécution" statusTone="forest" title="Programme Alpha 2024" desc="Académie panafricaine pour 240 jeunes leaders." lead={{name:"Dr. Mariama Diop",role:"Lead — Dakar",initials:"MD"}} progress={68} beneficiaries="240" budget="€480k" sdg={[4,5,8]} tone="forest" chapter="Pan-africain"/>
        <ProjectCard code="ε-18" status="Phase pilote" statusTone="terra" title="Initiative Eau Propre" desc="Forages solaires & gouvernance villageoise." lead={{name:"Boubacar Touré",role:"Lead — Mopti",initials:"BT"}} progress={42} beneficiaries="34 200" budget="€720k" sdg={[6,11,13]} tone="terra" chapter="Sahel"/>
        <ProjectCard code="κ-07" status="Audit final" statusTone="forest" title="Charte d'Intégrité Locale" desc="Codes éthiques pour 12 collectivités." lead={{name:"Aïssatou Ba",role:"Lead — Kigali",initials:"AB"}} progress={91} beneficiaries="12" budget="€140k" sdg={[16,17]} tone="forest" chapter="Est"/>
        <ProjectCard code="ω-02" status="Cadrage" statusTone="muted" title="Boussole Entrepreneuriale" desc="Finance patiente & mentorat femmes." lead={{name:"Linda Mwangi",role:"Lead — Nairobi",initials:"LM"}} progress={18} beneficiaries="60" budget="€310k" sdg={[5,8,9]} tone="terra" chapter="Est"/>
        <ProjectCard code="ι-11" status="En exécution" statusTone="forest" title="École des Maires" desc="Formation continue de 80 édiles locaux." lead={{name:"Pascal Mvogo",role:"Lead — Yaoundé",initials:"PM"}} progress={55} beneficiaries="80" budget="€220k" sdg={[11,16]} tone="forest" chapter="Centre"/>
        <ProjectCard code="δ-05" status="En exécution" statusTone="forest" title="Forêts Communautaires" desc="Reforestation gérée par 14 villages." lead={{name:"Awa Sané",role:"Lead — Ziguinchor",initials:"AS"}} progress={73} beneficiaries="14 villages" budget="€180k" sdg={[13,15]} tone="terra" chapter="Ouest"/>
      </div>
    </div>
  );
}

/* ---------- Governance view ---------- */
function GovView() {
  return (
    <div className="p-5 lg:p-8 max-w-[1180px] mx-auto">
      <div className="mb-8">
        <div className="text-[11px] uppercase tracking-[0.18em] text-ink-500 font-sans font-semibold flex items-center gap-2">
          <Icon name="landmark" className="w-3 h-3"/> Member OS · Gouvernance
        </div>
        <h1 className="mt-3 font-display text-[40px] text-forest-950 tracking-tight">Décisions & Redevabilité</h1>
      </div>

      <div className="grid lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 bg-white rounded-xl border border-line p-6 shadow-soft-sm">
          <SectionHeader kicker="Votes en cours" title="Trois résolutions ouvertes" sub="Quorum atteint pour les 3" />
          <div className="mt-5 space-y-4">
            {[
              { title: "Adoption du budget Q3 2026", quorum: 91, for: 78, against: 9,  close: "Clôture dans 3 j" },
              { title: "Charte d'inclusion linguistique", quorum: 88, for: 84, against: 4,  close: "Clôture dans 6 j" },
              { title: "Ouverture chapitre Libreville",   quorum: 76, for: 62, against: 14, close: "Clôture dans 9 j" },
            ].map((v,i) => (
              <div key={i} className="p-4 rounded-lg border border-line hover:bg-cream-warm/30 transition">
                <div className="flex items-center justify-between">
                  <div className="font-sans font-semibold text-forest-950">{v.title}</div>
                  <span className="text-[11px] text-terra-700 font-sans font-semibold">{v.close}</span>
                </div>
                <div className="mt-3 h-2 rounded-full bg-line/70 overflow-hidden flex">
                  <div className="bg-forest-800" style={{width:`${v.for}%`}}/>
                  <div className="bg-terra-600" style={{width:`${v.against}%`}}/>
                </div>
                <div className="mt-2 flex items-center justify-between text-[11px] font-sans">
                  <div className="flex items-center gap-3">
                    <span className="text-forest-800 font-semibold num">Pour {v.for}%</span>
                    <span className="text-terra-700 font-semibold num">Contre {v.against}%</span>
                    <span className="text-ink-500 num">Quorum {v.quorum}%</span>
                  </div>
                  <button className="text-forest-900 font-semibold inline-flex items-center gap-1 hover:gap-1.5 transition-all">Voter <Icon name="arrow-right" className="w-3 h-3"/></button>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="space-y-6">
          <div className="bg-white rounded-xl border border-line p-6 shadow-soft-sm">
            <SectionHeader kicker="Composition" title="Conseil d'éthique"/>
            <div className="mt-4 space-y-3">
              {[
                ["Aminata Sow","Présidente","AS","forest"],
                ["Kwame Asante","Vice-président","KA","terra"],
                ["Ngozi Eze","Secrétaire","NE","forest"],
                ["Felwine K.","Membre","FK","terra"],
              ].map(([n,r,i,t]) => (
                <div key={n} className="flex items-center gap-3">
                  <div className={`w-9 h-9 rounded-full flex items-center justify-center text-white text-[11px] font-sans font-bold
                    ${t === "forest" ? "bg-gradient-to-br from-forest-800 to-forest-950" : "bg-gradient-to-br from-terra-600 to-terra-800"}`}>{i}</div>
                  <div>
                    <div className="text-sm font-sans font-semibold text-forest-950">{n}</div>
                    <div className="text-[11px] text-ink-500">{r}</div>
                  </div>
                </div>
              ))}
            </div>
          </div>
          <PulseCard/>
        </div>
      </div>
    </div>
  );
}

/* ---------- Placeholder views ---------- */
function PlaceholderView({ title, icon }) {
  return (
    <div className="p-5 lg:p-8 max-w-[1180px] mx-auto">
      <div className="mb-8">
        <div className="text-[11px] uppercase tracking-[0.18em] text-ink-500 font-sans font-semibold flex items-center gap-2">
          <Icon name={icon} className="w-3 h-3"/> Member OS
        </div>
        <h1 className="mt-3 font-display text-[40px] text-forest-950 tracking-tight">{title}</h1>
        <p className="mt-2 text-ink-700 font-body">Module en cours de cadrage avec la commission concernée.</p>
      </div>

      <div className="bg-white border border-line border-dashed rounded-xl p-12 text-center shadow-soft-sm">
        <div className="w-14 h-14 mx-auto rounded-xl bg-forest-50 text-forest-800 flex items-center justify-center">
          <Icon name={icon} className="w-6 h-6"/>
        </div>
        <div className="mt-4 font-display text-2xl text-forest-950">Bientôt disponible</div>
        <p className="mt-2 text-sm text-ink-700 max-w-md mx-auto">Ce module sera publié lors du cycle II — après validation par le Conseil d'éthique du 14 juin.</p>
        <button className="mt-5 inline-flex items-center gap-2 px-4 py-2 rounded-lg bg-forest-900 hover:bg-forest-950 text-white font-sans font-semibold text-sm">
          Être notifié <Icon name="bell" className="w-4 h-4"/>
        </button>
      </div>
    </div>
  );
}

/* =====================================================
   ROOT APP
====================================================== */
function App() {
  const [view, setView] = useState("landing");

  // refresh lucide on mount + after each view change (to be safe)
  useEffect(() => { if (window.lucide) window.lucide.createIcons(); }, [view]);

  const OS = window.RilcotOS;

  return (
    <div className="min-h-screen bg-cream">
      <TopNav view={view} setView={setView} />
      {view === "landing"   ? <Landing   setView={setView} /> : null}
      {view === "os"   && OS ? <OS setView={setView} /> : null}
      {view === "dashboard" ? <Dashboard setView={setView} /> : null}
    </div>
  );
}

/* Expose helpers + App so the RILCOT OS file (loaded after) can reuse them,
   and so the inline boot script can mount <App/> after all scripts are evaluated. */
Object.assign(window, {
  React, ReactDOM,
  Icon, SdgBadge, SDG, RilcotMark, SectionHeader,
  KpiCard, Spark, Ring, ProjectCard,
  App,
  RILCOT_App: App,
});
