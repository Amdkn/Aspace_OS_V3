---
type: artifact-schema
artifact: ticket
---
# tickets/ — items client/support traités (WF2 / W*)

**Entre** : 1 fichier par ticket client traité : demande, réponse/action, frictions observées (→ dupliquer la friction en signal si récurrente).
**N'entre pas** : PII en clair — le proxy DLP (mission 05) expurge AVANT écriture. Un ticket contenant un secret détecté = quarantaine `_quarantine/` + signal `dlp-hit`.
**Schéma** : `type: ticket`, `client: <tenant-id>` (jamais le nom en clair), `status`, timeline append-only.
