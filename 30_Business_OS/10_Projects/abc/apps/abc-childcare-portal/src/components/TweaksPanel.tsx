'use client';

import { useEffect, useState } from 'react';
import { Icon } from './Icon';
import { COLORS } from '@/design/tokens';

export interface TweaksPanelProps {
  open: boolean;
  onClose: () => void;
  title?: string;
}

const ACCENT_OPTIONS = [
  '#e15f41',
  '#d4b042',
  '#10b981',
  '#5b8bb7',
  '#c47a96',
];

const PHONE_SIZES = [
  { value: 'small', label: 'Compact' },
  { value: 'large', label: 'Pro Max' },
] as const;

const HUB_TABS = [
  { value: '/community', label: 'Community' },
  { value: '/learn', label: 'Learn' },
  { value: '/build-hub', label: 'Build' },
  { value: '/brand', label: 'Brand' },
] as const;

const TWEAK_CSS = `
.twk-panel{
  position:absolute;top:0;right:0;height:100%;
  width:280px;max-width:90%;
  display:flex;flex-direction:column;
  background:rgba(250,249,247,.78);color:#29261b;
  -webkit-backdrop-filter:blur(24px) saturate(160%);backdrop-filter:blur(24px) saturate(160%);
  border-left:.5px solid rgba(255,255,255,.6);
  box-shadow:0 1px 0 rgba(255,255,255,.5) inset,0 12px 40px rgba(0,0,0,.18);
  font:11.5px/1.4 ui-sans-serif,system-ui,-apple-system,sans-serif;overflow:hidden;
  z-index:120;animation:twkSlide .25s ease-out;
}
@keyframes twkSlide{from{transform:translateX(100%)}to{transform:translateX(0)}}
.twk-backdrop{position:absolute;inset:0;background:rgba(0,0,0,.35);z-index:110;animation:twkFade .2s ease-out}
@keyframes twkFade{from{opacity:0}to{opacity:1}}
.twk-hd{display:flex;align-items:center;justify-content:space-between;padding:10px 8px 10px 14px;cursor:default}
.twk-hd b{font-size:12px;font-weight:600;letter-spacing:.01em}
.twk-x{appearance:none;border:0;background:transparent;color:rgba(41,38,27,.55);width:22px;height:22px;border-radius:6px;cursor:default;font-size:13px;line-height:1}
.twk-x:hover{background:rgba(0,0,0,.06);color:#29261b}
.twk-body{padding:2px 14px 14px;display:flex;flex-direction:column;gap:10px;overflow-y:auto;overflow-x:hidden;min-height:0;scrollbar-width:thin;scrollbar-color:rgba(0,0,0,.15) transparent}
.twk-body::-webkit-scrollbar{width:8px}
.twk-body::-webkit-scrollbar-track{background:transparent;margin:2px}
.twk-body::-webkit-scrollbar-thumb{background:rgba(0,0,0,.15);border-radius:4px;border:2px solid transparent;background-clip:content-box}
.twk-body::-webkit-scrollbar-thumb:hover{background:rgba(0,0,0,.25);border:2px solid transparent;background-clip:content-box}
.twk-row{display:flex;flex-direction:column;gap:5px}
.twk-row-h{flex-direction:row;align-items:center;justify-content:space-between;gap:10px}
.twk-lbl{display:flex;justify-content:space-between;align-items:baseline;color:rgba(41,38,27,.72)}
.twk-lbl>span:first-child{font-weight:500}
.twk-val{color:rgba(41,38,27,.5);font-variant-numeric:tabular-nums}
.twk-sect{font-size:10px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:rgba(41,38,27,.45);padding:10px 0 0}
.twk-sect:first-child{padding-top:0}
.twk-field{appearance:none;box-sizing:border-box;width:100%;min-width:0;height:26px;padding:0 8px;border:.5px solid rgba(0,0,0,.1);border-radius:7px;background:rgba(255,255,255,.6);color:inherit;font:inherit;outline:none}
.twk-field:focus{border-color:rgba(0,0,0,.25);background:rgba(255,255,255,.85)}
.twk-slider{appearance:none;-webkit-appearance:none;width:100%;height:4px;margin:6px 0;border-radius:999px;background:rgba(0,0,0,.12);outline:none}
.twk-slider::-webkit-slider-thumb{-webkit-appearance:none;appearance:none;width:14px;height:14px;border-radius:50%;background:#fff;border:.5px solid rgba(0,0,0,.12);box-shadow:0 1px 3px rgba(0,0,0,.2);cursor:default}
.twk-slider::-moz-range-thumb{width:14px;height:14px;border-radius:50%;background:#fff;border:.5px solid rgba(0,0,0,.12);box-shadow:0 1px 3px rgba(0,0,0,.2);cursor:default}
.twk-seg{position:relative;display:flex;padding:2px;border-radius:8px;background:rgba(0,0,0,.06);user-select:none}
.twk-seg-thumb{position:absolute;top:2px;bottom:2px;border-radius:6px;background:rgba(255,255,255,.9);box-shadow:0 1px 2px rgba(0,0,0,.12);transition:left .15s cubic-bezier(.3,.7,.4,1),width .15s}
.twk-seg button{appearance:none;position:relative;z-index:1;flex:1;border:0;background:transparent;color:inherit;font:inherit;font-weight:500;min-height:22px;border-radius:6px;cursor:default;padding:4px 6px;line-height:1.2;overflow-wrap:anywhere}
.twk-seg button[aria-checked="true"]{color:#000;font-weight:600}
.twk-toggle{position:relative;width:32px;height:18px;border:0;border-radius:999px;background:rgba(0,0,0,.15);transition:background .15s;cursor:default;padding:0}
.twk-toggle[data-on="1"]{background:#34c759}
.twk-toggle i{position:absolute;top:2px;left:2px;width:14px;height:14px;border-radius:50%;background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.25);transition:transform .15s}
.twk-toggle[data-on="1"] i{transform:translateX(14px)}
.twk-chips{display:flex;gap:6px}
.twk-chip{position:relative;appearance:none;flex:1;min-width:0;height:46px;padding:0;border:0;border-radius:6px;overflow:hidden;cursor:default;box-shadow:0 0 0 .5px rgba(0,0,0,.12),0 1px 2px rgba(0,0,0,.06);transition:transform .12s cubic-bezier(.3,.7,.4,1),box-shadow .12s}
.twk-chip:hover{transform:translateY(-1px);box-shadow:0 0 0 .5px rgba(0,0,0,.18),0 4px 10px rgba(0,0,0,.12)}
.twk-chip[data-on="1"]{box-shadow:0 0 0 1.5px rgba(0,0,0,.85),0 2px 6px rgba(0,0,0,.15)}
.twk-btn{appearance:none;height:26px;padding:0 12px;border:0;border-radius:7px;background:rgba(0,0,0,.78);color:#fff;font:inherit;font-weight:500;cursor:default}
.twk-btn:hover{background:rgba(0,0,0,.88)}
`;

/**
 * TweaksPanel — faithful port of the legacy `tweaks-panel.jsx`.
 *
 * In the legacy prototype this is a free-floating editor control. In the
 * Next.js shell it slides in from the right of the IOSDevice as a side
 * drawer (it is mounted inside the device frame so it visually fits the
 * mobile chrome). State is local — accent + phone size + dark toggle are
 * persisted to localStorage so A0 can play with them across reloads.
 */
export function TweaksPanel({ open, onClose, title = 'Tweaks' }: TweaksPanelProps) {
  const [accent, setAccent] = useState<string>(COLORS.terracotta);
  const [phoneSize, setPhoneSize] = useState<'small' | 'large'>('large');
  const [dark, setDark] = useState<boolean>(true);

  useEffect(() => {
    if (typeof window === 'undefined') return;
    const raw = window.localStorage.getItem('abc-tweaks');
    if (!raw) return;
    try {
      const v = JSON.parse(raw) as Partial<{
        accent: string;
        phoneSize: 'small' | 'large';
        dark: boolean;
      }>;
      if (v.accent) setAccent(v.accent);
      if (v.phoneSize) setPhoneSize(v.phoneSize);
      if (typeof v.dark === 'boolean') setDark(v.dark);
    } catch {
      /* ignore */
    }
  }, []);

  useEffect(() => {
    if (typeof window === 'undefined') return;
    window.localStorage.setItem(
      'abc-tweaks',
      JSON.stringify({ accent, phoneSize, dark })
    );
  }, [accent, phoneSize, dark]);

  if (!open) return null;

  return (
    <>
      <style>{TWEAK_CSS}</style>
      <div className="twk-backdrop" onClick={onClose} aria-hidden="true" />
      <div
        className="twk-panel"
        role="dialog"
        aria-modal="true"
        aria-label={title}
      >
        <div className="twk-hd">
          <b>{title}</b>
          <button
            className="twk-x"
            aria-label="Close tweaks"
            onClick={onClose}
          >
            <Icon name="x" size={13} stroke={2} />
          </button>
        </div>
        <div className="twk-body">
          <div className="twk-sect">View</div>

          <div className="twk-row twk-row-h">
            <div className="twk-lbl">
              <span>Dark mode</span>
            </div>
            <button
              type="button"
              className="twk-toggle"
              data-on={dark ? '1' : '0'}
              role="switch"
              aria-checked={dark}
              onClick={() => setDark((v) => !v)}
            >
              <i />
            </button>
          </div>

          <div className="twk-row">
            <div className="twk-lbl">
              <span>Phone size</span>
              <span className="twk-val">
                {phoneSize === 'small' ? 'Compact' : 'Pro Max'}
              </span>
            </div>
            <div className="twk-seg" role="radiogroup">
              {PHONE_SIZES.map((o) => {
                const active = phoneSize === o.value;
                return (
                  <button
                    key={o.value}
                    type="button"
                    role="radio"
                    aria-checked={active}
                    onClick={() => setPhoneSize(o.value)}
                    style={{ fontWeight: active ? 600 : 500 }}
                  >
                    {o.label}
                  </button>
                );
              })}
            </div>
          </div>

          <div className="twk-sect">Navigate</div>

          <div className="twk-row">
            <div className="twk-lbl">
              <span>Active hub</span>
            </div>
            <div className="twk-seg" role="radiogroup">
              {HUB_TABS.map((o) => {
                const active = false;
                return (
                  <a
                    key={o.value}
                    href={o.value}
                    role="link"
                    style={{
                      flex: 1,
                      textAlign: 'center',
                      fontWeight: 500,
                      color: '#29261b',
                      textDecoration: 'none',
                      padding: '4px 6px',
                      minHeight: 22,
                      display: 'inline-flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                    }}
                  >
                    {o.label}
                  </a>
                );
              })}
            </div>
          </div>

          <div className="twk-sect">Brand accent</div>

          <div className="twk-row">
            <div className="twk-lbl">
              <span>Accent</span>
              <span className="twk-val">{accent}</span>
            </div>
            <div className="twk-chips" role="radiogroup">
              {ACCENT_OPTIONS.map((o) => {
                const on = accent.toLowerCase() === o.toLowerCase();
                return (
                  <button
                    key={o}
                    type="button"
                    className="twk-chip"
                    role="radio"
                    aria-checked={on}
                    data-on={on ? '1' : '0'}
                    aria-label={o}
                    title={o}
                    style={{ background: o }}
                    onClick={() => setAccent(o)}
                  />
                );
              })}
            </div>
            <div
              style={{ fontSize: 11, color: '#777', padding: '4px 2px' }}
            >
              (Demo control — accent is persisted to localStorage only.)
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default TweaksPanel;
