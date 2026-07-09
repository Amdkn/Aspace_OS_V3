"use client";

import { useState, useEffect } from "react";
import { SOLARIS_DOMAINS } from "@/lib/data";
import type { SolarisDomain } from "@/lib/types";

interface OrbitalPlanet extends SolarisDomain {
  x: number;
  y: number;
  radius: number;
  a: number;
}

interface OrbitalDiagramProps {
  activeId: string;
  onHover: (id: string) => void;
}

export default function OrbitalDiagram({ activeId, onHover }: OrbitalDiagramProps) {
  const domains = SOLARIS_DOMAINS;
  const [t, setT] = useState(0);

  useEffect(() => {
    let raf: number;
    const start = performance.now();
    const loop = (now: number) => {
      setT((now - start) / 1000);
      raf = requestAnimationFrame(loop);
    };
    raf = requestAnimationFrame(loop);
    return () => cancelAnimationFrame(raf);
  }, []);

  // 8 domains spread across two orbital bands (4 each) for visual interest
  const planets: OrbitalPlanet[] = domains.map((d, i) => {
    const band = i % 2;
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
          A&apos;SPACE
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
                filter={isActive ? "url(#planetGlow)" : undefined}
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
        <div>
          <span className="k">SYS: </span>
          <span className="v">solaris.factory</span>
        </div>
        <div>
          <span className="k">PÔLE: </span>
          <span className="v">
            {active.n} {active.name.toUpperCase()}
          </span>
        </div>
        <div>
          <span className="k">VP B2: </span>
          <span className="v">{active.vp}</span>
        </div>
        <div>
          <span className="k">SQUADS B3: </span>
          <span className="v">{active.agents} actives</span>
        </div>
        <div>
          <span className="k">PULSE: </span>
          <span className="v" style={{ color: "var(--mint)" }}>
            {active.metric}
          </span>
        </div>
      </div>
    </div>
  );
}
