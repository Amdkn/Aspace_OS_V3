import { useState, useEffect } from 'react';
import { supabase } from '../lib/supabase';
import { Holding, GlobalMetrics } from '../types';
import { holdingsData as staticHoldings, globalMetrics as staticMetrics } from '../data/holdings';

export function useHoldings() {
  const [holdings, setHoldings] = useState<Holding[]>(staticHoldings);
  const [metrics, setMetrics] = useState<GlobalMetrics>(staticMetrics);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        if (supabase) {
          // En production, on fetcherait depuis Supabase
          // const { data: holdingsData } = await supabase.from('holdings').select('*');
          // if (holdingsData) setHoldings(holdingsData);
        }
        
        // Simulation d'un délai réseau pour valider l'UX
        await new Promise(resolve => setTimeout(resolve, 500));
      } catch (error) {
        console.error('Error fetching holdings:', error);
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, []);

  return { holdings, metrics, loading };
}
