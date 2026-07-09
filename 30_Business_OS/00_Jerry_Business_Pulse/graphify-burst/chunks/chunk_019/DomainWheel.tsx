"use client";

import { SOLARIS_DOMAINS } from "@/lib/data";

interface DomainWheelProps {
  activeIdx: number;
  onSelect: (idx: number) => void;
}

export default function DomainWheel({ activeIdx, onSelect }: DomainWheelProps) {
  const domains = SOLARIS_DOMAINS;
  const N = domains.length;
  const cx = 290,
    cy = 290,
    rIn = 90,
    rOut = 260,
    rLabel = 220;

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
        <circle
          cx={cx}
          cy={cy}
          r={rOut + 12}
          fill="none"
          stroke="var(--line)"
          strokeDasharray="1 3"
        />

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
                  if (!active)
                    (e.target as SVGPathElement).setAttribute("fill", "var(--surface)");
                }}
                onMouseLeave={(e) => {
                  if (!active)
                    (e.target as SVGPathElement).setAttribute("fill", "var(--surface-2)");
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
        <circle
          cx={cx}
          cy={cy}
          r={rIn - 14}
          fill="none"
          stroke="var(--accent)"
          strokeOpacity="0.5"
          strokeDasharray="2 4"
        />
        <text
          x={cx}
          y={cy - 8}
          textAnchor="middle"
          fontFamily="var(--font-display)"
          fontSize="20"
          fill="var(--ink)"
        >
          Roue
        </text>
        <text
          x={cx}
          y={cy + 14}
          textAnchor="middle"
          fontFamily="var(--font-mono)"
          fontSize="9"
          letterSpacing="2"
          fill="var(--ink-3)"
        >
          3×8 MATRIX
        </text>
      </svg>
    </div>
  );
}
