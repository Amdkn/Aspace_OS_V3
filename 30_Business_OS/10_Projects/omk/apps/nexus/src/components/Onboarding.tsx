"use client";

import { fonts } from "@/design/tokens";
import { steps } from "@/data/onboarding";

export default function Onboarding() {
  return (
    <section
      id="s07"
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
          07 · onboarding · zero friction, zero calls
        </div>
        <h2
          className="font-semibold text-[#F5EFE0] max-w-[780px] mb-[18px]"
          style={{
            fontFamily: fonts.serif,
            fontSize: "clamp(34px, 4.4vw, 58px)",
            lineHeight: 1.04,
          }}
        >
          On ne vend pas en call.{" "}
          <span className="italic" style={{ color: "#C8A55C" }}>
            Le vault parle pour vous.
          </span>
        </h2>
        <p
          className="text-[18px] max-w-[600px] mb-[54px]"
          style={{
            fontFamily: fonts.sans,
            color: "rgba(245,239,224,.6)",
          }}
        >
          Demo Vault · async closing preview. Vous droppez une URL, on chiffre,
          on active. Pas de démo, pas de pipeline.
        </p>
        <div
          className="grid gap-5"
          style={{ gridTemplateColumns: "repeat(3, minmax(0, 1fr))" }}
        >
          {steps.map((st) => (
            <div
              key={st.n}
              className="p-[30px] relative overflow-hidden"
              style={{
                border: "1px solid rgba(200,165,92,.22)",
                background:
                  "linear-gradient(160deg, rgba(200,165,92,.04), transparent)",
              }}
            >
              <div
                className="absolute top-0 left-0 h-[2px] w-full"
                style={{
                  background:
                    "linear-gradient(90deg, transparent, rgba(200,165,92,.6), transparent)",
                }}
              />
              <div
                className="text-[11px] tracking-[.1em] uppercase mb-[18px] text-[#C8A55C]"
                style={{ fontFamily: fonts.mono }}
              >
                {st.n}
              </div>
              <div
                className="text-[26px] font-semibold text-[#F5EFE0] leading-[1.1] mb-3"
                style={{ fontFamily: fonts.serif }}
              >
                {st.title}
              </div>
              <p
                className="text-[15px] leading-[1.6] mb-[18px]"
                style={{
                  fontFamily: fonts.sans,
                  color: "rgba(245,239,224,.6)",
                }}
              >
                {st.body}
              </p>
              <div
                className="text-[11px] pt-[14px]"
                style={{
                  fontFamily: fonts.mono,
                  color: "#6FA98A",
                  borderTop: "1px solid rgba(200,165,92,.14)",
                }}
              >
                {st.meta}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
