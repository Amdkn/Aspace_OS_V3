# 🪐 RILCOT OS — V0

> **Le Cœur de Contrôle de la Flotte Souveraine (Layer 0)**
> *Conçu sous la doctrine E-Myth : Visionnaire (A0), Manager (A1), Architecte (A2) et Technicien (A3)*

---

## 1. Vision & Philosophie E-Myth

**RILCOT OS** est le tableau de bord d'exploitation central (Master Dashboard) d'**ASpace OS V2**. Il incarne l'alliance parfaite entre **la souveraineté technologique** et l'**efficacité organisationnelle** (Biomimétisme, Solarpunk et Low-Tech intelligente). 

Dans la pyramide de décision ASpace :
- **A0 (L'Entrepreneur / Visionnaire) :** Définit les horizons de croissance et la vision à long terme.
- **A1 (Le Manager) :** Structure les processus, gère le backlog et assure le respect de la doctrine.
- **A2 (L'Architecte) :** Traduit la vision en contrats techniques stricts (SDD ➔ PRD ➔ ADR).
- **A3 (Le Technicien) :** Exécute et assemble le code de manière propre et robuste (DDD).

---

## 2. Caractéristiques Techniques

RILCOT OS est une application moderne de type **Single Page Application (SPA)** hautement performante :

- **⚡ Core Stack :** React 19.x, Vite 6.x, TypeScript Strict et TailwindCSS.
- **🔐 Authentification & Data :** Intégration native et sécurisée avec **Supabase** (Auth, RLS et Realtime).
- **📊 Business Pulse :** Modules de monitoring financiers, agenda partagé, annuaire des membres et gestion de gouvernance.
- **🐳 Infrastructure :** Conteneurisation optimisée (Nginx Alpine) conçue pour un déploiement PaaS souverain.

---

## 3. Architecture du Projet

Le dépôt est organisé de manière hautement modulaire :

```
RILCOT-OS-V0/
├── components/          # Composants UI partagés (ex: Icons.tsx)
├── contexts/            # Fournisseurs de contextes applicatifs (AuthContext.tsx)
├── screens/             # Vues principales du Master Dashboard
│   ├── Dashboard.tsx    # Accueil & monitoring des activités
│   ├── Calendar.tsx     # Agenda partagé
│   ├── Directory.tsx    # Annuaire des membres ASpace
│   ├── Finance.tsx      # Jauges financières & Business Pulse
│   ├── Governance.tsx   # Documentation & protocoles
│   └── Settings.tsx     # Configuration du profil & déconnexion
├── services/            # Services de données (projets, documents)
├── lib/                 # Utilitaires et clients (supabase.ts)
├── Dockerfile           # Build multi-stage Node 20 ➔ Nginx Alpine
├── nginx.conf           # Configuration Nginx SPA Router
├── docker-compose.yml   # Orchestration de production locale/Coolify (Port 3000)
├── coolify.yaml         # Configuration déclarative pour le PaaS Coolify
└── tsconfig.node.json   # Configuration TypeScript pour les fichiers d'outils Vite
```

---

## 4. Guide de Déploiement Souverain (Coolify)

Pour déployer RILCOT OS sur votre instance **Coolify** (VPS 1 : `148.230.92.235`) :

### 🔸 Étape 1 : Variables d'environnement
Préparez les identifiants Supabase. Créez les clés suivantes dans les réglages de votre application Coolify :

```env
VITE_SUPABASE_URL=https://votre-projet.supabase.co
VITE_SUPABASE_ANON_KEY=votre-cle-anon-publique
```
> [!IMPORTANT]
> Ces variables doivent obligatoirement être configurées comme **Build-Time Variables** dans Coolify car Vite compile ces clés dans les fichiers statiques de production.

### 🔸 Étape 2 : Lancement
1. Liez ce dépôt GitHub à votre service Coolify.
2. Choisissez le buildpack **Docker Compose**.
3. Coolify utilisera automatiquement le fichier `docker-compose.yml` et compilera l'application SPA via le `Dockerfile` multi-stage, servant les actifs de production sur le **port 3000**.

---

## 5. Dépannage & Résolution Technique (RCA)

### 🚨 L'erreur du "tsconfig.node.json"
Si le build échouait précédemment avec l'erreur :
```bash
Error: ENOENT: no such file or directory, open '/app/tsconfig.node.json'
```
**Diagnostic :** Vite utilise TypeScript pour charger son propre fichier de configuration (`vite.config.ts`). L'absence de la configuration spécifique pour Node (`tsconfig.node.json`) bloquait le processus de transpilation.

**Solution :** Un fichier `tsconfig.node.json` a été ajouté à la racine pour standardiser les options de module (`ESNext`), de résolution (`bundler`) et autoriser les imports synthétiques. Le projet compile désormais sans friction.
