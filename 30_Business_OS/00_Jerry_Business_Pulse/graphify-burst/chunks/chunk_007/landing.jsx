// ABC OS — Landing page
// Reuses ios-frame.jsx + abc/screens.jsx

const TABS_LANDING = [
  { key: 'community', label: 'Community', icon: 'users',         screen: () => <CommunityHub /> },
  { key: 'learn',     label: 'Learn',     icon: 'graduationCap', screen: () => <LearnHub /> },
  { key: 'build',     label: 'Build',     icon: 'wrench',        screen: () => <BuildHub /> },
  { key: 'brand',     label: 'Brand',     icon: 'award',         screen: () => <BrandHub /> },
];

// ── Reusable embedded phone ────────────────────────────────
function EmbeddedPhone({ tab = 'community', width = 360, height = 760, showNav = true, interactive = false, onChangeTab }) {
  const T = TABS_LANDING.find((x) => x.key === tab);
  return (
    <div style={{ width, height, position: 'relative' }}>
      <IOSDevice width={width} height={height} dark>
        <div className="relative" style={{ height: '100%', paddingTop: 54 }}>
          {T && T.screen()}
          {showNav && <EmbeddedNav current={tab} onChange={onChangeTab} />}
        </div>
      </IOSDevice>
    </div>
  );
}

function EmbeddedNav({ current, onChange }) {
  return (
    <div style={{
      position:'absolute', left:12, right:12, bottom:16, zIndex:40, height:68, borderRadius:24,
      background:'rgba(24,22,20,0.78)', backdropFilter:'blur(20px) saturate(1.4)', WebkitBackdropFilter:'blur(20px) saturate(1.4)',
      border:'1px solid rgba(245,242,235,0.07)', boxShadow:'0 18px 40px rgba(0,0,0,0.4), 0 1px 0 rgba(255,255,255,0.04) inset',
      display:'grid', gridTemplateColumns:'repeat(4,1fr)', alignItems:'center', padding:'0 4px',
    }}>
      {TABS_LANDING.map((t) => {
        const active = current === t.key;
        return (
          <button key={t.key} onClick={() => onChange && onChange(t.key)}
                  className="h-full flex flex-col items-center justify-center gap-1 relative"
                  style={{ color: active ? '#f5f2eb' : '#a89c8a' }}>
            {active && <span style={{ position:'absolute', top:6, left:'50%', transform:'translateX(-50%)', width:24, height:3, borderRadius:3, background:'#e15f41' }}/>}
            <div className="flex items-center justify-center"
                 style={{ width:38, height:32, borderRadius:12, background: active ? 'rgba(225,95,65,0.12)':'transparent',
                          color: active ? '#e15f41' : '#a89c8a', transition:'all .18s' }}>
              <Icon name={t.icon} size={18} stroke={active ? 2.2 : 1.8} />
            </div>
            <div className="text-[9.5px] font-semibold" style={{ letterSpacing: 0.2 }}>{t.label}</div>
          </button>
        );
      })}
    </div>
  );
}

// ══════════════════════════════════════════════════════════════
// LOGO
// ══════════════════════════════════════════════════════════════
function LogoMark({ size = 28 }) {
  return (
    <svg width={size} height={size} viewBox="0 0 32 32">
      <defs>
        <radialGradient id="lgs" cx="50%" cy="40%" r="55%">
          <stop offset="0%" stopColor="#f6c47a"/>
          <stop offset="60%" stopColor="#e15f41"/>
          <stop offset="100%" stopColor="#7a2818"/>
        </radialGradient>
      </defs>
      {Array.from({ length: 12 }).map((_, i) => {
        const a = (i * Math.PI * 2) / 12;
        const x1 = 16 + Math.cos(a) * 12, y1 = 16 + Math.sin(a) * 12;
        const x2 = 16 + Math.cos(a) * 15.5, y2 = 16 + Math.sin(a) * 15.5;
        return <line key={i} x1={x1} y1={y1} x2={x2} y2={y2} stroke="#e15f41" strokeWidth="1.5" strokeLinecap="round" opacity="0.9"/>;
      })}
      <circle cx="16" cy="16" r="9" fill="url(#lgs)"/>
      <path d="M21 12c2-0.5 4 1 3.5 3-2.5 0-4-1-3.5-3z" fill="#10b981"/>
    </svg>
  );
}

function Wordmark() {
  return (
    <div className="flex items-center gap-2">
      <LogoMark size={26}/>
      <span className="font-bold text-[15px] tracking-[0.18em]">ABC&nbsp;OS</span>
    </div>
  );
}

// ══════════════════════════════════════════════════════════════
// TOP NAV
// ══════════════════════════════════════════════════════════════
function TopNav() {
  return (
    <div className="topnav rounded-full mx-auto flex items-center justify-between px-3 py-2"
         style={{ maxWidth: 1180 }}>
      <div className="pl-3"><Wordmark/></div>
      <nav className="hidden md:flex items-center gap-7 text-[13px] font-medium" style={{ color:'#cfc4b3' }}>
        <a href="#manifeste" className="hover:text-white">Manifeste</a>
        <a href="#piliers" className="hover:text-white">Plateforme</a>
        <a href="#programme" className="hover:text-white">Programme</a>
        <a href="#cooperatives" className="hover:text-white">Coopératives</a>
        <a href="#faq" className="hover:text-white">FAQ</a>
      </nav>
      <div className="flex items-center gap-2">
        <a href="#" className="hidden sm:block text-[13px] font-medium px-3 py-2 rounded-full" style={{ color:'#cfc4b3' }}>Se connecter</a>
        <a href="#join" className="text-[13px] font-semibold px-4 h-10 rounded-full inline-flex items-center gap-1.5"
           style={{ background:'#e15f41', color:'#fff', boxShadow:'0 8px 22px -8px rgba(225,95,65,0.6)' }}>
          Rejoindre <Icon name="arrowRight" size={14}/>
        </a>
      </div>
    </div>
  );
}

// ══════════════════════════════════════════════════════════════
// HERO
// ══════════════════════════════════════════════════════════════
function HeroPhone() {
  const [tab, setTab] = React.useState('community');
  const order = ['community', 'learn', 'build', 'brand'];
  React.useEffect(() => {
    const id = setInterval(() => {
      setTab((cur) => order[(order.indexOf(cur) + 1) % order.length]);
    }, 5200);
    return () => clearInterval(id);
  }, []);
  return (
    <div className="relative">
      {/* Halo */}
      <div style={{
        position:'absolute', inset:'-60px -90px', zIndex:0,
        background:'radial-gradient(60% 50% at 50% 50%, rgba(225,95,65,0.35), transparent 70%)',
        filter:'blur(20px)'
      }}/>
      {/* Phone */}
      <div className="relative anim-float" style={{ filter:'drop-shadow(0 50px 80px rgba(0,0,0,0.5))' }}>
        <EmbeddedPhone tab={tab} width={368} height={780} interactive onChangeTab={setTab}/>
      </div>

      {/* Floating callouts */}
      <div className="absolute hidden lg:flex flex-col gap-1.5 px-3.5 py-2.5 rounded-2xl text-left"
           style={{ left:-180, top:90, width:200, background:'rgba(24,22,20,0.85)', border:'1px solid var(--line)', backdropFilter:'blur(8px)', zIndex:10 }}>
        <div className="eyebrow" style={{ fontSize:9 }}>Brand Impact</div>
        <div className="flex items-baseline gap-1">
          <span className="font-serif italic text-[36px] leading-none">85</span>
          <span className="text-[12px] text-[--mute] font-semibold">/ 100</span>
        </div>
        <div className="text-[11px]" style={{ color:'#a89c8a' }}>
          Résonance communautaire — <span style={{ color:'#10b981' }}>+6 cette semaine</span>
        </div>
        {/* connector */}
        <svg width="140" height="30" style={{ position:'absolute', right:-130, top:34 }}>
          <path d="M2 15 Q70 15 130 18" stroke="rgba(245,242,235,0.18)" strokeDasharray="3 4" fill="none"/>
          <circle cx="130" cy="18" r="3" fill="#e15f41"/>
        </svg>
      </div>

      <div className="absolute hidden lg:flex items-center gap-2.5 px-3.5 py-2 rounded-2xl"
           style={{ right:-170, top:360, background:'rgba(24,22,20,0.85)', border:'1px solid var(--line)', backdropFilter:'blur(8px)', zIndex:10 }}>
        <span className="anim-pulse-dot" style={{ width:8, height:8, borderRadius:99, background:'#10b981', boxShadow:'0 0 12px #10b981'}}/>
        <div>
          <div className="text-[11px]" style={{ color:'#a89c8a' }}>Solaris Agri-Coop</div>
          <div className="text-[12.5px] font-semibold">Étape 3 de 5 · validée</div>
        </div>
        <svg width="140" height="30" style={{ position:'absolute', left:-130, top:14 }}>
          <path d="M138 15 Q70 15 10 18" stroke="rgba(245,242,235,0.18)" strokeDasharray="3 4" fill="none"/>
          <circle cx="10" cy="18" r="3" fill="#10b981"/>
        </svg>
      </div>

      <div className="absolute hidden lg:flex items-center gap-3 px-3.5 py-2.5 rounded-2xl"
           style={{ left:-220, bottom:120, width:230, background:'rgba(24,22,20,0.85)', border:'1px solid var(--line)', backdropFilter:'blur(8px)', zIndex:10 }}>
        <div className="w-9 h-9 rounded-xl flex items-center justify-center" style={{ background:'rgba(225,95,65,0.18)', color:'#e15f41' }}>
          <Icon name="users" size={18}/>
        </div>
        <div className="flex-1">
          <div className="text-[12.5px] font-semibold">128 nouveaux membres</div>
          <div className="text-[11px]" style={{ color:'#a89c8a' }}>cette semaine, 9 pays</div>
        </div>
        <svg width="140" height="30" style={{ position:'absolute', right:-130, top:18 }}>
          <path d="M2 15 Q70 5 130 8" stroke="rgba(245,242,235,0.18)" strokeDasharray="3 4" fill="none"/>
          <circle cx="130" cy="8" r="3" fill="#e15f41"/>
        </svg>
      </div>
    </div>
  );
}

function Hero() {
  return (
    <section className="relative pt-12 md:pt-20 pb-24" style={{ zIndex: 2 }}>
      <div className="mx-auto px-6" style={{ maxWidth: 1200 }}>
        <div className="grid lg:grid-cols-[1.05fr_1fr] gap-12 items-center">
          <div className="anim-fade-up">
            <div className="eyebrow">African Business Cooperatives</div>
            <h1 className="display mt-5 text-[58px] md:text-[78px] leading-[0.94]" style={{ letterSpacing:'-0.015em' }}>
              De l'<span className="ital">apprentissage</span><br/>
              à la <span className="ital">coopération</span>,<br/>
              <span style={{ color:'#e15f41' }}>de la coopération<br/>à la civilisation.</span>
            </h1>
            <p className="mt-7 text-[16px] md:text-[17px] leading-[1.55] max-w-[520px]" style={{ color:'#cfc4b3' }}>
              ABC&nbsp;OS est le système d'exploitation des coopératives africaines :
              une plateforme régénérative où l'on apprend, où l'on bâtit, et où l'on raconte —
              ensemble — les marques de la prochaine civilisation.
            </p>

            <div className="mt-9 flex flex-wrap gap-3">
              <a href="#join" className="anim-pulse-btn inline-flex items-center gap-2 h-14 px-6 rounded-full font-semibold text-[15px]"
                 style={{ background:'linear-gradient(180deg, #e15f41 0%, #d95436 100%)', color:'#fff', boxShadow:'0 18px 30px -12px rgba(225,95,65,0.55)' }}>
                Rejoindre la Coopérative <Icon name="arrowRight" size={16}/>
              </a>
              <a href="#piliers" className="inline-flex items-center gap-2 h-14 px-6 rounded-full font-semibold text-[15px]"
                 style={{ background:'rgba(245,242,235,0.04)', color:'#f5f2eb', border:'1px solid rgba(245,242,235,0.1)' }}>
                Découvrir la plateforme
              </a>
            </div>

            {/* Trust */}
            <div className="mt-10 flex flex-wrap items-center gap-x-7 gap-y-3 text-[12.5px]" style={{ color:'#a89c8a' }}>
              <div className="flex items-center gap-2">
                <span className="anim-pulse-dot" style={{ width:8, height:8, borderRadius:99, background:'#10b981', boxShadow:'0 0 12px #10b981' }}/>
                <span><span style={{ color:'#f5f2eb', fontWeight:700 }}>2 348</span> coopérateurs actifs</span>
              </div>
              <div>· <span style={{ color:'#f5f2eb', fontWeight:700 }}>124</span> coopératives</div>
              <div>· <span style={{ color:'#f5f2eb', fontWeight:700 }}>17</span> pays d'Afrique</div>
            </div>
          </div>

          {/* Phone */}
          <div className="flex justify-center lg:justify-end relative">
            <HeroPhone/>
          </div>
        </div>
      </div>
    </section>
  );
}

// ══════════════════════════════════════════════════════════════
// MARQUEE — partner cooperatives
// ══════════════════════════════════════════════════════════════
function Marquee() {
  const names = [
    'Solaris Agri-Coop · Kenya',
    'Umoja Weavers · Tanzania',
    'Sahel Solar Builders · Mali',
    'Kola Roasters · Côte d\'Ivoire',
    'Baobab Treasury · Sénégal',
    'Mboga Greens · Rwanda',
    'Sankofa Studio · Ghana',
    'Atlas Looms · Maroc',
  ];
  const row = [...names, ...names];
  return (
    <section className="relative py-8" style={{ borderTop:'1px solid var(--line)', borderBottom:'1px solid var(--line)', background:'rgba(18,17,16,0.5)', zIndex:2 }}>
      <div className="flex items-center gap-6 px-6 mx-auto" style={{ maxWidth: 1200 }}>
        <div className="text-[10.5px] uppercase tracking-[0.24em] font-bold flex-shrink-0" style={{ color:'#6b6258' }}>
          Coopératives membres
        </div>
        <div className="flex-1 overflow-hidden" style={{ maskImage:'linear-gradient(90deg, transparent, black 8%, black 92%, transparent)' }}>
          <div className="anim-marquee flex gap-10 whitespace-nowrap" style={{ width:'max-content' }}>
            {row.map((n, i) => (
              <span key={i} className="flex items-center gap-3 text-[14px]" style={{ color:'#a89c8a' }}>
                <span className="w-1.5 h-1.5 rounded-full" style={{ background:'#e15f41' }}/>
                {n}
              </span>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

// ══════════════════════════════════════════════════════════════
// MANIFESTO
// ══════════════════════════════════════════════════════════════
function Manifesto() {
  return (
    <section id="manifeste" className="relative py-28" style={{ zIndex:2 }}>
      <div className="mx-auto px-6" style={{ maxWidth: 1100 }}>
        <div className="grid md:grid-cols-[1fr_2fr] gap-14">
          <div>
            <div className="eyebrow">Manifeste</div>
            <h2 className="display text-[42px] md:text-[52px] leading-[1.0] mt-5" style={{ letterSpacing:'-0.015em' }}>
              Un système<br/>
              <span className="ital" style={{ color:'#10b981' }}>vivant.</span>
            </h2>
          </div>
          <div className="text-[18px] md:text-[20px] leading-[1.5]" style={{ color:'#d8cdbb' }}>
            <p>
              Nous croyons que l'avenir économique de l'Afrique ne s'écrit pas
              dans la concurrence, mais dans la <em className="font-serif ital" style={{ color:'#e15f41' }}>coopération</em>.
              Que les marques les plus durables naissent de communautés enracinées —
              dans la terre, dans le savoir, dans la mémoire.
            </p>
            <p className="mt-5">
              ABC&nbsp;OS rassemble dans un seul outil ce qu'il faut pour
              <em className="font-serif ital"> apprendre, structurer, financer et raconter </em>
              une coopérative régénérative. C'est une boussole solarpunk
              pour les bâtisseurs de la prochaine civilisation.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

// ══════════════════════════════════════════════════════════════
// FOUR PILLARS
// ══════════════════════════════════════════════════════════════
const PILLARS = [
  { key:'community', icon:'users',         title:'Community',     fr:'L\'Assemblée',         accent:'#e15f41',
    desc:'Discussions, événements et coopératives — l\'agora numérique où se nouent les alliances.',
    bullets:['Fil de discussion par hub', 'Annuaire des coopératives', 'Rencontres locales & en ligne'] },
  { key:'learn',     icon:'graduationCap', title:'Learn',         fr:'Cultiver le savoir',   accent:'#10b981',
    desc:'Six parcours pour bâtir un sens commun — du principe d\'architecte aux principes solarpunk.',
    bullets:['76 cours en français & anglais', 'Mentorat entre pairs', 'Certifications coopératives'] },
  { key:'build',     icon:'wrench',        title:'Build',         fr:'Bâtir ensemble',       accent:'#d4b042',
    desc:'Les outils concrets de la coopérative : contrats, trésorerie, partenaires, jalons.',
    bullets:['Templates juridiques', 'Trésorerie partagée', 'Suivi de jalons & équipes'] },
  { key:'brand',     icon:'award',         title:'Brand',         fr:'Votre identité',       accent:'#c47a96',
    desc:'Mesurer la résonance, raconter votre histoire, faire rayonner votre coopérative.',
    bullets:['Score d\'impact de marque', 'Stratégies de monétisation', 'Études de cas inspirantes'] },
];

function PillarRow() {
  return (
    <section id="piliers" className="relative py-24" style={{ zIndex:2 }}>
      <div className="mx-auto px-6" style={{ maxWidth: 1200 }}>
        <div className="flex items-end justify-between flex-wrap gap-6 mb-10">
          <div>
            <div className="eyebrow">Les quatre piliers</div>
            <h2 className="display text-[44px] md:text-[58px] leading-[1.0] mt-5" style={{ letterSpacing:'-0.015em' }}>
              Une plateforme,<br/>
              <span className="ital">quatre territoires</span> d'action.
            </h2>
          </div>
          <p className="max-w-[420px] text-[15.5px] leading-[1.55]" style={{ color:'#a89c8a' }}>
            Chaque hub est un outil indépendant et complet — ensemble, ils forment
            l'écosystème complet d'une coopérative régénérative.
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-5">
          {PILLARS.map((p) => (
            <article key={p.key} className="rounded-3xl p-7 relative overflow-hidden"
                     style={{ background:'var(--card)', border:'1px solid var(--line)' }}>
              <div className="absolute inset-0 pointer-events-none"
                   style={{ background:`radial-gradient(400px 200px at 100% 0%, ${p.accent}1f, transparent 70%)` }}/>
              <div className="flex items-start justify-between relative">
                <div className="w-12 h-12 rounded-2xl flex items-center justify-center"
                     style={{ background:`${p.accent}22`, color:p.accent }}>
                  <Icon name={p.icon} size={22} stroke={2}/>
                </div>
                <div className="text-[10.5px] tracking-[0.22em] uppercase font-bold" style={{ color:p.accent }}>{p.fr}</div>
              </div>
              <h3 className="display text-[36px] mt-5 leading-none">{p.title}</h3>
              <p className="text-[14.5px] mt-3 leading-[1.5] max-w-[440px]" style={{ color:'#cfc4b3' }}>
                {p.desc}
              </p>
              <ul className="mt-5 space-y-2 text-[13.5px]" style={{ color:'#a89c8a' }}>
                {p.bullets.map((b, i) => (
                  <li key={i} className="flex items-center gap-2.5">
                    <Icon name="check" size={14} stroke={2.5} style={{ color:p.accent }}/>
                    {b}
                  </li>
                ))}
              </ul>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

// ══════════════════════════════════════════════════════════════
// TOUR — 4 phones side by side
// ══════════════════════════════════════════════════════════════
function PhoneTour() {
  const [active, setActive] = React.useState(0);
  return (
    <section className="relative py-24" style={{ zIndex:2, background:'linear-gradient(180deg, transparent 0%, rgba(225,95,65,0.04) 50%, transparent 100%)' }}>
      <div className="mx-auto px-6" style={{ maxWidth: 1280 }}>
        <div className="flex items-end justify-between flex-wrap gap-6 mb-10">
          <div>
            <div className="eyebrow">Une visite</div>
            <h2 className="display text-[44px] md:text-[58px] leading-[1.0] mt-5">
              L'OS en main, <span className="ital">tout le temps</span>.
            </h2>
          </div>
          <p className="max-w-[440px] text-[15.5px] leading-[1.55]" style={{ color:'#a89c8a' }}>
            Survolez chaque écran pour voir à quoi ressemble une journée
            dans la coopérative. Tout est mobile-first, hors-ligne disponible.
          </p>
        </div>

        <div className="relative">
          {/* Horizon line */}
          <div style={{
            position:'absolute', left:0, right:0, top:'62%', height:1,
            background:'linear-gradient(90deg, transparent, rgba(225,95,65,0.45), transparent)'
          }}/>

          <div className="flex gap-6 lg:gap-10 overflow-x-auto pb-8 px-2 scrollbar-hide justify-start lg:justify-center">
            {TABS_LANDING.map((t, i) => {
              const isActive = active === i;
              return (
                <div key={t.key}
                     onMouseEnter={() => setActive(i)}
                     className="flex-shrink-0 flex flex-col items-center gap-5 cursor-pointer transition-transform duration-500"
                     style={{ transform: isActive ? 'translateY(-12px)' : 'translateY(0)' }}>
                  <div className="relative" style={{
                    filter: isActive ? 'drop-shadow(0 40px 50px rgba(0,0,0,0.5))' : 'drop-shadow(0 18px 25px rgba(0,0,0,0.3))',
                    opacity: isActive ? 1 : 0.78,
                    transition: 'all .4s',
                  }}>
                    <EmbeddedPhone tab={t.key} width={260} height={560} showNav={true}/>
                  </div>
                  <div className="text-center">
                    <div className="text-[10.5px] tracking-[0.22em] uppercase font-bold"
                         style={{ color: isActive ? '#e15f41' : '#6b6258' }}>0{i+1}</div>
                    <div className="display text-[24px] mt-1" style={{ color: isActive ? '#f5f2eb':'#a89c8a' }}>{t.label}</div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </section>
  );
}

// ══════════════════════════════════════════════════════════════
// STATS
// ══════════════════════════════════════════════════════════════
function Stats() {
  const items = [
    { n:'124',  l:'Coopératives bâties' },
    { n:'2 348',l:'Coopérateurs actifs' },
    { n:'76',   l:'Cours et parcours' },
    { n:'17',   l:'Pays d\'Afrique' },
    { n:'€2,4M',l:'Financements débloqués' },
    { n:'92%',  l:'Taux de rétention' },
  ];
  return (
    <section className="relative py-12" style={{ zIndex:2, borderTop:'1px solid var(--line)', borderBottom:'1px solid var(--line)' }}>
      <div className="mx-auto px-6 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-y-8 gap-x-6" style={{ maxWidth: 1200 }}>
        {items.map((s) => (
          <div key={s.l}>
            <div className="display text-[44px] leading-none" style={{ letterSpacing:'-0.02em' }}>
              {s.n}
            </div>
            <div className="text-[12px] mt-2 uppercase tracking-[0.16em] font-semibold" style={{ color:'#a89c8a' }}>
              {s.l}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

// ══════════════════════════════════════════════════════════════
// PROGRAMME — 3-step journey
// ══════════════════════════════════════════════════════════════
const STEPS = [
  { n:'01', title:'Apprendre',  icon:'graduationCap', tex:'tex-weave',
    body:'Embarquez sur un parcours en six chapitres — du principe d\'architecte aux principes solarpunk. À votre rythme, en français ou en anglais.' },
  { n:'02', title:'Coopérer',   icon:'users',         tex:'tex-garden',
    body:'Rejoignez une coopérative existante ou fondez la vôtre. Trouvez des co-bâtisseurs alignés sur votre mission, près de chez vous ou ailleurs sur le continent.' },
  { n:'03', title:'Civiliser',  icon:'sun',           tex:'tex-solar',
    body:'Lancez votre marque coopérative. Mesurez votre impact, racontez votre histoire, inscrivez votre œuvre dans la civilisation régénérative à venir.' },
];

function Programme() {
  return (
    <section id="programme" className="relative py-24" style={{ zIndex:2 }}>
      <div className="mx-auto px-6" style={{ maxWidth: 1200 }}>
        <div className="text-center mb-14">
          <div className="eyebrow justify-center inline-flex">Le programme</div>
          <h2 className="display text-[44px] md:text-[64px] leading-[1.0] mt-5" style={{ letterSpacing:'-0.015em' }}>
            Trois actes pour <span className="ital" style={{ color:'#e15f41' }}>bâtir</span>.
          </h2>
        </div>

        <div className="grid md:grid-cols-3 gap-5">
          {STEPS.map((s, i) => (
            <div key={s.n} className="rounded-3xl overflow-hidden relative"
                 style={{ background:'var(--card)', border:'1px solid var(--line)' }}>
              <div className={s.tex} style={{ height:140, position:'relative' }}>
                <div style={{ position:'absolute', inset:0, background:'linear-gradient(180deg, transparent 30%, rgba(24,22,20,0.95) 100%)' }}/>
                <div className="absolute top-4 left-5 right-5 flex items-start justify-between">
                  <div className="text-[10.5px] tracking-[0.24em] uppercase font-bold text-white opacity-90">
                    Acte {s.n}
                  </div>
                  <div className="w-11 h-11 rounded-2xl flex items-center justify-center"
                       style={{ background:'rgba(0,0,0,0.4)', backdropFilter:'blur(6px)', color:'#fff' }}>
                    <Icon name={s.icon} size={20}/>
                  </div>
                </div>
                <div className="absolute bottom-3 left-5">
                  <div className="display text-[40px] leading-none" style={{ color:'#fff' }}>{s.title}</div>
                </div>
              </div>
              <div className="p-6">
                <p className="text-[14.5px] leading-[1.55]" style={{ color:'#cfc4b3' }}>
                  {s.body}
                </p>
                <div className="mt-5 inline-flex items-center gap-1.5 text-[12.5px] font-semibold" style={{ color:'#e15f41' }}>
                  En savoir plus <Icon name="arrowRight" size={13}/>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

// ══════════════════════════════════════════════════════════════
// TESTIMONIALS
// ══════════════════════════════════════════════════════════════
function Testimonials() {
  return (
    <section id="cooperatives" className="relative py-24" style={{ zIndex:2 }}>
      <div className="mx-auto px-6" style={{ maxWidth: 1200 }}>
        <div className="grid lg:grid-cols-[1fr_1fr] gap-5">
          {/* Big quote */}
          <article className="rounded-3xl p-9 md:p-12 relative overflow-hidden"
                   style={{ background:'var(--card)', border:'1px solid var(--line)' }}>
            <div className="absolute inset-0 pointer-events-none" style={{
              background:'radial-gradient(500px 300px at 0% 0%, rgba(16,185,129,0.10), transparent 60%)'
            }}/>
            <div className="display text-[120px] leading-none" style={{ color:'#e15f41', height:60 }}>"</div>
            <blockquote className="display text-[26px] md:text-[34px] leading-[1.2] mt-3" style={{ letterSpacing:'-0.005em' }}>
              ABC&nbsp;OS a transformé notre coopérative de tisserandes
              en une <span className="ital" style={{ color:'#10b981' }}>marque continentale</span>. Avant : un cahier et des
              messages WhatsApp éparpillés. Aujourd'hui : un système qui apprend,
              qui structure, qui raconte.
            </blockquote>
            <div className="flex items-center gap-3 mt-8">
              <Avatar initials="NN" hue={320} size={48}/>
              <div>
                <div className="font-semibold text-[15px]">Nailah Nyathi</div>
                <div className="text-[12.5px]" style={{ color:'#a89c8a' }}>Fondatrice · Umoja Weavers Collective · Tanzania</div>
              </div>
            </div>
          </article>

          {/* Two stacked smaller */}
          <div className="flex flex-col gap-5">
            <article className="rounded-3xl p-7 relative" style={{ background:'var(--card)', border:'1px solid var(--line)' }}>
              <div className="flex items-start gap-3">
                <Avatar initials="AO" hue={28} size={44}/>
                <div>
                  <div className="font-semibold text-[15px]">Amara Okoro</div>
                  <div className="text-[12px]" style={{ color:'#a89c8a' }}>Solaris Agri-Coop · Kenya</div>
                </div>
              </div>
              <p className="text-[15px] mt-4 leading-[1.5]" style={{ color:'#d8cdbb' }}>
                Le hub <span style={{ color:'#10b981', fontWeight:600 }}>Build</span> nous a donné la rigueur d'une scale-up
                — sans renier nos valeurs. Trois étapes franchies en deux mois.
              </p>
            </article>
            <article className="rounded-3xl p-7 relative" style={{ background:'var(--card)', border:'1px solid var(--line)' }}>
              <div className="flex items-start gap-3">
                <Avatar initials="KP" hue={210} size={44}/>
                <div>
                  <div className="font-semibold text-[15px]">Kaelan Patel</div>
                  <div className="text-[12px]" style={{ color:'#a89c8a' }}>Sahel Solar Builders · Mali</div>
                </div>
              </div>
              <p className="text-[15px] mt-4 leading-[1.5]" style={{ color:'#d8cdbb' }}>
                Les parcours Brand nous ont permis de doubler notre portée en six mois.
                Le storytelling coopératif, c'est l'arme du siècle.
              </p>
            </article>
          </div>
        </div>
      </div>
    </section>
  );
}

// ══════════════════════════════════════════════════════════════
// FAQ
// ══════════════════════════════════════════════════════════════
const FAQ_ITEMS = [
  { q:'À qui s\'adresse ABC OS ?', a:'À tout entrepreneur, artisan, agriculteur ou créatif basé en Afrique (ou de la diaspora) qui souhaite construire une activité économique en coopération plutôt qu\'en concurrence. Les coopératives existantes peuvent migrer leur fonctionnement sur la plateforme.' },
  { q:'Combien coûte la plateforme ?',         a:'L\'apprentissage est gratuit et le restera. Les outils Build et Brand sont facturés au prorata du chiffre d\'affaires de votre coopérative — jamais en avance, et plafonnés.' },
  { q:'L\'application fonctionne-t-elle hors-ligne ?', a:'Oui. ABC OS est conçu pour des terrains avec une connectivité variable : cours téléchargeables, synchronisation en arrière-plan, mode léger sur mobile.' },
  { q:'Comment rejoindre une coopérative existante ?',  a:'Depuis le Community Hub, parcourez l\'annuaire des coopératives, candidatez à celles qui résonnent avec votre mission. Les coopératives valident leurs membres collectivement.' },
];

function FAQ() {
  const [open, setOpen] = React.useState(0);
  return (
    <section id="faq" className="relative py-24" style={{ zIndex:2 }}>
      <div className="mx-auto px-6" style={{ maxWidth: 980 }}>
        <div className="text-center mb-12">
          <div className="eyebrow justify-center inline-flex">Questions courantes</div>
          <h2 className="display text-[44px] md:text-[56px] leading-[1.0] mt-5">
            Avant de <span className="ital">rejoindre</span>.
          </h2>
        </div>
        <div className="rounded-3xl overflow-hidden" style={{ background:'var(--card)', border:'1px solid var(--line)' }}>
          {FAQ_ITEMS.map((f, i) => {
            const isOpen = open === i;
            return (
              <button key={i} onClick={() => setOpen(isOpen ? -1 : i)}
                      className="w-full text-left px-6 py-5 flex items-start gap-4"
                      style={{ borderBottom: i === FAQ_ITEMS.length-1 ? 'none' : '1px solid var(--line)' }}>
                <div className="flex-1">
                  <div className="text-[16px] font-semibold flex items-center justify-between gap-4">
                    {f.q}
                    <Icon name="chevronDown" size={18}
                          style={{ color:'#a89c8a', transform: isOpen ? 'rotate(180deg)' : 'none', transition:'transform .2s' }}/>
                  </div>
                  <div style={{
                    maxHeight: isOpen ? 220 : 0, opacity: isOpen ? 1 : 0,
                    overflow:'hidden', transition:'all .35s ease',
                  }}>
                    <p className="text-[14.5px] mt-3 leading-[1.55]" style={{ color:'#cfc4b3' }}>
                      {f.a}
                    </p>
                  </div>
                </div>
              </button>
            );
          })}
        </div>
      </div>
    </section>
  );
}

// ══════════════════════════════════════════════════════════════
// CTA + FOOTER
// ══════════════════════════════════════════════════════════════
function CTABand() {
  const [email, setEmail] = React.useState('');
  const [sent, setSent] = React.useState(false);
  return (
    <section id="join" className="relative py-28" style={{ zIndex:2 }}>
      <div className="mx-auto px-6" style={{ maxWidth: 1100 }}>
        <div className="rounded-[36px] relative overflow-hidden p-10 md:p-16"
             style={{ background:'#181614', border:'1px solid var(--line)' }}>
          {/* sun */}
          <div style={{
            position:'absolute', right:-180, top:-180, width:520, height:520, borderRadius:'50%',
            background:'radial-gradient(50% 50% at 50% 50%, rgba(225,95,65,0.45), rgba(225,95,65,0) 70%)'
          }}/>
          {/* rays */}
          <svg style={{ position:'absolute', right:-60, top:-60, opacity:0.4 }} width="400" height="400" viewBox="0 0 400 400">
            {Array.from({ length: 30 }).map((_, i) => {
              const a = (i * Math.PI * 2) / 30;
              const x1 = 200 + Math.cos(a) * 140, y1 = 200 + Math.sin(a) * 140;
              const x2 = 200 + Math.cos(a) * 200, y2 = 200 + Math.sin(a) * 200;
              return <line key={i} x1={x1} y1={y1} x2={x2} y2={y2} stroke="#e15f41" strokeWidth="1" opacity={i%3===0?0.7:0.3}/>;
            })}
          </svg>

          <div className="relative max-w-[640px]">
            <div className="eyebrow">L'invitation</div>
            <h2 className="display text-[48px] md:text-[68px] leading-[0.98] mt-5" style={{ letterSpacing:'-0.015em' }}>
              Bâtissons<br/>
              la <span className="ital" style={{ color:'#e15f41' }}>prochaine civilisation</span>,<br/>
              <span className="ital" style={{ color:'#10b981' }}>ensemble</span>.
            </h2>
            <p className="mt-7 text-[16px] max-w-[480px] leading-[1.55]" style={{ color:'#cfc4b3' }}>
              Inscrivez-vous à la liste fondatrice. Vous recevrez le manifeste,
              l'accès anticipé à la plateforme et une invitation à la prochaine
              assemblée régénérative.
            </p>

            <form onSubmit={(e) => { e.preventDefault(); setSent(true); }}
                  className="mt-8 flex flex-col sm:flex-row gap-2.5 max-w-[520px]">
              <input
                type="email" required value={email} onChange={(e) => setEmail(e.target.value)}
                placeholder="votre@email.coop"
                className="flex-1 h-14 px-5 rounded-full text-[15px] outline-none"
                style={{ background:'rgba(245,242,235,0.05)', color:'#f5f2eb', border:'1px solid rgba(245,242,235,0.12)' }}
              />
              <button type="submit"
                      className="h-14 px-6 rounded-full font-semibold text-[15px] inline-flex items-center justify-center gap-2"
                      style={{ background:'linear-gradient(180deg, #e15f41 0%, #d95436 100%)', color:'#fff', boxShadow:'0 18px 30px -12px rgba(225,95,65,0.55)' }}>
                {sent ? <>Bienvenue ✦</> : <>Rejoindre la liste <Icon name="arrowRight" size={15}/></>}
              </button>
            </form>
            <div className="mt-3 text-[12px]" style={{ color:'#6b6258' }}>
              Pas de spam. Une lettre par mois. Désinscription en un clic.
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function Footer() {
  return (
    <footer className="relative pt-16 pb-10" style={{ zIndex:2, borderTop:'1px solid var(--line)' }}>
      <div className="mx-auto px-6 grid md:grid-cols-[1.4fr_1fr_1fr_1fr] gap-10" style={{ maxWidth: 1200 }}>
        <div>
          <Wordmark/>
          <p className="mt-4 text-[13px] leading-[1.55] max-w-[300px]" style={{ color:'#a89c8a' }}>
            African Business Cooperatives — Operating System.
            Un commun numérique pour la prochaine civilisation régénérative.
          </p>
        </div>
        {[
          ['Plateforme', ['Community','Learn','Build','Brand']],
          ['Programme',  ['Manifeste','Coopératives','Cas d\'étude','Tarifs']],
          ['Maison',     ['Équipe','Carrières','Presse','Contact']],
        ].map(([title, links]) => (
          <div key={title}>
            <div className="text-[10.5px] tracking-[0.22em] uppercase font-bold mb-3" style={{ color:'#6b6258' }}>{title}</div>
            <ul className="space-y-2.5 text-[13.5px]" style={{ color:'#cfc4b3' }}>
              {links.map((l) => <li key={l}><a href="#" className="hover:text-white">{l}</a></li>)}
            </ul>
          </div>
        ))}
      </div>
      <div className="mx-auto px-6 mt-12 pt-6 flex flex-wrap items-center justify-between gap-3" style={{ maxWidth: 1200, borderTop:'1px solid var(--line)' }}>
        <div className="text-[12px]" style={{ color:'#6b6258' }}>
          © 2026 ABC OS · Un commun open-source · <a href="#" className="underline" style={{ color:'#a89c8a' }}>Licence Régénérative</a>
        </div>
        <div className="flex items-center gap-4 text-[12px]" style={{ color:'#6b6258' }}>
          <span>De l'apprentissage à la civilisation.</span>
          <span style={{ width:6, height:6, borderRadius:99, background:'#e15f41' }}/>
          <span>Made on the continent.</span>
        </div>
      </div>
    </footer>
  );
}

// ══════════════════════════════════════════════════════════════
// APP
// ══════════════════════════════════════════════════════════════
function Landing() {
  return (
    <div style={{ position: 'relative' }}>
      <div className="horizon"/>
      <div className="grain"/>
      <div style={{ position:'relative', zIndex:5, padding:'16px 16px 0' }}>
        <TopNav/>
      </div>
      <Hero/>
      <Marquee/>
      <Manifesto/>
      <PillarRow/>
      <PhoneTour/>
      <Stats/>
      <Programme/>
      <Testimonials/>
      <FAQ/>
      <CTABand/>
      <Footer/>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<Landing/>);
