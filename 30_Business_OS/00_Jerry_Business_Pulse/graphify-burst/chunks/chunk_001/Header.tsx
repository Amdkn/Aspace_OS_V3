import { Menu } from 'lucide-react';
import Link from 'next/link';

export default function Header() {
  return (
    <header className="fixed top-0 w-full z-50 glass-nav border-b border-on-surface/5">
      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
        <Link href="/bana" className="text-xl font-bold tracking-tighter text-on-surface font-headline">
          Ali Real Estate Bana LLC
        </Link>
        <nav className="hidden md:flex items-center gap-8">
          <Link
            className="text-secondary hover:text-primary transition-colors font-label font-semibold text-xs tracking-widest uppercase"
            href="#process"
          >
            How It Works
          </Link>
          <Link
            className="text-secondary hover:text-primary transition-colors font-label font-semibold text-xs tracking-widest uppercase"
            href="#"
          >
            FAQ
          </Link>
          <Link
            className="bg-primary text-on-primary px-6 py-2.5 rounded-xl font-headline font-semibold text-sm hover:bg-primary-container transition-all active:scale-95"
            href="#intake"
          >
            Check Eligibility
          </Link>
        </nav>
        <button className="md:hidden text-on-surface">
          <Menu className="w-6 h-6" />
        </button>
      </div>
    </header>
  );
}
