"use client";

import { fonts } from "@/design/tokens";

const OLD_MODEL = [
  "SaaS publics multi-tenant, vos données ailleurs",
  "Greenwashing « RGPD compliant » non vérifié",
  "Excel + juniors + facturation manuelle",
];

const NEW_MODEL = [
  "Vault privé souverain, périmètre à vous",
  "Zero-PII by design, prouvé par l'audit log",
  "Sober 1an+, 3 superhumans + 32 squads",
];

export default function Manifeste() {
  return (
    <section
      id="s01"
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
          01 · le manifeste
        </div>
        <h2
          className="font-semibold text-[#F5EFE0] max-w-[880px] mb-[56px]"
          style={{
            fontFamily: fonts.serif,
            fontSize: "clamp(38px, 5vw, 68px)",
            lineHeight: 1.02,
          }}
        >
          Vous signez le mandat.{" "}
          <span className="italic" style={{ color: "#C8A55C" }}>
            Nous exécutons dans votre vault privé.
          </span>
        </h2>
        <div className="grid gap-6 md:grid-cols-2">
          {/* L'ancien modèle */}
          <div
            className="p-[34px] md:p-8"
            style={{
              border: "1px solid rgba(245,239,224,.12)",
              background: "rgba(255,255,255,.012)",
            }}
          >
            <div
              className="text-[10px] tracking-[.14em] uppercase mb-6"
              style={{
                fontFamily: fonts.mono,
                color: "rgba(245,239,224,.42)",
              }}
            >
              L&apos;ancien modèle
            </div>
            <ul className="list-none flex flex-col gap-[18px]">
              {OLD_MODEL.map((row) => (
                <li
                  key={row}
                  className="flex gap-[14px] items-start text-[17px]"
                  style={{
                    fontFamily: fonts.sans,
                    color: "rgba(245,239,224,.55)",
                  }}
                >
                  <span
                    className="text-[14px] flex-shrink-0"
                    style={{
                      fontFamily: fonts.mono,
                      color: "rgba(245,239,224,.3)",
                    }}
                  >
                    ✕
                  </span>
                  {row}
                </li>
              ))}
            </ul>
          </div>
          {/* Vous · sur Nexus */}
          <div
            className="p-[34px] md:p-8"
            style={{
              border: "1px solid rgba(200,165,92,.4)",
              background:
                "linear-gradient(160deg, rgba(200,165,92,.06), rgba(200,165,92,.01))",
            }}
          >
            <div
              className="text-[10px] tracking-[.14em] uppercase mb-6"
              style={{
                fontFamily: fonts.mono,
                color: "#C8A55C",
              }}
            >
              Vous · sur Nexus
            </div>
            <ul className="list-none flex flex-col gap-[18px]">
              {NEW_MODEL.map((row) => (
                <li
                  key={row}
                  className="flex gap-[14px] items-start text-[17px] text-[#F5EFE0]"
                  style={{ fontFamily: fonts.sans }}
                >
                  <span
                    className="text-[15px] flex-shrink-0"
                    style={{ color: "#C8A55C" }}
                  >
                    ◆
                  </span>
                  {row}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
}
