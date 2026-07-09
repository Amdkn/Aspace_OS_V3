import React from 'react';

interface SectionTitleProps {
  title: string;
  subtitle?: string;
  centered?: boolean;
}

export const SectionTitle: React.FC<SectionTitleProps> = ({ title, subtitle, centered = false }) => {
  return (
    <div className={`mb-12 ${centered ? 'text-center' : 'text-left'}`}>
      <h2 className="text-3xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 sm:text-4xl mb-4">
        {title}
      </h2>
      {subtitle && (
        <p className="max-w-2xl text-lg text-zinc-600 dark:text-zinc-400 mx-auto">
          {subtitle}
        </p>
      )}
    </div>
  );
};
