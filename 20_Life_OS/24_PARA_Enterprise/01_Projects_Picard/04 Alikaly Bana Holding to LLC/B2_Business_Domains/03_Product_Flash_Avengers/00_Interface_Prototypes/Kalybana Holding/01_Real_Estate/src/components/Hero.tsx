import { ShieldCheck } from 'lucide-react';

export default function Hero() {
  return (
    <section className="relative min-h-[870px] flex items-center overflow-hidden pt-24">
      <div className="absolute inset-0 z-0">
        <div className="absolute inset-0 bg-gradient-to-r from-surface via-surface/95 to-surface/40 z-10"></div>
        <img
          alt="Real Estate Background"
          className="w-full h-full object-cover"
          src="https://lh3.googleusercontent.com/aida-public/AB6AXuBtJgn42Ye283Op6yHp2OmfuP78qir_AQhEFnD72GYE2X0DuVJEKZYCf67i0MTkdx57ZECsZGx25rBt2qr2rU8PS0baQ8ypesqHmON47CjQFR-giPWK3R-Kvhc_odfXfKX28TjyvIGLxCUW6glPL3S5iDWiZSVq5dVjLmhJOXoduyO3qvskjGvbvcwWq9Aymy_jVjz2fzAb04ZU9PK9wkMOdhZ0eK2mO4wr8Zm9qMhZ35BwRx_AsJfck-swSF-t8AVtxXo1G-H43JM"
        />
      </div>
      <div className="relative z-20 max-w-7xl mx-auto px-6 w-full">
        <div className="max-w-3xl">
          <span className="inline-block px-3 py-1 bg-primary/10 text-primary font-label text-xs font-bold tracking-[0.2em] uppercase rounded mb-6">
            Ohio & Kentucky Asset Recovery Specialists
          </span>
          <h1 className="text-5xl md:text-7xl font-headline font-bold tracking-tight text-on-surface mb-8 leading-[1.1]">
            The County may be <span className="text-primary italic">holding funds</span> that belong to you.
          </h1>
          <p className="text-xl text-secondary leading-relaxed mb-12 max-w-2xl font-body">
            No upfront fees. No complex procedures. We audit your case and mandate an attorney to claim your foreclosure surplus.
          </p>
          <div className="flex flex-col sm:flex-row gap-4">
            <a
              className="bg-primary text-on-primary px-8 py-5 rounded-xl font-headline font-bold text-lg hover:bg-primary-container transition-all text-center shadow-lg shadow-primary/10"
              href="#intake"
            >
              Check My Eligibility (Free)
            </a>
            <div className="flex items-center gap-3 px-6 text-on-surface-variant font-label font-medium">
              <ShieldCheck className="w-6 h-6 text-primary" />
              100% Secure Process
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
