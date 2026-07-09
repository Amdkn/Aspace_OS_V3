import { MapPin, Phone, Mail, AlertTriangle } from "lucide-react";

export function Footer() {
  return (
    <footer id="contact" className="bg-background">
      <div className="max-w-[1400px] mx-auto px-6 lg:px-10 pt-16 pb-10">
        <div className="grid lg:grid-cols-12 gap-12 pb-12 border-b border-slate-800/70">
          {/* Brand */}
          <div className="lg:col-span-5">
            <div className="flex items-center gap-3 mb-5">
              <div className="w-10 h-10 border border-slate-700 rounded-sm flex items-center justify-center bg-gradient-to-br from-slate-900 to-slate-950">
                <span className="font-display font-bold text-emerald-500 text-lg leading-none">A</span>
              </div>
              <div>
                <div className="font-display font-semibold tracking-[0.08em] text-white text-[15px] uppercase">Alykaly Holding</div>
                <div className="text-[10px] uppercase tracking-[0.22em] text-slate-500 font-mono">Real Estate &middot; Legal Audits</div>
              </div>
            </div>
            <p className="text-[13.5px] text-slate-400 leading-relaxed max-w-md">
              Cabinet d'audit juridique privé dédié à la récupération des fonds excédentaires post-saisie. Opérations cadrées par les statuts ORC §2329.44 et ORC §5721.20 de l'Ohio.
            </p>

            <div className="mt-7 space-y-2.5 text-[12.5px] font-mono text-slate-400">
              <div className="flex items-center gap-3">
                <MapPin size={13} className="text-emerald-500/80" />
                <span>312 Walnut St &middot; Cincinnati, OH 45202</span>
              </div>
              <div className="flex items-center gap-3">
                <Phone size={13} className="text-emerald-500/80" />
                <span>+1 (513) 555&middot;0101</span>
              </div>
              <div className="flex items-center gap-3">
                <Mail size={13} className="text-emerald-500/80" />
                <span>audit@alykaly-holding.com</span>
              </div>
            </div>
          </div>

          {/* Links */}
          <div className="lg:col-span-2">
            <div className="text-[10.5px] uppercase tracking-[0.22em] text-slate-500 font-mono mb-4">Cabinet</div>
            <ul className="space-y-2.5 text-[13px] text-slate-400">
              <li><a href="#" className="hover:text-cream">À propos</a></li>
              <li><a href="#" className="hover:text-cream">Équipe juridique</a></li>
              <li><a href="#" className="hover:text-cream">Bilan public</a></li>
              <li><a href="#" className="hover:text-cream">Presse</a></li>
            </ul>
          </div>

          <div className="lg:col-span-2">
            <div className="text-[10.5px] uppercase tracking-[0.22em] text-slate-500 font-mono mb-4">Expertises</div>
            <ul className="space-y-2.5 text-[13px] text-slate-400">
              <li><a href="#" className="hover:text-cream">Foreclosure Surplus</a></li>
              <li><a href="#" className="hover:text-cream">Tax Lien Overages</a></li>
              <li><a href="#" className="hover:text-cream">Ghost Probate</a></li>
              <li><a href="#" className="hover:text-cream">Unclaimed Property</a></li>
            </ul>
          </div>

          <div className="lg:col-span-3">
            <div className="text-[10.5px] uppercase tracking-[0.22em] text-slate-500 font-mono mb-4">Juridictions</div>
            <ul className="space-y-2.5 text-[13px] text-slate-400">
              <li className="flex items-center justify-between"><span>Hamilton County</span><span className="text-emerald-500 text-[11px] font-mono">ACTIF</span></li>
              <li className="flex items-center justify-between"><span>Butler County</span><span className="text-emerald-500 text-[11px] font-mono">ACTIF</span></li>
              <li className="flex items-center justify-between"><span>Warren County</span><span className="text-emerald-500 text-[11px] font-mono">ACTIF</span></li>
              <li className="flex items-center justify-between"><span>Franklin County</span><span className="text-slate-500 text-[11px] font-mono">Q3 2026</span></li>
            </ul>
          </div>
        </div>

        {/* Disclaimer */}
        <div className="py-8 border-b border-slate-800/70">
          <div className="flex items-start gap-4 max-w-4xl">
            <AlertTriangle size={16} className="text-amber-500/80 mt-0.5 flex-shrink-0" />
            <p className="text-[12px] text-slate-500 leading-relaxed font-mono">
              <span className="text-slate-300 uppercase tracking-[0.14em]">Disclaimer —</span> Alykaly Holding est un cabinet d'audit privé et n'est pas affilié à une agence gouvernementale, à l'Ohio Department of Commerce, au Hamilton County Clerk of Courts ni à aucun bureau du Treasurer. Les services juridiques sont rendus par des avocats indépendants licenciés au Barreau de l'Ohio. Les résultats passés ne préjugent pas des résultats futurs. La signature d'un mandat est requise avant toute démarche.
            </p>
          </div>
        </div>

        {/* Bottom strip */}
        <div className="pt-8 flex flex-col md:flex-row md:items-center md:justify-between gap-5 text-[11.5px] text-slate-500 font-mono uppercase tracking-[0.18em]">
          <div>© 2024–2026 Alykaly Holding LLC &middot; OH&middot;BL2024&middot;887401</div>
          <div className="flex items-center gap-5">
            <a href="#" className="hover:text-cream">Mentions légales</a>
            <a href="#" className="hover:text-cream">Confidentialité</a>
            <a href="#" className="hover:text-cream">Cookies</a>
            <a href="#" className="hover:text-cream">Plan du site</a>
          </div>
        </div>
      </div>
    </footer>
  );
}
