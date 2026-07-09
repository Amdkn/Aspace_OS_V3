import React from 'react';
import { Icon } from '../atoms/Icons';

export const Hero: React.FC = () => {
  return (
    <section className="relative overflow-hidden pt-24 pb-20 px-6">
      <div className="max-w-7xl mx-auto grid lg:grid-cols-2 gap-12 items-center">
        <div className="flex flex-col gap-8">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 dark:bg-blue-900/20 text-blue-700 dark:text-blue-300 text-xs font-bold uppercase tracking-wider w-fit">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
            </span>
            Souveraineté Technologique
          </div>
          <h1 className="text-5xl md:text-6xl font-extrabold tracking-tight text-zinc-900 dark:text-zinc-50 leading-[1.1]">
            L'Excellence en <span className="text-blue-600 italic">Ingénierie</span> Industrielle.
          </h1>
          <p className="text-xl text-zinc-600 dark:text-zinc-400 leading-relaxed max-w-xl">
            Optimisez vos processus, sécurisez vos infrastructures et boostez votre productivité avec nos services d'ingénierie avancés et nos solutions de maintenance prédictive.
          </p>
          <div className="flex flex-wrap gap-4">
            <button className="px-8 py-4 bg-blue-600 text-white rounded-full font-bold hover:bg-blue-700 transition-colors flex items-center gap-2 group">
              Démarrer un Projet
              <Icon.ArrowRight className="group-hover:translate-x-1 transition-transform" />
            </button>
            <button className="px-8 py-4 border border-zinc-200 dark:border-zinc-800 rounded-full font-bold hover:bg-zinc-50 dark:hover:bg-zinc-900 transition-colors">
              Voir l'Expertise
            </button>
          </div>
          <div className="flex items-center gap-6 pt-4 border-t border-zinc-100 dark:border-zinc-900">
            <div className="flex flex-col">
              <span className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">150+</span>
              <span className="text-sm text-zinc-500">Projets Livrés</span>
            </div>
            <div className="w-px h-10 bg-zinc-200 dark:bg-zinc-800"></div>
            <div className="flex flex-col">
              <span className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">98%</span>
              <span className="text-sm text-zinc-500">Satisfaction Client</span>
            </div>
          </div>
        </div>
        <div className="relative aspect-square lg:aspect-auto lg:h-[600px] bg-zinc-100 dark:bg-zinc-900 rounded-3xl overflow-hidden border border-zinc-200 dark:border-zinc-800 flex items-center justify-center">
          {/* Placeholder for real image or 3D element */}
          <div className="absolute inset-0 opacity-10 bg-[radial-gradient(#3b82f6_1px,transparent_1px)] [background-size:20px_20px]"></div>
          <Icon.Workflow size={120} className="text-blue-500/20 animate-pulse" />
        </div>
      </div>
    </section>
  );
};
