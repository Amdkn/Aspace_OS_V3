import TopBar from "@/components/marketing/TopBar";
import Header from "@/components/marketing/Header";
import Hero from "@/components/marketing/Hero";
import PromiseBar from "@/components/marketing/PromiseBar";
import Expertises from "@/components/marketing/Expertises";
import Methode from "@/components/marketing/Methode";
import ClosingCTA from "@/components/marketing/ClosingCTA";
import Footer from "@/components/marketing/Footer";

export default function Home() {
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