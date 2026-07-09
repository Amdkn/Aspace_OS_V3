/* global React, window */
// SOLARIS — interactive diagrams

const { useState, useEffect, useRef, useMemo } = React;

// =================================================================
// Orbital Diagram — used in hero
// 8 domains as planets on offset orbits, sun in center
// =================================================================
function OrbitalDiagram({ activeId, onHover }) {
  const domains = window.SOLARIS_DOMAINS;
  const [t, setT] = useState(0);

  useEffect(() => {
    let raf;
    const start = performance.now();
    const loop = (now) => {
      setT((now - start) / 1000);
      raf = requestAnimationFrame(loop);
    };
    raf = requestAnimationFrame(loop);
    return () => cancelAnimationFrame(raf);
  }, []);

  // 8 domains spread across two orbital bands (4 each) for visual interest
  const planets = domains.map((d, i) => {
    const band = i % 2;            // 0 outer, 1 inner
    const radius = band === 0 ? 200 : 150;
    const speed = band === 0 ? 0.045 : 0.07;
    const dir = band === 0 ? 1 : -1;
    const base = (i / domains.length) * Math.PI * 2;
    const a = base + t * speed * dir;
    const x = 250 + Math.cos(a) * radius;
    const y = 250 + Math.sin(a) * radius;
    return { ...d, x, y, radius, a };
  });

  const active = planets.find((p) => p.id === activeId) || planets[0];

  return (
    <div className="orbital-stage">
      <svg viewBox="0 0 500 500" className="orbital-svg" aria-hidden="true">
        <defs>
          <radialGradient id="sunGrad" cx="35%" cy="30%" r="70%">
            <stop offset="0%" stopColor="var(--core)" />
            <stop offset="50%" stopColor="var(--accent)" />
            <stop offset="100%" stopColor="var(--flare)" />
          </radialGradient>
          <filter id="sunGlow" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="6" result="b" />
            <feMerge>
              <feMergeNode in="b" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>
          <filter id="planetGlow" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="3" result="b" />
            <feMerge>
              <feMergeNode in="b" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>
        </defs>

        {/* concentric reference rings */}
        <circle cx="250" cy="250" r="60" className="orbital-ring-soft" />
        <circle cx="250" cy="250" r="100" className="orbital-ring-soft" />
        <circle cx="250" cy="250" r="150" className="orbital-ring" />
        <circle cx="250" cy="250" r="200" className="orbital-ring" />
        <circle cx="250" cy="250" r="240" className="orbital-ring-soft" />

        {/* radial ticks */}
        {Array.from({ length: 24 }).map((_, i) => {
          const a = (i / 24) * Math.PI * 2;
          const x1 = 250 + Math.cos(a) * 238;
          const y1 = 250 + Math.sin(a) * 238;
          const x2 = 250 + Math.cos(a) * 244;
          const y2 = 250 + Math.sin(a) * 244;
          return (
            <line
              key={i}
              x1={x1}
              y1={y1}
              x2={x2}
              y2={y2}
              stroke="var(--line-2)"
              strokeWidth="1"
            />
          );
        })}

        {/* sun */}
        <circle cx="250" cy="250" r="42" className="orbital-sun" />
        <circle
          cx="250"
          cy="250"
          r="54"
          fill="none"
          stroke="var(--accent)"
          strokeOpacity="0.4"
          strokeDasharray="2 4"
        />
        <text
          x="250"
          y="248"
          textAnchor="middle"
          className="orbital-label"
          fill="var(--bg)"
          fontSize="9"
        >
          A'SPACE
        </text>
        <text
          x="250"
          y="260"
          textAnchor="middle"
          className="orbital-label"
          fill="var(--bg)"
          fontSize="9"
        >
          OS
        </text>

        {/* planets */}
        {planets.map((p) => {
          const isActive = activeId === p.id;
          return (
            <g key={p.id} style={{ cursor: "pointer" }} onMouseEnter={() => onHover(p.id)}>
              {isActive && (
                <circle
                  cx={p.x}
                  cy={p.y}
                  r="18"
                  fill="none"
                  stroke="var(--accent)"
                  strokeOpacity="0.5"
                  strokeDasharray="2 3"
                />
              )}
              <circle
                cx={p.x}
                cy={p.y}
                r={isActive ? 9 : 6}
                className={"orbital-planet" + (isActive ? " active" : "")}
                filter={isActive ? "url(#planetGlow)" : null}
              />
              <text
                x={p.x}
                y={p.y - 16}
                textAnchor="middle"
                className={"orbital-label" + (isActive ? " active" : "")}
              >
                {p.n} · {p.name}
              </text>
            </g>
          );
        })}
      </svg>

      <div className="orbital-readout">
        <div><span className="k">SYS: </span><span className="v">solaris.factory</span></div>
        <div><span className="k">PÔLE: </span><span className="v">{active.n} {active.name.toUpperCase()}</span></div>
        <div><span className="k">VP B2: </span><span className="v">{active.vp}</span></div>
        <div><span className="k">SQUADS B3: </span><span className="v">{active.agents} actives</span></div>
        <div><span className="k">PULSE: </span><span className="v" style={{color: 'var(--mint)'}}>{active.metric}</span></div>
      </div>
    </div>
  );
}

// =================================================================
// Wheel of Business — 8 domain pie wheel
// =================================================================
function DomainWheel({ activeIdx, onSelect }) {
  const domains = window.SOLARIS_DOMAINS;
  const N = domains.length;
  const cx = 290, cy = 290, rIn = 90, rOut = 260, rLabel = 220;

  return (
    <div className="wheel">
      <svg viewBox="0 0 580 580" style={{ width: "100%", overflow: "visible" }}>
        <defs>
          <radialGradient id="wheelGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="var(--accent)" stopOpacity="0.3" />
            <stop offset="100%" stopColor="var(--accent)" stopOpacity="0" />
          </radialGradient>
        </defs>

        {/* outer ring */}
        <circle cx={cx} cy={cy} r={rOut + 12} fill="none" stroke="var(--line)" strokeDasharray="1 3" />

        {domains.map((d, i) => {
          const startA = (i / N) * Math.PI * 2 - Math.PI / 2;
          const endA = ((i + 1) / N) * Math.PI * 2 - Math.PI / 2;
          const midA = (startA + endA) / 2;
          const active = i === activeIdx;

          // arc path (filled wedge)
          const x1 = cx + Math.cos(startA) * rIn;
          const y1 = cy + Math.sin(startA) * rIn;
          const x2 = cx + Math.cos(startA) * rOut;
          const y2 = cy + Math.sin(startA) * rOut;
          const x3 = cx + Math.cos(endA) * rOut;
          const y3 = cy + Math.sin(endA) * rOut;
          const x4 = cx + Math.cos(endA) * rIn;
          const y4 = cy + Math.sin(endA) * rIn;

          const path = [
            `M ${x1} ${y1}`,
            `L ${x2} ${y2}`,
            `A ${rOut} ${rOut} 0 0 1 ${x3} ${y3}`,
            `L ${x4} ${y4}`,
            `A ${rIn} ${rIn} 0 0 0 ${x1} ${y1}`,
            "Z",
          ].join(" ");

          // label position
          const lx = cx + Math.cos(midA) * rLabel;
          const ly = cy + Math.sin(midA) * rLabel;
          const nx = cx + Math.cos(midA) * (rIn + 22);
          const ny = cy + Math.sin(midA) * (rIn + 22);

          return (
            <g key={d.id} style={{ cursor: "pointer" }} onClick={() => onSelect(i)}>
              <path
                d={path}
                fill={active ? "var(--accent)" : "var(--surface-2)"}
                stroke="var(--line-2)"
                strokeWidth="1"
                style={{ transition: "fill 0.25s" }}
                onMouseEnter={(e) => {
                  if (!active) e.target.setAttribute("fill", "var(--surface)");
                }}
                onMouseLeave={(e) => {
                  if (!active) e.target.setAttribute("fill", "var(--surface-2)");
                }}
              />
              <text
                x={lx}
                y={ly}
                textAnchor="middle"
                dominantBaseline="central"
                fontFamily="var(--font-display)"
                fontSize="22"
                fill={active ? "var(--bg)" : "var(--ink)"}
                style={{ pointerEvents: "none" }}
              >
                {d.name}
              </text>
              <text
                x={lx}
                y={ly + 22}
                textAnchor="middle"
                dominantBaseline="central"
                fontFamily="var(--font-mono)"
                fontSize="10"
                letterSpacing="2"
                fill={active ? "var(--bg)" : "var(--ink-3)"}
                style={{ pointerEvents: "none" }}
              >
                {d.n}
              </text>
              <text
                x={nx}
                y={ny}
                textAnchor="middle"
                dominantBaseline="central"
                fontFamily="var(--font-mono)"
                fontSize="9"
                letterSpacing="1.5"
                fill={active ? "var(--bg)" : "var(--ink-4)"}
                style={{ pointerEvents: "none" }}
              >
                {d.sub.toUpperCase()}
              </text>
            </g>
          );
        })}

        {/* center */}
        <circle cx={cx} cy={cy} r={rIn - 4} fill="var(--bg)" stroke="var(--line)" />
        <circle cx={cx} cy={cy} r={rIn - 14} fill="none" stroke="var(--accent)" strokeOpacity="0.5" strokeDasharray="2 4" />
        <text x={cx} y={cy - 8} textAnchor="middle" fontFamily="var(--font-display)" fontSize="20" fill="var(--ink)">Roue</text>
        <text x={cx} y={cy + 14} textAnchor="middle" fontFamily="var(--font-mono)" fontSize="9" letterSpacing="2" fill="var(--ink-3)">3×8 MATRIX</text>
      </svg>
    </div>
  );
}

// =================================================================
// Animated Terminal — Capability Routing demo
// =================================================================
function RoutingTerminal() {
  const [step, setStep] = useState(0);
  const lines = useMemo(() => [
    { p: true, t: "vous@solaris.factory" },
    { c: "post --payload \"audit complet + 3 propositions de pivot\"" },
    { type: "out", t: "→ B1.Jerry reçoit la commande..." },
    { type: "dim", t: "  · traduction en spécifications" },
    { type: "ok", t: "✓ routé : B2.Wonder Woman (Production)" },
    { type: "out", t: "" },
    { p: true, t: "B2.Wonder Woman" },
    { c: "dispatch --task extract --priority routine" },
    { type: "out", t: "→ analyse de complexité..." },
    { type: "dim", t: "  · payload léger · 4.2kb" },
    { type: "ok", t: "✓ assigné : B3.Star-Lord  · coût : $0.0003" },
    { type: "out", t: "" },
    { p: true, t: "B2.Wonder Woman" },
    { c: "dispatch --task synthèse --priority lourde" },
    { type: "out", t: "→ escalade nécessaire..." },
    { type: "dim", t: "  · raisonnement long · 38kb" },
    { type: "warn", t: "↑ escaladé : B3.Captain Marvel · capé à $0.04" },
    { type: "out", t: "" },
    { p: true, t: "B2.Batman" },
    { c: "watch --margin status" },
    { type: "out", t: "  routine compute  $00.47 / jour" },
    { type: "out", t: "  plafond actif    $20.00 / mois" },
    { type: "ok", t: "  marge protégée   91% headroom" },
    { type: "out", t: "" },
    { p: true, t: "B3.Star-Lord" },
    { c: "loop --scrape OH-KY" },
    { type: "err", t: "✗ agent en boucle · 4 retries · arrêté" },
    { type: "warn", t: "↪ B2.Batman intercepte · budget protégé" },
    { type: "ok", t: "✓ agent mis en quarantaine · enquête" },
  ], []);

  useEffect(() => {
    if (step >= lines.length) return;
    const delay = lines[step].c ? 600 : lines[step].p ? 200 : 320;
    const id = setTimeout(() => setStep((s) => s + 1), delay);
    return () => clearTimeout(id);
  }, [step, lines]);

  // reset loop
  useEffect(() => {
    if (step < lines.length) return;
    const id = setTimeout(() => setStep(0), 4000);
    return () => clearTimeout(id);
  }, [step, lines.length]);

  return (
    <div className="terminal">
      <div className="terminal-bar">
        <div className="dots"><div className="dot" /><div className="dot" /><div className="dot" /></div>
        <div>routage interne · vous n'avez jamais à voir ceci</div>
      </div>
      <div className="terminal-body">
        {lines.slice(0, step).map((l, i) => (
          <div key={i} className="line">
            {l.p && <span><span className="prompt">{l.t} </span><span className="dim">$</span> </span>}
            {l.c && <><span className="dim">$ </span><span className="cmd">{l.c}</span></>}
            {l.type === "out" && <span className="out">{l.t}</span>}
            {l.type === "dim" && <span className="dim">{l.t}</span>}
            {l.type === "ok" && <span className="ok">{l.t}</span>}
            {l.type === "warn" && <span className="warn">{l.t}</span>}
            {l.type === "err" && <span className="err">{l.t}</span>}
          </div>
        ))}
        {step < lines.length && <span className="cursor" />}
      </div>
    </div>
  );
}

// =================================================================
// Margin Shield — interactive cost-load chart
// =================================================================
function MarginShield() {
  const [load, setLoad] = useState(60);
  const [mode, setMode] = useState("shield"); // shield | brute

  // Routing distribution
  const cheapShare = mode === "shield" ? Math.max(60, 95 - load * 0.4) : Math.max(10, 50 - load * 0.5);
  const midShare = mode === "shield" ? Math.min(30, load * 0.3) : 30;
  const heavyShare = 100 - cheapShare - midShare;

  // Cost: shield stays flat near $0.50/day, brute scales linearly
  const dailyCost = mode === "shield"
    ? 0.20 + (load / 100) * 0.50
    : 0.40 + (load / 100) * 9.00;
  const monthlyCost = dailyCost * 30;
  const ceiling = 20;
  const headroom = Math.max(0, Math.round((1 - monthlyCost / ceiling) * 100));
  const exceeded = monthlyCost > ceiling;

  // bars — 14 ticks, evolving with load
  const bars = useMemo(() => {
    return Array.from({ length: 18 }).map((_, i) => {
      const variance = Math.sin(i * 0.9) * 0.18 + 1;
      const base = mode === "shield"
        ? 12 + (load / 100) * 25 * variance
        : 8 + (load / 100) * 85 * variance;
      return Math.min(95, base);
    });
  }, [load, mode]);

  return (
    <div className="shield-card">
      <div className="label-row">
        <div>Margin Shield · télémétrie compute</div>
        <div className="live">live</div>
      </div>

      <div className="shield-chart">
        <div className="shield-threshold" data-label="$20 / mois — plafond" style={{ top: `${(1 - 20 / (monthlyCost > 20 ? monthlyCost * 1.1 : 25)) * 100}%` }} />
        {bars.map((h, i) => (
          <div
            key={i}
            className={"shield-bar" + (mode === "brute" ? " brute" : "")}
            style={{ height: `${h}%`, left: `${i * (100 / 18) + 0.5}%` }}
          />
        ))}
      </div>

      <div className="shield-readouts">
        <div className="shield-readout">
          <div className="k">Coût / jour</div>
          <div className={"v " + (exceeded ? "bad" : "good")}>${dailyCost.toFixed(2)}</div>
        </div>
        <div className="shield-readout">
          <div className="k">Coût / mois</div>
          <div className={"v " + (exceeded ? "bad" : "good")}>${monthlyCost.toFixed(2)}</div>
        </div>
        <div className="shield-readout">
          <div className="k">Marge restante</div>
          <div className={"v " + (exceeded ? "bad" : "good")}>{exceeded ? "OVER" : `${headroom}%`}</div>
        </div>
      </div>

      <div className="shield-router">
        <div className="router-row cheap">
          <div className="model">MiniMax 2.7</div>
          <div className="bar"><div style={{ width: `${cheapShare}%` }} /></div>
          <div className="pct">{cheapShare.toFixed(0)}%</div>
        </div>
        <div className="router-row mid">
          <div className="model">GLM 4.7 Flash</div>
          <div className="bar"><div style={{ width: `${midShare}%` }} /></div>
          <div className="pct">{midShare.toFixed(0)}%</div>
        </div>
        <div className="router-row heavy">
          <div className="model">Claude / GPT</div>
          <div className="bar"><div style={{ width: `${heavyShare}%` }} /></div>
          <div className="pct">{heavyShare.toFixed(0)}%</div>
        </div>
      </div>

      <div className="shield-control">
        <div className="row">
          <span>Charge de production</span>
          <span style={{ color: "var(--ink)" }}>{load}%</span>
        </div>
        <input
          type="range"
          className="shield-slider"
          min="10"
          max="100"
          value={load}
          onChange={(e) => setLoad(parseInt(e.target.value))}
        />
        <div className="row" style={{ marginTop: 14 }}>
          <span>Mode routeur</span>
          <span style={{ display: "flex", gap: 0, border: "1px solid var(--line-2)", borderRadius: 0 }}>
            <button
              onClick={() => setMode("shield")}
              style={{
                padding: "4px 10px",
                fontSize: 10,
                fontFamily: "var(--font-mono)",
                letterSpacing: "0.15em",
                background: mode === "shield" ? "var(--accent)" : "transparent",
                color: mode === "shield" ? "var(--bg)" : "var(--ink-2)",
              }}
            >SHIELD</button>
            <button
              onClick={() => setMode("brute")}
              style={{
                padding: "4px 10px",
                fontSize: 10,
                fontFamily: "var(--font-mono)",
                letterSpacing: "0.15em",
                background: mode === "brute" ? "var(--flare)" : "transparent",
                color: mode === "brute" ? "var(--bg)" : "var(--ink-2)",
              }}
            >FORCE BRUTE</button>
          </span>
        </div>
      </div>
    </div>
  );
}

Object.assign(window, {
  OrbitalDiagram,
  DomainWheel,
  RoutingTerminal,
  MarginShield,
});
