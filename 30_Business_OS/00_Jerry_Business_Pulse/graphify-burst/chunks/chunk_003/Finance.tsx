import React, { useState } from 'react';
import { motion } from 'motion/react';
import { 
  Building2, 
  ArrowRightLeft, 
  Wallet, 
  Calculator, 
  Receipt,
  ArrowUpRight,
  ArrowDownRight,
  RefreshCcw,
  CheckCircle2,
  Clock
} from 'lucide-react';
import { cn } from '../lib/utils';

const ledgerData = [
  { id: '1', date: '2026-05-18', caseId: 'A 2403702', type: 'inflow', amount: 8450.00, status: 'completed' },
  { id: '2', date: '2026-05-16', caseId: 'B 1984221', type: 'outflow', amount: 1500.00, status: 'completed', desc: 'Avocat Probate' },
  { id: '3', date: '2026-05-15', caseId: 'C 8829103', type: 'outflow', amount: 150.00, status: 'completed', desc: 'Notaire Mobile' },
  { id: '4', date: '2026-05-12', caseId: 'A 2401198', type: 'inflow', amount: 12200.00, status: 'pending' },
  { id: '5', date: '2026-05-10', caseId: 'D 3302911', type: 'outflow', amount: 3200.00, status: 'pending', desc: 'Acompte 10% (Rachat)' },
];

export function Finance() {
  const [calcAmount, setCalcAmount] = useState<string>('29531');
  const [calcModule, setCalcModule] = useState<'cession' | 'rachat'>('cession');
  const [calcRate, setCalcRate] = useState<string>('30');
  const [hasProbate, setHasProbate] = useState(false);

  const amount = parseFloat(calcAmount) || 0;
  const rate = parseFloat(calcRate) || 0;
  
  const grossCommission = amount * (rate / 100);
  const notaryFee = 150;
  const probateFee = hasProbate ? 1500 : 0;
  const totalFees = notaryFee + probateFee;
  const netProfit = grossCommission - totalFees;
  const downPayment = calcModule === 'rachat' ? amount * 0.10 : 0;

  return (
    <motion.div 
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
      className="p-8 max-w-7xl mx-auto space-y-8"
    >
      <header className="flex justify-between items-end">
        <div>
          <h1 className="text-2xl font-display font-semibold tracking-tight text-stone-100">Le Coffre-Fort</h1>
          <p className="text-sm text-stone-500 mt-1">Pilotage des flux de trésorerie et allocation du capital.</p>
        </div>
      </header>

      {/* Top Widgets: Liquidity Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="p-5 rounded-xl bg-stone-900 border border-stone-800 flex flex-col gap-4 relative overflow-hidden group">
          <div className="w-10 h-10 rounded-lg bg-stone-800 flex items-center justify-center border border-stone-700">
            <Building2 className="w-5 h-5 text-emerald-500" />
          </div>
          <div>
            <h4 className="text-stone-400 text-sm font-medium mb-1">The War Chest</h4>
            <div className="text-2xl font-display font-semibold text-stone-100">$84,500.00</div>
            <p className="text-xs text-stone-500 mt-1">Liquidités pures disponibles</p>
          </div>
          <div className="absolute -bottom-6 -right-6 w-24 h-24 bg-emerald-500/5 blur-2xl rounded-full" />
        </div>
        
        <div className="p-5 rounded-xl bg-stone-900 border border-stone-800 flex flex-col gap-4 relative overflow-hidden">
          <div className="w-10 h-10 rounded-lg bg-stone-800 flex items-center justify-center border border-stone-700">
            <ArrowRightLeft className="w-5 h-5 text-stone-400" />
          </div>
          <div>
            <h4 className="text-stone-400 text-sm font-medium mb-1">Capital Déployé</h4>
            <div className="text-2xl font-display font-semibold text-stone-100">$18,250.00</div>
            <p className="text-xs text-stone-500 mt-1">Frais & acomptes bloqués</p>
          </div>
        </div>

        <div className="p-5 rounded-xl bg-stone-900 border border-stone-800 flex flex-col gap-4 relative overflow-hidden">
          <div className="w-10 h-10 rounded-lg bg-stone-800 flex items-center justify-center border border-stone-700">
            <RefreshCcw className="w-5 h-5 text-emerald-400" />
          </div>
          <div>
            <h4 className="text-stone-400 text-sm font-medium mb-1">Inflows (En transit)</h4>
            <div className="text-2xl font-display font-semibold text-stone-100">$34,800.00</div>
            <p className="text-xs text-stone-500 mt-1">Orders Signed, attente chèques</p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Deal Calculator */}
        <div className="col-span-1 rounded-xl bg-stone-900 border border-stone-800 flex flex-col h-full">
          <div className="p-5 border-b border-stone-800">
            <h3 className="text-sm font-display font-semibold text-stone-100 flex items-center gap-2">
              <Calculator className="w-4 h-4 text-emerald-500" />
              Simulateur de Marge
            </h3>
            <p className="text-xs text-stone-500 mt-1">Évaluation de rentabilité Alpha Lead</p>
          </div>
          <div className="p-5 flex-1 flex flex-col gap-5">
            <div className="space-y-4">
              <div>
                <label className="text-xs font-medium text-stone-400 mb-1.5 block">Excédent Brut ($)</label>
                <div className="relative">
                  <span className="absolute left-3 top-1/2 -translate-y-1/2 text-stone-500">$</span>
                  <input 
                    type="number" 
                    value={calcAmount} 
                    onChange={e => setCalcAmount(e.target.value)}
                    className="w-full bg-stone-950 border border-stone-800 rounded-md py-2 pl-7 pr-3 text-sm text-stone-200 outline-none focus:border-emerald-500/50 focus:ring-1 focus:ring-emerald-500/50 transition-all font-mono"
                  />
                </div>
              </div>
              
              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="text-xs font-medium text-stone-400 mb-1.5 block">Taux Négocié (%)</label>
                  <div className="relative">
                    <input 
                      type="number" 
                      value={calcRate} 
                      onChange={e => setCalcRate(e.target.value)}
                      className="w-full bg-stone-950 border border-stone-800 rounded-md py-2 px-3 text-sm text-stone-200 outline-none focus:border-emerald-500/50 focus:ring-1 focus:ring-emerald-500/50 transition-all font-mono"
                    />
                    <span className="absolute right-3 top-1/2 -translate-y-1/2 text-stone-500">%</span>
                  </div>
                </div>
                <div>
                  <label className="text-xs font-medium text-stone-400 mb-1.5 block">Module</label>
                  <select 
                    value={calcModule} 
                    onChange={e => setCalcModule(e.target.value as any)}
                    className="w-full bg-stone-950 border border-stone-800 rounded-md py-2 px-3 text-sm text-stone-200 outline-none focus:border-emerald-500/50 transition-all appearance-none"
                  >
                    <option value="cession">1: Cession</option>
                    <option value="rachat">3: Rachat Structuré</option>
                  </select>
                </div>
              </div>

              <div className="pt-2">
                <label className="flex items-center gap-2 cursor-pointer group">
                  <div className="relative flex items-center justify-center">
                    <input 
                      type="checkbox" 
                      checked={hasProbate} 
                      onChange={e => setHasProbate(e.target.checked)}
                      className="peer appearance-none w-4 h-4 border border-stone-700 rounded bg-stone-950 checked:bg-emerald-500 checked:border-emerald-500 transition-colors"
                    />
                    <CheckCircle2 className="w-3 h-3 text-stone-950 absolute opacity-0 peer-checked:opacity-100 pointer-events-none" strokeWidth={3} />
                  </div>
                  <span className="text-xs text-stone-400 group-hover:text-stone-300 transition-colors">Nécessite Probate (+$1,500)</span>
                </label>
              </div>
            </div>

            <div className="mt-auto border-t border-stone-800 pt-5 space-y-3">
              <div className="flex justify-between items-center text-sm">
                <span className="text-stone-400">Commission Brute</span>
                <span className="font-mono text-stone-300">${grossCommission.toLocaleString('en-US', {minimumFractionDigits: 2})}</span>
              </div>
              <div className="flex justify-between items-center text-sm">
                <span className="text-stone-500">Frais Estimés (Notaire + Avocat)</span>
                <span className="font-mono text-stone-500">-${totalFees.toLocaleString('en-US', {minimumFractionDigits: 2})}</span>
              </div>
              
              {calcModule === 'rachat' && (
                <div className="flex justify-between items-center text-sm p-2 rounded bg-amber-500/5 border border-amber-500/10">
                  <span className="text-amber-500/80">Acompte Requis (10%)</span>
                  <span className="font-mono text-amber-500/90">${downPayment.toLocaleString('en-US', {minimumFractionDigits: 2})}</span>
                </div>
              )}
              
              <div className="flex justify-between items-center pt-2 border-t border-stone-800/50">
                <span className="text-sm font-medium text-stone-200">Net Profit Alykaly</span>
                <span className="font-mono font-semibold text-emerald-400">${Math.max(0, netProfit).toLocaleString('en-US', {minimumFractionDigits: 2})}</span>
              </div>
            </div>
          </div>
        </div>

        {/* The Ledger */}
        <div className="col-span-1 lg:col-span-2 rounded-xl bg-stone-900 border border-stone-800 overflow-hidden flex flex-col">
          <div className="p-5 border-b border-stone-800 flex justify-between items-center">
            <h3 className="text-sm font-display font-semibold text-stone-100 flex items-center gap-2">
              <Receipt className="w-4 h-4 text-stone-400" />
              Le Grand Livre
            </h3>
            <button className="text-xs font-medium text-stone-400 hover:text-stone-300 transition-colors flex items-center gap-1">
              Exporter <ArrowUpRight className="w-3 h-3" />
            </button>
          </div>
          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm">
              <thead className="bg-stone-950/50 text-xs text-stone-500 uppercase tracking-wider">
                <tr>
                  <th className="px-5 py-3 font-medium">Date</th>
                  <th className="px-5 py-3 font-medium">Case ID</th>
                  <th className="px-5 py-3 font-medium">Type</th>
                  <th className="px-5 py-3 font-medium text-right">Montant</th>
                  <th className="px-5 py-3 font-medium text-right">Statut</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-stone-800/50">
                {ledgerData.map((tx) => (
                  <tr key={tx.id} className="hover:bg-stone-800/20 transition-colors group">
                    <td className="px-5 py-4 whitespace-nowrap text-stone-400 font-mono text-xs">{tx.date}</td>
                    <td className="px-5 py-4 whitespace-nowrap text-stone-300 font-medium">{tx.caseId}</td>
                    <td className="px-5 py-4 whitespace-nowrap">
                      {tx.type === 'inflow' ? (
                        <div className="flex items-center gap-1.5 text-emerald-400/90 text-xs font-medium">
                          <ArrowDownRight className="w-3.5 h-3.5" /> Commission
                        </div>
                      ) : (
                        <div className="flex items-center gap-1.5 text-stone-500 text-xs font-medium">
                          <ArrowUpRight className="w-3.5 h-3.5" /> Sortie {tx.desc && <span className="opacity-75">({tx.desc})</span>}
                        </div>
                      )}
                    </td>
                    <td className="px-5 py-4 whitespace-nowrap text-right font-mono">
                      <span className={cn(
                        tx.type === 'inflow' ? "text-emerald-400 group-hover:drop-shadow-[0_0_8px_rgba(52,211,153,0.3)] transition-all" : "text-stone-400"
                      )}>
                        {tx.type === 'inflow' ? '+' : '-'}${tx.amount.toLocaleString('en-US', {minimumFractionDigits: 2})}
                      </span>
                    </td>
                    <td className="px-5 py-4 whitespace-nowrap text-right">
                      {tx.status === 'completed' ? (
                        <span className="inline-flex items-center gap-1 text-xs text-stone-500">
                          <CheckCircle2 className="w-3.5 h-3.5" /> Clôturé
                        </span>
                      ) : (
                        <span className="inline-flex items-center gap-1 text-xs text-amber-500/80">
                          <Clock className="w-3.5 h-3.5" /> En attente
                        </span>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </motion.div>
  );
}
