"use client";

import { fonts } from "@/design/tokens";
import { leviers } from "@/data/leviers";

export default function Leviers() {
  return (
    <section
      id="s06"
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
          06 · les 3 leviers 2026
        </div>
        <h2
          className="font-semibold text-[#F5EFE0] max-w-[820px] mb-[56px]"
          style={{
            fontFamily: fonts.serif,
            fontSize: "clamp(34px, 4.4vw, 58px)",
            lineHeight: 1.04,
          }}
        >
          Les cabinets ne croient plus{" "}
          <span className="italic" style={{ color: "#C8A55C" }}>
            aux outils SaaS publics.
          </span>
        </h2>
        <div
          className="grid gap-5"
          style={{ gridTemplateColumns: "repeat(3, minmax(0, 1fr))" }}
        >
          {leviers.map((l) => (
            <div
              key={l.n}
              className="p-[34px] md:p-8 flex flex-col min-h-[300px] hover:border-[rgba(200,165,92,.4)] transition-colors"
              style={{
                border: "1px solid rgba(245,239,224,.12)",
                background: "rgba(255,255,255,.012)",
              }}
            >
              <div
                className="text-[52px] font-semibold leading-none mb-6"
                style={{
                  fontFamily: fonts.serif,
                  color: "rgba(200,165,92,.35)",
                }}
              >
                {l.n}
              </div>
              <div className="flex items-center gap-3 mb-[18px] flex-wrap">
                <span
                  className="text-[13px] line-through"
                  style={{
                    fontFamily: fonts.mono,
                    color: "rgba(245,239,224,.45)",
                  }}
                >
                  {l.from}
                </span>
                <span style={{ color: "#C8A55C" }}>→</span>
                <span
                  className="text-[13px] font-bold"
                  style={{
                    fontFamily: fonts.mono,
                    color: "#C8A55C",
                  }}
                >
                  {l.to}
                </span>
              </div>
              <div
                className="text-[10px] tracking-[.1em] uppercase self-start mb-[18px] px-[10px] py-[5px]"
                style={{
                  fontFamily: fonts.mono,
                  color: "#6FA98A",
                  border: "1px solid rgba(111,169,138,.3)",
                }}
              >
                {l.tag}
              </div>
              <p
                className="text-[15.5px] leading-[1.62]"
                style={{
                  fontFamily: fonts.sans,
                  color: "rgba(245,239,224,.62)",
                }}
              >
                {l.body}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
