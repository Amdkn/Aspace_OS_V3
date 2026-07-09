// ABC OS — All screen components
// Tokens
const COLORS = {
  bg: '#121110',
  bgAlt: '#181614',
  card: '#221f1c',
  cardHi: '#2a2622',
  line: 'rgba(245,242,235,0.08)',
  text: '#f5f2eb',
  textMute: '#a89c8a',
  textDim: '#6b6258',
  green: '#10b981',
  greenDeep: '#059669',
  terracotta: '#e15f41',
  terracottaDeep: '#d95436',
  blue: '#5b8bb7',
};

// ── Small atoms ─────────────────────────────────────────────
function Avatar({ initials, hue = 30, size = 36, ring = false }) {
  return (
    <div
      style={{
        width: size, height: size, borderRadius: '50%',
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        fontWeight: 700, fontSize: size * 0.36, color: '#fff',
        letterSpacing: 0.2,
        background: `radial-gradient(120% 120% at 25% 20%, hsl(${hue} 55% 55%), hsl(${hue + 25} 45% 28%))`,
        boxShadow: ring ? `0 0 0 2px ${COLORS.card}` : 'none',
        flexShrink: 0,
      }}
    >
      {initials}
    </div>
  );
}

function Pill({ children, color = '#10b981', bg, className = '' }) {
  return (
    <span
      className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold tracking-wide uppercase ${className}`}
      style={{ background: bg || `${color}22`, color }}
    >
      <span style={{ width: 6, height: 6, borderRadius: 99, background: color, display: 'inline-block' }} />
      {children}
    </span>
  );
}

function ProgressBar({ value, color = COLORS.green, height = 6 }) {
  return (
    <div style={{ height, background: 'rgba(245,242,235,0.07)', borderRadius: 999, overflow: 'hidden', width: '100%' }}>
      <div style={{
        width: `${value}%`, height: '100%',
        background: `linear-gradient(90deg, ${color} 0%, ${color}cc 100%)`,
        borderRadius: 999,
        boxShadow: `0 0 12px ${color}55`,
      }} />
    </div>
  );
}

function ScreenHeader({ title, kicker, children }) {
  return (
    <div className="px-5 pt-3 pb-2">
      {kicker && (
        <div className="text-[11px] tracking-[0.18em] uppercase font-semibold mb-1.5"
             style={{ color: COLORS.terracotta }}>{kicker}</div>
      )}
      <h1 className="text-[28px] leading-[1.05] font-bold" style={{ color: COLORS.text, letterSpacing: '-0.02em' }}>
        {title}
      </h1>
      {children && <div className="mt-3">{children}</div>}
    </div>
  );
}

function SearchBar({ placeholder, accessory }) {
  return (
    <div className="flex items-center gap-2">
      <div
        className="flex-1 flex items-center gap-2.5 px-3.5 h-11 rounded-2xl"
        style={{ background: COLORS.card, border: `1px solid ${COLORS.line}` }}
      >
        <Icon name="search" size={17} style={{ color: COLORS.textMute }} stroke={2} />
        <input
          placeholder={placeholder}
          className="flex-1 bg-transparent outline-none text-[13.5px]"
          style={{ color: COLORS.text }}
        />
      </div>
      {accessory}
    </div>
  );
}

function NotifBell() {
  return (
    <button className="relative w-11 h-11 rounded-2xl flex items-center justify-center"
            style={{ background: COLORS.card, border: `1px solid ${COLORS.line}`, color: COLORS.text }}>
      <Icon name="bell" size={19} stroke={1.9} />
      <span className="absolute top-2.5 right-2.5 w-2 h-2 rounded-full" style={{ background: COLORS.terracotta }} />
    </button>
  );
}

function CardFrame({ children, className = '', style = {} }) {
  return (
    <div
      className={`rounded-3xl ${className}`}
      style={{
        background: COLORS.card,
        border: `1px solid ${COLORS.line}`,
        ...style,
      }}
    >
      {children}
    </div>
  );
}

// ══════════════════════════════════════════════════════════════
// SPLASH
// ══════════════════════════════════════════════════════════════
function SplashScreen({ onEnter }) {
  return (
    <div className="abc-screen relative h-full flex flex-col overflow-hidden" style={{ background: COLORS.bg, color: COLORS.text }}>
      {/* Background rays */}
      <div style={{
        position: 'absolute', inset: 0, zIndex: 0, opacity: 0.55,
        background:
          'radial-gradient(420px 320px at 50% 22%, rgba(225,95,65,0.35), transparent 70%),' +
          'radial-gradient(620px 480px at 50% 110%, rgba(16,185,129,0.18), transparent 70%)',
      }} />
      {/* Sun mark */}
      <div className="flex-1 flex flex-col items-center justify-center px-8 relative z-10 pt-16">
        <div className="relative" style={{ width: 132, height: 132 }}>
          <svg viewBox="0 0 132 132" width="132" height="132">
            <defs>
              <radialGradient id="sunG" cx="50%" cy="40%" r="60%">
                <stop offset="0%" stopColor="#f6c47a" />
                <stop offset="55%" stopColor="#e15f41" />
                <stop offset="100%" stopColor="#7a2818" />
              </radialGradient>
            </defs>
            {/* rays */}
            {Array.from({ length: 12 }).map((_, i) => {
              const a = (i * Math.PI * 2) / 12;
              const x1 = 66 + Math.cos(a) * 50, y1 = 66 + Math.sin(a) * 50;
              const x2 = 66 + Math.cos(a) * 64, y2 = 66 + Math.sin(a) * 64;
              return <line key={i} x1={x1} y1={y1} x2={x2} y2={y2} stroke="#e15f41" strokeWidth="2" strokeLinecap="round" opacity="0.85" />;
            })}
            <circle cx="66" cy="66" r="38" fill="url(#sunG)" />
            <path d="M48 76c8-4 14-4 18 0 4 4 10 4 18 0" stroke="#1a0e08" strokeWidth="3" strokeLinecap="round" fill="none" opacity="0.45"/>
            {/* leaf */}
            <path d="M82 50c8-2 16 4 14 12-10 0-16-4-14-12z" fill="#10b981" />
          </svg>
        </div>

        <div className="mt-7 text-center">
          <div className="text-[13px] tracking-[0.32em] uppercase font-semibold" style={{ color: COLORS.terracotta }}>
            ABC&nbsp;OS
          </div>
          <div className="font-serif italic text-[30px] leading-[1.15] mt-3 max-w-[300px]" style={{ color: COLORS.text }}>
            De l'Apprentissage<br/>à la Coopération,<br/>
            <span style={{ color: COLORS.green }}>de la Coopération<br/>à la Civilisation.</span>
          </div>
          <div className="text-[12.5px] mt-4" style={{ color: COLORS.textMute }}>
            African Business Cooperatives — Operating System
          </div>
        </div>
      </div>

      {/* Buttons */}
      <div className="px-6 pb-12 pt-2 flex flex-col gap-2.5 relative z-10">
        <button
          onClick={onEnter}
          className="h-14 rounded-2xl font-semibold text-[15px] flex items-center justify-center gap-2 anim-pulse"
          style={{
            background: `linear-gradient(180deg, ${COLORS.terracotta} 0%, ${COLORS.terracottaDeep} 100%)`,
            color: '#fff',
            boxShadow: '0 14px 30px -10px rgba(225,95,65,0.55)',
          }}
        >
          Rejoindre la Coopérative
          <Icon name="arrowRight" size={17} />
        </button>
        <button
          onClick={onEnter}
          className="h-14 rounded-2xl font-semibold text-[14.5px]"
          style={{ background: 'transparent', color: COLORS.text, border: `1px solid ${COLORS.line}` }}
        >
          Se connecter
        </button>
        <div className="text-center text-[11px] mt-2 tracking-wide" style={{ color: COLORS.textDim }}>
          Une œuvre régénérative · Open Source
        </div>
      </div>
    </div>
  );
}

// ══════════════════════════════════════════════════════════════
// COMMUNITY
// ══════════════════════════════════════════════════════════════
function FeedCard({ name, initials, hue, time, badge, text, likes, comments, shares, image, last }) {
  return (
    <article
      className="anim-fade-up"
      style={{
        background: COLORS.card,
        border: `1px solid ${COLORS.line}`,
        borderRadius: 24,
        padding: 16,
        marginBottom: last ? 0 : 14,
      }}
    >
      <header className="flex items-center gap-3">
        <Avatar initials={initials} hue={hue} size={42} />
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2">
            <div className="text-[14.5px] font-semibold truncate" style={{ color: COLORS.text }}>{name}</div>
            {badge && (
              <span className="text-[10px] px-1.5 py-0.5 rounded-md font-semibold tracking-wide"
                    style={{ background: `${COLORS.green}22`, color: COLORS.green }}>
                {badge}
              </span>
            )}
          </div>
          <div className="text-[11.5px]" style={{ color: COLORS.textMute }}>{time}</div>
        </div>
        <button className="w-8 h-8 rounded-full flex items-center justify-center" style={{ color: COLORS.textMute }}>
          <svg width="16" height="4" viewBox="0 0 16 4"><circle cx="2" cy="2" r="1.6" fill="currentColor"/><circle cx="8" cy="2" r="1.6" fill="currentColor"/><circle cx="14" cy="2" r="1.6" fill="currentColor"/></svg>
        </button>
      </header>

      <p className="text-[14px] leading-[1.5] mt-3" style={{ color: COLORS.text }}>
        {text}
      </p>

      {image && (
        <div className="mt-3 rounded-2xl overflow-hidden relative" style={{ height: 168, border: `1px solid ${COLORS.line}` }}>
          <div className={image} style={{ position: 'absolute', inset: 0 }} />
          <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(180deg, transparent 50%, rgba(0,0,0,0.55) 100%)' }} />
          <div className="absolute bottom-3 left-3 right-3 flex items-end justify-between">
            <div>
              <div className="text-[11px] uppercase tracking-[0.18em] font-semibold" style={{ color: '#cdebd6' }}>
                Solaris Agri-Coop · Kenya
              </div>
              <div className="text-[15px] font-semibold text-white">Maïs &amp; sorgho · Saison 2</div>
            </div>
            <Pill color="#cdebd6">harvest</Pill>
          </div>
        </div>
      )}

      <footer className="flex items-center gap-5 mt-3.5 pt-3.5" style={{ borderTop: `1px solid ${COLORS.line}` }}>
        <button className="flex items-center gap-1.5 text-[12.5px] font-medium" style={{ color: COLORS.textMute }}>
          <Icon name="heart" size={16} stroke={1.7} /> {likes}
        </button>
        <button className="flex items-center gap-1.5 text-[12.5px] font-medium" style={{ color: COLORS.textMute }}>
          <Icon name="message" size={16} stroke={1.7} /> {comments}
        </button>
        {shares !== undefined && (
          <button className="flex items-center gap-1.5 text-[12.5px] font-medium" style={{ color: COLORS.textMute }}>
            <Icon name="share" size={15} stroke={1.7} /> {shares}
          </button>
        )}
        <div className="flex-1" />
        <button style={{ color: COLORS.textMute }}>
          <Icon name="bookmark" size={16} stroke={1.7} />
        </button>
      </footer>
    </article>
  );
}

function CommunityHub() {
  const [sub, setSub] = React.useState('Feed');
  return (
    <div className="abc-screen relative h-full flex flex-col" style={{ background: COLORS.bg, color: COLORS.text }}>
      <ScreenHeader title="Community" kicker="L'Assemblée">
        <SearchBar placeholder="Search discussions and members…" accessory={<NotifBell />} />
        <div className="flex items-center gap-5 mt-4 px-1 text-[14px] font-semibold" style={{ color: COLORS.textMute }}>
          {['Feed', 'Co-ops', 'Events'].map((t) => (
            <button key={t} onClick={() => setSub(t)}
              className={`tab-underline ${sub === t ? 'active' : ''}`}
              style={{ color: sub === t ? COLORS.text : COLORS.textMute, paddingBottom: 2 }}>
              {t}
              {t === 'Events' && (
                <span className="ml-1.5 text-[10px] px-1.5 py-[1px] rounded-full font-bold"
                      style={{ background: COLORS.terracotta, color: '#fff' }}>3</span>
              )}
            </button>
          ))}
        </div>
      </ScreenHeader>

      <div className="flex-1 overflow-y-auto px-5 pt-3 pb-28 scrollbar-hide">
        <FeedCard
          name="Kaelan Patel"
          initials="KP"
          hue={210}
          time="2h ago · Lagos, NG"
          text={
            <>
              Looking for advice from anyone who has gone through the process. What are the key documents and registrations required?{' '}
              <span style={{ color: COLORS.terracotta, fontWeight: 600 }}>#Legal</span>{' '}
              <span style={{ color: COLORS.terracotta, fontWeight: 600 }}>#Startup</span>
            </>
          }
          likes={12}
          comments={5}
          shares={2}
        />
        <FeedCard
          name="Amara Okoro"
          initials="AO"
          hue={28}
          badge="Co-op lead"
          time="1 day ago · Nairobi, KE"
          text={
            <>
              Our Agri-Tech coop just secured its first round of funding! A huge thank you to everyone in the{' '}
              <span style={{ color: COLORS.green, fontWeight: 600 }}>#BuildHub</span>{' '}
              for the feedback on our pitch deck. The journey continues 🌱
            </>
          }
          image="tex-field"
          likes={78}
          comments={23}
          last
        />

        <div className="mt-3 mb-1 text-[11px] tracking-[0.18em] uppercase font-semibold px-1" style={{ color: COLORS.textDim }}>
          Suggested for you
        </div>
        <CardFrame className="px-4 py-3 flex items-center gap-3">
          <div className="w-11 h-11 rounded-2xl flex items-center justify-center"
               style={{ background: `${COLORS.green}22`, color: COLORS.green }}>
            <Icon name="users" size={20} />
          </div>
          <div className="flex-1 min-w-0">
            <div className="text-[14px] font-semibold">Sahel Solar Builders</div>
            <div className="text-[12px]" style={{ color: COLORS.textMute }}>248 members · 4 you know</div>
          </div>
          <button className="px-3.5 h-9 rounded-full text-[12.5px] font-semibold"
                  style={{ background: COLORS.terracotta, color: '#fff' }}>
            Join
          </button>
        </CardFrame>
      </div>

      {/* FAB */}
      <button
        className="absolute right-5 bottom-[112px] w-14 h-14 rounded-full flex items-center justify-center"
        style={{
          background: `linear-gradient(180deg, ${COLORS.terracotta}, ${COLORS.terracottaDeep})`,
          color: '#fff',
          boxShadow: '0 14px 30px -8px rgba(225,95,65,0.6), 0 2px 0 rgba(255,255,255,0.15) inset',
        }}
      >
        <Icon name="plus" size={26} stroke={2.3} />
      </button>
    </div>
  );
}

// ══════════════════════════════════════════════════════════════
// LEARN
// ══════════════════════════════════════════════════════════════
function CourseCard({ title, sub, progress, color, accent }) {
  return (
    <div
      className="flex-shrink-0 rounded-3xl p-4 flex flex-col justify-between"
      style={{
        width: 200, height: 168,
        background: COLORS.card,
        border: `1px solid ${COLORS.line}`,
      }}
    >
      <div className="w-10 h-10 rounded-xl flex items-center justify-center"
           style={{ background: `${accent}22`, color: accent }}>
        <Icon name={color} size={20} />
      </div>
      <div>
        <div className="text-[10.5px] tracking-[0.18em] uppercase font-semibold mb-1" style={{ color: COLORS.textDim }}>
          {sub}
        </div>
        <div className="text-[15.5px] font-semibold leading-[1.2] mb-2.5" style={{ color: COLORS.text }}>
          {title}
        </div>
        <div className="flex items-center gap-2">
          <ProgressBar value={progress} color={accent} height={5} />
          <span className="text-[11px] font-semibold" style={{ color: accent }}>{progress}%</span>
        </div>
      </div>
    </div>
  );
}

function RecCard({ title, sub, tex, badge }) {
  return (
    <div
      className="rounded-3xl relative overflow-hidden flex-shrink-0"
      style={{
        width: 220, height: 248,
        border: `1px solid ${COLORS.line}`,
      }}
    >
      <div className={tex} style={{ position: 'absolute', inset: 0 }} />
      <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(180deg, rgba(0,0,0,0.05) 35%, rgba(8,6,4,0.9) 100%)' }} />
      <div className="absolute top-3 left-3">
        <Pill color="#f5f2eb" bg="rgba(0,0,0,0.4)">{badge}</Pill>
      </div>
      <div className="absolute bottom-4 left-4 right-4">
        <div className="text-[11px] tracking-[0.18em] uppercase font-semibold opacity-80" style={{ color: '#fff' }}>{sub}</div>
        <div className="text-[18px] font-bold mt-1 leading-[1.15]" style={{ color: '#fff' }}>{title}</div>
        <div className="text-[12px] mt-1.5 opacity-80" style={{ color: '#fff' }}>8 lessons · 2h 40m</div>
      </div>
    </div>
  );
}

function CategoryTile({ icon, title, count, accent }) {
  return (
    <button
      className="rounded-2xl p-3.5 flex flex-col items-start gap-3 text-left"
      style={{
        background: COLORS.card,
        border: `1px solid ${COLORS.line}`,
        minHeight: 116,
      }}
    >
      <div className="w-10 h-10 rounded-xl flex items-center justify-center"
           style={{ background: `${accent}1f`, color: accent }}>
        <Icon name={icon} size={20} />
      </div>
      <div className="flex-1">
        <div className="text-[13.5px] font-semibold leading-[1.15]" style={{ color: COLORS.text }}>{title}</div>
        <div className="text-[11px] mt-0.5" style={{ color: COLORS.textMute }}>{count} courses</div>
      </div>
    </button>
  );
}

function LearnHub() {
  return (
    <div className="abc-screen relative h-full flex flex-col" style={{ background: COLORS.bg, color: COLORS.text }}>
      <ScreenHeader title="Learn Hub" kicker="Cultiver le savoir">
        <SearchBar placeholder="Search courses & topics…" accessory={
          <button className="w-11 h-11 rounded-2xl flex items-center justify-center"
                  style={{ background: COLORS.card, border: `1px solid ${COLORS.line}`, color: COLORS.text }}>
            <Icon name="sliders" size={17} stroke={2} />
          </button>
        }/>
      </ScreenHeader>

      <div className="flex-1 overflow-y-auto pb-28 scrollbar-hide">
        {/* My Courses */}
        <section className="mt-3">
          <div className="px-5 flex items-center justify-between mb-2.5">
            <h2 className="text-[16px] font-bold" style={{ color: COLORS.text }}>My Courses</h2>
            <button className="text-[12px] font-semibold" style={{ color: COLORS.terracotta }}>See all</button>
          </div>
          <div className="flex gap-3 overflow-x-auto px-5 scrollbar-hide pb-1">
            <CourseCard title="Architect Principles" sub="Foundations" progress={60} color="layers" accent={COLORS.green} />
            <CourseCard title="Financial Literacy" sub="Numbers" progress={30} color="landmark" accent={COLORS.green} />
            <CourseCard title="Brand Storytelling" sub="Marketing" progress={12} color="megaphone" accent={COLORS.terracotta} />
          </div>
        </section>

        {/* Recommended */}
        <section className="mt-6">
          <div className="px-5 flex items-center justify-between mb-2.5">
            <h2 className="text-[16px] font-bold" style={{ color: COLORS.text }}>Recommended for You</h2>
            <Icon name="sparkles" size={16} style={{ color: COLORS.terracotta }} />
          </div>
          <div className="flex gap-3 overflow-x-auto px-5 scrollbar-hide pb-1">
            <RecCard title="System Building" sub="Cooperative Foundations" tex="tex-weave" badge="featured" />
            <RecCard title="Brand Storytelling" sub="Marketing & Comm" tex="tex-loom" badge="new" />
            <RecCard title="Regenerative Finance" sub="Money as Soil" tex="tex-garden" badge="advanced" />
          </div>
        </section>

        {/* Categories */}
        <section className="mt-7 px-5">
          <h2 className="text-[16px] font-bold mb-3" style={{ color: COLORS.text }}>Course Categories</h2>
          <div className="grid grid-cols-2 gap-3">
            <CategoryTile icon="layers"     title="Architect Principles"  count={14} accent={COLORS.green} />
            <CategoryTile icon="users"      title="System Building"        count={9}  accent={COLORS.terracotta} />
            <CategoryTile icon="megaphone"  title="Brand Storytelling"     count={11} accent="#d4b042" />
            <CategoryTile icon="landmark"   title="Financial Literacy"     count={18} accent={COLORS.green} />
            <CategoryTile icon="leaf"       title="Sustainable Practices"  count={8}  accent="#5a9f6c" />
            <CategoryTile icon="sun"        title="Solarpunk Principles"   count={6}  accent={COLORS.terracotta} />
          </div>
        </section>
      </div>
    </div>
  );
}

// ══════════════════════════════════════════════════════════════
// BUILD
// ══════════════════════════════════════════════════════════════
function ProjectCard({ name, tagline, tex, status, statusColor, milestoneText, milestoneCurrent, milestoneTotal, next, members }) {
  const progress = (milestoneCurrent / milestoneTotal) * 100;
  return (
    <article
      className="rounded-3xl overflow-hidden anim-fade-up"
      style={{ background: COLORS.card, border: `1px solid ${COLORS.line}`, marginBottom: 14 }}
    >
      <div className="relative" style={{ height: 152 }}>
        <div className={tex} style={{ position: 'absolute', inset: 0 }} />
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(180deg, rgba(0,0,0,0.05) 40%, rgba(0,0,0,0.6) 100%)' }} />
        <div className="absolute top-3 left-3 right-3 flex items-start justify-between">
          <Pill color={statusColor}>{status}</Pill>
          <button className="w-8 h-8 rounded-full flex items-center justify-center"
                  style={{ background: 'rgba(0,0,0,0.35)', backdropFilter: 'blur(6px)', color: '#fff' }}>
            <Icon name="chevronRight" size={16} />
          </button>
        </div>
        <div className="absolute bottom-3 left-4 right-4">
          <div className="text-[18px] font-bold leading-tight" style={{ color: '#fff' }}>{name}</div>
          <div className="text-[12px] opacity-85 mt-0.5" style={{ color: '#fff' }}>{tagline}</div>
        </div>
      </div>

      <div className="p-4">
        <div className="flex items-center justify-between mb-2">
          <div className="text-[12px] font-semibold" style={{ color: COLORS.textMute }}>
            {milestoneText}
          </div>
          <div className="text-[12px] font-bold" style={{ color: statusColor }}>
            {milestoneCurrent} / {milestoneTotal}
          </div>
        </div>
        <ProgressBar value={progress} color={statusColor} height={6} />

        <div className="mt-3.5 flex items-center justify-between">
          <div className="flex items-center gap-2 min-w-0">
            <div className="w-7 h-7 rounded-lg flex-shrink-0 flex items-center justify-center"
                 style={{ background: `${statusColor}1f`, color: statusColor }}>
              <Icon name="arrowRight" size={14} />
            </div>
            <div className="min-w-0">
              <div className="text-[10.5px] uppercase tracking-[0.16em] font-semibold" style={{ color: COLORS.textDim }}>
                Next
              </div>
              <div className="text-[13px] font-semibold truncate" style={{ color: COLORS.text }}>
                {next}
              </div>
            </div>
          </div>

          {/* Avatars */}
          <div className="flex items-center -space-x-2">
            {members.map((m, i) => (
              <div key={i} style={{ zIndex: members.length - i }}>
                <Avatar initials={m.i} hue={m.h} size={30} ring />
              </div>
            ))}
            <div className="w-[30px] h-[30px] rounded-full flex items-center justify-center text-[11px] font-bold"
                 style={{ background: COLORS.cardHi, color: COLORS.text, boxShadow: `0 0 0 2px ${COLORS.card}`, zIndex: 0 }}>
              +2
            </div>
          </div>
        </div>
      </div>
    </article>
  );
}

function ToolTile({ icon, title, sub, accent }) {
  return (
    <button className="rounded-2xl p-3.5 text-left flex flex-col gap-3"
            style={{ background: COLORS.card, border: `1px solid ${COLORS.line}`, minHeight: 124 }}>
      <div className="w-10 h-10 rounded-xl flex items-center justify-center"
           style={{ background: `${accent}1f`, color: accent }}>
        <Icon name={icon} size={20} />
      </div>
      <div>
        <div className="text-[13.5px] font-semibold leading-tight">{title}</div>
        <div className="text-[11px] mt-1" style={{ color: COLORS.textMute }}>{sub}</div>
      </div>
    </button>
  );
}

function BuildHub() {
  const [tab, setTab] = React.useState('My Projects');

  return (
    <div className="abc-screen relative h-full flex flex-col" style={{ background: COLORS.bg, color: COLORS.text }}>
      <ScreenHeader title="Build Hub" kicker="Bâtir ensemble">
        <div className="flex gap-2 p-1 rounded-2xl"
             style={{ background: COLORS.card, border: `1px solid ${COLORS.line}`, width: '100%' }}>
          {['My Projects', 'Cooperative Tools'].map((t) => (
            <button key={t} onClick={() => setTab(t)}
              className="flex-1 h-10 text-[13px] font-semibold rounded-xl transition-colors"
              style={{
                background: tab === t ? COLORS.terracotta : 'transparent',
                color: tab === t ? '#fff' : COLORS.textMute,
              }}>
              {t}
            </button>
          ))}
        </div>
      </ScreenHeader>

      <div className="flex-1 overflow-y-auto px-5 pt-3 pb-28 scrollbar-hide">
        {tab === 'My Projects' ? (
          <>
            <ProjectCard
              name="Solaris Agri-Coop"
              tagline="Solar-powered cooperative farming · Kenya"
              tex="tex-solar"
              status="In Progress"
              statusColor={COLORS.green}
              milestoneText="Milestone progress"
              milestoneCurrent={3}
              milestoneTotal={5}
              next="Finalize Distribution Plan"
              members={[
                { i: 'AO', h: 28 },
                { i: 'KP', h: 210 },
                { i: 'JM', h: 140 },
              ]}
            />
            <ProjectCard
              name="Umoja Weavers Collective"
              tagline="Heritage textiles & shared looms · Tanzania"
              tex="tex-garden"
              status="Planning"
              statusColor={COLORS.blue}
              milestoneText="Milestone progress"
              milestoneCurrent={1}
              milestoneTotal={8}
              next="Draft Cooperative Agreement"
              members={[
                { i: 'NN', h: 320 },
                { i: 'TM', h: 18 },
                { i: 'EA', h: 280 },
              ]}
            />

            {/* CTA — dotted */}
            <button
              className="w-full rounded-3xl px-5 py-6 flex flex-col items-center text-center mt-1"
              style={{
                border: `1.5px dashed ${COLORS.line}`,
                background: 'linear-gradient(180deg, rgba(225,95,65,0.05) 0%, rgba(225,95,65,0.0) 100%)',
              }}
            >
              <div className="w-12 h-12 rounded-full flex items-center justify-center"
                   style={{ background: `${COLORS.terracotta}22`, color: COLORS.terracotta }}>
                <Icon name="plus" size={22} stroke={2.2} />
              </div>
              <div className="text-[14.5px] font-semibold mt-2.5" style={{ color: COLORS.text }}>
                Ready to build together?
              </div>
              <div className="text-[12.5px] leading-[1.45] mt-1.5 max-w-[260px]" style={{ color: COLORS.textMute }}>
                Tap the "+" button to start your first cooperative business and bring your vision to life.
              </div>
            </button>
          </>
        ) : (
          <div className="grid grid-cols-2 gap-3">
            <ToolTile icon="feather"   title="Agreement Drafter"    sub="Co-op contract templates" accent={COLORS.green} />
            <ToolTile icon="dollar"    title="Treasury Ledger"      sub="Shared books & payouts"   accent={COLORS.terracotta} />
            <ToolTile icon="users"     title="Member Onboarding"    sub="Vote, invite, ratify"     accent="#d4b042" />
            <ToolTile icon="globe"     title="Supply Network"       sub="Find regional partners"   accent={COLORS.green} />
            <ToolTile icon="calendar"  title="Harvest Calendar"     sub="Seasonal milestones"      accent="#5a9f6c" />
            <ToolTile icon="trendUp"   title="Impact Reporting"     sub="Track regenerative KPIs"  accent={COLORS.terracotta} />
          </div>
        )}
      </div>
    </div>
  );
}

// ══════════════════════════════════════════════════════════════
// BRAND
// ══════════════════════════════════════════════════════════════
function RadialScore({ value = 85, max = 100 }) {
  const r = 78;
  const circ = 2 * Math.PI * r;
  const off = circ * (1 - value / max);
  return (
    <div className="relative" style={{ width: 200, height: 200 }}>
      <svg width="200" height="200" viewBox="0 0 200 200">
        <defs>
          <linearGradient id="scoreG" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stopColor="#10b981" />
            <stop offset="60%" stopColor="#34d3a1" />
            <stop offset="100%" stopColor="#e15f41" />
          </linearGradient>
        </defs>
        {/* track */}
        <circle cx="100" cy="100" r={r} stroke="rgba(245,242,235,0.07)" strokeWidth="14" fill="none" />
        {/* tick marks */}
        {Array.from({ length: 60 }).map((_, i) => {
          const a = (i / 60) * Math.PI * 2 - Math.PI / 2;
          const x1 = 100 + Math.cos(a) * 92, y1 = 100 + Math.sin(a) * 92;
          const x2 = 100 + Math.cos(a) * 96, y2 = 100 + Math.sin(a) * 96;
          return <line key={i} x1={x1} y1={y1} x2={x2} y2={y2} stroke="rgba(245,242,235,0.12)" strokeWidth={i % 5 === 0 ? 1.5 : 1} />;
        })}
        {/* progress */}
        <circle
          cx="100" cy="100" r={r}
          stroke="url(#scoreG)"
          strokeWidth="14" fill="none"
          strokeLinecap="round"
          strokeDasharray={circ}
          strokeDashoffset={off}
          transform="rotate(-90 100 100)"
          style={{ filter: 'drop-shadow(0 0 12px rgba(16,185,129,0.35))' }}
        />
      </svg>
      <div className="absolute inset-0 flex flex-col items-center justify-center">
        <div className="text-[11px] tracking-[0.22em] uppercase font-semibold" style={{ color: COLORS.textDim }}>
          Brand Impact
        </div>
        <div className="flex items-baseline mt-1">
          <span className="font-serif italic text-[64px] leading-none" style={{ color: COLORS.text }}>85</span>
          <span className="text-[15px] font-semibold ml-1" style={{ color: COLORS.textMute }}>/ 100</span>
        </div>
        <div className="text-[10.5px] uppercase tracking-[0.18em] font-semibold mt-1" style={{ color: COLORS.green }}>
          ↗ +6 this week
        </div>
      </div>
    </div>
  );
}

function ActionRow({ icon, title, sub, accent, last }) {
  return (
    <button
      className="w-full flex items-center gap-3.5 px-4 py-3.5 text-left"
      style={{ borderBottom: last ? 'none' : `1px solid ${COLORS.line}` }}
    >
      <div className="w-11 h-11 rounded-2xl flex items-center justify-center flex-shrink-0"
           style={{ background: `${accent}1c`, color: accent }}>
        <Icon name={icon} size={20} />
      </div>
      <div className="flex-1 min-w-0">
        <div className="text-[14.5px] font-semibold" style={{ color: COLORS.text }}>{title}</div>
        <div className="text-[12px] mt-0.5" style={{ color: COLORS.textMute }}>{sub}</div>
      </div>
      <Icon name="chevronRight" size={18} style={{ color: COLORS.textDim }} />
    </button>
  );
}

function BrandHub() {
  return (
    <div className="abc-screen relative h-full flex flex-col" style={{ background: COLORS.bg, color: COLORS.text }}>
      <ScreenHeader title="Brand Hub" kicker="Votre identité collective" />

      <div className="flex-1 overflow-y-auto px-5 pb-28 scrollbar-hide">
        {/* Score */}
        <div
          className="rounded-3xl flex flex-col items-center pt-5 pb-5 px-4 mt-2 relative overflow-hidden"
          style={{ background: COLORS.card, border: `1px solid ${COLORS.line}` }}
        >
          <div style={{
            position: 'absolute', inset: 0,
            background: 'radial-gradient(280px 200px at 50% -10%, rgba(16,185,129,0.16), transparent 70%)',
            pointerEvents: 'none'
          }} />
          <RadialScore value={85} />
          <div className="text-[12.5px] mt-2 text-center max-w-[260px]" style={{ color: COLORS.textMute }}>
            Your current community resonance. Steady growth this month — keep telling your story.
          </div>

          <div className="grid grid-cols-3 gap-2 mt-4 w-full">
            {[
              { l: 'Story', v: '92' },
              { l: 'Reach', v: '78' },
              { l: 'Impact', v: '84' },
            ].map((s) => (
              <div key={s.l} className="rounded-2xl px-3 py-2.5"
                   style={{ background: COLORS.bgAlt, border: `1px solid ${COLORS.line}` }}>
                <div className="text-[10.5px] tracking-[0.16em] uppercase font-semibold" style={{ color: COLORS.textDim }}>{s.l}</div>
                <div className="text-[20px] font-bold mt-0.5" style={{ color: COLORS.text }}>{s.v}</div>
              </div>
            ))}
          </div>
        </div>

        {/* Action list */}
        <div className="mt-5 rounded-3xl overflow-hidden"
             style={{ background: COLORS.card, border: `1px solid ${COLORS.line}` }}>
          <ActionRow icon="bookOpen" title="Crafting Your Story"     sub="Define values, mission, and visual identity."     accent={COLORS.terracotta} />
          <ActionRow icon="dollar"   title="Monetization Strategies" sub="Explore pricing, digital products, and grants."   accent="#d4b042" />
          <ActionRow icon="users"    title="Community Impact"        sub="Track social good and member collaboration."      accent={COLORS.green} last />
        </div>

        {/* Inspiration */}
        <section className="mt-6">
          <div className="flex items-center justify-between mb-2.5">
            <h2 className="text-[16px] font-bold">Inspiration Hub</h2>
            <Icon name="flame" size={16} style={{ color: COLORS.terracotta }} />
          </div>
          <article
            className="rounded-3xl overflow-hidden flex"
            style={{ background: COLORS.card, border: `1px solid ${COLORS.line}` }}
          >
            <div className="relative flex-shrink-0" style={{ width: 124 }}>
              <div className="tex-loom" style={{ position: 'absolute', inset: 0 }} />
              <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(90deg, transparent 60%, rgba(34,31,28,0.85) 100%)' }} />
              <div className="absolute top-2.5 left-2.5">
                <Pill color="#fff" bg="rgba(0,0,0,0.4)">Case study</Pill>
              </div>
            </div>
            <div className="p-3.5 flex-1">
              <div className="text-[10.5px] tracking-[0.18em] uppercase font-semibold" style={{ color: COLORS.terracotta }}>
                Soko Weavers
              </div>
              <div className="text-[14px] font-bold leading-[1.2] mt-1" style={{ color: COLORS.text }}>
                Doubled Their Reach
              </div>
              <div className="text-[11.5px] mt-1.5 leading-[1.4]" style={{ color: COLORS.textMute }}>
                How cooperative marketing expanded their global footprint.
              </div>
              <div className="flex items-center gap-1.5 mt-2 text-[11.5px] font-semibold" style={{ color: COLORS.green }}>
                Read story <Icon name="arrowRight" size={13} />
              </div>
            </div>
          </article>

          <article className="rounded-3xl flex items-center gap-3 px-4 py-3 mt-3"
                   style={{ background: COLORS.card, border: `1px solid ${COLORS.line}` }}>
            <div className="w-11 h-11 rounded-2xl flex items-center justify-center"
                 style={{ background: `${COLORS.green}1f`, color: COLORS.green }}>
              <Icon name="globe" size={20} />
            </div>
            <div className="flex-1 min-w-0">
              <div className="text-[13.5px] font-semibold" style={{ color: COLORS.text }}>Brand Atlas</div>
              <div className="text-[11.5px]" style={{ color: COLORS.textMute }}>Visual identities from 24 African co-ops</div>
            </div>
            <Icon name="chevronRight" size={18} style={{ color: COLORS.textDim }} />
          </article>
        </section>
      </div>
    </div>
  );
}

Object.assign(window, {
  COLORS,
  SplashScreen, CommunityHub, LearnHub, BuildHub, BrandHub,
  Avatar, Pill, ProgressBar,
});
