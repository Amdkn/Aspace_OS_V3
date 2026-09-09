#!/usr/bin/env python3
"""
A'Space OS V3 — Gatekeeper A1 Beth Filter
Filtre de garde déterministe pour valider les intentions entrantes contre la table Engram.
Incarnation de Beth (Alignement & Veto A1) sous la coordination du 12e Docteur.
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

try:
    from .engram_loader import EngramPhraseBook
except ImportError:
    from engram_loader import EngramPhraseBook


class BethFilter:
    """Gatekeeper A1 Beth — Filtre d'alignement et veto déterministe."""

    def __init__(self, phrasebook: Optional[EngramPhraseBook] = None):
        self.phrasebook = phrasebook or EngramPhraseBook()

    def _tokenize(self, intent: Union[str, List[str], Dict[str, Any]]) -> List[str]:
        if isinstance(intent, str):
            return intent.split()
        elif isinstance(intent, list):
            return [str(item) for item in intent]
        elif isinstance(intent, dict):
            text = intent.get("text") or intent.get("prompt") or intent.get("intent") or ""
            return str(text).split()
        return []

    def evaluate_intent(self, intent: Union[str, List[str], Dict[str, Any]]) -> Dict[str, Any]:
        """
        Évalue une intention contre la table Engram.
        Retourne la décision de validation (allowed, veto, matched_key, payload, reason).
        """
        tokens = self._tokenize(intent)
        if not tokens:
            return {
                "allowed": True,
                "veto": False,
                "matched_key": None,
                "reason": "Intention vide ou non textuelle — transmise sans veto."
            }

        match = self.phrasebook.resolve(tokens)
        if not match:
            return {
                "allowed": True,
                "veto": False,
                "matched_key": None,
                "reason": "Aucun invariant Engram détecté — intention conforme au passage A1."
            }

        key = match["matched_key"]
        payload = match.get("payload", {})
        resolution_type = match.get("resolution_type")
        dimension = match.get("dimension")

        # Analyse des règles spéciques Engram
        if resolution_type == "CIRCUIT_BREAKER":
            return {
                "allowed": False,
                "veto": True,
                "matched_key": key,
                "dimension": dimension,
                "action": payload.get("action"),
                "reason": f"Veto Beth A1 : Circuit breaker activé pour {key} ({payload.get('action')}).",
                "match": match
            }

        if resolution_type == "DETERMINISTIC_EVAL":
            rules = payload.get("rules", [])
            return {
                "allowed": True,
                "veto": False,
                "matched_key": key,
                "dimension": dimension,
                "required_rules": rules,
                "reason": f"Alignement Engram A1 : Respect strict des règles {rules} requis.",
                "match": match
            }

        return {
            "allowed": True,
            "veto": False,
            "matched_key": key,
            "dimension": dimension,
            "resolution_type": resolution_type,
            "reason": f"Engram A1 résolu avec succès : {key} [{dimension}].",
            "match": match
        }


if __name__ == "__main__":
    filter_a1 = BethFilter()
    sample_intents = [
        "Demande d'activation os hyoide resilience pour purger la file",
        "Vérifier la definition of done du build",
        "Lancer un scan sur LD01 self operating business"
    ]
    for intent in sample_intents:
        res = filter_a1.evaluate_intent(intent)
        print(f"[*] Intent : '{intent}'")
        print(f"    Résultat : {json.dumps(res, indent=2, ensure_ascii=False)}\n")
