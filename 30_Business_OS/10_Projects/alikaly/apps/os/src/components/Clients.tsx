import React, { useState } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { 
  Users2, 
  FileCheck, 
  Clock, 
  ShieldCheck, 
  UploadCloud, 
  MessageSquare,
  FileSignature,
  FileText,
  CheckCircle2,
  AlertCircle
} from 'lucide-react';
import { cn } from '../lib/utils';

const mockClients = [
  { id: '1', name: 'Estate of Robert Chase', module: 'cession', status: 'DocuSign Envoyé', lastActive: 'Il y a 2h' },
  { id: '2', name: 'Apex Industrial LLC', module: 'buyout', status: 'En attente Notaire', lastActive: 'Hier' },
  { id: '3', name: 'Michael T. Vance', module: 'cession', status: 'Dossier Complet', lastActive: 'Il y a 10m' },
];

export function Clients() {
  const [selectedClient, setSelectedClient] = useState<typeof mockClients[0]>(mockClients[2]);

  return (
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="flex h-full"
    >
      {/* Sidebar: Client List */}
      <div className="w-80 bg-stone-900 border-r border-stone-800 flex flex-col h-full shrink-0">
        <div className="p-5 border-b border-stone-800">
          <h2 className="text-lg font-display font-semibold text-stone-100 mb-3">Dossiers Actifs</h2>
          <div className="flex gap-2 text-xs">
            <button className="px-2 py-1 bg-stone-800 text-stone-300 rounded hover:bg-stone-700 transition-colors">Tous</button>
            <button className="px-2 py-1 border border-amber-500/20 text-amber-500/80 rounded hover:bg-amber-500/10 transition-colors">Attente Notaire</button>
          </div>
        </div>
        <div className="flex-1 overflow-y-auto p-3 space-y-2">
          {mockClients.map((client) => (
            <button
              key={client.id}
              onClick={() => setSelectedClient(client)}
              className={cn(
                "w-full text-left p-3 rounded-lg border transition-all",
                selectedClient.id === client.id 
                  ? "bg-stone-800/80 border-stone-700" 
                  : "bg-transparent border-transparent hover:bg-stone-800/40"
              )}
            >
              <div className="flex justify-between items-start mb-1">
                <span className="font-medium text-stone-200 text-sm truncate pr-2">{client.name}</span>
                <span className="text-[10px] text-stone-500 whitespace-nowrap">{client.lastActive}</span>
              </div>
              <div className="flex items-center gap-2">
                <span className={cn(
                  "text-[10px] px-1.5 py-0.5 rounded font-medium",
                  client.module === 'buyout' ? "bg-indigo-500/10 text-indigo-400" : "bg-emerald-500/10 text-emerald-400"
                )}>
                  {client.module === 'buyout' ? 'Module 3: Buyout' : 'Module 1: Cession'}
                </span>
                <span className="text-[10px] text-stone-400 truncate">{client.status}</span>
              </div>
            </button>
          ))}
        </div>
      </div>

      {/* Main Area: Medical Profile View */}
      <div className="flex-1 overflow-y-auto p-8 bg-stone-950">
        <div className="max-w-4xl mx-auto space-y-8">
          
          {/* Header */}
          <header className="flex justify-between items-start">
            <div>
              <div className="flex items-center gap-3 mb-2">
                <h1 className="text-2xl font-display font-semibold tracking-tight text-stone-100">{selectedClient.name}</h1>
                <span className={cn(
                  "text-xs px-2 py-1 rounded-md font-medium border",
                  selectedClient.module === 'buyout' ? "bg-indigo-500/10 text-indigo-400 border-indigo-500/20" : "bg-emerald-500/10 text-emerald-400 border-emerald-500/20"
                )}>
                  {selectedClient.module === 'buyout' ? 'Module 3: Rachat Structuré' : 'Module 1: Cession Simple'}
                </span>
              </div>
              <p className="text-sm text-stone-500">Case #A 2401198 • Hamilton County</p>
            </div>
            {selectedClient.module === 'buyout' && (
              <div className="flex items-center gap-2 bg-amber-500/10 border border-amber-500/20 text-amber-500/90 px-3 py-1.5 rounded-lg text-sm font-medium">
                <AlertCircle className="w-4 h-4" /> Acompte 10% requis sous 10j
              </div>
            )}
          </header>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            
            {/* Left Col: Compliance & Timeline */}
            <div className="col-span-1 space-y-6">
              
              {/* Compliance Checklist */}
              <div className="bg-stone-900 border border-stone-800 rounded-xl p-5">
                <h3 className="text-sm font-display font-semibold text-stone-100 flex items-center gap-2 mb-4">
                  <ShieldCheck className="w-4 h-4 text-emerald-500" />
                  Compliance Checklist
                </h3>
                <div className="space-y-3">
                  <label className="flex items-start gap-3 cursor-pointer group">
                    <div className="mt-0.5 relative flex items-center justify-center shrink-0">
                      <input type="checkbox" defaultChecked className="peer appearance-none w-4 h-4 border border-stone-700 rounded bg-stone-950 checked:bg-emerald-500 checked:border-emerald-500 transition-colors" />
                      <CheckCircle2 className="w-3 h-3 text-stone-950 absolute opacity-0 peer-checked:opacity-100 pointer-events-none" strokeWidth={3} />
                    </div>
                    <div>
                      <span className="text-sm font-medium text-stone-300 block">ID Valide (Permis/Passeport)</span>
                      <span className="text-xs text-stone-500">Document scanné présent</span>
                    </div>
                  </label>
                  <label className="flex items-start gap-3 cursor-pointer group">
                    <div className="mt-0.5 relative flex items-center justify-center shrink-0">
                      <input type="checkbox" defaultChecked className="peer appearance-none w-4 h-4 border border-stone-700 rounded bg-stone-950 checked:bg-emerald-500 checked:border-emerald-500 transition-colors" />
                      <CheckCircle2 className="w-3 h-3 text-stone-950 absolute opacity-0 peer-checked:opacity-100 pointer-events-none" strokeWidth={3} />
                    </div>
                    <div>
                      <span className="text-sm font-medium text-stone-300 block">Limited Power of Attorney</span>
                      <span className="text-xs text-emerald-500/80">Signé via DocuSign</span>
                    </div>
                  </label>
                  <label className="flex items-start gap-3 cursor-pointer group">
                    <div className="mt-0.5 relative flex items-center justify-center shrink-0">
                      <input type="checkbox" className="peer appearance-none w-4 h-4 border border-stone-700 rounded bg-stone-950 checked:bg-emerald-500 checked:border-emerald-500 transition-colors" />
                      <CheckCircle2 className="w-3 h-3 text-stone-950 absolute opacity-0 peer-checked:opacity-100 pointer-events-none" strokeWidth={3} />
                    </div>
                    <div>
                      <span className="text-sm font-medium text-stone-300 block">Affidavit of Heirship</span>
                      <span className="text-xs text-amber-500/80">En attente (Notaire Mobile)</span>
                    </div>
                  </label>
                </div>
              </div>

              {/* Timeline */}
              <div className="bg-stone-900 border border-stone-800 rounded-xl p-5">
                <h3 className="text-sm font-display font-semibold text-stone-100 flex items-center gap-2 mb-4">
                  <Clock className="w-4 h-4 text-stone-400" />
                  Activity Timeline
                </h3>
                <div className="relative pl-4 border-l border-stone-800 space-y-6">
                  <div className="relative">
                    <span className="absolute -left-[21px] top-1 w-2.5 h-2.5 rounded-full bg-emerald-500 ring-4 ring-stone-900" />
                    <p className="text-sm font-medium text-stone-300 mb-0.5">DocuSign Complété</p>
                    <p className="text-xs text-stone-500">Aujourd'hui, 09:42 AM</p>
                  </div>
                  <div className="relative">
                    <span className="absolute -left-[21px] top-1 w-2.5 h-2.5 rounded-full bg-stone-700 ring-4 ring-stone-900" />
                    <p className="text-sm font-medium text-stone-300 mb-0.5">Vault Accédé par Client</p>
                    <p className="text-xs text-stone-500">Hier, 16:30 PM</p>
                  </div>
                  <div className="relative">
                    <span className="absolute -left-[21px] top-1 w-2.5 h-2.5 rounded-full bg-stone-700 ring-4 ring-stone-900" />
                    <p className="text-sm font-medium text-stone-300 mb-0.5">SMS Relance Envoyé</p>
                    <p className="text-xs text-stone-500">14 Mai 2026, 10:00 AM</p>
                  </div>
                </div>
              </div>

            </div>

            {/* Right Col: Document Vault */}
            <div className="col-span-1 lg:col-span-2">
              <div className="bg-stone-900 border border-stone-800 rounded-xl p-5 flex flex-col h-full">
                <div className="flex justify-between items-center mb-6">
                  <h3 className="text-sm font-display font-semibold text-stone-100 flex items-center gap-2">
                    <UploadCloud className="w-4 h-4 text-stone-400" />
                    Document Vault
                  </h3>
                  <button className="text-xs font-medium text-emerald-400 hover:text-emerald-300 transition-colors">
                    + Ajouter
                  </button>
                </div>
                
                {/* Drag Drop Zone */}
                <div className="border-2 border-dashed border-stone-800 rounded-lg bg-stone-950/50 p-6 flex flex-col items-center justify-center text-center mb-6 hover:border-emerald-500/50 hover:bg-emerald-500/5 transition-colors cursor-pointer">
                  <div className="w-10 h-10 rounded-full bg-stone-900 flex items-center justify-center mb-3">
                    <UploadCloud className="w-5 h-5 text-stone-500" />
                  </div>
                  <p className="text-sm font-medium text-stone-300 mb-1">Glissez vos fichiers ici</p>
                  <p className="text-xs text-stone-500">PDF, JPG, PNG (Max 50MB)</p>
                </div>

                {/* File List */}
                <div className="space-y-2">
                  <div className="flex items-center justify-between p-3 rounded-lg bg-stone-950 border border-stone-800 group hover:border-stone-700 transition-colors">
                    <div className="flex items-center gap-3">
                      <FileSignature className="w-5 h-5 text-emerald-500/80" />
                      <div>
                        <p className="text-sm font-medium text-stone-200">Limited_POA_Signed.pdf</p>
                        <p className="text-xs text-stone-500">2.4 MB • Récemment ajouté</p>
                      </div>
                    </div>
                    <button className="text-stone-500 hover:text-stone-300"><FileText className="w-4 h-4" /></button>
                  </div>
                  <div className="flex items-center justify-between p-3 rounded-lg bg-stone-950 border border-stone-800 group hover:border-stone-700 transition-colors">
                    <div className="flex items-center gap-3">
                      <FileCheck className="w-5 h-5 text-indigo-400/80" />
                      <div>
                        <p className="text-sm font-medium text-stone-200">Driver_License_Scan.jpg</p>
                        <p className="text-xs text-stone-500">1.1 MB • Hier</p>
                      </div>
                    </div>
                    <button className="text-stone-500 hover:text-stone-300"><FileText className="w-4 h-4" /></button>
                  </div>
                </div>

              </div>
            </div>

          </div>
        </div>
      </div>
    </motion.div>
  );
}
