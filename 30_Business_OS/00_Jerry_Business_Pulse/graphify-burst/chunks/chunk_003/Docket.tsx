import React, { useState } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { 
  Search, 
  Filter, 
  ExternalLink, 
  Star, 
  UserPlus, 
  Save, 
  X,
  ChevronRight,
  AlertCircle
} from 'lucide-react';
import { cn } from '../lib/utils';

const mockLeads = [
  { id: '1', caseNumber: 'A 2403702', defendant: 'Estate of Robert Chase', amount: 29531.00, priority: 'Généalogie', status: 'new', confidence: 0 },
  { id: '2', caseNumber: 'B 1984221', defendant: 'Apex Industrial LLC', amount: 14200.50, priority: 'B2B', status: 'ready', confidence: 5 },
  { id: '3', caseNumber: 'C 8829103', defendant: 'Sarah Jenkins', amount: 8450.00, priority: 'Expulsion', status: 'tracking', confidence: 2 },
  { id: '4', caseNumber: 'A 2401198', defendant: 'Michael T. Vance', amount: 41200.00, priority: 'Généalogie', status: 'ready', confidence: 4 },
  { id: '5', caseNumber: 'D 3302911', defendant: 'Horizon Realty Trust', amount: 112000.00, priority: 'B2B', status: 'new', confidence: 0 },
];

export function Docket() {
  const [selectedLead, setSelectedLead] = useState<typeof mockLeads[0] | null>(null);

  return (
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="flex h-full"
    >
      {/* Main Data Grid */}
      <div className="flex-1 p-8 space-y-6 flex flex-col h-full overflow-hidden">
        <header className="flex justify-between items-end shrink-0">
          <div>
            <h1 className="text-2xl font-display font-semibold tracking-tight text-stone-100">Le Laboratoire OSINT</h1>
            <p className="text-sm text-stone-500 mt-1">Matrice d'investigation et purification des Alpha Leads.</p>
          </div>
          <div className="flex items-center gap-3">
            <div className="relative">
              <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-stone-500" />
              <input 
                type="text" 
                placeholder="Case ID, Nom..."
                className="bg-stone-900 border border-stone-800 rounded-lg py-2 pl-9 pr-4 text-sm text-stone-300 focus:border-emerald-500/50 outline-none w-64"
              />
            </div>
            <button className="p-2 bg-stone-900 border border-stone-800 rounded-lg text-stone-400 hover:text-stone-300 transition-colors">
              <Filter className="w-4 h-4" />
            </button>
          </div>
        </header>

        <div className="flex-1 bg-stone-900 border border-stone-800 rounded-xl overflow-hidden flex flex-col">
          <div className="overflow-x-auto flex-1">
            <table className="w-full text-left text-sm whitespace-nowrap">
              <thead className="bg-stone-950/50 text-xs text-stone-500 uppercase tracking-wider sticky top-0 z-10 border-b border-stone-800">
                <tr>
                  <th className="px-5 py-4 font-medium">Case Number</th>
                  <th className="px-5 py-4 font-medium">Défendeur</th>
                  <th className="px-5 py-4 font-medium text-right">Montant</th>
                  <th className="px-5 py-4 font-medium">Priorité</th>
                  <th className="px-5 py-4 font-medium">Statut OSINT</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-stone-800/50">
                {mockLeads.map((lead) => (
                  <tr 
                    key={lead.id} 
                    onClick={() => setSelectedLead(lead)}
                    className={cn(
                      "hover:bg-stone-800/40 transition-colors cursor-pointer group",
                      selectedLead?.id === lead.id && "bg-stone-800/60"
                    )}
                  >
                    <td className="px-5 py-4 text-stone-300 font-mono text-xs">{lead.caseNumber}</td>
                    <td className="px-5 py-4 text-stone-200 font-medium">{lead.defendant}</td>
                    <td className="px-5 py-4 text-right font-mono text-stone-300 font-medium">
                      ${lead.amount.toLocaleString('en-US', {minimumFractionDigits: 2})}
                    </td>
                    <td className="px-5 py-4">
                      <span className={cn(
                        "text-xs px-2 py-1 rounded-md font-medium border",
                        lead.priority === 'Généalogie' ? "bg-indigo-500/10 text-indigo-400 border-indigo-500/20" :
                        lead.priority === 'B2B' ? "bg-amber-500/10 text-amber-400 border-amber-500/20" :
                        "bg-rose-500/10 text-rose-400 border-rose-500/20"
                      )}>
                        {lead.priority}
                      </span>
                    </td>
                    <td className="px-5 py-4">
                      <div className="flex items-center gap-2">
                        <div className={cn(
                          "w-2 h-2 rounded-full",
                          lead.status === 'new' ? "bg-stone-600" :
                          lead.status === 'tracking' ? "bg-amber-500 animate-pulse" :
                          "bg-emerald-500 shadow-[0_0_8px_rgba(16,185,129,0.5)]"
                        )} />
                        <span className="text-xs text-stone-400 capitalize">
                          {lead.status === 'new' ? 'New Lead' : lead.status === 'tracking' ? 'Pivot Requis' : 'Ready to Call'}
                        </span>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      {/* Focus Panel (Right Slide-out) */}
      <AnimatePresence>
        {selectedLead && (
          <motion.div
            initial={{ width: 0, opacity: 0 }}
            animate={{ width: 400, opacity: 1 }}
            exit={{ width: 0, opacity: 0 }}
            className="bg-stone-900 border-l border-stone-800 h-full shrink-0 flex flex-col"
          >
            <div className="p-5 border-b border-stone-800 flex justify-between items-start">
              <div>
                <h2 className="text-lg font-display font-semibold text-stone-100">{selectedLead.defendant}</h2>
                <div className="flex items-center gap-2 mt-1">
                  <span className="text-xs font-mono text-stone-500">{selectedLead.caseNumber}</span>
                  <span className="text-stone-700">•</span>
                  <span className="text-xs font-mono text-emerald-400 font-medium">${selectedLead.amount.toLocaleString()}</span>
                </div>
              </div>
              <button 
                onClick={() => setSelectedLead(null)}
                className="p-1.5 hover:bg-stone-800 rounded-md text-stone-500 transition-colors"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <div className="p-5 flex-1 overflow-y-auto space-y-6">
              {/* Deep Links */}
              <div>
                <h3 className="text-xs font-semibold text-stone-500 tracking-wider uppercase mb-3">Deep Links</h3>
                <div className="grid grid-cols-2 gap-2">
                  <a href="#" className="flex justify-between items-center p-2 rounded-lg bg-stone-950 border border-stone-800 hover:border-stone-700 text-xs text-stone-300 transition-colors group">
                    TruePeopleSearch
                    <ExternalLink className="w-3 h-3 text-stone-600 group-hover:text-stone-400" />
                  </a>
                  <a href="#" className="flex justify-between items-center p-2 rounded-lg bg-stone-950 border border-stone-800 hover:border-stone-700 text-xs text-stone-300 transition-colors group">
                    Microbilt
                    <ExternalLink className="w-3 h-3 text-stone-600 group-hover:text-stone-400" />
                  </a>
                  <a href="#" className="col-span-2 flex justify-between items-center p-2 rounded-lg bg-stone-950 border border-stone-800 hover:border-stone-700 text-xs text-stone-300 transition-colors group">
                    County Auditor (Property Records)
                    <ExternalLink className="w-3 h-3 text-stone-600 group-hover:text-stone-400" />
                  </a>
                </div>
              </div>

              {/* Zone d'Enrichissement */}
              <div>
                <h3 className="text-xs font-semibold text-stone-500 tracking-wider uppercase mb-3 flex justify-between items-center">
                  Enrichissement (Vault)
                  <button className="text-emerald-500 hover:text-emerald-400 transition-colors"><UserPlus className="w-3.5 h-3.5" /></button>
                </h3>
                <div className="space-y-3">
                  <div className="space-y-1">
                    <label className="text-xs text-stone-400">Mobile Principal (SMS)</label>
                    <input type="text" placeholder="(555) 123-4567" defaultValue={selectedLead.confidence > 2 ? "(513) 489-0021" : ""} className="w-full bg-stone-950 border border-stone-800 rounded-md py-1.5 px-3 text-sm text-stone-200 outline-none focus:border-emerald-500/50" />
                  </div>
                  <div className="space-y-1">
                    <label className="text-xs text-stone-400">Relatives / Héritiers Probables</label>
                    <textarea rows={2} placeholder="Ex: Mary Chase (Fille)..." className="w-full bg-stone-950 border border-stone-800 rounded-md py-1.5 px-3 text-sm text-stone-200 outline-none focus:border-emerald-500/50 resize-none font-mono text-xs"></textarea>
                  </div>
                  <div className="space-y-1">
                    <label className="text-xs text-stone-400">Obituary Notes</label>
                    <input type="text" placeholder="Lien vers Legacy.com..." className="w-full bg-stone-950 border border-stone-800 rounded-md py-1.5 px-3 text-sm text-stone-200 outline-none focus:border-emerald-500/50" />
                  </div>
                </div>
              </div>

              {/* Confidence Score */}
              <div className="p-4 rounded-lg bg-stone-950/50 border border-stone-800">
                <h3 className="text-xs font-medium text-stone-400 mb-2 flex flex-col">
                  Confidence Score
                  <span className="text-[10px] text-stone-600">Certitude de l'identité avant outreach</span>
                </h3>
                <div className="flex gap-1.5">
                  {[1, 2, 3, 4, 5].map((star) => (
                    <button key={star} className="p-1 hover:scale-110 transition-transform">
                      <Star className={cn("w-5 h-5", star <= selectedLead.confidence ? "fill-emerald-500 text-emerald-500" : "text-stone-700")} />
                    </button>
                  ))}
                </div>
              </div>
            </div>

            <div className="p-4 border-t border-stone-800 bg-stone-900">
              <button className="w-full py-2 bg-emerald-500 hover:bg-emerald-400 text-stone-950 font-semibold rounded-md text-sm transition-colors flex items-center justify-center gap-2">
                <Save className="w-4 h-4" /> Save & Push to Nurture
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
}
