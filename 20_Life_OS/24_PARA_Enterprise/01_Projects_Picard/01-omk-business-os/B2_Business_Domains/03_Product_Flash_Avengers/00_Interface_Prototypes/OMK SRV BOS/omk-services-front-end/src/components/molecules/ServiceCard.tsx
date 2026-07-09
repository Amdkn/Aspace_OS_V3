import React from 'react';
import { Icon } from '../atoms/Icons';

interface ServiceCardProps {
  title: string;
  description: string;
  iconName: keyof typeof Icon;
}

export const ServiceCard: React.FC<ServiceCardProps> = ({ title, description, iconName }) => {
  const SelectedIcon = Icon[iconName];

  return (
    <div className="flex flex-col p-8 bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-2xl transition-all hover:shadow-lg hover:-translate-y-1">
      <div className="w-12 h-12 flex items-center justify-center bg-blue-100 dark:bg-blue-900/30 text-blue-600 dark:text-blue-400 rounded-xl mb-6">
        <SelectedIcon size={24} />
      </div>
      <h3 className="text-xl font-bold text-zinc-900 dark:text-zinc-50 mb-3">{title}</h3>
      <p className="text-zinc-600 dark:text-zinc-400 leading-relaxed">{description}</p>
    </div>
  );
};
