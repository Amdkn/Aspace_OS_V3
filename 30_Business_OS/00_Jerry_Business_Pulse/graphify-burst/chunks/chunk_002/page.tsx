"use client";

import { useState, useEffect } from "react";
import Topbar from "@/components/sections/Topbar";
import Hero from "@/components/sections/Hero";
import HookSection from "@/components/sections/HookSection";
import AnatomySection from "@/components/sections/AnatomySection";
import MarginShieldSection from "@/components/sections/MarginShieldSection";
import WheelSection from "@/components/sections/WheelSection";
import ArchetypeSection from "@/components/sections/ArchetypeSection";
import ParadigmSection from "@/components/sections/ParadigmSection";
import VaultSection from "@/components/sections/VaultSection";
import FinalCTA from "@/components/sections/FinalCTA";
import Footer from "@/components/sections/Footer";

export default function Home() {
  const [icp, setIcp] = useState("aaa");

  // Mirror archetype/density into the document for CSS theming
  useEffect(() => {
    document.documentElement.setAttribute("data-archetype", icp);
  }, [icp]);

  return (
    <div className="page">
      <Topbar icp={icp} setIcp={setIcp} />
      <Hero icp={icp} />
      <HookSection />
      <AnatomySection />
      <MarginShieldSection />
      <WheelSection />
      <ArchetypeSection icp={icp} setIcp={setIcp} />
      <ParadigmSection />
      <VaultSection icp={icp} />
      <FinalCTA />
      <Footer />
    </div>
  );
}
