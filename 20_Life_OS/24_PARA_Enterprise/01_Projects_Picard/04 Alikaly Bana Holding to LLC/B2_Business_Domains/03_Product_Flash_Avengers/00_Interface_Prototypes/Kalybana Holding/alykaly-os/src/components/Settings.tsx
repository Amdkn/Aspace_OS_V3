import React from 'react';
import { motion } from 'motion/react';
import { 
  Settings as SettingsIcon, 
  Key, 
  SlidersHorizontal,
  EyeOff,
  Save,
  ShieldCheck
} from 'lucide-react';
import { cn } from '../lib/utils';

export function Settings() {
  return (
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="p-8 max-w-4xl mx-auto space-y-8"
    >
      <header className="flex justify-between items-end">
        <div>
          <h1 className="text-2xl font-display font-semibold tracking-tight text-stone-100 flex items-center gap-3">
            Settings <SettingsIcon className="w-6 h-6 text-stone-500" />
          </h1>
          <p className="text-sm text-stone-500 mt-1">Configuration globale et constantes de la Holding.</p>
        </div>
        <button className="bg-emerald-500 hover:bg-emerald-400 text-stone-950 font-semibold px-4 py-2 rounded-lg text-sm transition-colors flex items-center gap-2">
          <Save className="w-4 h-4" /> Save Changes
        </button>
      </header>

      <div className="space-y-6">
        
        {/* Component B: Business Logic Variables */}
        <div className="bg-stone-900 border border-stone-800 rounded-xl overflow-hidden">
          <div className="p-4 border-b border-stone-800 bg-stone-900/50 flex items-center gap-2">
            <SlidersHorizontal className="w-4 h-4 text-emerald-500" />
            <h3 className="text-sm font-display font-semibold text-stone-100">Variables de la Holding (Business Logic)</h3>
          </div>
          <div className="p-6 grid grid-cols-1 md:grid-cols-2 gap-6">
            
            <div className="space-y-1">
              <label className="text-xs font-medium text-stone-400 block">Taux Acompte Standard (Module 3)</label>
              <div className="relative">
                <input type="number" defaultValue={10} className="w-full bg-stone-950 border border-stone-800 rounded-md py-2 px-3 text-sm text-stone-200 outline-none focus:border-emerald-500/50 font-mono" />
                <span className="absolute right-3 top-1/2 -translate-y-1/2 text-stone-500 text-sm">%</span>
              </div>
              <p className="text-[10px] text-stone-600 mt-1">Impacte direct. le "War Chest" sur la page Finance.</p>
            </div>

            <div className="space-y-1">
              <label className="text-xs font-medium text-stone-400 block">Taux de Commission (Module 1)</label>
              <div className="relative">
                <input type="number" defaultValue={30} className="w-full bg-stone-950 border border-stone-800 rounded-md py-2 px-3 text-sm text-stone-200 outline-none focus:border-emerald-500/50 font-mono" />
                <span className="absolute right-3 top-1/2 -translate-y-1/2 text-stone-500 text-sm">%</span>
              </div>
            </div>

            <div className="space-y-1">
              <label className="text-xs font-medium text-stone-400 block">Provision Frais Notaire Mobile</label>
              <div className="relative">
                <span className="absolute left-3 top-1/2 -translate-y-1/2 text-stone-500 text-sm">$</span>
                <input type="number" defaultValue={150} className="w-full bg-stone-950 border border-stone-800 rounded-md py-2 pl-7 pr-3 text-sm text-stone-200 outline-none focus:border-emerald-500/50 font-mono" />
              </div>
            </div>
            
            <div className="space-y-1">
              <label className="text-xs font-medium text-stone-400 block">Provision Frais Avocat (Si Probate)</label>
              <div className="relative">
                <span className="absolute left-3 top-1/2 -translate-y-1/2 text-stone-500 text-sm">$</span>
                <input type="number" defaultValue={1500} className="w-full bg-stone-950 border border-stone-800 rounded-md py-2 pl-7 pr-3 text-sm text-stone-200 outline-none focus:border-emerald-500/50 font-mono" />
              </div>
            </div>

          </div>
        </div>

        {/* Component A: API Vault */}
        <div className="bg-stone-900 border border-stone-800 rounded-xl overflow-hidden">
          <div className="p-4 border-b border-stone-800 bg-stone-900/50 flex items-center justify-between">
            <div className="flex items-center gap-2">
              <Key className="w-4 h-4 text-stone-400" />
              <h3 className="text-sm font-display font-semibold text-stone-100">API Vault</h3>
            </div>
            <span className="flex items-center gap-1 text-[10px] font-medium px-2 py-1 bg-stone-950 border border-stone-800 text-stone-500 rounded uppercase tracking-wider">
              <ShieldCheck className="w-3 h-3 text-emerald-500" /> Encrypted at rest
            </span>
          </div>
          <div className="p-6 space-y-4">
            
            <div className="grid grid-cols-[200px_1fr] items-center gap-4">
              <label className="text-sm font-medium text-stone-300">TruePeopleSearch API</label>
              <div className="relative">
                <input type="password" value="sk_test_tps_99182283910" readOnly className="w-full bg-stone-950 border border-stone-800 rounded-md py-2 pl-3 pr-10 text-sm text-stone-500 font-mono outline-none" />
                <button className="absolute right-3 top-1/2 -translate-y-1/2 text-stone-600 hover:text-stone-400"><EyeOff className="w-4 h-4" /></button>
              </div>
            </div>

            <div className="grid grid-cols-[200px_1fr] items-center gap-4">
              <label className="text-sm font-medium text-stone-300">Stripe Secret Key</label>
              <div className="relative">
                <input type="password" value="sk_test_51Nx..." readOnly className="w-full bg-stone-950 border border-stone-800 rounded-md py-2 pl-3 pr-10 text-sm text-stone-500 font-mono outline-none" />
                <button className="absolute right-3 top-1/2 -translate-y-1/2 text-stone-600 hover:text-stone-400"><EyeOff className="w-4 h-4" /></button>
              </div>
            </div>

            <div className="grid grid-cols-[200px_1fr] items-center gap-4">
              <label className="text-sm font-medium text-stone-300">n8n Webhook Token</label>
              <div className="relative">
                <input type="password" value="n8n_wh_3321ojf..." readOnly className="w-full bg-stone-950 border border-stone-800 rounded-md py-2 pl-3 pr-10 text-sm text-stone-500 font-mono outline-none" />
                <button className="absolute right-3 top-1/2 -translate-y-1/2 text-stone-600 hover:text-stone-400"><EyeOff className="w-4 h-4" /></button>
              </div>
            </div>

            <div className="grid grid-cols-[200px_1fr] items-center gap-4">
              <label className="text-sm font-medium text-stone-300">DocuSign Integrator Key</label>
              <div className="relative">
                <input type="password" value="" placeholder="Enter Integrator Key" className="w-full bg-stone-950 border border-stone-800 rounded-md py-2 pl-3 pr-10 text-sm text-stone-300 font-mono outline-none focus:border-stone-600 focus:bg-stone-900" />
              </div>
            </div>

          </div>
        </div>

      </div>
    </motion.div>
  );
}
