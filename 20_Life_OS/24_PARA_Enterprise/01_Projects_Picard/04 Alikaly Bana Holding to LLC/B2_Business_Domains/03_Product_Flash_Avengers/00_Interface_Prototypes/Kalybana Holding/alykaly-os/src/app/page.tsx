"use client";

import { TopBar, Header } from "@/components/Header";
import { Hero, PromiseBar, Expertises } from "@/components/Hero";
import { Methode, ClosingCTA } from "@/components/Methode";
import { Footer } from "@/components/Footer";

export default function App() {
  return (
    <div className="min-h-screen text-[15px] antialiased">
      <TopBar />
      <Header />
      <main>
        <Hero />
        <PromiseBar />
        <Expertises />
        <Methode />
        <ClosingCTA />
      </main>
      <Footer />
    </div>
  );
}
