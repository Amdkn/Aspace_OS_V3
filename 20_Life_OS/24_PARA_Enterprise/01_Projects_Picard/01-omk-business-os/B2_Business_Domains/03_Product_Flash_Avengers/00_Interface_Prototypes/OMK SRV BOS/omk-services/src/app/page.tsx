"use client";

import { useReveal } from "@/lib/hooks";
import { MeshBackdrop } from "@/components/Base";
import { Header } from "@/components/Header";
import { Hero } from "@/components/Hero";
import { Marquee, Piliers } from "@/components/Piliers";
import { BusinessOS } from "@/components/BusinessOS";
import { Nova, FinalCTA } from "@/components/Nova";
import { Footer } from "@/components/Footer";

export default function App() {
  useReveal();
  return (
    <div className="relative">
      <MeshBackdrop/>
      <Header/>
      <main className="relative">
        <Hero/>
        <Marquee/>
        <Piliers/>
        <BusinessOS/>
        <Nova/>
        <FinalCTA/>
      </main>
      <Footer/>
    </div>
  );
}
