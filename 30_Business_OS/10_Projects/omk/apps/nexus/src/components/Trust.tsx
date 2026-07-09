"use client";

import { useEffect, useState } from "react";
import { fonts } from "@/design/tokens";

// Verbatim from Nexus.dc.html logData
const LOG_DATA = [
  { t: "00.000", msg: "Practice Owner → B2.Vault-Auditor", meta: "route" },
  { t: "00.114", msg: "B2.Vault-Auditor → zero-PII redaction", meta: "scan" },
  { t: "00.231", msg: "B3.Vault-Redactor · 14 PII masqués", meta: "redact" },
  { t: "00.402", msg: "B3.Audit-Log-Immutable · write append-only", meta: "commit" },
  { t: "00.518", msg: "AI-Act gate · classification low-risk", meta: "gate" },
  { t: "00.640", msg: "coût $0.0012 · trust +94% · ships to you", meta: "done" },
];

// Verbatim from Nexus.dc.html telShield
const TEL_SHIELD = [
  { label: "Audit log immutable", value: "append-only", pct: "100%", color: "#6FA98A" },
  { label: "Zero-PII scan", value: "100%", pct: "100%", color: "#C8A55C" },
  { label: "AI-Act compliance", value: "94%", pct: "94%", color: "#C8A55C" },
  { label: "Sober score · 1an+", value: "A+", pct: "92%", color: "#6FA98A" },
];

// Verbatim from Nexus.dc.html telBrute
const TEL_BRUTE = [
  { label: "Audit log immutable", value: "OFF", pct: "18%", color: "#C16B5A" },
  { label: "Zero-PII scan", value: "leaking", pct: "34%", color: "#C16B5A" },
  { label: "AI-Act compliance", value: "unknown", pct: "22%", color: "#C16B5A" },
  { label: "Sober score · 1an+", value: "D — burn", pct: "14%", color: "#C16B5A" },
];

const META_COLORS: Record<string, string> = {
  route: "#7E93B8",
  scan: "#C8A55C",
  redact: "#C8A55C",
  commit: "#6FA98A",
  gate: "#C8A55C",
  done: "#6FA98A",
};

export default function Trust() {
  const [vaultMode, setVaultMode] = useState<"shield" | "brute">("shield");
  const [reveal, setReveal] = useState<number>(1);

  // Verbatim from Nexus.dc.html componentDidMount: cycle reveal every 1.6s
  useEffect(() => {
    const handle = setInterval(() => {
      setReveal((r) => (r % 6) + 1);
    }, 1600);
    return () => clearInterval(handle);
  }, []);

  const isShield = vaultMode === "shield";
  const statusColor = isShield ? "#6FA98A" : "#C16B5A";
  const statusLabel = isShield ? "secured" : "exposed";
  const shieldBorder = isShield
    ? "rgba(200,165,92,.4)"
    : "rgba(193,107,90,.45)";
  const shieldBg = isShield
    ? "linear-gradient(160deg, rgba(200,165,92,.05), transparent)"
    : "linear-gradient(160deg, rgba(193,107,90,.07), transparent)";

  return (
    <section
      id="s03"
      className="relative px-6 md:px-10"
      style={{
        paddingTop: "110px",
        paddingBottom: "110px",
        background: "#08090C",
        borderTop: "1px solid rgba(200,165,92,.12)",
      }}
    >
      <div className="mx-auto" style={{ maxWidth: "1180px" }}>
        <div className="flex justify-between items-end flex-wrap gap-6 mb-12">
          <div>
            <div
              className="text-[11px] tracking-[.18em] uppercase mb-[22px] text-[#C8A55C]"
              style={{ fontFamily: fonts.mono }}
            >
              03 · trust, locked in
            </div>
            <h2
              className="font-semibold text-[#F5EFE0] max-w-[640px]"
              style={{
                fontFamily: fonts.serif,
                fontSize: "clamp(36px, 4.6vw, 62px)",
                lineHeight: 1.03,
              }}
            >
              Votre conformité est{" "}
              <span className="italic" style={{ color: "#C8A55C" }}>
                un input fixe.
              </span>
            </h2>
          </div>
          {/* mode toggle */}
          <div
            className="flex p-1 gap-1"
            style={{ border: "1px solid rgba(200,165,92,.3)" }}
          >
            <button
              onClick={() => setVaultMode("shield")}
              className="text-[11px] tracking-[.08em] px-4 py-[9px] cursor-pointer border-0"
              style={{
                fontFamily: fonts.mono,
                background: isShield ? "#C8A55C" : "transparent",
                color: isShield ? "#0A0E16" : "rgba(245,239,224,.6)",
                fontWeight: isShield ? 700 : 400,
              }}
            >
              SHIELD
            </button>
            <button
              onClick={() => setVaultMode("brute")}
              className="text-[11px] tracking-[.08em] px-4 py-[9px] cursor-pointer border-0"
              style={{
                fontFamily: fonts.mono,
                background: !isShield ? "#C16B5A" : "transparent",
                color: !isShield ? "#0A0E16" : "rgba(245,239,224,.6)",
                fontWeight: !isShield ? 700 : 400,
              }}
            >
              FORCE BRUTE
            </button>
          </div>
        </div>

        <div
          className="grid gap-6 items-stretch"
          style={{ gridTemplateColumns: "minmax(0, 1fr) minmax(0, 1.1fr)" }}
        >
          {/* Trust Shield telemetry */}
          <div
            className="p-[30px] flex flex-col gap-[22px]"
            style={{
              border: `1px solid ${shieldBorder}`,
              background: shieldBg,
            }}
          >
            <div className="flex justify-between items-center">
              <div
                className="text-[10px] tracking-[.14em] uppercase"
                style={{
                  fontFamily: fonts.mono,
                  color: "rgba(245,239,224,.5)",
                }}
              >
                Trust Shield · télémétrie live
              </div>
              <div
                className="text-[10px] tracking-[.08em] uppercase flex items-center gap-[7px]"
                style={{
                  fontFamily: fonts.mono,
                  color: statusColor,
                }}
              >
                <span
                  className="rounded-full"
                  style={{
                    width: 7,
                    height: 7,
                    background: statusColor,
                    animation: "nx-pulse 2s infinite",
                  }}
                />
                {statusLabel}
              </div>
            </div>
            {(isShield ? TEL_SHIELD : TEL_BRUTE).map((m) => (
              <div key={m.label}>
                <div className="flex justify-between items-baseline mb-2">
                  <span
                    className="text-[14px]"
                    style={{
                      fontFamily: fonts.sans,
                      color: "rgba(245,239,224,.75)",
                    }}
                  >
                    {m.label}
                  </span>
                  <span
                    className="text-[13px] font-bold"
                    style={{
                      fontFamily: fonts.mono,
                      color: m.color,
                    }}
                  >
                    {m.value}
                  </span>
                </div>
                <div
                  className="overflow-hidden"
                  style={{ height: 5, background: "rgba(255,255,255,.06)" }}
                >
                  <div
                    style={{
                      height: "100%",
                      width: m.pct,
                      background: m.color,
                      transition: "width .5s",
                    }}
                  />
                </div>
              </div>
            ))}
          </div>

          {/* Terminal log */}
          <div
            className="flex flex-col overflow-hidden"
            style={{
              border: "1px solid rgba(245,239,224,.12)",
              background: "#050608",
            }}
          >
            <div
              className="flex items-center gap-2 px-[18px] py-[13px]"
              style={{
                borderBottom: "1px solid rgba(245,239,224,.08)",
                background: "rgba(255,255,255,.015)",
              }}
            >
              <span
                className="rounded-full"
                style={{
                  width: 9,
                  height: 9,
                  background: "#C8A55C",
                  opacity: 0.7,
                }}
              />
              <span
                className="rounded-full"
                style={{
                  width: 9,
                  height: 9,
                  background: "rgba(245,239,224,.25)",
                }}
              />
              <span
                className="rounded-full"
                style={{
                  width: 9,
                  height: 9,
                  background: "rgba(245,239,224,.25)",
                }}
              />
              <span
                className="text-[10px] tracking-[.1em] uppercase ml-2"
                style={{
                  fontFamily: fonts.mono,
                  color: "rgba(245,239,224,.4)",
                }}
              >
                vault://audit-log · append-only
              </span>
            </div>
            <div
              className="px-[18px] py-5 flex flex-col gap-[11px] flex-1 min-h-[240px]"
              style={{ fontFamily: fonts.mono }}
            >
              {LOG_DATA.map((line, i) => {
                const on = i < reveal;
                const cur = i === reveal - 1;
                const metaColor = isShield
                  ? META_COLORS[line.meta] || "#C8A55C"
                  : line.meta === "redact" || line.meta === "scan"
                    ? "#C16B5A"
                    : "#9AA0AA";
                const textColor = on
                  ? isShield
                    ? cur
                      ? "#F5EFE0"
                      : "rgba(245,239,224,.7)"
                    : "rgba(245,239,224,.45)"
                  : "rgba(245,239,224,.12)";
                return (
                  <div
                    key={line.t}
                    className="flex items-center gap-[10px] transition-opacity duration-400"
                    style={{
                      opacity: on ? 1 : 0.4,
                      transform: cur ? "translateX(2px)" : undefined,
                    }}
                  >
                    <span
                      className="text-[11px]"
                      style={{ color: "rgba(245,239,224,.3)" }}
                    >
                      {line.t}
                    </span>
                    <span
                      className="text-[10px] uppercase tracking-[.06em] px-[6px] py-[1px]"
                      style={{
                        color: metaColor,
                        border: "1px solid currentColor",
                      }}
                    >
                      {line.meta}
                    </span>
                    <span className="text-[12.5px]" style={{ color: textColor }}>
                      {line.msg}
                    </span>
                  </div>
                );
              })}
              <div
                className="text-[12.5px] mt-1"
                style={{
                  fontFamily: fonts.mono,
                  color: "#C8A55C",
                }}
              >
                vault ${" "}
                <span
                  style={{
                    borderBottom: "2px solid #C8A55C",
                    animation: "nx-blink 1.1s infinite",
                  }}
                >
                  &nbsp;
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
