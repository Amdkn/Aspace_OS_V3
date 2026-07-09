import React from 'react';
import { LucideIcon } from 'lucide-react';

interface IconProps {
  icon: LucideIcon;
  className?: string;
  size?: number;
  strokeWidth?: number;
}

export const Icon = ({ icon: LucideIcon, className = "", size = 18, strokeWidth = 1.5 }: IconProps) => {
  return <LucideIcon className={className} size={size} strokeWidth={strokeWidth} aria-hidden="true" />;
};
