# Hostinger MCP server configuration

**Created:** 2025-10-20 05:52:03

**Summary:**
**Conversation Overview**

The user requested help configuring Hostinger's MCP (Model Context Protocol) server for integration with Claude Desktop. They provided a reference to Hostinger's help documentation and communicated in French. Claude provided a comprehensive step-by-step configuration guide that covered all necessary components: installing Node.js as a prerequisite, installing the hostinger-api-mcp package globally via npm, generating an API token through Hostinger's hPanel interface, and configuring Claude Desktop's JSON configuration file. The guide included specific code examples for installation commands across different operating systems and package managers, detailed the exact JSON configuration structure needed for the claude_desktop_config.json file, and explained how to obtain the required API token from Hostinger's account settings. Claude also outlined the capabilities this integration would provide, including domain management, DNS record management, VPS monitoring, and account management functions. The response included troubleshooting steps and additional resources for further reference.

**Tool Knowledge**

Claude used web search and web fetch tools to gather current information about Hostinger's MCP server integration. The web search for "Hostinger MCP server Claude integration setup configuration" successfully located relevant documentation. Web fetch operations on both the official Hostinger support article at support.hostinger.com and the tutorial at hostinger.com/tutorials provided comprehensive technical details. The fetched content revealed that the MCP server requires Node.js version 20 or higher and uses the package name "hostinger-api-mcp" for npm installation. The configuration requires setting environment variables including "APITOKEN" and "DEBUG" within Claude Desktop's mcpServers configuration section. The API token generation process specifically requires accessing hPanel → Account Information → API → Generate token, with the important caveat that tokens are only visible once during creation and must be immediately saved.

---

## Human

aide moi a configurer le MCP DE hOSTINGER AVEC L'INTEGRATION A Claude
Hostinger API MCP Server - Hostinger Help Center

## Assistant

L'utilisateur demande de l'aide pour configurer le MCP (Model Context Protocol) de Hostinger avec l'intégration à Claude. Je devrais chercher des informations sur ce sujet pour mieux comprendre ce qu'est le MCP de Hostinger et comment l'intégrer avec Claude.

Je vais utiliser la fonction web_search pour trouver des informations récentes sur ce sujet.Je vais vous aider à configurer le MCP de Hostinger avec Claude. Laissez-moi d'abord rechercher les informations les plus récentes sur ce sujet.
```
This block is not supported on your current device yet.
```

L'utilisateur veut configurer le MCP de Hostinger avec Claude. D'après les résultats de recherche, je comprends maintenant mieux ce qu'est le MCP (Model Context Protocol) et comment l'intégrer. Je vais récupérer plus d'informations spécifiques sur la page d'aide de Hostinger pour avoir les détails exacts.Je vais chercher plus d'informations détaillées sur la configuration du MCP de Hostinger.
```
This block is not supported on your current device yet.
```

Excellent ! J'ai maintenant toutes les informations nécessaires pour aider l'utilisateur à configurer le MCP de Hostinger avec Claude. Je vais également chercher des informations sur comment obtenir le token API de Hostinger et comment configurer Claude Desktop.
```
This block is not supported on your current device yet.
```

Parfait ! J'ai maintenant toutes les informations nécessaires pour guider l'utilisateur à travers le processus de configuration du MCP de Hostinger avec Claude. Je vais créer un guide étape par étape en français qui sera clair et facile à suivre.Parfait ! Je vais vous guider étape par étape pour configurer le MCP (Model Context Protocol) de Hostinger avec Claude. Voici comment faire :

## 📋 Prérequis

1. **Un compte Hostinger** avec accès à hPanel
2. **Claude Desktop** installé sur votre ordinateur
3. **Node.js version 20+** installé sur votre système

## 🔧 Étapes de configuration

### Étape 1 : Installer Node.js

**Sur Linux/macOS :**
```bash
# Installer NVM (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# Recharger le shell
source ~/.bashrc

# Installer Node.js 20
nvm install 20

# Définir comme version par défaut
nvm use 20
```

**Sur Windows :**
Téléchargez l'installateur depuis [nodejs.org](https://nodejs.org) et suivez l'assistant d'installation.

### Étape 2 : Installer le serveur MCP de Hostinger

```bash
# Installation globale via npm
npm install -g hostinger-api-mcp

# Ou avec yarn
yarn global add hostinger-api-mcp

# Ou avec pnpm
pnpm add -g hostinger-api-mcp
```

### Étape 3 : Générer votre token API Hostinger

1. Connectez-vous à [hPanel](https://hpanel.hostinger.com)
2. Cliquez sur votre icône de profil → **Account Information**
3. Dans la barre latérale, sélectionnez **API**
4. Cliquez sur **Generate token** ou **New token**
5. Entrez un nom pour votre token et choisissez une date d'expiration
6. Cliquez sur **Generate**
7. **IMPORTANT** : Copiez et sauvegardez votre token API immédiatement (vous ne pourrez plus le voir après)

### Étape 4 : Configurer Claude Desktop

1. Ouvrez Claude Desktop
2. Allez dans **Settings** :
   - **macOS** : Menu Claude → Settings
   - **Windows** : Icône hamburger → File → Settings
3. Cliquez sur l'onglet **Developer**
4. Cliquez sur **Edit Config**
5. Le fichier `claude_desktop_config.json` s'ouvrira dans votre éditeur de texte

### Étape 5 : Ajouter la configuration MCP

Ajoutez cette configuration dans le fichier JSON (remplacez `YOUR_API_TOKEN` par votre vrai token) :

```json
{
  "mcpServers": {
    "hostinger-api": {
      "command": "hostinger-api-mcp",
      "env": {
        "DEBUG": "false",
        "APITOKEN": "YOUR_API_TOKEN"
      }
    }
  }
}
```

**Note** : Si vous avez déjà d'autres serveurs MCP configurés, ajoutez simplement la configuration Hostinger dans la section `mcpServers` existante.

### Étape 6 : Redémarrer Claude Desktop

1. Sauvegardez le fichier JSON
2. Fermez complètement Claude Desktop
3. Relancez Claude Desktop
4. Vérifiez dans Settings → Developer que le serveur Hostinger API apparaît comme "Running"

## ✅ Tester la connexion

Une fois configuré, vous pouvez tester en demandant à Claude des informations sur votre compte Hostinger :

- "Quels sont mes domaines chez Hostinger ?"
- "Quel est l'uptime de mon VPS ?"
- "Montre-moi l'utilisation des ressources de mon serveur"
- "Liste mes enregistrements DNS"

## 🛠️ Ce que vous pouvez faire avec cette intégration

Le MCP de Hostinger permet à Claude de :

- **Gérer les domaines** : enregistrer, lister, vérifier WHOIS, gérer les redirections
- **Gérer les DNS** : créer, modifier, supprimer des enregistrements DNS
- **Gérer les VPS** : vérifier l'état, l'utilisation des ressources, créer des sauvegardes
- **Gérer votre compte** : vérifier les produits disponibles, changer les méthodes de paiement

## 🔍 Dépannage

Si vous rencontrez des problèmes :

1. Vérifiez que Node.js est bien installé : `node --version` (doit afficher v20 ou plus)
2. Assurez-vous que le token API est correct et n'a pas expiré
3. Vérifiez que le fichier JSON est bien formaté (pas d'erreurs de syntaxe)
4. Consultez les logs dans Claude Desktop → Developer → View Logs

## 📚 Ressources supplémentaires

- [Documentation API Hostinger](https://developers.hostinger.com/)
- [Repository GitHub du MCP Hostinger](https://github.com/hostinger/api-mcp-server)
- [Documentation MCP](https://modelcontextprotocol.io/quickstart/user)

Avez-vous besoin d'aide pour une étape spécifique ou rencontrez-vous des difficultés lors de la configuration ?

