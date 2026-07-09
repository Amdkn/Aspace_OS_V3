# Les Clés du VPS : Le Manuel de l'Architecte

**Objectif** : Apprendre à "Voir" la Matrice.
**Rôle** : L'Architecte (Toi) inspectant le travail du Technicien.
**Philosophie** : "Ne jamais faire confiance. Vérifier."

---

## 🔑 1. Navigation (Se déplacer dans le TARDIS)

Pour construire une carte mentale de ton royaume, tu dois en arpenter les couloirs.

### La Boussole : `pwd` (Print Working Directory)
*   **Concept** : "Où suis-je actuellement ?"
*   **Commande** : `pwd`
*   **Sortie** : `/root/aspace_a0_amadeus` signifie que tu es dans le Cœur.

### L'Oeil : `ls` (List)
*   **Concept** : "Qu'y a-t-il dans cette pièce ?"
*   **Commande** : `ls -F` (Ajoute des symboles : `/` pour les dossiers, `*` pour les exécutables).
*   **Commande** : `ls -la` (Les Rayons X. Montre les fichiers cachés comme `.env` et les permissions).
*   **Essaye** : `ls -F 10_Tech_OS/` -> Tu devrais voir `11_Infra`, `12_Interface`, `13_Data`.

### Le Portail : `cd` (Change Directory)
*   **Concept** : "Téléporte-moi vers..."
*   **Commande** : `cd 10_Tech_OS` (Descendre).
*   **Commande** : `cd ..` (Remonter d'un niveau).
*   **Commande** : `cd ~` (Rentrer à la Maison / Le Pont).

---

## 🔋 2. Signes Vitaux (Vérifier les Moteurs)

Le 13ème Docteur (Infra) a besoin d'énergie.

### Le Scanner : `htop` (Vue Holistique)
*   **Concept** : Le Tableau de Bord de la Console du TARDIS.
*   **Action** : Tape `htop`.
*   **Regarde** :
    *   **Barres CPU** : Sont-elles pleines (100%) ? (Mauvais). Vides ? (Bon).
    *   **Mem (RAM)** : C'est ta "Mémoire à Court Terme". Si elle est pleine, le système oublie.
    *   **Swap** : La Réserve d'Urgence. Si elle est utilisée, tu as besoin de plus de RAM.
*   **Sortie** : Appuie sur `F10` ou `q` pour quitter.

### Le Stockage : `df` (Disk Free)
*   **Concept** : "La soute est-elle pleine ?"
*   **Commande** : `df -h` (Human readable - Lisible par l'humain).
*   **Regarde** : La ligne finissant par `/`. Si `Use%` est > 80%, Graham (Backup) doit purger les vieux fichiers.

---

## 👻 3. La Population (Qui vit ici ?)

### Le Recensement : `ps` (Process Status)
*   **Concept** : "Qui travaille en ce moment ?"
*   **Commande** : `ps aux | grep node`
*   **Traduction** : "Montre-moi tous (a) les utilisateurs (u) processus (x) et filtre (grep) pour 'node' (apps)."
*   **Résultat** : Tu devrais voir `OpenClaw` ou `react-scripts`.

### L'Identité : `whoami` & `hostname`
*   **Concept** : "En tant que qui suis-je connecté ?"
*   **Commande** : `whoami` -> Devrait être `root` (Mode Dieu).
*   **Commande** : `hostname` -> Devrait être `aspace-vps` (Ton Territoire).

---

## 🛡️ 4. Les Boucliers (Le Domaine de Yaz)

### Le Mur : `ufw` (Uncomplicated Firewall)
*   **Concept** : "Les portes sont-elles verrouillées ?"
*   **Commande** : `ufw status`
*   **Attendu** :
    *   `22/tcp ALLOW` (SSH - Ta Clé).
    *   `80, 443 ALLOW` (Web Traffic).
    *   Si tu vois `Anywhere` sur autre chose, sois prudent.

### Le Videur : `fail2ban`
*   **Concept** : "Qui avons-nous mis à la porte ?"
*   **Commande** : `fail2ban-client status sshd`
*   **Résultat** : Montre combien de tentatives non autorisées ont été bloquées.

---

## 🎓 L'Exercice (Ton Premier Audit)

1.  **Connexion** : `ssh root@...`
2.  **Maison** : `cd /root/aspace_a0_amadeus`
3.  **Vérifier la Structure** : `tree -L 2` (ou `ls -R` si tree est absent).
    *   *Vois-tu les dossiers du 11ème, 12ème et 13ème Docteur ?*
4.  **Vérifier les Ressources** : `htop`
    *   *La machine respire-t-elle bien ?*
5.  **Vérifier les Boucliers** : `ufw status`
    *   *Yaz monte-t-elle la garde ?*

*C'est ainsi qu'un Visionnaire touche le métal.*
