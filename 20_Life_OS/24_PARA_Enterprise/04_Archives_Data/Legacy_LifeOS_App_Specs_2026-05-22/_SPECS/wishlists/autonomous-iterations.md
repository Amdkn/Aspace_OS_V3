# Wishlist: Autonomous Iteration Engine (Conductor + Ralph)
## Target Layer: L2 / L3 (Business Pulse & Execution)
## Purpose: Créer un moteur d'orchestration Méta-Agentique fusionnant Conductor (Structuration A1/A2) et Ralph Loop (Exécution A3) pour automatiser intégralement le cycle V0.1.1 à V0.1.9 sans intervention humaine.
## Strategic Alignment: Méta-Science / Automatisation BMad

### Required Components
- [ ] **Le Cerveau de Structuration (Conductor pour A1/A2)**
  - *Rationale* : Utiliser `/conductor:newTrack` pour chaque version mineure (ex: Track "V0.1.1"). Conductor va générer le `spec.md` et le `plan.md` strict basé sur le Skill des 7 Phases.
  - *Intégration BMad* : Le fichier `conductor/product-guidelines.md` doit contenir les lois de GravityClaw, les TVR, et l'architecture DDD pour que l'agent ne dévie pas lors du planning.
- [ ] **Le Moteur d'Exécution Infaillible (Ralph Loop pour A3)**
  - *Rationale* : L'A3 (Gemini CLI) ne doit pas exécuter un simple `/conductor:implement` qui pourrait s'essouffler en mémoire. Il doit utiliser `/ralph:loop` pour enfermer l'implémentation de **chaque phase** dans une boucle de TDD (Rédiger test → Coder → Vérifier → Boucler).
  - *Concept* : `ralph:loop` avec une `--completion-promise` spécifique pour la Phase (ex: "PHASE_7_AUDIT_PASSED"). La mémoire de l'agent est rafraîchie à chaque tour pour éviter l'hallucination (No Compaction).
- [ ] **Le Pont de Relais (The Handshake Workflow)**
  - *Rationale* : Un Workflow automatisé ou un fichier `.agent/workflows/run-iteration.md` qui dicte la séquence. Exemple : L'OS lance `conductor:newTrack`, l'A0/A1 valide. L'OS lance `ralph:loop` sur le plan Conductor. Ralph complète la Phase 7. L'OS scelle la Release V0.1.x.
- [ ] **Veto Intégré aux Hooks Ralph**
  - *Rationale* : Exploiter le système de `hooks/stop-hook.sh` de Ralph pour vérifier le Veto de Beth avant de continuer l'itération. Si le Veto est actif, Ralph s'arrête (Ghost Protection).

### Explicitly Excluded (Anti-Wishlist)
- [ ] **YOLO Autonomie Aveugle**
  - *Pourquoi* : On ne lance pas une boucle infinie de la V0.1.1 à la V0.1.9 d'un seul coup. La limite d'autonomie s'arrête à la fin de la Phase 7 d'une version donnée (Handshake requis avant la version suivante).
- [ ] **Mélange de Conductor et des anciens Prompts**
  - *Pourquoi* : Conductor devient la seule source de vérité pour le plan. L'agent ne doit pas lire de "vieux" tasks.md disparates, il doit suivre strictement `conductor/tracks/`.

### Non-Negotiable Constraints
- **Security**: Ralph Loop doit tourner en "Sandbox Mode" (`gemini -s -y`) avec des outils restreints définis dans `.gemini/settings.json` (pas de push git automatique en boucle).
- **Performance**: `--max-iterations` doit être intelligemment capé (ex: 15 par Phase) pour ne pas vider les quotas bêtement si un bug A3 bloque la boucle.
- **Dependencies**: Nécessite Gemini CLI, l'extension Conductor installée (`conductor:setup` exécuté), et l'extension Ralph installée et hookée.

### TVR Assessment
- **Teachable**: Oui, c'est la formalisation ultime du rôle de l'Architecte (A2) et du Technicien (A3) via des outils CLI.
- **Valuable**: Oui, cela nous permet de lancer "Construis la V0.1.1" le soir, et de retrouver le code propre et audité le lendemain matin.
- **Repeatable**: Absolument. C'est le cœur même de Ralph (Self-referential loop) couplé à l'idempotence de Conductor.
