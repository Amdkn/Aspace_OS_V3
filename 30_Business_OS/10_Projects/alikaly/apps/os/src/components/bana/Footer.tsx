export default function Footer() {
  return (
    <footer className="bg-surface border-t border-on-surface/10 py-16">
      <div className="max-w-7xl mx-auto px-6">
        <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-12">
          <div className="space-y-4">
            <div className="font-bold text-on-surface text-lg font-headline">Ali Real Estate Bana LLC</div>
            <p className="font-label text-sm text-secondary leading-relaxed max-w-sm">
              © 2024 Ali Real Estate Bana LLC. Asset Recovery Specialists in Ohio & Kentucky. Specialized in surplus fund recovery and judicial sale auditing.
            </p>
          </div>
          <nav className="flex flex-wrap gap-x-8 gap-y-4">
            <a className="font-label text-sm text-secondary hover:text-primary transition-colors" href="#">Privacy Policy</a>
            <a className="font-label text-sm text-secondary hover:text-primary transition-colors" href="#">Terms of Service</a>
            <a className="font-label text-sm text-secondary hover:text-primary transition-colors" href="#">Contact Us</a>
            <a className="font-label text-sm text-secondary hover:text-primary transition-colors" href="#">Affiliations</a>
          </nav>
        </div>
        <div className="mt-16 pt-8 border-t border-on-surface/5 flex flex-col md:flex-row justify-between items-center gap-6">
          <div className="flex items-center gap-6 opacity-40 grayscale">
            {/* Placeholders for logos */}
            <div className="h-8 w-24 bg-on-surface/20 rounded flex items-center justify-center text-[10px] font-bold">LEGAL SHIELD</div>
            <div className="h-8 w-24 bg-on-surface/20 rounded flex items-center justify-center text-[10px] font-bold">FAIR HOUSING</div>
          </div>
          <div className="text-xs font-label text-secondary/40">
            NMLS: #RE-44092-OH | Firm ID: KY-992031
          </div>
        </div>
      </div>
    </footer>
  );
}
