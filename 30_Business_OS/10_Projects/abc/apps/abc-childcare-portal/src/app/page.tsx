import { TopNav } from '@/components/TopNav';
import { Hero } from '@/components/Hero';
import {
  CTABand,
  FAQ,
  Footer,
  Manifesto,
  Marquee,
  PillarRow,
  PhoneTour,
  Programme,
  Stats,
  Testimonials,
} from '@/components/LandingSections';

export default function HomePage() {
  return (
    <div style={{ position: 'relative' }}>
      <div className="horizon" />
      <div className="grain" />
      <div style={{ position: 'relative', zIndex: 5, padding: '16px 16px 0' }}>
        <TopNav />
      </div>
      <Hero />
      <Marquee />
      <Manifesto />
      <PillarRow />
      <PhoneTour />
      <Stats />
      <Programme />
      <Testimonials />
      <FAQ />
      <CTABand />
      <Footer />
    </div>
  );
}
