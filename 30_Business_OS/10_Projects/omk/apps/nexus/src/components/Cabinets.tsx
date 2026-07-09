"use client";

import { useState } from "react";
import { fonts } from "@/design/tokens";
import { cabinets } from "@/data/cabinets";

// Verbatim from Nexus.dc.html wheelGeometry()
// r=43, cx=50, cy=50 — produces 9 positions around a circle
function wheelGeometry(i: number, active: boolean): React.CSSProperties {
  const r = 43;
  const cx = 50;
  const cy = 50;
  const ang = (i / 9) * 2 * Math.PI - Math.PI / 2;
  const x = cx + r * Math.cos(ang);
  const y = cy + r * Math.sin(ang);
  return {
    position: "absolute",
    left: `${x}%`,
    top: `${y}%`,
    transform: "translate(-50%, -50%)",
    zIndex: 5,
    fontFamily: fonts.mono,
    fontSize: 10,
    letterSpacing: ".03em",
    whiteSpace: "nowrap",
    cursor: "pointer",
    padding: "9px 12px",
    borderRadius: 2,
    transition: "all .25s",
    border: `1px solid ${active ? "#C8A55C" : "rgba(245,239,224,.16)"}`,
    background: active ? "#C8A55C" : "rgba(10,14,22,.85)",
    color: active ? "#0A0E16" : "rgba(245,239,224,.72)",
    fontWeight: active ? 700 : 400,
    boxShadow: active ? "0 0 24px rgba(200,165,92,.35)" : "none",
  };
}

export default function Cabinets() {
  const [activeCabinet, setActiveCabinet] = useState<number>(1);
  const activeCab = cabinets[activeCabinet] ?? cabinets[0];
  const activeCabPad = `${String(activeCabinet + 1).padStart(2, "0")} / 09`;

  return (
    <section
      id="s04"
      className="relative px-6 md:px-10"
      style={{
        paddingTop: "110px",
        paddingBottom: "110px",
        background: "#0A0E16",
      }}
    >
      <div className="mx-auto" style={{ maxWidth: "1180px" }}>
        <div
          className="text-[11px] tracking-[.18em] uppercase mb-[22px] text-[#C8A55C]"
          style={{ fontFamily: fonts.mono }}
        >
          04 · les 9 cabinets
        </div>
        <h2
          className="font-semibold text-[#F5EFE0] max-w-[880px] mb-[56px]"
          style={{
            fontFamily: fonts.serif,
            fontSize: "clamp(34px, 4.4vw, 58px)",
            lineHeight: 1.04,
          }}
        >
          Neuf chiefs. Trente-deux squads.{" "}
          <span className="italic" style={{ color: "#C8A55C" }}>
            Un seul vault à ouvrir.
          </span>
        </h2>
        <div
          className="grid gap-12 items-center"
          style={{ gridTemplateColumns: "minmax(0, 1fr) minmax(0, 420px)" }}
        >
          {/* wheel */}
          <div
            className="relative aspect-square w-full max-w-[500px] mx-auto"
          >
            <div
              className="absolute rounded-full"
              style={{
                inset: "14%",
                border: "1px dashed rgba(200,165,92,.16)",
              }}
            />
            <div
              className="absolute rounded-full bg-nx-vault-radial flex flex-col items-center justify-center text-center"
              style={{
                top: "50%",
                left: "50%",
                transform: "translate(-50%, -50%)",
                zIndex: 6,
                width: 118,
                height: 118,
                border: "1px solid rgba(200,165,92,.4)",
              }}
            >
              <div
                className="text-[8px] tracking-[.14em] uppercase"
                style={{
                  fontFamily: fonts.mono,
                  color: "#C8A55C",
                }}
              >
                vault
              </div>
              <div
                className="text-[22px] font-semibold text-[#F5EFE0]"
                style={{ fontFamily: fonts.serif }}
              >
                9 / 32
              </div>
              <div
                className="text-[7px] tracking-[.1em] uppercase"
                style={{
                  fontFamily: fonts.mono,
                  color: "rgba(245,239,224,.45)",
                }}
              >
                chiefs / squads
              </div>
            </div>
            {cabinets.map((c, i) => (
              <button
                key={c.name}
                onClick={() => setActiveCabinet(i)}
                style={wheelGeometry(i, i === activeCabinet)}
              >
                {c.name}
              </button>
            ))}
          </div>

          {/* detail panel */}
          <div
            className="p-8 min-h-[360px]"
            style={{
              border: "1px solid rgba(200,165,92,.3)",
              background:
                "linear-gradient(160deg, rgba(200,165,92,.05), transparent)",
            }}
          >
            <div className="flex justify-between items-center mb-[6px]">
              <div
                className="text-[10px] tracking-[.12em] uppercase"
                style={{
                  fontFamily: fonts.mono,
                  color: "#C8A55C",
                }}
              >
                cabinet · {activeCabPad}
              </div>
              <div
                className="text-[10px] tracking-[.08em] uppercase flex items-center gap-[6px]"
                style={{
                  fontFamily: fonts.mono,
                  color: "#6FA98A",
                }}
              >
                <span
                  className="rounded-full"
                  style={{
                    width: 6,
                    height: 6,
                    background: "#6FA98A",
                  }}
                />
                {activeCab.status}
              </div>
            </div>
            <div
              className="text-[38px] font-semibold text-[#F5EFE0] leading-[1.05] mb-6"
              style={{ fontFamily: fonts.serif }}
            >
              {activeCab.name}
            </div>
            <div className="flex flex-col gap-[18px]">
              <div>
                <div
                  className="text-[9px] tracking-[.1em] uppercase mb-[6px]"
                  style={{
                    fontFamily: fonts.mono,
                    color: "rgba(245,239,224,.4)",
                  }}
                >
                  ICP signal
                </div>
                <div
                  className="text-[16px] text-[#F5EFE0]"
                  style={{ fontFamily: fonts.sans }}
                >
                  {activeCab.icp}
                </div>
              </div>
              <div>
                <div
                  className="text-[9px] tracking-[.1em] uppercase mb-[6px]"
                  style={{
                    fontFamily: fonts.mono,
                    color: "rgba(245,239,224,.4)",
                  }}
                >
                  B2 cabinet
                </div>
                <div
                  className="text-[14px] text-[#C8A55C]"
                  style={{ fontFamily: fonts.mono }}
                >
                  {activeCab.b2}
                </div>
              </div>
              <div>
                <div
                  className="text-[9px] tracking-[.1em] uppercase mb-2"
                  style={{
                    fontFamily: fonts.mono,
                    color: "rgba(245,239,224,.4)",
                  }}
                >
                  B3 squads Zero-PII
                </div>
                <div className="flex flex-wrap gap-[7px]">
                  {activeCab.squads.map((sq) => (
                    <span
                      key={sq}
                      className="text-[11px] px-[9px] py-[5px]"
                      style={{
                        fontFamily: fonts.mono,
                        color: "rgba(245,239,224,.72)",
                        border: "1px solid rgba(245,239,224,.14)",
                      }}
                    >
                      {sq}
                    </span>
                  ))}
                </div>
              </div>
              <div
                className="flex justify-between items-center pt-4 mt-1"
                style={{ borderTop: "1px solid rgba(200,165,92,.18)" }}
              >
                <span
                  className="text-[10px] tracking-[.1em] uppercase"
                  style={{
                    fontFamily: fonts.mono,
                    color: "rgba(245,239,224,.4)",
                  }}
                >
                  trust pulse
                </span>
                <span
                  className="text-[32px] font-semibold text-[#C8A55C]"
                  style={{ fontFamily: fonts.serif }}
                >
                  {activeCab.pulse}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
