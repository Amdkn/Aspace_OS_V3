"use client";

import React from 'react';

interface ImageSlotProps {
  id: string;
  placeholder?: string;
  className?: string;
  aspectRatio?: string;
  background?: string;
}

export const ImageSlot = ({ id, placeholder = "Drop an image", className = "", aspectRatio = "4/5", background = "linear-gradient(160deg,#ECFCCB 0%, #F5F5F4 60%, #FAFAF9 100%)" }: ImageSlotProps) => {
  return (
    <div 
      className={`relative overflow-hidden group cursor-pointer photo-ph ${className}`}
      style={{ aspectRatio, background }}
      data-slot-id={id}
    >
      <div className="absolute inset-0 flex flex-col items-center justify-center gap-3 p-6 text-center opacity-60 group-hover:opacity-80 transition-opacity">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
          <rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/>
          <path d="m21 15-5-5L5 21"/>
        </svg>
        <div>
          <div className="text-sm font-semibold">{placeholder}</div>
          <div className="text-[11px] mt-1 opacity-70">or <u>browse files</u></div>
        </div>
      </div>
      {/* Placeholder logic for future upload integration */}
      <input type="file" className="hidden" accept="image/*" />
    </div>
  );
};
