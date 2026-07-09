"use client";

import { useCallback, useMemo, useState } from "react";
import Header from "@/components/Header";
import Hero from "@/components/Hero";
import Manifeste from "@/components/Manifeste";
import Anatomy from "@/components/Anatomy";
import Trust from "@/components/Trust";
import Cabinets from "@/components/Cabinets";
import Profiles from "@/components/Profiles";
import Leviers from "@/components/Leviers";
import Onboarding from "@/components/Onboarding";
import CTASection from "@/components/CTASection";
import Footer from "@/components/Footer";
import { personas, defaultPersonaId } from "@/data/personas";
import { cabinets } from "@/data/cabinets";

function scrollToId(id: string): void {
  if (typeof document === "undefined") return;
  const el = document.getElementById(id);
  if (!el) return;
  const top = el.getBoundingClientRect().top + window.scrollY - 70;
  window.scrollTo({ top, behavior: "smooth" });
}

export default function Home() {
  const [personaId, setPersonaId] = useState<string>(defaultPersonaId);

  const activePersona = useMemo(
    () => personas.find((p) => p.id === personaId) ?? personas[0]!,
    [personaId],
  );

  // Verbatim from Nexus.dc.html setPersona: switch persona also re-anchors
  // the cabinet wheel to the matching cabinet name.
  const handleSelectPersona = useCallback((id: string) => {
    setPersonaId(id);
    const persona = personas.find((p) => p.id === id);
    if (!persona) return;
    const idx = cabinets.findIndex((c) => c.name === persona.name);
    if (idx >= 0) {
      // Cabinets component owns its own state — passive hint via data attribute.
      // Anchor scroll happens in CTASection via #s04 deep-link.
      const target = document.getElementById("s04");
      if (target) {
        const top = target.getBoundingClientRect().top + window.scrollY - 70;
        window.scrollTo({ top, behavior: "smooth" });
      }
    }
  }, []);

  return (
    <>
      <Header onScrollToForm={() => scrollToId("cta")} />
      <main>
        <Hero
          persona={activePersona}
          onScrollToForm={() => scrollToId("cta")}
          onScrollToAnatomy={() => scrollToId("s02")}
        />
        <Manifeste />
        <Anatomy />
        <Trust />
        <Cabinets />
        <Profiles
          activePersonaId={personaId}
          onSelectPersona={handleSelectPersona}
        />
        <Leviers />
        <Onboarding />
        <CTASection />
      </main>
      <Footer />
    </>
  );
}
