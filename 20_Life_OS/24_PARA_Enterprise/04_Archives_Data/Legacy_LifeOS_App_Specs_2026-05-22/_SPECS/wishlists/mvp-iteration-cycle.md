# Wishlist: Le Cycle d'Itération 7-Phases (V0.1.x)
## Target Layer: L0 / L1 / L2 / L3 (Méta-Processus)
## Purpose: Standardiser un cycle de développement incrémental (V0.1.1 à V0.1.9) basé sur 7 phases strictes pour garantir l'antifragilité et l'idempotence avant d'atteindre la V0.2.
## Strategic Alignment: Méta-Science / Architecture BMad

### Required Components (Les 7 Phases du Cycle)
- [ ] **Phase 1 & 2 : Nettoyage et Dette Technique** 
  - *Rationale* : La première étape d'une itération n'est jamais d'ajouter de la nouveauté. C'est d'abord de rembourser la dette technique contractée lors du cycle précédent, corriger les bugs majeurs, optimiser le CSS/TypeScript existant.
- [ ] **Phase 3 & 4 : Renforcement des Fondations**
  - *Rationale* : Avant d'ajouter du poids sur l'édifice, on consolide les murs porteurs. Amélioration des Stores (Zustand/IndexedDB), refactorisation des middlewares (ex: Veto), sécurisation du routage (Cross-links).
- [ ] **Phase 5 & 6 : Nouvelles Features (2 Max)**
  - *Rationale* : Développement contrôlé. On n'ajoute que 2 nouvelles "User Stories" majeures ou applications par itération (V0.1.x). Cela évite l'entropie et limite la casse.
- [ ] **Phase 7 : Audit, Tests & Conformité (Q/A)**
  - *Rationale* : Le filet de sécurité. La phase 7 est obligatoire pour valider la Release. Check d'isolation des bases (LD01-LD08), tests des fail-safes (Error Boundaries), vérification visuelle (Glassmorphism intact), et Handoff autonome testé.

### Explicitly Excluded (Anti-Wishlist)
- [ ] **Refonte d'Architecture Complète (Big Bang)** 
  - *Pourquoi* : Les V0.1.x sont des itérations. On ne change pas le cœur de l'OS (pas de remplacement de React ou Vite). Ce serait de la V1.0.
- [ ] **Ajout massif de fonctionnalités (Scope Creep)**
  - *Pourquoi* : Limité à 2 features (Phases 5 & 6) pour garantir que 5 phases sur 7 sont allouées au maintien de la stabilité.

### Non-Negotiable Constraints
- **Security**: L'itération ne doit jamais briser la règle d'isolation stricte (Domain-Driven Data).
- **Performance**: L'itération doit se terminer par un Audit (Phase 7) prouvant qu'il n'y a pas d'écran blanc ou de crash silencieux.
- **Dependencies**: La boucle V0.1.1 → V0.1.9 doit pouvoir s'exécuter de façon autonome par Gemini CLI (A3) une fois les Specs (A1/A2) approuvées.

### TVR Assessment
- **Teachable**: Oui, ce cycle en 7 étapes est une méthodologie qui peut devenir un `Skill` explicite pour les agents.
- **Valuable**: Oui, cela empêche les prototypes de se transformer en "spaghetti code" avant d'atteindre la Maturité (V0.2).
- **Repeatable**: Oui, c'est une boucle mathématique fermée qui garantit l'idempotence entre chaque version de patch (V0.1.x).
