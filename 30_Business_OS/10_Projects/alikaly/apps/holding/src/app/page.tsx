import { TopBar } from "@/components/layout/TopBar";
import { Header } from "@/components/layout/Header";
import { Footer } from "@/components/layout/Footer";
import { Hero } from "@/components/marketing/Hero";
import { Expertises } from "@/components/marketing/Expertises";
import { Methode } from "@/components/marketing/Methode";
import { ClosingCTA } from "@/components/marketing/ClosingCTA";
import { PromiseBar } from "@/components/marketing/PromiseBar";

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col">
      <TopBar />
      <Header />
      <main className="flex-grow">
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
