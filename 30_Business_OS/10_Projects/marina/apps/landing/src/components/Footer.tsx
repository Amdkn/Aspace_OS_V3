"use client";

import React from "react";
import { Mail, Phone, Clock, MessageSquareText, MapPin, ArrowRight } from "lucide-react";
import { Icon } from "./Icon";

export function Footer() {
  return (
    <footer id="zone" className="bg-stone-100 border-t border-stone-200">
      <div className="max-w-[1280px] mx-auto px-5 sm:px-8 lg:px-12 py-16 lg:py-20">
        <div className="grid lg:grid-cols-12 gap-12">
          <div className="lg:col-span-5">
            <div className="flex items-center gap-2.5">
              <span className="w-10 h-10 rounded-xl bg-white ring-leaf flex items-center justify-center">
                <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="#064E3B" strokeWidth="1.6">
                  <path d="M4 20c2-10 8-16 16-16 0 8-6 14-16 16Z"/>
                  <path d="M4 20c4-4 8-7 12-9"/>
                </svg>
              </span>
              <span className="font-display font-extrabold text-[20px] text-emerald-950">
                Marina Cleaning<span className="text-lime-600">.</span> Co.
              </span>
            </div>
            <p className="mt-5 text-stone-700 text-[15px] leading-relaxed max-w-sm">
              Le ménage à domicile, livré comme un produit. Standards hôteliers, prix fixe, prise de tête : zéro.
            </p>

            <div className="mt-6 flex flex-wrap gap-3">
              <a href="#packs" className="btn-cta rounded-full h-11 px-5 inline-flex items-center gap-2 text-[14px] font-semibold font-display">
                Réserver mon Pack <Icon icon={ArrowRight} size={15}/>
              </a>
              <a href="tel:+18595551212" className="btn-ghost rounded-full h-11 px-5 inline-flex items-center gap-2 text-[14px] font-semibold font-display">
                <Icon icon={Phone} size={14}/> (859) 555-1212
              </a>
            </div>
          </div>

          <div className="lg:col-span-7 grid sm:grid-cols-3 gap-8">
            <div>
              <h4 className="font-display font-bold text-[13px] uppercase tracking-[0.18em] text-stone-500">Zone couverte</h4>
              <ul className="mt-4 space-y-2.5 text-[14.5px] text-stone-800">
                {["Cincinnati, OH","Florence, KY","Newport, KY","Covington, KY","Hyde Park · Oakley","Fort Mitchell"].map(z=>(
                  <li key={z} className="flex items-center gap-2"><Icon icon={MapPin} size={13} className="text-emerald-700"/>{z}</li>
                ))}
              </ul>
            </div>

            <div>
              <h4 className="font-display font-bold text-[13px] uppercase tracking-[0.18em] text-stone-500">Service</h4>
              <ul className="mt-4 space-y-2.5 text-[14.5px] text-stone-800">
                {["Les Packs","La Méthode","SOP & Standards","FAQ","Espace pro / B2B","Devenir technicien·ne"].map(z=>(
                  <li key={z}><a href="#" className="link-u hover:text-emerald-900 font-medium">{z}</a></li>
                ))}
              </ul>
            </div>

            <div>
              <h4 className="font-display font-bold text-[13px] uppercase tracking-[0.18em] text-stone-500">Contact</h4>
              <ul className="mt-4 space-y-2.5 text-[14.5px] text-stone-800 font-medium">
                <li className="flex items-start gap-2"><Icon icon={Mail} size={13} className="text-emerald-700 mt-1"/>hello@marinacleaning.co</li>
                <li className="flex items-start gap-2"><Icon icon={Phone} size={13} className="text-emerald-700 mt-1"/>(859) 555-1212</li>
                <li className="flex items-start gap-2"><Icon icon={Clock} size={13} className="text-emerald-700 mt-1"/>Lun–Dim · 7h–20h</li>
                <li className="flex items-start gap-2"><Icon icon={MessageSquareText} size={13} className="text-emerald-700 mt-1"/>Réponse &lt; 1h en semaine</li>
              </ul>
            </div>
          </div>
        </div>

        <div className="mt-14 pt-6 border-t border-stone-200 flex flex-col sm:flex-row gap-4 items-start sm:items-center justify-between text-[12.5px] text-stone-500">
          <div>© 2026 Marina Cleaning Co. — Tous droits réservés · Operated from Florence, KY</div>
          <div className="flex items-center gap-5">
            <a href="#" className="link-u hover:text-emerald-900">Mentions légales</a>
            <a href="#" className="link-u hover:text-emerald-900">CGV</a>
            <a href="#" className="link-u hover:text-emerald-900">Confidentialité</a>
            <a href="#" className="link-u hover:text-emerald-900">Assurance RC pro</a>
          </div>
        </div>
      </div>
    </footer>
  );
}
