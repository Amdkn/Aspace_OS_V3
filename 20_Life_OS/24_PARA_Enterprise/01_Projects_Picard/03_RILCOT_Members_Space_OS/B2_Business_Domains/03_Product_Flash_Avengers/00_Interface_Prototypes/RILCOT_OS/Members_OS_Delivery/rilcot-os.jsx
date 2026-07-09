/* RILCOT OS — System Operating Blueprint v1.0
   Portail souverain présentant la doctrine opératoire complète.
   Exporte: window.RilcotOS  (composant racine de la 3e vue)
*/

(function() {
  const { useState } = React;
  // Helpers exposed by rilcot-app.jsx
  const Icon       = window.Icon;
  const SdgBadge   = window.SdgBadge;
  const RilcotMark = window.RilcotMark;

  /* ---------- Small section header used across the page ---------- */
  function OsHeader({ num, kicker, title, sub }) {
    return (
      <header className="mb-10 lg:mb-14">
        <div className="flex items-center gap-3 text-[11px] uppercase tracking-[0.2em] font-sans font-bold text-terra-700">
          <span className="font-mono text-ink-400">{num}</span>
          <span className="h-px w-8 bg-terra-700/40" />
          {kicker}
        </div>
        <h2 className="mt-3 font-display text-4xl lg:text-[52px] text-forest-950 tracking-[-0.015em] leading-[1.05] max-w-3xl">
          {title}
        </h2>
        {sub && <p className="mt-4 text-ink-700 max-w-2xl font-body leading-relaxed">{sub}</p>}
      </header>
    );
  }

  /* ============================================================
     1 · HERO
  ============================================================ */
  function HeroSob({ setView }) {
    return (
      <section className="relative hero-pattern overflow-hidden">
        <div className="absolute inset-0 grain opacity-50 pointer-events-none" />

        {/* Big concentric compass */}
        <div className="absolute -right-40 -top-20 w-[640px] h-[640px] rounded-full compass-ring opacity-60 pointer-events-none hidden lg:block" />
        <div className="absolute -right-24 top-20 w-[420px] h-[420px] rounded-full border border-forest-900/15 pointer-events-none hidden lg:block" />
        <div className="absolute right-12 top-56 w-[240px] h-[240px] rounded-full border border-terra-700/20 pointer-events-none hidden lg:block" />

        <div className="max-w-[1400px] mx-auto px-5 lg:px-8 pt-14 lg:pt-20 pb-20 lg:pb-28 relative">
          {/* Eyebrow doctrinaire */}
          <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/80 border border-line text-xs font-sans font-medium text-forest-900 tracking-wide shadow-soft-sm">
            <span className="font-mono text-terra-700">SOB</span>
            <span className="text-ink-400">·</span>
            <span>System Operating Blueprint</span>
            <span className="text-ink-400">·</span>
            <span className="font-mono">v1.0</span>
            <span className="text-ink-400">·</span>
            <span className="text-ink-500">Souverain · Promulgué 14 mai 2026</span>
          </div>

          <div className="mt-7 grid lg:grid-cols-12 gap-10 lg:gap-14 items-end">
            <div className="lg:col-span-7">
              <div className="text-[11px] uppercase tracking-[0.22em] text-ink-500 font-sans font-semibold mb-4">
                Le portail souverain
              </div>
              <h1 className="font-display text-[44px] sm:text-[64px] lg:text-[84px] leading-[0.93] tracking-[-0.025em] text-forest-950">
                RILCOT <span className="italic font-medium text-terra-700">OS</span>.<br/>
                La doctrine<br/>d'<span className="italic font-medium text-terra-700">opération</span>.
              </h1>
              <p className="mt-7 text-lg lg:text-xl text-ink-700 max-w-xl leading-relaxed font-body">
                Une seule architecture, neuf modules, quatre instances. Le RILCOT OS est le contrat
                opératoire qui aligne la vision, les décisions et les preuves d'impact.
              </p>

              <div className="mt-9 flex flex-wrap items-center gap-3">
                <button className="group h-12 px-6 rounded-lg bg-forest-900 hover:bg-forest-950 text-white font-sans font-semibold text-[15px] flex items-center gap-2 shadow-soft-md transition">
                  Rejoindre le Mouvement
                  <Icon name="arrow-up-right" className="w-4 h-4 transition-transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
                </button>
                <button onClick={() => setView("dashboard")}
                  className="h-12 px-6 rounded-lg bg-white hover:bg-cream-warm/60 border border-line text-forest-900 font-sans font-semibold text-[15px] flex items-center gap-2 transition">
                  <Icon name="log-in" className="w-4 h-4 text-terra-700" />
                  Entrer dans l'Espace Membres
                </button>
              </div>

              {/* Doctrine strip */}
              <div className="mt-12 grid grid-cols-3 gap-4 max-w-xl">
                {[
                  ["09", "Modules d'opération"],
                  ["04", "Instances statutaires"],
                  ["12", "Flux critiques (SOP)"],
                ].map(([n, l]) => (
                  <div key={l}>
                    <div className="font-display text-3xl text-forest-950 num">{n}</div>
                    <div className="mt-1 text-[11px] uppercase tracking-[0.16em] text-ink-500 font-sans font-medium">{l}</div>
                  </div>
                ))}
              </div>
            </div>

            {/* Sommaire doctrinaire */}
            <div className="lg:col-span-5">
              <div className="bg-white rounded-2xl border border-line shadow-soft-lg p-6 lg:p-7">
                <div className="flex items-center justify-between">
                  <div>
                    <div className="text-[11px] uppercase tracking-[0.18em] text-ink-500 font-sans font-semibold">Sommaire</div>
                    <div className="font-display text-2xl text-forest-950 mt-1">Neuf sections statutaires</div>
                  </div>
                  <span className="text-[10px] font-mono text-terra-700 px-2 py-1 bg-terra-50 rounded">SOB v1.0</span>
                </div>

                <div className="mt-5 space-y-px">
                  {[
                    ["I",    "Hero & Préambule",          "hero"],
                    ["II",   "Boussole · North Star",     "northstar"],
                    ["III",  "Gouvernance & Holarchie",   "gouvernance"],
                    ["IV",   "Architecture des Modules",  "modules"],
                    ["V",    "Flux Critiques · SOP",      "flux"],
                    ["VI",   "Rituels & Mesure (KPI)",    "rituels"],
                    ["VII",  "RACI & Sécurité",           "raci"],
                    ["VIII", "Roadmap 0–180 jours",       "roadmap"],
                    ["IX",   "Accès Espace Membres",      "access"],
                  ].map(([r, t, id]) => (
                    <a key={id} href={`#sob-${id}`}
                      className="group flex items-center gap-3 py-2 px-2 -mx-2 rounded-md hover:bg-cream-warm/60 transition">
                      <span className="w-9 font-mono text-xs text-ink-400 tracking-wider">{r}</span>
                      <span className="flex-1 text-sm font-sans font-medium text-forest-950">{t}</span>
                      <Icon name="chevron-right" className="w-3.5 h-3.5 text-ink-300 group-hover:text-forest-900 group-hover:translate-x-0.5 transition-all" />
                    </a>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="stripe-divider" />
      </section>
    );
  }

  /* ============================================================
     2 · NORTH STAR (Boussole)
  ============================================================ */
  function NorthStar() {
    return (
      <section id="sob-northstar" className="max-w-[1400px] mx-auto px-5 lg:px-8 py-20 lg:py-28">
        <OsHeader num="§ II" kicker="Boussole · North Star"
          title={<>L'intention, les capabilités‑cœur,<br/>les <span className="italic text-terra-700">contrats d'impact</span>.</>}
          sub="La boussole n'est ni un slogan ni une mission abstraite : c'est l'ensemble vérifiable des engagements que RILCOT prend devant ses membres, ses partenaires et les territoires." />

        <div className="grid lg:grid-cols-12 gap-6 lg:gap-8">
          {/* Intention */}
          <div className="lg:col-span-5">
            <div className="bg-forest-950 text-cream rounded-2xl p-7 lg:p-9 relative overflow-hidden h-full">
              <div className="absolute -right-16 -top-16 w-60 h-60 rounded-full bg-terra-700/20 blur-3xl" />
              <div className="text-[11px] uppercase tracking-[0.2em] text-terra-200 font-sans font-bold">Intention souveraine</div>
              <h3 className="mt-4 font-display text-3xl lg:text-4xl leading-tight">
                Faire émerger une<br/>génération de bâtisseurs<br/><span className="italic">d'institutions justes</span>.
              </h3>
              <p className="mt-5 text-cream/80 leading-relaxed text-[15px]">
                Le RILCOT existe pour outiller — en méthode, en discipline et en redevabilité — celles et ceux
                qui forgent l'institutionnalité africaine de la prochaine génération.
              </p>
              <div className="mt-7 pt-6 border-t border-cream/15 flex items-center gap-3 text-xs font-sans text-cream/70">
                <Icon name="bookmark" className="w-4 h-4 text-terra-200" />
                Ratifiée par l'Assemblée Constituante · Dakar, 14 mai 2026
              </div>
            </div>
          </div>

          {/* Capabilités cœur */}
          <div className="lg:col-span-7">
            <div className="text-[11px] uppercase tracking-[0.18em] text-ink-500 font-sans font-bold mb-4">
              06 · Capabilités‑cœur (Core Capabilities)
            </div>
            <div className="grid sm:grid-cols-2 gap-3">
              {[
                ["compass",      "Discernement éthique",      "Aptitude collective à trancher des dilemmes institutionnels."],
                ["users-round",  "Coordination polycentrique","Animer une holarchie de chapitres autonomes mais alignés."],
                ["bar-chart-3",  "Mesure de l'impact",        "Produire des preuves vérifiables d'avancement, par cycle."],
                ["wallet",       "Soutenabilité financière",  "Diversifier les flux et soumettre la trésorerie à l'audit."],
                ["graduation-cap","Transmission générationnelle","Académies, mentorat et succession explicite des rôles."],
                ["shield-check", "Intégrité opérationnelle",  "Charte de Veto, lanceurs d'alerte, recours indépendant."],
              ].map(([icon, t, d]) => (
                <div key={t} className="group p-4 rounded-xl border border-line bg-white hover:shadow-soft-md transition-all">
                  <div className="flex items-center gap-3">
                    <div className="w-9 h-9 rounded-lg bg-forest-50 text-forest-900 flex items-center justify-center">
                      <Icon name={icon} className="w-4 h-4" />
                    </div>
                    <div className="font-sans font-semibold text-[14px] text-forest-950">{t}</div>
                  </div>
                  <p className="mt-2.5 text-[13px] text-ink-700 leading-relaxed font-body">{d}</p>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Contrats d'impact */}
        <div className="mt-12 lg:mt-14 bg-white border border-line rounded-2xl p-6 lg:p-8 shadow-soft-sm">
          <div className="flex flex-col md:flex-row md:items-end md:justify-between gap-4 mb-6">
            <div>
              <div className="text-[11px] uppercase tracking-[0.18em] text-terra-700 font-sans font-bold">04 · Contrats d'impact</div>
              <h3 className="mt-2 font-display text-2xl lg:text-3xl text-forest-950">Engagements vérifiables · Horizon 2030</h3>
            </div>
            <span className="text-xs text-ink-500 font-sans inline-flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-forest-600 pulse-dot" /> Mesurés trimestre par trimestre
            </span>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-px bg-line/70 rounded-xl overflow-hidden">
            {[
              { c: "C-01", t: "Former 5 000 leaders éthiques certifiés",      pct: 32, sdg:[4,5] },
              { c: "C-02", t: "Faire éclore 500 institutions territoriales", pct: 18, sdg:[16,17] },
              { c: "C-03", t: "Mobiliser €40M de finance patiente africaine", pct: 11, sdg:[8,9] },
              { c: "C-04", t: "Publier 1 200 jeux de données d'impact ouverts", pct: 27, sdg:[16,17] },
            ].map(k => (
              <div key={k.c} className="bg-cream p-5">
                <div className="flex items-center justify-between">
                  <span className="font-mono text-xs text-terra-700">{k.c}</span>
                  <div className="flex gap-1">{k.sdg.map(n => <SdgBadge key={n} n={n}/>)}</div>
                </div>
                <div className="mt-3 font-display text-[18px] text-forest-950 leading-tight">{k.t}</div>
                <div className="mt-4">
                  <div className="flex items-center justify-between text-[11px] font-sans">
                    <span className="text-ink-500 uppercase tracking-[0.14em] font-medium">Avancement</span>
                    <span className="font-semibold text-forest-950 num">{k.pct}%</span>
                  </div>
                  <div className="mt-1.5 h-1.5 rounded-full bg-line overflow-hidden">
                    <div className="h-full bg-forest-800 rounded-full" style={{width:`${k.pct}%`}}/>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
    );
  }

  /* ============================================================
     3 · GOUVERNANCE & HOLARCHIE
  ============================================================ */
  function Governance() {
    const bodies = [
      { code: "AG", name: "Assemblée Générale",     role: "Souverain · Statuts & Orientation",
        members: 1204, cadence: "1× / an", power: "Décide à 2/3", tone: "forest" },
      { code: "CC", name: "Conseil de Coordination",role: "Exécutif · Mise en œuvre",
        members: 12, cadence: "1× / mois", power: "Majorité simple", tone: "terra" },
      { code: "CF", name: "Commission Fiduciaire",  role: "Finances · Audit & Trésorerie",
        members: 7, cadence: "1× / trimestre", power: "Veto sur dépenses", tone: "forest" },
      { code: "CR", name: "Cercle de Régulation",   role: "Éthique · Recours & Médiation",
        members: 5, cadence: "Sur saisine", power: "Veto éthique", tone: "terra" },
    ];

    return (
      <section id="sob-gouvernance" className="bg-cream-warm/40 border-y border-line">
        <div className="max-w-[1400px] mx-auto px-5 lg:px-8 py-20 lg:py-28">
          <OsHeader num="§ III" kicker="Gouvernance & Holarchie"
            title={<>Qui décide,<br/><span className="italic text-terra-700">comment</span>, et à quelle cadence.</>}
            sub="Quatre instances articulées en holarchie : pouvoirs distincts, contre-pouvoirs explicites, traçabilité publique des décisions." />

          {/* 4 organes */}
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-4 mb-12">
            {bodies.map(b => (
              <div key={b.code} className="bg-white border border-line rounded-xl p-5 shadow-soft-sm hover:shadow-soft-md transition-all">
                <div className="flex items-center justify-between">
                  <div className={`w-12 h-12 rounded-lg flex items-center justify-center font-display text-xl
                    ${b.tone === "forest" ? "bg-forest-50 text-forest-900" : "bg-terra-50 text-terra-700"}`}>
                    {b.code}
                  </div>
                  <span className="text-[10px] font-mono text-ink-400">Statuts §{Math.floor(Math.random()*4)+2}</span>
                </div>
                <h3 className="mt-4 font-display text-xl text-forest-950 leading-tight">{b.name}</h3>
                <p className="mt-1 text-[12px] text-ink-500 font-sans">{b.role}</p>
                <div className="mt-4 pt-4 border-t border-line/70 space-y-1.5 text-[12px] font-sans">
                  <div className="flex justify-between"><span className="text-ink-500">Composition</span><span className="font-semibold text-ink-900 num">{b.members} m.</span></div>
                  <div className="flex justify-between"><span className="text-ink-500">Cadence</span><span className="font-semibold text-ink-900">{b.cadence}</span></div>
                  <div className="flex justify-between"><span className="text-ink-500">Décision</span><span className={`font-semibold ${b.tone === "forest" ? "text-forest-800" : "text-terra-700"}`}>{b.power}</span></div>
                </div>
              </div>
            ))}
          </div>

          {/* Decision flow */}
          <div className="bg-white border border-line rounded-2xl p-6 lg:p-8 shadow-soft-sm">
            <div className="flex flex-col md:flex-row md:items-end md:justify-between gap-4 mb-7">
              <div>
                <div className="text-[11px] uppercase tracking-[0.18em] text-terra-700 font-sans font-bold">Flux de décision</div>
                <h3 className="mt-2 font-display text-2xl lg:text-3xl text-forest-950">De la proposition à la promulgation</h3>
              </div>
              <span className="text-xs text-ink-500 font-sans">Délai médian observé · 18 jours</span>
            </div>

            {/* Horizontal pipeline */}
            <div className="overflow-x-auto -mx-2 px-2 pb-2">
              <div className="flex items-stretch gap-2 min-w-[820px]">
                {[
                  { n:1, t:"Proposition",    a:"Membre / Chapitre",    color:"forest", icon:"file-edit" },
                  { n:2, t:"Instruction",    a:"CC — 14 j max",        color:"forest", icon:"search" },
                  { n:3, t:"Avis fiduciaire",a:"CF — si €",            color:"terra",  icon:"wallet" },
                  { n:4, t:"Avis éthique",   a:"CR — si risque",       color:"terra",  icon:"shield-check" },
                  { n:5, t:"Vote",           a:"AG ou CC selon seuil", color:"forest", icon:"vote" },
                  { n:6, t:"Promulgation",   a:"Journal officiel SOB", color:"forest", icon:"badge-check" },
                ].map((s, i, arr) => (
                  <React.Fragment key={s.n}>
                    <div className={`flex-1 p-4 rounded-xl border
                      ${s.color === "forest" ? "border-forest-100 bg-forest-50/40" : "border-terra-100 bg-terra-50/40"}`}>
                      <div className="flex items-center gap-2">
                        <span className={`w-6 h-6 rounded-md flex items-center justify-center text-[11px] font-mono font-bold text-white
                          ${s.color === "forest" ? "bg-forest-900" : "bg-terra-700"}`}>{s.n}</span>
                        <Icon name={s.icon} className={`w-4 h-4 ${s.color === "forest" ? "text-forest-900" : "text-terra-700"}`} />
                      </div>
                      <div className="mt-3 font-sans font-semibold text-sm text-forest-950 leading-tight">{s.t}</div>
                      <div className="mt-1 text-[11px] text-ink-500 font-sans">{s.a}</div>
                    </div>
                    {i < arr.length-1 && (
                      <div className="self-center text-ink-300"><Icon name="chevron-right" className="w-4 h-4" /></div>
                    )}
                  </React.Fragment>
                ))}
              </div>
            </div>

            {/* Cadence band */}
            <div className="mt-7 pt-6 border-t border-line/70 grid sm:grid-cols-4 gap-4">
              {[
                ["Hebdomadaire", "Stand-up CC + chapitres", "calendar-clock"],
                ["Mensuel",      "Conseil de Coordination", "calendar"],
                ["Trimestriel",  "CF + restitution publique","calendar-check"],
                ["Annuel",       "AG ordinaire + Forum",    "calendar-days"],
              ].map(([t,d,i]) => (
                <div key={t} className="flex items-start gap-3">
                  <div className="w-9 h-9 rounded-lg bg-cream-warm/70 text-forest-900 flex items-center justify-center flex-shrink-0">
                    <Icon name={i} className="w-4 h-4" />
                  </div>
                  <div>
                    <div className="text-[10px] uppercase tracking-[0.16em] text-terra-700 font-sans font-bold">{t}</div>
                    <div className="text-[13px] text-ink-900 font-sans font-medium mt-0.5">{d}</div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>
    );
  }

  /* ============================================================
     4 · MODULES (9)
  ============================================================ */
  function Modules() {
    const mods = [
      { n:"M01", t:"Adhésion & Membres",      d:"Cycle de vie membre, cotisations, attestations.",   icon:"id-card",       lead:"Sec. Générale", health:96, sdg:[16] },
      { n:"M02", t:"Gouvernance & Statuts",   d:"Délibérations, votes, journal officiel SOB.",       icon:"landmark",      lead:"CC",            health:92, sdg:[16] },
      { n:"M03", t:"Finances & Trésorerie",   d:"Budget, paiements, audit, transparence comptable.", icon:"wallet",        lead:"CF",            health:88, sdg:[8]  },
      { n:"M04", t:"Projets & Impact",        d:"Portefeuille, jalons, indicateurs ODD.",            icon:"rocket",        lead:"DG Projets",    health:81, sdg:[8,9,11] },
      { n:"M05", t:"Communication & Réseau",  d:"Voix institutionnelle, plaidoyer, presse.",         icon:"megaphone",     lead:"Direction Com", health:74, sdg:[17] },
      { n:"M06", t:"Académie & Formation",    d:"Cohortes, mentorat, certifications.",               icon:"graduation-cap",lead:"Doyenné",       health:84, sdg:[4,5] },
      { n:"M07", t:"Éthique & Audit",         d:"Charte de Veto, alertes, médiation.",               icon:"shield-check",  lead:"CR",            health:97, sdg:[16] },
      { n:"M08", t:"Données & Mesure",        d:"Télémétrie, dashboards, données ouvertes.",         icon:"database",      lead:"Bureau Mesure", health:79, sdg:[17] },
      { n:"M09", t:"Partenariats & Alliances",d:"UA, PNUD, universités, finance patiente.",          icon:"handshake",     lead:"Affaires Ext.", health:71, sdg:[17] },
    ];

    return (
      <section id="sob-modules" className="max-w-[1400px] mx-auto px-5 lg:px-8 py-20 lg:py-28">
        <OsHeader num="§ IV" kicker="Architecture des modules"
          title={<>Neuf modules d'opération,<br/>une <span className="italic text-terra-700">seule</span> grammaire.</>}
          sub="Chaque module possède un propriétaire désigné, un cycle de revue et un score de santé opérationnelle publié au tableau de bord." />

        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {mods.map(m => (
            <div key={m.n} className="group bg-white border border-line rounded-xl p-5 shadow-soft-sm hover:shadow-soft-md hover:-translate-y-0.5 transition-all relative overflow-hidden">
              <div className="absolute right-0 top-0 w-32 h-32 rounded-full bg-forest-100 blur-3xl opacity-0 group-hover:opacity-100 transition" />
              <div className="relative">
                <div className="flex items-center justify-between">
                  <div className="w-10 h-10 rounded-lg bg-forest-50 text-forest-900 flex items-center justify-center">
                    <Icon name={m.icon} className="w-4 h-4"/>
                  </div>
                  <span className="font-mono text-[11px] text-ink-400">{m.n}</span>
                </div>
                <h3 className="mt-4 font-display text-xl text-forest-950 leading-tight">{m.t}</h3>
                <p className="mt-1.5 text-[13px] text-ink-700 font-body leading-relaxed">{m.d}</p>

                <div className="mt-4 pt-4 border-t border-line/70">
                  <div className="flex items-center justify-between text-[11px] font-sans">
                    <span className="text-ink-500">Propriétaire</span>
                    <span className="font-semibold text-ink-900">{m.lead}</span>
                  </div>
                  <div className="mt-2 flex items-center justify-between text-[11px] font-sans">
                    <span className="text-ink-500">Santé du module</span>
                    <span className={`font-semibold num ${m.health >= 90 ? "text-forest-800" : m.health >= 80 ? "text-forest-700" : "text-terra-700"}`}>{m.health}/100</span>
                  </div>
                  <div className="mt-1.5 h-1 rounded-full bg-line overflow-hidden">
                    <div className={`h-full rounded-full ${m.health >= 90 ? "bg-forest-800" : m.health >= 80 ? "bg-forest-600" : "bg-terra-600"}`} style={{width:`${m.health}%`}}/>
                  </div>
                  <div className="mt-3 flex items-center justify-between">
                    <div className="flex gap-1">{m.sdg.map(n => <SdgBadge key={n} n={n}/>)}</div>
                    <a className="text-[11px] font-sans font-semibold text-forest-900 inline-flex items-center gap-1 hover:gap-1.5 transition-all">
                      Spécification <Icon name="arrow-right" className="w-3 h-3"/>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>
    );
  }

  /* ============================================================
     5 · FLUX CRITIQUES (SOP)
  ============================================================ */
  function Flows() {
    const [tab, setTab] = useState(0);
    const flows = [
      {
        name: "Adhésion d'un membre",
        code: "SOP-01",
        sla: "≤ 21 jours",
        steps: [
          { t: "Candidature",        d: "Formulaire + lettre d'intention", a: "Candidat",     i:"file-edit" },
          { t: "Pré-instruction",    d: "Vérification éthique et identité", a: "Sec. Générale", i:"search" },
          { t: "Entretien holarchique", d: "Avec deux pairs du chapitre", a: "Chapitre",      i:"users-round" },
          { t: "Décision",           d: "Avis du CC à majorité",            a: "CC",           i:"vote" },
          { t: "Onboarding",         d: "Accès OS, parrainage, charte",     a: "Académie",     i:"badge-check" },
        ],
      },
      {
        name: "Cycle budgétaire annuel",
        code: "SOP-02",
        sla: "Cycle 90 j · clôture 30 j",
        steps: [
          { t: "Appel à initiatives",  d: "Toutes commissions",            a: "CC",          i:"megaphone" },
          { t: "Cadrage chiffré",      d: "Hypothèses + scénarios",        a: "CF",          i:"calculator" },
          { t: "Arbitrages",           d: "Priorités par boussole",        a: "CC + CF",     i:"scale" },
          { t: "Adoption",             d: "Vote AG aux 2/3",               a: "AG",          i:"vote" },
          { t: "Exécution & reporting",d: "Dashboard public trimestriel",  a: "Tous modules",i:"bar-chart-3" },
          { t: "Audit & quitus",       d: "Audit externe + quitus AG",     a: "CF + CR",     i:"shield-check" },
        ],
      },
      {
        name: "Lancement d'un projet d'impact",
        code: "SOP-03",
        sla: "≤ 45 jours",
        steps: [
          { t: "Note d'opportunité",   d: "1 page · alignement boussole",  a: "Lead projet", i:"file-text" },
          { t: "Due diligence",        d: "Faisabilité + risques",         a: "Bureau Mesure", i:"search" },
          { t: "Co-conception",        d: "Avec communauté bénéficiaire",  a: "Chapitre",    i:"users-round" },
          { t: "Validation éthique",   d: "Test contre Charte de Veto",    a: "CR",          i:"shield-check" },
          { t: "Engagement de fonds",  d: "Tranchage par jalons",          a: "CF",          i:"wallet" },
          { t: "Kickoff & jalons",     d: "Inscription au portefeuille",   a: "Lead projet", i:"rocket" },
        ],
      },
      {
        name: "Recours & médiation",
        code: "SOP-04",
        sla: "≤ 30 jours",
        steps: [
          { t: "Saisine confidentielle",d: "Canal protégé · lanceur d'alerte",a: "Plaignant",  i:"shield" },
          { t: "Recevabilité",          d: "Quorum CR 3/5",                  a: "CR",         i:"gavel" },
          { t: "Instruction contradictoire",d: "Auditions parties",           a: "CR",         i:"messages-square" },
          { t: "Décision motivée",      d: "Publiée + recours possible",     a: "CR",         i:"badge-check" },
          { t: "Mise en conformité",    d: "Plan correctif suivi 90 j",      a: "CC + module",i:"check-check" },
        ],
      },
    ];
    const f = flows[tab];

    return (
      <section id="sob-flux" className="bg-cream-warm/40 border-y border-line">
        <div className="max-w-[1400px] mx-auto px-5 lg:px-8 py-20 lg:py-28">
          <OsHeader num="§ V" kicker="Flux critiques · SOP"
            title={<>Comment on fait,<br/><span className="italic text-terra-700">concrètement</span>.</>}
            sub="Quatre des douze procédures opératoires standards (SOP) qui transforment la doctrine en gestes quotidiens." />

          {/* Tabs */}
          <div className="flex flex-wrap gap-2 mb-7">
            {flows.map((fl, i) => (
              <button key={fl.code} onClick={() => setTab(i)}
                className={`px-4 py-2 rounded-lg text-sm font-sans font-medium border transition flex items-center gap-2
                  ${i === tab ? "bg-forest-900 text-white border-forest-900 shadow-soft-sm" : "bg-white text-ink-700 border-line hover:bg-cream-warm/60"}`}>
                <span className="font-mono text-[11px] opacity-70">{fl.code}</span>
                {fl.name}
              </button>
            ))}
          </div>

          {/* Active flow */}
          <div className="bg-white border border-line rounded-2xl p-6 lg:p-8 shadow-soft-sm">
            <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-3 mb-6">
              <div>
                <div className="text-[11px] uppercase tracking-[0.18em] text-terra-700 font-sans font-bold">{f.code}</div>
                <h3 className="mt-1 font-display text-2xl lg:text-3xl text-forest-950">{f.name}</h3>
              </div>
              <span className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-md bg-forest-50 text-forest-800 font-sans font-semibold text-xs">
                <Icon name="timer" className="w-3.5 h-3.5"/> SLA : {f.sla}
              </span>
            </div>

            <div className="space-y-3">
              {f.steps.map((s, i) => (
                <div key={i} className="flex items-stretch gap-4">
                  {/* Number rail */}
                  <div className="flex flex-col items-center">
                    <div className={`w-9 h-9 rounded-full flex items-center justify-center font-mono text-sm font-bold
                      ${i === 0 ? "bg-terra-700 text-white" :
                        i === f.steps.length-1 ? "bg-forest-900 text-white" :
                        "bg-white border border-line text-forest-900"}`}>{i+1}</div>
                    {i < f.steps.length-1 && <div className="w-px flex-1 bg-line my-1"/>}
                  </div>
                  {/* Card */}
                  <div className="flex-1 flex flex-col md:flex-row md:items-center gap-3 p-4 rounded-xl bg-cream/60 border border-line/70">
                    <div className="w-9 h-9 rounded-lg bg-white border border-line text-forest-900 flex items-center justify-center flex-shrink-0">
                      <Icon name={s.i} className="w-4 h-4"/>
                    </div>
                    <div className="flex-1">
                      <div className="font-sans font-semibold text-[15px] text-forest-950">{s.t}</div>
                      <div className="text-[12px] text-ink-700 font-body mt-0.5">{s.d}</div>
                    </div>
                    <div className="md:text-right">
                      <div className="text-[10px] uppercase tracking-[0.14em] text-ink-500 font-sans">Responsable</div>
                      <div className="text-[12px] font-sans font-semibold text-forest-900 mt-0.5">{s.a}</div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>
    );
  }

  /* ============================================================
     6 · RITUELS & KPI
  ============================================================ */
  function Rituals() {
    return (
      <section id="sob-rituels" className="max-w-[1400px] mx-auto px-5 lg:px-8 py-20 lg:py-28">
        <OsHeader num="§ VI" kicker="Rituels & Mesure"
          title={<>Le rythme,<br/>les <span className="italic text-terra-700">preuves</span>.</>}
          sub="Quatre cadences statutaires articulées à un tableau de bord public. Le RILCOT ne mesure pas pour contrôler : il mesure pour rendre des comptes." />

        <div className="grid lg:grid-cols-12 gap-6 lg:gap-8">
          {/* Rituals column */}
          <div className="lg:col-span-7 space-y-3">
            <div className="text-[11px] uppercase tracking-[0.18em] text-ink-500 font-sans font-bold mb-1">
              Rituels opératoires
            </div>
            {[
              { c:"Weekly",    d:"Stand-up Coordination · 45 min", who:"CC + secrétariats", i:"calendar-clock", art:"PV publié sous 48h", tone:"forest" },
              { c:"Bi-weekly", d:"Pouls des chapitres · 60 min",   who:"Délégués chapitres", i:"activity",       art:"Notes de pouls",     tone:"terra"  },
              { c:"Monthly",   d:"Conseil de Coordination · 3h",   who:"CC complet + invités",i:"calendar",       art:"Résolutions signées", tone:"forest" },
              { c:"Quarterly", d:"Restitution publique + CF",      who:"AG large + presse",  i:"calendar-check", art:"Rapport Q1/Q2/Q3/Q4", tone:"terra"  },
              { c:"Annual",    d:"AG ordinaire · 2 jours",         who:"Tous les membres",   i:"calendar-days",  art:"Quitus + boussole",  tone:"forest" },
            ].map(r => (
              <div key={r.c} className="group bg-white border border-line rounded-xl p-4 hover:shadow-soft-md transition-all flex items-center gap-4">
                <div className={`w-12 h-12 rounded-lg flex items-center justify-center flex-shrink-0
                  ${r.tone === "forest" ? "bg-forest-50 text-forest-900" : "bg-terra-50 text-terra-700"}`}>
                  <Icon name={r.i} className="w-5 h-5" />
                </div>
                <div className="flex-1">
                  <div className="flex items-center gap-2">
                    <span className={`text-[10px] uppercase tracking-[0.16em] font-sans font-bold
                      ${r.tone === "forest" ? "text-forest-700" : "text-terra-700"}`}>{r.c}</span>
                  </div>
                  <div className="font-sans font-semibold text-[14px] text-forest-950 mt-0.5">{r.d}</div>
                  <div className="text-[11px] text-ink-500 mt-0.5">{r.who}</div>
                </div>
                <div className="text-right hidden sm:block">
                  <div className="text-[10px] uppercase tracking-[0.14em] text-ink-500 font-sans">Artefact</div>
                  <div className="text-[12px] font-sans font-semibold text-ink-900 mt-0.5">{r.art}</div>
                </div>
              </div>
            ))}
          </div>

          {/* KPI dashboard preview */}
          <div className="lg:col-span-5">
            <div className="bg-white border border-line rounded-2xl p-6 shadow-soft-md sticky top-20">
              <div className="flex items-center justify-between">
                <div>
                  <div className="text-[11px] uppercase tracking-[0.18em] text-ink-500 font-sans font-bold">Mesure · KPI</div>
                  <h3 className="mt-1 font-display text-2xl text-forest-950">Tableau de bord souverain</h3>
                </div>
                <span className="text-[10px] font-mono text-forest-800 px-2 py-1 bg-forest-50 rounded">LIVE</span>
              </div>

              <div className="mt-5 grid grid-cols-2 gap-3">
                {[
                  ["Boussole",          "92",   "/100", "forest", "compass"],
                  ["Exécution",         "76",   "%",    "terra",  "trending-up"],
                  ["Intégrité",         "A−",   "",     "forest", "shield-check"],
                  ["Transparence",      "98",   "%",    "terra",  "eye"],
                ].map(([l,v,u,t,i]) => (
                  <div key={l} className="p-3 rounded-lg bg-cream-warm/40 border border-line/70">
                    <div className="flex items-center justify-between">
                      <div className="text-[10px] uppercase tracking-[0.14em] text-ink-500 font-sans font-medium">{l}</div>
                      <Icon name={i} className={`w-3.5 h-3.5 ${t === "forest" ? "text-forest-800" : "text-terra-700"}`}/>
                    </div>
                    <div className="mt-1 flex items-baseline gap-1">
                      <div className="font-display text-3xl text-forest-950 num">{v}</div>
                      <div className="text-xs text-ink-500 font-sans">{u}</div>
                    </div>
                  </div>
                ))}
              </div>

              <div className="mt-5 pt-5 border-t border-line">
                <div className="text-[10px] uppercase tracking-[0.16em] text-ink-500 font-sans font-bold mb-3">Indicateurs publics</div>
                <div className="space-y-2.5">
                  {[
                    ["Délai médian d'une décision",  "18 j",   62],
                    ["Taux de promesse tenue",       "87 %",   87],
                    ["Diversité géographique",       "34 pays",78],
                    ["Parité dans les instances",    "49/51",  98],
                  ].map(([l,v,p]) => (
                    <div key={l}>
                      <div className="flex items-center justify-between text-[12px] font-sans">
                        <span className="text-ink-700">{l}</span>
                        <span className="font-semibold text-forest-950 num">{v}</span>
                      </div>
                      <div className="mt-1 h-1 rounded-full bg-line overflow-hidden">
                        <div className="h-full bg-forest-800 rounded-full" style={{width:`${p}%`}}/>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    );
  }

  /* ============================================================
     7 · RACI & SÉCURITÉ
  ============================================================ */
  function RaciSecurity() {
    const raci = [
      ["Adhésion d'un membre",      "Sec. G.", "AG",  "CR",   "Tous"],
      ["Vote d'un budget",          "CF",      "AG",  "CC",   "Membres"],
      ["Lancement de projet",       "Lead",    "CC",  "CR/CF","Chapitre"],
      ["Audit annuel",              "CF",      "AG",  "Externe","Tous"],
      ["Saisine éthique",           "CR",      "AG",  "Médiateur","Plaignant"],
      ["Promulgation de norme SOB", "CC",      "AG",  "CR",   "Tous"],
    ];
    const head = ["Processus", "R · Réalise", "A · Approuve", "C · Consulté", "I · Informé"];

    return (
      <section id="sob-raci" className="bg-forest-950 text-cream relative overflow-hidden">
        <div className="absolute -left-32 top-0 w-[480px] h-[480px] rounded-full bg-terra-700/15 blur-3xl"/>
        <div className="absolute right-0 -bottom-20 w-[420px] h-[420px] rounded-full bg-forest-700/30 blur-3xl"/>
        <div className="max-w-[1400px] mx-auto px-5 lg:px-8 py-20 lg:py-28 relative">
          <div className="mb-12">
            <div className="flex items-center gap-3 text-[11px] uppercase tracking-[0.2em] font-sans font-bold text-terra-200">
              <span className="font-mono text-cream/40">§ VII</span>
              <span className="h-px w-8 bg-terra-200/40" />
              RACI & Sécurité
            </div>
            <h2 className="mt-3 font-display text-4xl lg:text-[52px] tracking-[-0.015em] leading-[1.05] max-w-3xl">
              Qui porte quoi, et qui peut <span className="italic">dire non</span>.
            </h2>
            <p className="mt-4 text-cream/75 max-w-2xl font-body leading-relaxed">
              Toute responsabilité est nommée, toute décision a un veto explicite. C'est le contrat de sûreté du RILCOT OS.
            </p>
          </div>

          <div className="grid lg:grid-cols-12 gap-6 lg:gap-8">
            {/* RACI table */}
            <div className="lg:col-span-8">
              <div className="rounded-2xl overflow-hidden border border-cream/15 bg-forest-900/50 backdrop-blur">
                <table className="w-full text-sm">
                  <thead>
                    <tr className="border-b border-cream/15">
                      {head.map((h, i) => (
                        <th key={h} className={`px-4 py-3 text-left text-[10px] uppercase tracking-[0.16em] font-sans font-bold ${i === 0 ? "text-cream" : "text-terra-200"}`}>{h}</th>
                      ))}
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-cream/10">
                    {raci.map((row, i) => (
                      <tr key={i} className="hover:bg-cream/5 transition">
                        {row.map((cell, j) => (
                          <td key={j} className={`px-4 py-3 ${j === 0 ? "font-sans font-semibold text-cream" : "text-cream/75 font-sans"}`}>{cell}</td>
                        ))}
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
              <div className="mt-3 text-[11px] text-cream/50 font-sans">RACI complet · 38 processus · Annexe C du SOB v1.0.</div>
            </div>

            {/* Charte de Veto */}
            <div className="lg:col-span-4">
              <div className="rounded-2xl bg-cream/5 border border-cream/15 p-6 backdrop-blur h-full">
                <div className="flex items-center gap-2">
                  <div className="w-9 h-9 rounded-lg bg-terra-600/30 text-terra-200 flex items-center justify-center">
                    <Icon name="shield-alert" className="w-4 h-4"/>
                  </div>
                  <div className="text-[11px] uppercase tracking-[0.18em] text-terra-200 font-sans font-bold">Charte de Veto</div>
                </div>
                <h3 className="mt-4 font-display text-2xl text-cream leading-tight">Quatre droits de veto explicites</h3>
                <ul className="mt-5 space-y-3 text-sm text-cream/80">
                  {[
                    ["CR", "Veto éthique sur toute décision qui contrevient à la charte."],
                    ["CF", "Veto fiduciaire sur engagement financier non couvert."],
                    ["AG", "Veto souverain par 2/3 sur toute promulgation du CC."],
                    ["Membre", "Droit d'alerte protégé · saisine confidentielle CR."],
                  ].map(([who, what]) => (
                    <li key={who} className="flex items-start gap-3">
                      <span className="mt-0.5 px-1.5 py-0.5 rounded font-mono text-[10px] bg-cream text-forest-950 font-bold flex-shrink-0">{who}</span>
                      <span className="leading-relaxed font-body">{what}</span>
                    </li>
                  ))}
                </ul>
                <div className="mt-6 pt-5 border-t border-cream/15 text-[11px] text-cream/60 font-sans">
                  Tout veto exercé est consigné publiquement au Journal du SOB sous 7 jours.
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    );
  }

  /* ============================================================
     8 · ROADMAP 0–180 jours
  ============================================================ */
  function Roadmap() {
    const phases = [
      { range:"J 0–30",   t:"Constitution",   d:"Statuts ratifiés, CC installé, charte signée.",     tone:"forest", milestones:["Statuts AG","Site OS v1","Premiers chapitres"], pct: 100 },
      { range:"J 30–60",  t:"Activation",     d:"CF & CR opérationnels, 12 chapitres ouverts.",      tone:"forest", milestones:["CF actif","CR actif","12 chapitres"], pct: 88 },
      { range:"J 60–90",  t:"Premiers projets",d:"Lancement des SOPs Adhésion, Budget, Projet.",      tone:"terra",  milestones:["SOP-01 live","SOP-02 live","SOP-03 live"], pct: 64 },
      { range:"J 90–120", t:"Mesure",         d:"Tableau de bord public en ligne, premiers KPI.",     tone:"terra",  milestones:["Dashboard public","Q1 publié","Audit blanc"], pct: 41 },
      { range:"J 120–150",t:"Forum",          d:"Restitution citoyenne, plaidoyer continental.",      tone:"forest", milestones:["Forum Dakar","Plaidoyer UA","Presse"], pct: 22 },
      { range:"J 150–180",t:"Bilan & v1.1",   d:"Audit indépendant, mise à jour du SOB.",            tone:"forest", milestones:["Audit ext.","SOB v1.1","Roadmap H2"], pct: 8 },
    ];

    return (
      <section id="sob-roadmap" className="max-w-[1400px] mx-auto px-5 lg:px-8 py-20 lg:py-28">
        <OsHeader num="§ VIII" kicker="Feuille de route"
          title={<>De 0 à 180 jours,<br/>en <span className="italic text-terra-700">six</span> phases.</>}
          sub="La trajectoire promulguée par l'Assemblée Constituante du 14 mai 2026. Chaque phase a ses jalons publics et son audit." />

        <div className="relative">
          {/* Center timeline */}
          <div className="hidden md:block absolute left-1/2 top-2 bottom-2 w-px bg-line -translate-x-1/2" />

          <div className="space-y-6">
            {phases.map((p, i) => {
              const left = i % 2 === 0;
              return (
                <div key={p.range} className="md:grid md:grid-cols-2 md:gap-10 items-stretch relative">
                  {/* Dot */}
                  <div className="hidden md:block absolute left-1/2 top-7 -translate-x-1/2 z-10">
                    <div className={`w-3.5 h-3.5 rounded-full ring-4 ring-cream
                      ${p.pct === 100 ? "bg-forest-900" : p.pct >= 50 ? "bg-terra-600" : "bg-line"}`}/>
                  </div>

                  <div className={`${left ? "md:order-1 md:text-right md:pr-6" : "md:order-2 md:pl-6"}`}>
                    <div className={`bg-white border border-line rounded-xl p-5 shadow-soft-sm hover:shadow-soft-md transition-all`}>
                      <div className={`flex items-center gap-2 ${left ? "md:justify-end" : ""}`}>
                        <span className={`font-mono text-[11px] px-2 py-0.5 rounded font-bold
                          ${p.tone === "forest" ? "bg-forest-50 text-forest-800" : "bg-terra-50 text-terra-700"}`}>{p.range}</span>
                        <span className="text-[10px] uppercase tracking-[0.14em] text-ink-500 font-sans font-medium num">{p.pct}%</span>
                      </div>
                      <h3 className="mt-3 font-display text-2xl text-forest-950 leading-tight">{p.t}</h3>
                      <p className="mt-1.5 text-[13px] text-ink-700 leading-relaxed font-body">{p.d}</p>
                      <div className={`mt-4 flex flex-wrap gap-1.5 ${left ? "md:justify-end" : ""}`}>
                        {p.milestones.map(m => (
                          <span key={m} className={`text-[10px] px-2 py-0.5 rounded-md font-sans font-medium
                            ${p.tone === "forest" ? "bg-forest-50 text-forest-800" : "bg-terra-50 text-terra-700"}`}>{m}</span>
                        ))}
                      </div>
                      <div className="mt-3 h-1 rounded-full bg-line overflow-hidden">
                        <div className={`h-full rounded-full ${p.tone === "forest" ? "bg-forest-800" : "bg-terra-600"}`} style={{width:`${p.pct}%`}}/>
                      </div>
                    </div>
                  </div>

                  {/* Empty side (or label) */}
                  <div className={`hidden md:block ${left ? "md:order-2" : "md:order-1"}`}>
                    <div className={`pt-7 ${left ? "pl-6" : "pr-6 text-right"}`}>
                      <div className="font-display italic text-2xl text-ink-300">Phase {String(i+1).padStart(2,"0")}</div>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </section>
    );
  }

  /* ============================================================
     9 · ACCESS DASHBOARD
  ============================================================ */
  function AccessDashboard({ setView }) {
    return (
      <section id="sob-access" className="relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-b from-cream to-cream-warm/60" />
        <div className="absolute inset-0 grain opacity-50" />
        <div className="absolute -right-32 -top-32 w-[520px] h-[520px] rounded-full compass-ring opacity-50 pointer-events-none" />

        <div className="max-w-[1400px] mx-auto px-5 lg:px-8 py-20 lg:py-28 relative">
          <div className="grid lg:grid-cols-12 gap-10 lg:gap-14 items-center">
            <div className="lg:col-span-7">
              <div className="text-[11px] uppercase tracking-[0.2em] text-terra-700 font-sans font-bold mb-3">§ IX · Point d'accès</div>
              <h2 className="font-display text-4xl lg:text-[56px] text-forest-950 tracking-[-0.015em] leading-[1.02]">
                Entrer dans le<br/><span className="italic text-terra-700">Member Space</span>.
              </h2>
              <p className="mt-6 text-ink-700 max-w-xl text-lg font-body leading-relaxed">
                L'Espace Membres est la couche d'exécution du RILCOT OS. Vous y trouvez vos rituels,
                vos projets, vos votes ouverts et la télémétrie de votre chapitre.
              </p>

              <div className="mt-8 flex flex-wrap items-center gap-3">
                <button onClick={() => setView("dashboard")}
                  className="h-12 px-6 rounded-lg bg-forest-900 hover:bg-forest-950 text-white font-sans font-semibold text-[15px] flex items-center gap-2 shadow-soft-md transition">
                  Accéder à la plateforme
                  <Icon name="arrow-up-right" className="w-4 h-4"/>
                </button>
                <button className="h-12 px-6 rounded-lg bg-white border border-line hover:bg-cream-warm/60 text-forest-900 font-sans font-semibold text-[15px] flex items-center gap-2 transition">
                  Télécharger le SOB v1.0
                  <Icon name="download" className="w-4 h-4 text-terra-700"/>
                </button>
              </div>
            </div>

            <div className="lg:col-span-5">
              <div className="bg-white border border-line rounded-2xl shadow-soft-lg overflow-hidden">
                <div className="px-5 py-4 border-b border-line flex items-center gap-2">
                  <div className="flex gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-terra-400"/>
                    <span className="w-2.5 h-2.5 rounded-full bg-cream-warm"/>
                    <span className="w-2.5 h-2.5 rounded-full bg-forest-200"/>
                  </div>
                  <div className="ml-2 text-[11px] text-ink-500 font-mono">rilcot.os / member-space</div>
                </div>
                <div className="p-5 bg-cream-warm/30">
                  <div className="grid grid-cols-2 gap-3">
                    {[
                      ["Membres",        "1 204"],
                      ["Projets",        "28"],
                      ["Votes ouverts",  "03"],
                      ["Intégrité",      "A−"],
                    ].map(([l,v]) => (
                      <div key={l} className="bg-white rounded-lg p-3 border border-line/70">
                        <div className="text-[10px] uppercase tracking-[0.14em] text-ink-500 font-sans font-medium">{l}</div>
                        <div className="mt-1 font-display text-2xl text-forest-950 num">{v}</div>
                      </div>
                    ))}
                  </div>
                  <div className="mt-4 p-3 rounded-lg bg-forest-950 text-cream">
                    <div className="text-[10px] uppercase tracking-[0.16em] text-terra-200 font-sans font-bold">Prochain rituel</div>
                    <div className="mt-1 font-display text-lg leading-tight">AG Ordinaire · 14 juin</div>
                    <div className="text-[11px] text-cream/70 mt-1">Dakar · Hybride · 248 inscrits</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    );
  }

  /* ============================================================
     STATUTORY FOOTER
  ============================================================ */
  function StatutoryFooter() {
    return (
      <footer className="bg-forest-950 text-cream/85">
        <div className="max-w-[1400px] mx-auto px-5 lg:px-8 py-14">
          <div className="grid lg:grid-cols-12 gap-10">
            <div className="lg:col-span-5">
              <div className="flex items-center gap-2.5">
                <RilcotMark className="w-9 h-9"/>
                <div className="leading-none">
                  <div className="font-display text-lg text-cream font-bold">RILCOT</div>
                  <div className="text-[10px] uppercase tracking-[0.18em] text-cream/60 mt-1">Members OS · SOB v1.0</div>
                </div>
              </div>
              <p className="mt-5 text-cream/70 max-w-md text-sm leading-relaxed">
                Réseau Institutionnel pour le Leadership Communautaire et la Transformation.
                Promulgué par l'Assemblée Constituante de Dakar, le 14 mai 2026.
              </p>
              <div className="mt-6 inline-flex items-center gap-2 text-[11px] text-cream/60 font-mono">
                <Icon name="bookmark" className="w-3.5 h-3.5 text-terra-200"/>
                Document souverain · SOB‑2026‑05‑14‑v1.0
              </div>
            </div>

            <div className="lg:col-span-7 grid sm:grid-cols-3 gap-8">
              <div>
                <div className="text-[10px] uppercase tracking-[0.18em] text-terra-200 font-sans font-bold mb-3">Doctrine</div>
                <ul className="space-y-2 text-sm">
                  <li><a className="hover:text-cream">Statuts</a></li>
                  <li><a className="hover:text-cream">Charte éthique</a></li>
                  <li><a className="hover:text-cream">Charte de Veto</a></li>
                  <li><a className="hover:text-cream">SOB · Journal</a></li>
                </ul>
              </div>
              <div>
                <div className="text-[10px] uppercase tracking-[0.18em] text-terra-200 font-sans font-bold mb-3">Instances</div>
                <ul className="space-y-2 text-sm">
                  <li><a className="hover:text-cream">Assemblée Générale</a></li>
                  <li><a className="hover:text-cream">Conseil de Coordination</a></li>
                  <li><a className="hover:text-cream">Commission Fiduciaire</a></li>
                  <li><a className="hover:text-cream">Cercle de Régulation</a></li>
                </ul>
              </div>
              <div>
                <div className="text-[10px] uppercase tracking-[0.18em] text-terra-200 font-sans font-bold mb-3">Transparence</div>
                <ul className="space-y-2 text-sm">
                  <li><a className="hover:text-cream">Données ouvertes</a></li>
                  <li><a className="hover:text-cream">Rapport Q1 2026</a></li>
                  <li><a className="hover:text-cream">Lanceurs d'alerte</a></li>
                  <li><a className="hover:text-cream">Contact presse</a></li>
                </ul>
              </div>
            </div>
          </div>

          <div className="mt-12 pt-6 border-t border-cream/15 flex flex-col md:flex-row md:items-center md:justify-between gap-3 text-[11px] text-cream/55 font-sans">
            <div>© 2026 RILCOT · Tous droits statutaires réservés · Promulgué le 14 mai 2026.</div>
            <div className="inline-flex items-center gap-4">
              <span>Audit annuel · KPMG Sénégal</span>
              <span>·</span>
              <span>Hébergement : OS sécurisé · Dakar</span>
            </div>
          </div>
        </div>
      </footer>
    );
  }

  /* ============================================================
     ROOT EXPORT
  ============================================================ */
  function RilcotOS({ setView }) {
    return (
      <main className="min-h-screen">
        <HeroSob       setView={setView} />
        <NorthStar/>
        <Governance/>
        <Modules/>
        <Flows/>
        <Rituals/>
        <RaciSecurity/>
        <Roadmap/>
        <AccessDashboard setView={setView}/>
        <StatutoryFooter/>
      </main>
    );
  }

  window.RilcotOS = RilcotOS;
})();
