"use client";

import { useState } from "react";
import type { FormEvent } from "react";
import { fonts } from "@/design/tokens";

const SPECIALTIES = [
  "Expert-Comptable",
  "Avocat",
  "Family-Office",
  "Coach",
  "Cabinet-Médical",
];

export default function CTASection() {
  const [formDone, setFormDone] = useState<boolean>(false);

  function submitForm(e: FormEvent<HTMLFormElement>): void {
    e.preventDefault();
    setFormDone(true);
  }

  return (
    <section
      id="cta"
      className="relative px-6 md:px-10"
      style={{
        paddingTop: "120px",
        paddingBottom: "120px",
        background: "#0A0E16",
        borderTop: "1px solid rgba(200,165,92,.16)",
      }}
    >
      <div
        className="mx-auto text-center"
        style={{ maxWidth: "880px" }}
      >
        <h2
          className="font-semibold text-[#F5EFE0] mb-[18px]"
          style={{
            fontFamily: fonts.serif,
            fontSize: "clamp(40px, 5.4vw, 76px)",
            lineHeight: 1.02,
          }}
        >
          Soumettez votre cabinet.
          <br />
          <span className="italic" style={{ color: "#C8A55C" }}>
            Audit vault sous 48h.
          </span>
        </h2>
        <p
          className="text-[12px] tracking-[.1em] uppercase mb-12"
          style={{
            fontFamily: fonts.mono,
            color: "rgba(245,239,224,.45)",
          }}
        >
          async · zero calls · vault chiffré
        </p>
        {formDone ? (
          <div
            className="max-w-[560px] mx-auto p-[48px] md:p-12"
            style={{
              border: "1px solid rgba(111,169,138,.45)",
              background: "rgba(111,169,138,.07)",
            }}
          >
            <div
              className="text-[11px] tracking-[.12em] uppercase mb-[14px]"
              style={{
                fontFamily: fonts.mono,
                color: "#6FA98A",
              }}
            >
              ✓ mandat reçu · vault en queue
            </div>
            <div
              className="text-[30px] font-semibold text-[#F5EFE0]"
              style={{ fontFamily: fonts.serif }}
            >
              Votre audit silencieux a démarré.
            </div>
            <div
              className="text-[15px] mt-3"
              style={{
                fontFamily: fonts.sans,
                color: "rgba(245,239,224,.6)",
              }}
            >
              Activation sous 48h. Aucun appel. On vous écrit depuis le vault.
            </div>
          </div>
        ) : (
          <form
            onSubmit={submitForm}
            className="max-w-[560px] mx-auto flex flex-col gap-[14px] text-left"
          >
            <div className="grid gap-[14px]" style={{ gridTemplateColumns: "1fr 1fr" }}>
              <input
                placeholder="Nom"
                className="text-[15px] text-[#F5EFE0] px-4 py-[14px] outline-none"
                style={{
                  fontFamily: fonts.sans,
                  background: "rgba(255,255,255,.03)",
                  border: "1px solid rgba(245,239,224,.16)",
                }}
              />
              <input
                placeholder="Cabinet"
                className="text-[15px] text-[#F5EFE0] px-4 py-[14px] outline-none"
                style={{
                  fontFamily: fonts.sans,
                  background: "rgba(255,255,255,.03)",
                  border: "1px solid rgba(245,239,224,.16)",
                }}
              />
            </div>
            <input
              type="email"
              placeholder="Email"
              className="text-[15px] text-[#F5EFE0] px-4 py-[14px] outline-none"
              style={{
                fontFamily: fonts.sans,
                background: "rgba(255,255,255,.03)",
                border: "1px solid rgba(245,239,224,.16)",
              }}
            />
            <select
              defaultValue=""
              className="text-[15px] text-[#F5EFE0] px-4 py-[14px] outline-none"
              style={{
                fontFamily: fonts.sans,
                background: "rgba(255,255,255,.03)",
                border: "1px solid rgba(245,239,224,.16)",
                color: "#F5EFE0",
              }}
            >
              <option value="" disabled>
                Spécialité
              </option>
              {SPECIALTIES.map((s) => (
                <option key={s} value={s} style={{ background: "#0A0E16" }}>
                  Spécialité — {s}
                </option>
              ))}
            </select>
            <button
              type="submit"
              className="text-[13px] tracking-[.08em] uppercase font-bold cursor-pointer border-0 py-[17px] mt-[6px]"
              style={{
                fontFamily: fonts.mono,
                color: "#0A0E16",
                background: "#C8A55C",
              }}
            >
              Soumettre mon cabinet →
            </button>
          </form>
        )}
      </div>
    </section>
  );
}
