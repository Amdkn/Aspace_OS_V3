"use client";

import { fonts } from "@/design/tokens";
import { b2 } from "@/data/b2";
import { b3, additionalSquadsLabel } from "@/data/b3";

export default function Anatomy() {
  return (
    <section
      id="s02"
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
          02 · l&apos;anatomie de votre cabinet fantôme
        </div>
        <h2
          className="font-semibold text-[#F5EFE0] max-w-[820px] mb-[18px]"
          style={{
            fontFamily: fonts.serif,
            fontSize: "clamp(36px, 4.6vw, 62px)",
            lineHeight: 1.03,
          }}
        >
          Oubliez les juniors.{" "}
          <span className="italic" style={{ color: "#C8A55C" }}>
            Rencontrez votre escouade fantôme.
          </span>
        </h2>
        <p
          className="text-[18px] max-w-[620px] mb-[54px]"
          style={{
            fontFamily: fonts.sans,
            color: "rgba(245,239,224,.6)",
          }}
        >
          B1 délègue à B2 → B2 délègue à B3 → B3 ships to you. Vous ne managez
          rien.
        </p>

        <div
          className="grid gap-7 items-start"
          style={{ gridTemplateColumns: "minmax(0, 280px) minmax(0, 1fr)" }}
        >
          {/* B1 Practice Owner */}
          <div
            className="p-7"
            style={{
              border: "1px solid rgba(200,165,92,.4)",
              background:
                "linear-gradient(160deg, rgba(200,165,92,.08), transparent)",
              position: "sticky",
              top: "90px",
            }}
          >
            <div
              className="text-[10px] tracking-[.14em] uppercase mb-3"
              style={{
                fontFamily: fonts.mono,
                color: "#C8A55C",
              }}
            >
              B1 · le chef
            </div>
            <div
              className="text-[30px] font-semibold text-[#F5EFE0] leading-[1.05] mb-[14px]"
              style={{ fontFamily: fonts.serif }}
            >
              Practice Owner
            </div>
            <p
              className="text-[15px] leading-[1.6] mb-[18px]"
              style={{
                fontFamily: fonts.sans,
                color: "rgba(245,239,224,.6)",
              }}
            >
              1 agent. 24/7 routing. Reçoit vos mandats et les distribue. Vous
              lui parlez, il s&apos;occupe du reste.
            </p>
            <div className="flex flex-col gap-[9px]">
              {[
                { k: "agents", v: "1" },
                { k: "uptime", v: "99.94%" },
                { k: "routing", v: "24/7" },
              ].map((row) => (
                <div
                  key={row.k}
                  className="flex justify-between text-[11px]"
                  style={{
                    fontFamily: fonts.mono,
                    color: "rgba(245,239,224,.5)",
                  }}
                >
                  <span>{row.k}</span>
                  <span style={{ color: "#C8A55C" }}>{row.v}</span>
                </div>
              ))}
            </div>
          </div>

          <div className="flex flex-col gap-7">
            {/* B2 8 cabinets */}
            <div
              className="p-[26px]"
              style={{
                border: "1px solid rgba(245,239,224,.12)",
                background: "rgba(255,255,255,.012)",
              }}
            >
              <div className="flex justify-between items-baseline mb-5">
                <div
                  className="text-[10px] tracking-[.14em] uppercase"
                  style={{
                    fontFamily: fonts.mono,
                    color: "#C8A55C",
                  }}
                >
                  B2 · 8 cabinets
                </div>
                <div
                  className="text-[10px]"
                  style={{
                    fontFamily: fonts.mono,
                    color: "rgba(245,239,224,.4)",
                  }}
                >
                  délègue ↓
                </div>
              </div>
              <div
                className="grid gap-3"
                style={{ gridTemplateColumns: "repeat(4, minmax(0, 1fr))" }}
              >
                {b2.map((c, i) => (
                  <div
                    key={c.hero}
                    className="p-[14px] hover:bg-[rgba(200,165,92,.08)] transition-colors"
                    style={{
                      border: "1px solid rgba(200,165,92,.18)",
                      background: "rgba(200,165,92,.03)",
                    }}
                  >
                    <div
                      className="text-[9px] mb-[6px]"
                      style={{
                        fontFamily: fonts.mono,
                        color: "rgba(245,239,224,.35)",
                      }}
                    >
                      {String(i + 1).padStart(2, "0")}
                    </div>
                    <div
                      className="text-[14px] font-semibold text-[#F5EFE0] leading-[1.15]"
                      style={{ fontFamily: fonts.sans }}
                    >
                      {c.hero}
                    </div>
                    <div
                      className="text-[9px] tracking-[.04em] uppercase mt-[5px]"
                      style={{
                        fontFamily: fonts.mono,
                        color: "#C8A55C",
                      }}
                    >
                      {c.domain}
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* B3 32 squads */}
            <div
              className="p-[26px]"
              style={{
                border: "1px solid rgba(245,239,224,.12)",
                background: "rgba(255,255,255,.012)",
              }}
            >
              <div className="flex justify-between items-baseline mb-5">
                <div
                  className="text-[10px] tracking-[.14em] uppercase"
                  style={{
                    fontFamily: fonts.mono,
                    color: "#C8A55C",
                  }}
                >
                  B3 · 32 squads Zero-PII
                </div>
                <div
                  className="text-[10px]"
                  style={{
                    fontFamily: fonts.mono,
                    color: "rgba(245,239,224,.4)",
                  }}
                >
                  ships to you ↓
                </div>
              </div>
              <div className="flex flex-wrap gap-[9px]">
                {b3.map((sq) => (
                  <span
                    key={sq}
                    className="text-[11px] px-[11px] py-[6px]"
                    style={{
                      fontFamily: fonts.mono,
                      color: "rgba(245,239,224,.7)",
                      border: "1px solid rgba(245,239,224,.14)",
                      background: "rgba(255,255,255,.02)",
                    }}
                  >
                    {sq}
                  </span>
                ))}
                <span
                  className="text-[11px] px-[11px] py-[6px]"
                  style={{
                    fontFamily: fonts.mono,
                    color: "#C8A55C",
                    border: "1px dashed rgba(200,165,92,.4)",
                  }}
                >
                  {additionalSquadsLabel}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
