"use client";

import { fonts } from "@/design/tokens";
import { personas, type Persona } from "@/data/personas";
import { pricing } from "@/data/pricing";

interface ProfilesProps {
  activePersonaId: string;
  onSelectPersona: (id: string) => void;
}

export default function Profiles({
  activePersonaId,
  onSelectPersona,
}: ProfilesProps) {
  return (
    <section
      id="s05"
      className="relative px-6 md:px-10"
      style={{
        paddingTop: "110px",
        paddingBottom: "110px",
        background: "#08090C",
        borderTop: "1px solid rgba(200,165,92,.12)",
      }}
    >
      <div className="mx-auto" style={{ maxWidth: "1180px" }}>
        <div
          className="text-[11px] tracking-[.18em] uppercase mb-[22px] text-[#C8A55C]"
          style={{ fontFamily: fonts.mono }}
        >
          05 · profiles
        </div>
        <h2
          className="font-semibold text-[#F5EFE0] max-w-[760px] mb-[14px]"
          style={{
            fontFamily: fonts.serif,
            fontSize: "clamp(34px, 4.4vw, 58px)",
            lineHeight: 1.04,
          }}
        >
          Chaque cabinet a ses fuites.{" "}
          <span className="italic" style={{ color: "#C8A55C" }}>
            Trouvez le vôtre.
          </span>
        </h2>
        <p
          className="text-[17px] max-w-[560px] mb-12"
          style={{
            fontFamily: fonts.sans,
            color: "rgba(245,239,224,.55)",
          }}
        >
          Cliquez un profil pour rethèmer le site sur votre cabinet.
        </p>
        <div className="flex flex-col gap-[14px]">
          {personas.map((p: Persona) => {
            const active = p.id === activePersonaId;
            return (
              <button
                key={p.id}
                onClick={() => onSelectPersona(p.id)}
                className="block w-full cursor-pointer text-left transition-all duration-250 px-[26px] py-[22px]"
                style={{
                  border: `1px solid ${active ? "#C8A55C" : "rgba(245,239,224,.12)"}`,
                  background: active
                    ? "linear-gradient(120deg, rgba(200,165,92,.14), rgba(200,165,92,.04))"
                    : "rgba(255,255,255,.012)",
                }}
              >
                <div
                  className="grid gap-6 items-center w-full text-left"
                  style={{
                    gridTemplateColumns: "minmax(0, 120px) minmax(0, 1.4fr) minmax(0, 1fr) minmax(0, 1fr) minmax(0, 160px)",
                  }}
                >
                  <div>
                    <div
                      className="text-[13px] tracking-[.06em] font-bold"
                      style={{
                        fontFamily: fonts.mono,
                        color: active ? "#0A0E16" : p.accent,
                      }}
                    >
                      {p.code}
                    </div>
                    <div
                      className="text-[9px] tracking-[.1em] uppercase mt-[5px]"
                      style={{
                        fontFamily: fonts.mono,
                        color: p.priority
                          ? active
                            ? "rgba(10,14,22,.7)"
                            : "#6FA98A"
                          : active
                            ? "rgba(10,14,22,.55)"
                            : "rgba(245,239,224,.35)",
                      }}
                    >
                      {p.priority ? "priority · wave 01" : "queue"}
                    </div>
                  </div>
                  <div>
                    <div
                      className="text-[25px] font-semibold text-[#F5EFE0] leading-[1.05]"
                      style={{ fontFamily: fonts.serif }}
                    >
                      {p.name}
                    </div>
                    <div
                      className="text-[13.5px] mt-1"
                      style={{
                        fontFamily: fonts.sans,
                        color: "rgba(245,239,224,.55)",
                      }}
                    >
                      Pain · {p.pain}
                    </div>
                  </div>
                  <div>
                    <div
                      className="text-[9px] tracking-[.08em] uppercase mb-1"
                      style={{
                        fontFamily: fonts.mono,
                        color: "rgba(245,239,224,.4)",
                      }}
                    >
                      Remedy
                    </div>
                    <div
                      className="text-[14px] font-semibold text-[#C8A55C]"
                      style={{ fontFamily: fonts.sans }}
                    >
                      {p.remedy}
                    </div>
                  </div>
                  <div>
                    <div
                      className="text-[9px] tracking-[.08em] uppercase mb-1"
                      style={{
                        fontFamily: fonts.mono,
                        color: "rgba(245,239,224,.4)",
                      }}
                    >
                      Signal
                    </div>
                    <div
                      className="text-[13px]"
                      style={{
                        fontFamily: fonts.mono,
                        color: "rgba(245,239,224,.7)",
                      }}
                    >
                      {p.signal}
                    </div>
                  </div>
                  <div className="text-right">
                    <div
                      className="text-[21px] font-semibold text-[#F5EFE0] leading-[1.1]"
                      style={{ fontFamily: fonts.serif }}
                    >
                      {p.ticket}
                    </div>
                    <div
                      className="text-[10px] mt-[3px]"
                      style={{
                        fontFamily: fonts.mono,
                        color: "rgba(245,239,224,.45)",
                      }}
                    >
                      {p.lead}
                    </div>
                  </div>
                </div>
              </button>
            );
          })}
        </div>
        {/* pricing canon strip */}
        <div
          className="grid mt-8"
          style={{
            gridTemplateColumns: "repeat(4, minmax(0, 1fr))",
            gap: 1,
            background: "rgba(200,165,92,.16)",
            border: "1px solid rgba(200,165,92,.16)",
          }}
        >
          {pricing.map((t) => (
            <div
              key={t.tier}
              className="px-5 py-[22px]"
              style={{ background: "#08090C" }}
            >
              <div
                className="text-[9px] tracking-[.1em] uppercase mb-2"
                style={{
                  fontFamily: fonts.mono,
                  color: "rgba(245,239,224,.45)",
                }}
              >
                {t.tier}
              </div>
              <div
                className="text-[30px] font-semibold text-[#C8A55C] leading-none"
                style={{ fontFamily: fonts.serif }}
              >
                {t.price}
              </div>
              <div
                className="text-[13px] mt-2"
                style={{
                  fontFamily: fonts.sans,
                  color: "rgba(245,239,224,.55)",
                }}
              >
                {t.note}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
