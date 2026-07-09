import { Menu } from 'lucide-react';

export default function Header() {
  return (
    <header className="fixed top-0 w-full z-50 glass-nav border-b border-on-surface/5">
      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
        <div className="text-xl font-bold tracking-tighter text-on-surface font-headline">
          Ali Real Estate Bana LLC
        </div>
        <nav className="hidden md:flex items-center gap-8">
          <a
            className="text-secondary hover:text-primary transition-colors font-label font-semibold text-xs tracking-widest uppercase"
            href="#"
          >
            How It Works
          </a>
          <a
            className="text-secondary hover:text-primary transition-colors font-label font-semibold text-xs tracking-widest uppercase"
            href="#"
          >
            FAQ
          </a>
          <a
            className="bg-primary text-on-primary px-6 py-2.5 rounded-xl font-headline font-semibold text-sm hover:bg-primary-container transition-all active:scale-95"
            href="#intake"
          >
            Check Eligibility
          </a>
        </nav>
        <button className="md:hidden text-on-surface">
          <Menu className="w-6 h-6" />
        </button>
      </div>
    </header>
  );
}
