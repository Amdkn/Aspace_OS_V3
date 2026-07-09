# Protocole de Sobriété

> "Tout ce qui n'est pas essentiel est un poids qui te ralentit."

---

## ⚡ Philosophie
La puissance ne vient pas de l'accumulation, mais de la **concentration**.
Un système sobre est :
1.  **Auditable** (On sait ce qui tourne).
2.  **Sécurisé** (Moins de surface d'attaque).
3.  **Performant** (Pas de cycles CPU gâchés).

## 🛑 Liste Rouge (Interdictions)
*   **Pas de Bloatware** : Pas d'agents de monitoring propriétaires (sauf si Open Source).
*   **Pas de GUI Serveur** : Tout se gère en SSH.
*   **Pas de Dépendances Mortes** : `npm prune` est ton ami.

## 🟢 Liste Verte (Standards)
*   **Text Files** : Markdown, JSON, YAML. Lisible par un humain dans 50 ans.
*   **Docker** : Isolation parfaite.
*   **Bash/PowerShell** : Les langages natifs de la machine.

## ♻️ Le Cycle de Nettoyage
Chaque Dimanche (Sunday Uplink) :
1.  Vérifier les logs.
2.  Supprimer les fichiers temporaires.
3.  Archiver ce qui n'a pas bougé depuis 6 mois (`00_Amadeus/04_Memory`).
