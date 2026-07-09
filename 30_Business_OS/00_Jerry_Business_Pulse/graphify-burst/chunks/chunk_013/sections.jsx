/* global React, window */
// SOLARIS — page sections. Voice: front-stage, second person.
const { useState, useEffect } = React;

// ---------------------------------------------------------------
// TOPBAR
// ---------------------------------------------------------------
function Topbar({ icp, setIcp }) {
  return (
    <header className="topbar">
      <div className="brand">
        <div className="brand-mark" />
        <div className="brand-name"><b>solaris</b></div>
        <div className="brand-tag">the ghost factory · oh / ky</div>
      </div>
      <nav className="nav" aria-label="Sections">
        <a href="#hook"><span className="num">01</span>The hook</a>
        <a href="#anatomy"><span className="num">02</span>B1/B2/B3 anatomy</a>
        <a href="#shield"><span className="num">03</span>Your margins</a>
        <a href="#wheel"><span className="num">04</span>8 poles</a>
        <a href="#archetypes"><span className="num">05</span>Profiles</a>
        <a href="#paradigms"><span className="num">06</span>2026 levers</a>
        <a href="#vault"><span className="num">07</span>Onboarding</a>
      </nav>
      <div style={{ display: "flex", gap: 14, alignItems: "center" }}>
        <div className="icp-strip" aria-label="Your profile">
          {window.SOLARIS_ARCHETYPES.map((f) => (
            <button
              key={f.id}
              className={icp === f.id ? "active" : ""}
              onClick={() => setIcp(f.id)}
            >{f.name}</button>
          ))}
        </div>
        <a className="top-cta" href="#vault">
          <span className="pulse" />
          submit a url
        </a>
      </div>
    </header>
  );
}

// ---------------------------------------------------------------
// HERO
// ---------------------------------------------------------------
function Hero({ icp }) {
  const domains = window.SOLARIS_DOMAINS;
  const [active, setActive] = useState(domains[0].id);
  const icpData = window.SOLARIS_ARCHETYPES.find((f) => f.id === icp);

  useEffect(() => {
    const id = setInterval(() => {
      setActive((curr) => {
        const i = domains.findIndex((d) => d.id === curr);
        return domains[(i + 1) % domains.length].id;
      });
    }, 3200);
    return () => clearInterval(id);
  }, []);

  return (
    <section className="hero">
      <div className="hero-grid" />
      <div className="hero-copy">
        <div className="eyebrow">
          AaaS · agency as a service · profile detected · {icpData.name}
        </div>
        <h1 className="display">
          Stop hiring<br />
          operators.<br />
          <em>Plug into our factory.</em>
        </h1>
        <p className="sub">
          You sell the strategy and own the client relationship. We handle total
          execution in the background. Solaris is a white-label production
          infrastructure. Scale your operations and protect your margins —
          without ever growing your payroll, without managing freelances.
        </p>
        <p className="sub" style={{ marginTop: 18, fontStyle: "italic", color: "var(--accent-2)" }}>
          You're not buying another SaaS tool.<br />
          You're renting an <b style={{color: "var(--ink)", fontStyle: "normal", fontWeight: 500}}>autonomous org chart</b>.
        </p>
        <div className="hero-cta-row">
          <a className="btn-primary" href="#vault">
            submit your url <span className="arrow">→</span>
          </a>
          <a className="btn-ghost" href="#anatomy">
            meet your new team
          </a>
        </div>
        <div className="hero-meta">
          <div className="stat">
            <div className="v">70%</div>
            <div className="l">margin kept · under your brand</div>
          </div>
          <div className="stat">
            <div className="v">0</div>
            <div className="l">hires · 0 freelances to manage</div>
          </div>
          <div className="stat">
            <div className="v">24h</div>
            <div className="l">audit delivered · no calls</div>
          </div>
          <div className="stat">
            <div className="v">3<span style={{fontSize: "60%", opacity: 0.5}}>×</span>10<span style={{fontSize: "60%", opacity: 0.5}}>²</span>+</div>
            <div className="l">agents · ready to execute</div>
          </div>
        </div>
      </div>
      <OrbitalDiagram activeId={active} onHover={setActive} />
    </section>
  );
}

// ---------------------------------------------------------------
// HOOK / Positioning
// ---------------------------------------------------------------
function HookSection() {
  return (
    <section className="section" id="hook">
      <div className="aaas">
        <div>
          <div className="eyebrow">01 · the positioning</div>
          <h2 className="display" style={{ fontSize: "clamp(40px, 5.5vw, 80px)", margin: "20px 0 0", lineHeight: 1 }}>
            You sell the<br />strategy.<br /><em>We execute<br />in silence.</em>
          </h2>
        </div>
        <div className="aaas-prose">
          <p style={{ fontSize: 19 }}>
            Solaris is a white-label
            <b style={{color: "var(--accent)", fontWeight: 500}}> Agency-as-a-Service</b> production
            infrastructure. A ghost factory running under your logo —
            never visible to your clients.
          </p>
          <p>
            You keep the relationship, the brief, the invoice. We run extraction,
            production, QA, delivery. Your clients don't even know we exist.
          </p>
          <div className="compare">
            <div className="compare-cell bad">
              <h4>The old model</h4>
              <ul>
                <li><span className="sym">·</span>Hire, train, manage, lose</li>
                <li><span className="sym">·</span>Freelancers ghost you on Mondays</li>
                <li><span className="sym">·</span>Endless sync meetings</li>
                <li><span className="sym">·</span>Margin eaten by salaries</li>
              </ul>
            </div>
            <div className="compare-cell good">
              <h4>You · on Solaris</h4>
              <ul>
                <li><span className="sym">+</span>A full org chart ready in 24h</li>
                <li><span className="sym">+</span>Agents that never sleep</li>
                <li><span className="sym">+</span>Zero meetings · async orders</li>
                <li><span className="sym">+</span>70% margin, mathematically</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

// ---------------------------------------------------------------
// ANATOMY B1/B2/B3
// ---------------------------------------------------------------
function AnatomySection() {
  const anatomy = window.SOLARIS_ANATOMY;
  return (
    <section className="section" id="anatomy">
      <div className="s-eye-h-wrap">
        <div>
          <div className="eyebrow">02 · the anatomy of your strike force</div>
          <h2 className="s-h" style={{ marginTop: 20 }}>
            Forget the<br />job descriptions.<br /><em>Meet your new team.</em>
          </h2>
        </div>
        <p className="s-sub">
          Your Solaris infrastructure is split into 8 expertise poles, run by a
          strict and invisible hierarchy that never sleeps. Three tiers, three
          codenames, one single org chart.
        </p>
      </div>

      <div className="anatomy-stack">
        {anatomy.map((tier, i) => (
          <div className="anatomy-tier" key={tier.tier} data-tier={tier.tier.toLowerCase()}>
            <div className="anatomy-side">
              <div className="anatomy-tier-id">{tier.tier}</div>
              <div className="anatomy-codename">{tier.codename}</div>
              <div className="anatomy-meta">{tier.headcount}</div>
            </div>
            <div className="anatomy-body">
              <div className="anatomy-role">{tier.role}</div>
              <h3 className="anatomy-name">{tier.name}</h3>
              <p className="anatomy-desc">{tier.desc}</p>
              {tier.members && (
                <div className="anatomy-roster">
                  <div className="anatomy-roster-label">Current {tier.tier} roster</div>
                  <div className="anatomy-chips">
                    {tier.members.map((m) => (
                      <span key={m} className="anatomy-chip">{tier.tier}.{m}</span>
                    ))}
                  </div>
                </div>
              )}
            </div>
            <div className="anatomy-flow">
              {i < anatomy.length - 1 && (
                <>
                  <div className="anatomy-arrow">↓</div>
                  <div className="anatomy-flow-label">delegates to</div>
                </>
              )}
              {i === anatomy.length - 1 && (
                <>
                  <div className="anatomy-arrow" style={{color: "var(--mint)"}}>✓</div>
                  <div className="anatomy-flow-label">ships to you</div>
                </>
              )}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

// ---------------------------------------------------------------
// MARGIN SHIELD
// ---------------------------------------------------------------
function MarginShieldSection() {
  return (
    <section className="section" id="shield" style={{ background: "var(--bg-2)" }}>
      <div className="shield-wrap">
        <div>
          <div className="eyebrow">03 · margins, locked in</div>
          <h2 className="s-h" style={{ marginTop: 20 }}>
            Your execution cost<br />is <em>a fixed input.</em>
          </h2>
          <p className="s-sub" style={{ marginTop: 28 }}>
            Your competitors burn margin sending every task to the most
            expensive AI on the market. We route. Routine work — extraction,
            sorting, formatting — runs on lean B3 squads. Only heavy reasoning
            ever escalates, and always under a ceiling.
          </p>
          <p className="s-sub" style={{ marginTop: 18 }}>
            If a squad stalls, <b style={{ color: "var(--ink)", fontWeight: 500 }}>Batman</b>
            {" "}(B2 · Ops) shuts it down before it loops through your budget.
            You bill on value. We pay for frugality. That gap — that's your margin.
          </p>
          <div style={{ marginTop: 36 }}>
            <RoutingTerminal />
          </div>
        </div>
        <MarginShield />
      </div>
    </section>
  );
}

// ---------------------------------------------------------------
// WHEEL of 8 poles
// ---------------------------------------------------------------
function WheelSection() {
  const domains = window.SOLARIS_DOMAINS;
  const [idx, setIdx] = useState(0);
  const d = domains[idx];

  return (
    <section className="section" id="wheel">
      <div className="s-eye-h-wrap">
        <div>
          <div className="eyebrow">04 · the 8 expertise poles</div>
          <h2 className="s-h" style={{ marginTop: 20 }}>
            Eight chiefs.<br />Thirty-two squads.<br /><em>One order to give.</em>
          </h2>
        </div>
        <p className="s-sub">
          Each pole is run by a VP (B2 · Justice League DC) who signs off
          deliverables before release. Underneath, B3 squads (Marvels) crush
          the execution. Click a pole to see who's working for you there.
        </p>
      </div>
      <div className="wheel-wrap">
        <DomainWheel activeIdx={idx} onSelect={setIdx} />
        <div className="wheel-detail" key={d.id} style={{ display: "flex", flexDirection: "column" }}>
          <div className="domain-num">POLE {d.n} · {d.sub.toUpperCase()}</div>
          <h3>{d.name}</h3>
          <div className="role">{d.vp} · {d.agents} B3 squads under their command</div>
          <p className="description">{d.role}</p>
          {d.squads && (
            <div style={{
              display: "flex",
              flexWrap: "wrap",
              gap: 6,
              marginBottom: 18,
            }}>
              {d.squads.map((s) => (
                <span key={s} style={{
                  fontFamily: "var(--font-mono)",
                  fontSize: 11,
                  letterSpacing: "0.05em",
                  padding: "4px 10px",
                  border: "1px solid var(--line-2)",
                  borderRadius: 999,
                  color: "var(--accent-2)",
                }}>{s}</span>
              ))}
            </div>
          )}
          <div className="telemetry">
            <div className="telem-cell">
              <div className="k">Pulse</div>
              <div className="v" style={{ color: "var(--mint)" }}>● {d.metric}</div>
            </div>
            <div className="telem-cell">
              <div className="k">Status</div>
              <div className="v">{d.status === "active" ? "active" : d.status === "stable" ? "stable" : "standby"}</div>
            </div>
            <div className="telem-cell">
              <div className="k">B2 VP</div>
              <div className="v">{d.vp}</div>
            </div>
            <div className="telem-cell">
              <div className="k">B3 squads</div>
              <div className="v">{d.agents} active</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

// ---------------------------------------------------------------
// ARCHETYPES
// ---------------------------------------------------------------
function ArchGlyph({ id }) {
  if (id === "revops") return (
    <svg viewBox="0 0 56 56" width="56" height="56" aria-hidden="true">
      <rect x="6" y="14" width="12" height="10" fill="none" stroke="var(--accent)" />
      <rect x="22" y="6" width="12" height="10" fill="none" stroke="var(--accent)" />
      <rect x="22" y="40" width="12" height="10" fill="none" stroke="var(--accent)" />
      <rect x="38" y="14" width="12" height="10" fill="none" stroke="var(--accent)" />
      <rect x="38" y="32" width="12" height="10" fill="none" stroke="var(--accent)" />
      <path d="M18 19 L22 11 M18 19 L22 45 M34 11 L38 19 M34 45 L38 37 M28 16 V40" stroke="var(--accent)" strokeOpacity="0.6" strokeDasharray="2 2" fill="none" />
      <circle cx="28" cy="28" r="4" fill="var(--accent)" />
    </svg>
  );
  if (id === "forges") return (
    <svg viewBox="0 0 56 56" width="56" height="56" aria-hidden="true">
      {[10, 18, 26, 34, 42].map((y) => (
        <line key={y} x1="6" y1={y} x2="50" y2={y} stroke="var(--accent)" strokeOpacity={y === 26 ? 1 : 0.4} strokeWidth={y === 26 ? 1.5 : 1} />
      ))}
      <rect x="22" y="6" width="2" height="44" fill="var(--accent)" />
      <rect x="32" y="6" width="2" height="44" fill="var(--accent)" opacity="0.4" />
    </svg>
  );
  if (id === "aaa") return (
    <svg viewBox="0 0 56 56" width="56" height="56" aria-hidden="true">
      <path d="M8 48 L8 28 L28 8 L48 28 L48 48 Z" fill="none" stroke="var(--accent)" />
      <rect x="22" y="34" width="12" height="14" fill="var(--accent)" />
      <circle cx="28" cy="26" r="3" fill="var(--accent)" />
      <line x1="8" y1="28" x2="48" y2="28" stroke="var(--accent)" strokeOpacity="0.5" />
    </svg>
  );
  return (
    <svg viewBox="0 0 56 56" width="56" height="56" aria-hidden="true">
      <polygon points="28,6 50,42 6,42" fill="none" stroke="var(--accent)" />
      <circle cx="28" cy="30" r="3" fill="var(--accent)" />
      <circle cx="20" cy="36" r="2" fill="var(--accent)" opacity="0.6" />
      <circle cx="36" cy="36" r="2" fill="var(--accent)" opacity="0.6" />
    </svg>
  );
}

function ArchetypeSection({ icp, setIcp }) {
  const archetypes = window.SOLARIS_ARCHETYPES;
  return (
    <section className="section" id="archetypes" style={{ background: "var(--bg-2)" }}>
      <div className="s-eye-h-wrap">
        <div>
          <div className="eyebrow">05 · solutions by profile</div>
          <h2 className="s-h" style={{ marginTop: 20 }}>
            Entropy hits<br />every model differently.<br /><em>Find yours.</em>
          </h2>
        </div>
        <p className="s-sub">
          Four agency archetypes. Four named pains. Four pre-configured
          factories. Pick your profile — your Solaris instance is already built.
        </p>
      </div>
      <div className="archetype-grid">
        {archetypes.map((a) => (
          <article
            key={a.id}
            className={"archetype" + (icp === a.id ? " current" : "") + (a.recommended ? " recommended" : "")}
            onClick={() => setIcp(a.id)}
          >
            {a.recommended && <div className="reco-badge">PRIORITY · WAVE 01</div>}
            <div className="arch-head">
              <div className="arch-code">
                <span className="ix">{a.code}</span>
                <span className="full">{a.fullName}</span>
              </div>
              <div className="arch-glyph"><ArchGlyph id={a.id} /></div>
            </div>
            <h3 className="arch-name">{a.name}</h3>
            <div className="arch-tag">{a.tag}</div>

            <div className="arch-pain">
              <div className="k">⚠ Your pain · {a.painName}</div>
              <p>{a.painDesc}</p>
            </div>

            <div className="arch-remedy">
              <div className="k">↻ The Solaris remedy · {a.remedyName}</div>
              <p>{a.remedyDesc}</p>
            </div>

            <div className="arch-pitch">{a.pitch}</div>

            <ul className="arch-targets">
              {a.targets.map((t, i) => (
                <li key={i}>
                  <span className="k">{t.k}</span>
                  <span className="v">{t.v}</span>
                </li>
              ))}
              {a.ticket && (
                <li>
                  <span className="k">Ticket</span>
                  <span className="v" style={{ color: "var(--accent-2)" }}>{a.ticket}</span>
                </li>
              )}
            </ul>

            <div className="arch-footer">
              {icp === a.id ? "✓ active profile in the vault" : "→ this is my profile"}
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}

// ---------------------------------------------------------------
// PARADIGMS (3 levers for 2026)
// ---------------------------------------------------------------
function ParadigmSection() {
  const paradigms = window.SOLARIS_PARADIGMS;
  return (
    <section className="section" id="paradigms">
      <div className="s-eye-h-wrap">
        <div>
          <div className="eyebrow">06 · the 2026 levers</div>
          <h2 className="s-h" style={{ marginTop: 20 }}>
            Agencies no longer<br />believe in <em>tools.</em>
          </h2>
        </div>
        <p className="s-sub">
          You believe in <b style={{ color: "var(--ink)", fontWeight: 500 }}>system guarantees</b>.
          Three levers Solaris unlocks for you — each one shatters an old
          belief about what an agency is supposed to be.
        </p>
      </div>
      <div className="paradigm-grid">
        {paradigms.map((p) => (
          <div className="paradigm" key={p.n}>
            <div className="paradigm-n">{p.n}</div>
            <div className="paradigm-anchor">
              <span className="from">{p.anchor.split("→")[0].trim()}</span>
              <span className="arrow">→</span>
              <span className="to">{p.anchor.split("→")[1].trim()}</span>
            </div>
            <h3 className="paradigm-name">{p.name}</h3>
            <p className="paradigm-promise">{p.promise}</p>
            <div className="paradigm-mech">
              <div className="k">How</div>
              <p>{p.mechanism}</p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

// ---------------------------------------------------------------
// ONBOARDING / VAULT — 3-step
// ---------------------------------------------------------------
const VAULT_BY_ARCH = {
  revops: {
    slug: "revops-cincinnati",
    lead: "Lyrebird Performance",
    headline: "Five fragmentation points detected.",
    rows: [
      { l: "HubSpot ↔ Stripe: 14 fragmented Zaps", s: "high", t: "12ms" },
      { l: "Multi-touch attribution: 3 conflicting models", s: "high", t: "9ms" },
      { l: "Client A CRM ≠ Client B CRM (manual replication)", s: "high", t: "7ms" },
      { l: "Ad platforms: reporting copy-pasted · 4h / wk", s: "med", t: "5ms" },
      { l: "No versioning on data pipelines", s: "med", t: "4ms" },
    ],
    remedy: "IT Squads · bulletproof pipelines · you sell the revenue",
  },
  forges: {
    slug: "forges-columbus",
    lead: "Mason & Lark Studio",
    headline: "Margin Bleed measured — 78% lost on revisions.",
    rows: [
      { l: "Creator/QA ratio: 8 / 1 · critical Founder Load", s: "high", t: "14ms" },
      { l: "Avg client revision rounds: 7.2 per asset", s: "high", t: "8ms" },
      { l: "Prompt-Fatigue: 38% of senior time", s: "high", t: "6ms" },
      { l: "No brand RAG · 9% hallucination rate", s: "med", t: "5ms" },
      { l: "Templates: 12 versions, no source of truth", s: "low", t: "3ms" },
    ],
    remedy: "Paperclip Workspaces · B2 Flash validates before delivery · 10× without a reviewer",
  },
  aaa: {
    slug: "aaa-lexington",
    lead: "Halcyon Automation Co.",
    headline: "Cobbler's Paradox confirmed.",
    rows: [
      { l: "Back-office on Make.com · public scenarios", s: "high", t: "11ms" },
      { l: "OpenAI bill: $3,200 / mo · 71% of costs", s: "high", t: "9ms" },
      { l: "No control plane · no owned infrastructure", s: "high", t: "13ms" },
      { l: "AI flows delivered via public platforms", s: "med", t: "6ms" },
      { l: "No defensible technical moat", s: "med", t: "4ms" },
    ],
    remedy: "Cyborg squads · you become a software publisher · $1,555 ticket",
  },
  boutiques: {
    slug: "boutiques-louisville",
    lead: "Atelier Norden",
    headline: "Glass Ceiling identified.",
    rows: [
      { l: "Headcount: 2 founders · 0 delivery team", s: "high", t: "10ms" },
      { l: "Tier-1 clients: 4 · LTV capped at strategy", s: "high", t: "8ms" },
      { l: "Execution refused: 6 requests / qtr lost", s: "high", t: "7ms" },
      { l: "Past freelancers: 3 abrupt exits", s: "med", t: "5ms" },
      { l: "Tech white-label: nonexistent", s: "low", t: "3ms" },
    ],
    remedy: "Pure AaaS · ghost factory under your logo · 70% margin",
  },
};

function VaultSection({ icp }) {
  const v = VAULT_BY_ARCH[icp] || VAULT_BY_ARCH.aaa;
  const arch = window.SOLARIS_ARCHETYPES.find((a) => a.id === icp) || window.SOLARIS_ARCHETYPES[2];

  return (
    <section className="section" id="vault">
      <div className="s-eye-h-wrap">
        <div>
          <div className="eyebrow">07 · onboarding · zero friction, zero calls</div>
          <h2 className="s-h" style={{ marginTop: 20 }}>
            We don't do<br />discovery calls.<br /><em>Time is non-renewable.</em>
          </h2>
        </div>
        <p className="s-sub">
          Three async steps. No calendar. No sales follow-up. You read, you
          decide, you activate. Your new team is ready to take its first work
          order within 48 hours.
        </p>
      </div>
      <div className="vault-wrap">
        <div className="vault-mock">
          <div className="vault-chrome">
            <div className="dots"><div className="dot" /><div className="dot" /><div className="dot" /></div>
            <div className="url">vault.solaris.factory / {v.slug} / 7f3a-2c81</div>
            <div className="lock">⬢ TLS · async · 2-FA</div>
          </div>
          <div className="vault-body">
            <div className="vault-greet">
              <b>{v.lead}</b> · {arch.code} · audit delivered · {new Date().toLocaleDateString("en-US", { day: "2-digit", month: "short" })}
            </div>
            <h3 className="vault-title">
              Friction report.<br />
              <span style={{ color: "var(--accent-2)", fontStyle: "italic" }}>{v.headline}</span>
            </h3>
            <div className="vault-audit">
              {v.rows.map((a, i) => (
                <div className="vault-audit-row" key={i}>
                  <div className="label">{a.l}</div>
                  <div className={"sev " + a.s}>{a.s === "high" ? "critical" : a.s === "med" ? "moderate" : "minor"}</div>
                  <div className="ms">{a.t}</div>
                </div>
              ))}
            </div>
            <div style={{
              fontFamily: "var(--font-mono)",
              fontSize: 11,
              letterSpacing: "0.15em",
              textTransform: "uppercase",
              color: "var(--ink-3)",
              padding: "12px 14px",
              border: "1px solid var(--line)",
              borderRadius: 4,
              background: "var(--surface-2)",
            }}>
              <div style={{ color: "var(--ink-4)", marginBottom: 6 }}>Pre-configured remedy</div>
              <div style={{ color: "var(--accent)", textTransform: "none", letterSpacing: 0, fontSize: 13 }}>↻ {v.remedy}</div>
            </div>
            <div className="vault-actions">
              <div className="vault-action">
                <div className="k">Action / 01</div>
                <div className="v">Review the architecture plan</div>
              </div>
              <div className="vault-action primary">
                <div className="k">Action / 02</div>
                <div className="v">Activate my factory →</div>
              </div>
            </div>
          </div>
        </div>

        <div className="vault-steps">
          <div className="vault-step done">
            <div className="step-meta">
              <span className="num">STEP / 01</span>
              <span className="when">D · now</span>
            </div>
            <h4>The Silent Audit</h4>
            <p>Drop your URL or your operational bottleneck through our portal.
            No 40-question form. No call. You post, we take it from there.</p>
          </div>
          <div className="vault-step done">
            <div className="step-meta">
              <span className="num">STEP / 02</span>
              <span className="when">D+1 · &lt;24h</span>
            </div>
            <h4>The Sanctuary</h4>
            <p>You get an encrypted link to a secure space. Inside: the friction
            report on your agency drafted by our B2 VPs, plus the exact
            architecture plan of your future factory. Read at your own pace.</p>
          </div>
          <div className="vault-step">
            <div className="step-meta">
              <span className="num">STEP / 03</span>
              <span className="when">on your signal</span>
            </div>
            <h4>Activation</h4>
            <p>You sign off. The B1/B2/B3 hierarchy is instantiated and wired
            into your comms channels (Slack/Teams). Your new async team
            is ready to take its first work order.</p>
          </div>
        </div>
      </div>
    </section>
  );
}

// ---------------------------------------------------------------
// CTA + FOOTER
// ---------------------------------------------------------------
function FinalCTA() {
  return (
    <section className="cta">
      <div className="cta-sun" />
      <div className="eyebrow" style={{ justifyContent: "center", display: "inline-flex" }}>
        wave 01 · live · ohio / kentucky
      </div>
      <h2 style={{ marginTop: 32 }}>
        Plug in.<br />
        <em>Once.</em>
      </h2>
      <p className="sub">
        No call. No SaaS to rent. No freelance to manage. One URL, one audit,
        one vault — your new async team is waiting for its first order.
      </p>
      <div className="hero-cta-row" style={{ justifyContent: "center", marginTop: 32 }}>
        <a className="btn-primary" href="#vault">
          submit your url <span className="arrow">→</span>
        </a>
        <a className="btn-ghost" href="mailto:hello@solaris.factory">
          contact the factory
        </a>
      </div>
    </section>
  );
}

function Footer() {
  return (
    <footer>
      <div className="row" style={{ gap: 16 }}>
        <div>solaris.factory</div>
        <div>·</div>
        <div>the ghost factory · oh / ky · async</div>
      </div>
      <div className="row">
        <div>wave 01 · 2026</div>
        <div>uptime 99.94</div>
        <div style={{ color: "var(--mint)" }}>● factory online</div>
      </div>
    </footer>
  );
}

Object.assign(window, {
  Topbar, Hero, HookSection, AnatomySection, MarginShieldSection,
  WheelSection, ArchetypeSection, ParadigmSection, VaultSection, FinalCTA, Footer,
});
