// ABC OS — App shell, bottom nav, tweaks

const TABS = [
  { key: 'community', label: 'Community', icon: 'users' },
  { key: 'learn',     label: 'Learn',     icon: 'graduationCap' },
  { key: 'build',     label: 'Build',     icon: 'wrench' },
  { key: 'brand',     label: 'Brand',     icon: 'award' },
];

const TWEAK_DEFAULTS = /*EDITMODE-BEGIN*/{
  "accent": "#e15f41",
  "showSplash": false,
  "phoneSize": "large"
}/*EDITMODE-END*/;

function BottomNav({ current, onChange }) {
  return (
    <div
      style={{
        position: 'absolute',
        left: 12, right: 12, bottom: 16,
        zIndex: 40,
        height: 72,
        borderRadius: 28,
        background: 'rgba(24,22,20,0.78)',
        backdropFilter: 'blur(20px) saturate(1.4)',
        WebkitBackdropFilter: 'blur(20px) saturate(1.4)',
        border: '1px solid rgba(245,242,235,0.07)',
        boxShadow: '0 18px 40px rgba(0,0,0,0.4), 0 1px 0 rgba(255,255,255,0.04) inset',
        display: 'grid',
        gridTemplateColumns: 'repeat(4, 1fr)',
        alignItems: 'center',
        padding: '0 4px',
      }}
    >
      {TABS.map((t) => {
        const active = current === t.key;
        return (
          <button
            key={t.key}
            onClick={() => onChange(t.key)}
            className="h-full flex flex-col items-center justify-center gap-1 relative"
            style={{ color: active ? COLORS.text : COLORS.textMute }}
          >
            {active && (
              <span
                style={{
                  position: 'absolute', top: 8, left: '50%', transform: 'translateX(-50%)',
                  width: 28, height: 3, borderRadius: 3, background: COLORS.terracotta,
                }}
              />
            )}
            <div
              className="flex items-center justify-center"
              style={{
                width: 44, height: 36, borderRadius: 14,
                background: active ? 'rgba(225,95,65,0.12)' : 'transparent',
                color: active ? COLORS.terracotta : COLORS.textMute,
                transition: 'all .18s',
              }}
            >
              <Icon name={t.icon} size={20} stroke={active ? 2.2 : 1.8} />
            </div>
            <div className="text-[10.5px] font-semibold" style={{ letterSpacing: 0.2 }}>
              {t.label}
            </div>
          </button>
        );
      })}
    </div>
  );
}

function App() {
  const [t, setTweak] = useTweaks(TWEAK_DEFAULTS);
  const [tab, setTab] = React.useState('community');
  const [splash, setSplash] = React.useState(t.showSplash);

  // keep splash visible if tweak forces it
  React.useEffect(() => { setSplash(t.showSplash); }, [t.showSplash]);

  const phoneW = t.phoneSize === 'small' ? 380 : 414;
  const phoneH = t.phoneSize === 'small' ? 824 : 900;

  return (
    <div style={{ position: 'relative', display: 'flex', gap: 24, alignItems: 'center' }}>
      {/* Side caption */}
      <div className="hidden md:flex flex-col" style={{ maxWidth: 260, color: '#f5f2eb' }}>
        <div className="text-[11px] tracking-[0.32em] uppercase font-semibold" style={{ color: '#e15f41' }}>
          ABC OS
        </div>
        <div className="font-serif italic text-[36px] leading-[1.05] mt-2">
          African Business Cooperatives Operating System
        </div>
        <div className="text-[13px] mt-3 leading-[1.55]" style={{ color: '#a89c8a' }}>
          A deep-dark solarpunk prototype. Switch tabs in the bottom bar, or open the splash from Tweaks.
        </div>
        <div className="mt-5 flex flex-wrap gap-2 text-[11px]" style={{ color: '#a89c8a' }}>
          {['Community', 'Learn', 'Build', 'Brand'].map((l) => (
            <span key={l} className="px-2.5 py-1 rounded-full"
                  style={{ background: 'rgba(245,242,235,0.05)', border: '1px solid rgba(245,242,235,0.08)' }}>
              {l}
            </span>
          ))}
        </div>
      </div>

      {/* Phone */}
      <IOSDevice width={phoneW} height={phoneH} dark>
        <div className="relative h-full" data-screen-label={splash ? '00 Splash' : `0${TABS.findIndex(x => x.key === tab) + 1} ${TABS.find(x => x.key === tab).label}`}>
          {/* push content below status bar */}
          <div className="absolute inset-0" style={{ paddingTop: 54 }}>
            {splash ? (
              <SplashScreen onEnter={() => { setSplash(false); setTweak('showSplash', false); }} />
            ) : (
              <>
                {tab === 'community' && <CommunityHub />}
                {tab === 'learn'     && <LearnHub />}
                {tab === 'build'     && <BuildHub />}
                {tab === 'brand'     && <BrandHub />}
                <BottomNav current={tab} onChange={setTab} />
              </>
            )}
          </div>
        </div>
      </IOSDevice>

      {/* Tweaks */}
      <TweaksPanel title="Tweaks">
        <TweakSection label="View">
          <TweakToggle
            label="Show splash screen"
            value={splash}
            onChange={(v) => { setSplash(v); setTweak('showSplash', v); }}
          />
          <TweakRadio
            label="Phone size"
            value={t.phoneSize}
            options={[
              { value: 'small', label: 'Compact' },
              { value: 'large', label: 'Pro Max' },
            ]}
            onChange={(v) => setTweak('phoneSize', v)}
          />
        </TweakSection>
        <TweakSection label="Navigate">
          <TweakRadio
            label="Active tab"
            value={tab}
            options={TABS.map((x) => ({ value: x.key, label: x.label }))}
            onChange={(v) => { setTab(v); setSplash(false); }}
          />
        </TweakSection>
        <TweakSection label="Brand accent">
          <TweakColor
            label="Accent"
            value={t.accent}
            options={['#e15f41', '#d4b042', '#10b981', '#5b8bb7', '#c47a96']}
            onChange={(v) => setTweak('accent', v)}
          />
          <div style={{ fontSize: 11, color: '#777', padding: '4px 2px' }}>
            (Demo control — wire to live styles next iteration.)
          </div>
        </TweakSection>
      </TweaksPanel>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
