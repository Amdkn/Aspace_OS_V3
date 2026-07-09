"use client";

import { fonts } from "@/design/tokens";
import { b2 } from "@/data/b2";
import type { Persona } from "@/data/personas";

interface HeroProps {
  persona: Persona;
  onScrollToForm: () => void;
  onScrollToAnatomy: () => void;
}

const HERO_STATS = [
  { k: "100%", l: "Zero-PII" },
  { k: "0", l: "SaaS public" },
  { k: "AI-Act", l: "ready" },
  { k: "48h", l: "audit delivered" },
];

// 8-point orbital geometry from Nexus.dc.html orbitGeometry()
// Reproduced client-side (not in DOM string concatenation) for clarity
const ORBIT_POINTS: ReadonlyArray<readonly [number, number]> = [
  [50, 7],
  [80, 20],
  [93, 50],
  [80, 80],
  [50, 93],
  [20, 80],
  [7, 50],
  [20, 20],
];

export default function Hero({ persona, onScrollToForm, onScrollToAnatomy }: HeroProps) {
  return (
    <section
      className="relative px-6 md:px-10 grid items-center min-h-[86vh] mx-auto"
      style={{
        paddingTop: "88px",
        paddingBottom: "96px",
        maxWidth: "1280px",
        gridTemplateColumns: "minmax(0, 1.05fr) minmax(0, .95fr)",
        gap: "56px",
      }}
    >
      <div>
        <div
          className="inline-flex items-center gap-[10px] text-[11px] tracking-[.16em] uppercase border px-[14px] py-2 rounded-[2px] mb-[30px]"
          style={{
            fontFamily: fonts.mono,
            color: "#C8A55C",
            borderColor: "rgba(200,165,92,.3)",
          }}
        >
          <span
            className="inline-block rounded-full"
            style={{
              width: 6,
              height: 6,
              background: "#C8A55C",
              animation: "nx-pulse 2.4s infinite",
            }}
          />
          Nexus · Agentic Governance ·{" "}
          <span style={{ color: persona.accent, fontWeight: 700 }}>
            profile detected · {persona.short}
          </span>{" "}
          · Cabinet
        </div>
        <h1
          className="font-semibold leading-[.98] tracking-[-.01em] text-[#F5EFE0] mb-[26px]"
          style={{
            fontFamily: fonts.serif,
            fontSize: "clamp(48px, 6vw, 88px)",
          }}
        >
          Stop juggling cabinets.
          <br />
          <span className="italic" style={{ color: "#C8A55C" }}>
            Switch to Zero-PII Agentic Governance.
          </span>
        </h1>
        <p
          className="text-[19px] leading-[1.66] mb-[36px] max-w-[560px]"
          style={{
            fontFamily: fonts.sans,
            color: "rgba(245,239,224,.66)",
          }}
        >
          Vous signez le mandat. Nous exécutons en silence dans votre vault privé.{" "}
          <span className="text-[#F5EFE0]">
            Zero-PII by default. AI-Act ready. Sober 1an+.
          </span>
        </p>
        <div className="flex gap-[14px] flex-wrap mb-[46px]">
          <button
            onClick={onScrollToForm}
            className="text-[12px] tracking-[.08em] uppercase font-medium cursor-pointer border-0 px-[26px] py-[15px]"
            style={{
              fontFamily: fonts.mono,
              color: "#0A0E16",
              background: "#C8A55C",
            }}
          >
            Soumettre mon cabinet →
          </button>
          <button
            onClick={onScrollToAnatomy}
            className="text-[12px] tracking-[.08em] uppercase cursor-pointer px-[26px] py-[15px]"
            style={{
              fontFamily: fonts.mono,
              color: "#F5EFE0",
              background: "transparent",
              border: "1px solid rgba(245,239,224,.28)",
            }}
          >
            Rencontrer mon équipe
          </button>
        </div>
        <div
          className="grid gap-[18px] pt-6"
          style={{
            gridTemplateColumns: "repeat(4, 1fr)",
            borderTop: "1px solid rgba(200,165,92,.16)",
          }}
        >
          {HERO_STATS.map((s) => (
            <div key={s.l}>
              <div
                className="text-[30px] font-semibold leading-none text-[#C8A55C]"
                style={{ fontFamily: fonts.serif }}
              >
                {s.k}
              </div>
              <div
                className="text-[10px] tracking-[.08em] uppercase mt-[7px]"
                style={{
                  fontFamily: fonts.mono,
                  color: "rgba(245,239,224,.5)",
                }}
              >
                {s.l}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* ORBITAL DIAGRAM */}
      <div
        className="relative flex items-center justify-center aspect-square w-full max-w-[480px] mx-auto"
      >
        <div
          className="absolute rounded-full"
          style={{
            inset: "6%",
            border: "1px solid rgba(200,165,92,.14)",
          }}
        />
        <div
          className="absolute rounded-full"
          style={{
            inset: "20%",
            border: "1px dashed rgba(200,165,92,.18)",
          }}
        />
        <div
          className="absolute rounded-full bg-nx-orbital-conic"
        />
        {/* 8 cabinet nodes */}
        {b2.map((node, i) => {
          const [x, y] = ORBIT_POINTS[i];
          return (
            <div
              key={node.hero}
              className="absolute flex flex-col items-center"
              style={{
                left: `${x}%`,
                top: `${y}%`,
                transform: "translate(-50%, -50%)",
                zIndex: 4,
              }}
            >
              <div
                className="text-[9px] tracking-[.04em] font-bold px-2 py-1 whitespace-nowrap"
                style={{
                  fontFamily: fonts.mono,
                  color: "#0A0E16",
                  background: "#C8A55C",
                }}
              >
                {node.hero}
              </div>
              <div
                className="text-[8px] tracking-[.06em] uppercase mt-[3px] whitespace-nowrap text-center"
                style={{
                  fontFamily: fonts.mono,
                  color: "rgba(245,239,224,.6)",
                }}
              >
                {node.domain}
              </div>
            </div>
          );
        })}
        {/* center */}
        <div
          className="relative z-[5] w-[140px] h-[140px] rounded-full bg-nx-vault-sphere flex flex-col items-center justify-center text-center"
          style={{
            border: "1px solid rgba(200,165,92,.45)",
            boxShadow: "0 0 60px rgba(200,165,92,.12)",
          }}
        >
          <div
            className="absolute rounded-full"
            style={{
              inset: -10,
              border: "1px solid rgba(200,165,92,.2)",
              animation: "nx-pulse 3s infinite",
            }}
          />
          <div
            className="text-[8px] tracking-[.16em] uppercase text-[#C8A55C]"
            style={{ fontFamily: fonts.mono }}
          >
            B1
          </div>
          <div
            className="text-[19px] font-semibold text-[#F5EFE0] leading-[1.05] mt-[2px]"
            style={{ fontFamily: fonts.serif }}
          >
            Practice
            <br />
            Owner
          </div>
          <div
            className="text-[7px] tracking-[.1em] uppercase mt-[5px]"
            style={{
              fontFamily: fonts.mono,
              color: "rgba(245,239,224,.45)",
            }}
          >
            24/7 routing
          </div>
        </div>
      </div>
    </section>
  );
}
