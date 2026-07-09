"use client";

import { Header } from "@/components/Header";
import { Hero } from "@/components/Hero";
import { Packs } from "@/components/Packs";
import { Methode } from "@/components/Methode";
import { Standards } from "@/components/Standards";
import { Footer } from "@/components/Footer";

export default function App() {
  return (
    <main className="relative">
      <Header/>
      <Hero/>
      <Packs/>
      <Methode/>
      <Standards/>
      <Footer/>
    </main>
  );
}
