'use client';

import { useCallback, useEffect, useState } from 'react';

/**
 * Persistent local state backed by `window.localStorage`.
 *
 * Replaces the legacy prototype's `postMessage` parent/host dependency
 * (`__edit_mode_set_keys` + `window.parent.postMessage`) with a plain,
 * in-page hook. Server-render safe: returns the initial value on the first
 * pass and rehydrates from localStorage on mount.
 */
export function useLocalStorage<T>(
  key: string,
  initialValue: T,
): readonly [T, (value: T | ((prev: T) => T)) => void] {
  const [value, setValue] = useState<T>(initialValue);

  useEffect(() => {
    if (typeof window === 'undefined') return;
    try {
      const stored = window.localStorage.getItem(key);
      if (stored !== null) {
        setValue(JSON.parse(stored) as T);
      }
    } catch {
      // ignore corrupted storage
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [key]);

  const update = useCallback(
    (next: T | ((prev: T) => T)) => {
      setValue((prev) => {
        const resolved =
          typeof next === 'function' ? (next as (p: T) => T)(prev) : next;
        if (typeof window !== 'undefined') {
          try {
            window.localStorage.setItem(key, JSON.stringify(resolved));
          } catch {
            // storage might be full or disabled — degrade silently
          }
        }
        return resolved;
      });
    },
    [key],
  );

  return [value, update] as const;
}
