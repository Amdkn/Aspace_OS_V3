# SPEC Jerry Business Pulse v2 — historisation mensuelle du pulse

> Ruban φ. Test du ruban : GO permanent, aucune question à l'opérateur.
> Chemin : `C:/Users/amado/ASpace_OS_V3/00_Amadeus/60_Tape_Specs/2026-09-02-spec-jerry-business-pulse-v2.md`
> Base existante (v1, mesurée le 2026-09-02) : 4 variantes prime/bio/nexus/solarpunk avec `pulse.json` (3 métriques à zéro), `00_Registre/registre.json` version `v1`, `verifier.py` affichant `PULSE_OK` (rc=0). Preuve : lecture directe des fichiers + arborescence.

---

## 1. Objectif

Ajouter l'historisation mensuelle du pulse B1 : chaque mois, un snapshot JSON
par variante est produit depuis le `pulse.json` courant, de façon idempotente,
et le vérificateur couvre v0 + v1 + v2. `PULSE_OK` signifie : les trois
niveaux verts.

## 2. Périmètre

- IN : `30_Business_OS/00_Jerry_Business_Pulse/` uniquement —
  nouveau dossier `00_Registre/historique/`, nouveau script `snapshot.py`,
  extension de `verifier.py`, passage du registre à `version: v2`.
- OUT : aucun changement aux 4 `pulse.json`, aux README de variantes, au
  README racine, à la structure des dossiers de variantes.

## 3. Structure fichiers exacte (état final)

```
00_Jerry_Business_Pulse/
├── README.md                        (inchangé)
├── verifier.py                      (étendu v2)
├── snapshot.py                      (NOUVEAU)
└── 00_Registre/
    ├── registre.json                (version: "v2", champ historisation ajouté)
    └── historique/                  (NOUVEAU dossier)
        ├── hist-prime-2026-09.json
        ├── hist-bio-2026-09.json
        ├── hist-nexus-2026-09.json
        └── hist-solarpunk-2026-09.json
```

## 4. Format JSON exact

### 4.1 registre.json (v2)

Identique à v1 sauf :
- `"version": "v2"` (au lieu de `v1`) ;
- champ ajouté après `date_init` : `"historisation": {"dossier": "00_Registre/historique", "format": "hist-<variante>-<AAAA-MM>.json", "actif": true}`.

Les 4 entrées `variantes` restent strictement identiques (id, nom, dossier,
cree) et dans l'ordre prime, bio, nexus, solarpunk.

### 4.2 Snapshot `hist-<variante>-<AAAA-MM>.json`

Un fichier par variante et par mois. Exemple pour prime, septembre 2026 :

```json
{
  "variante": "prime",
  "mois": "2026-09",
  "metriques": {
    "revenus_mois": 0,
    "clients_actifs": 0,
    "offres_lancees": 0
  },
  "horodatage": "2026-09-02T12:00:00"
}
```

Règles :
- `variante` : id de la variante (prime|bio|nexus|solarpunk).
- `mois` : `AAAA-MM` du mois courant au moment de la génération, dérivé de
  `datetime.now()` local.
- `metriques` : copie intégrale et exacte de l'objet `metriques` du
  `pulse.json` courant de la variante (noms de champs identiques : 3 clés
  v1 ; toute clé future du pulse est copiée telle quelle).
- `horodatage` : ISO 8601 local, `datetime.now().strftime("%Y-%m-%dT%H:%M:%S")`.
- Encodage UTF-8, `json.dump(..., indent=2, ensure_ascii=False)` + saut de
  ligne final.

## 5. snapshot.py — comportement exact

- Chemin : racine du module (`BASE = os.path.dirname(os.path.abspath(__file__))`).
- Stdlib uniquement (os, sys, json, datetime).
- Invocation : `python snapshot.py` (aucun argument requis).
- Algorithme :
  1. `mois = datetime.now().strftime("%Y-%m")` (une seule fois, en tête).
  2. Créer `00_Registre/historique/` si absent (`os.makedirs(..., exist_ok=True)`).
  3. Pour chaque variante dans l'ordre prime, bio, nexus, solarpunk :
     lire `<dossier>/pulse.json`, construire le snapshot (§4.2), écrire
     `00_Registre/historique/hist-<variante>-<mois>.json`.
  4. **Idempotence** : le contenu est déterministe SAUF `horodatage`. Pour
     garantir la régénération du même fichier : si le fichier cible existe
     déjà et contient un snapshot valide pour le même `variante`/`mois` avec
     les mêmes `metriques`, réécrire le fichier à l'identique en conservant
     l'`horodatage` existant (ne pas le rafraîchir). Sinon, écrire avec un
     nouvel `horodatage`. Résultat : deux exécutions successives dans le
     même mois, sans changement de métrique, produisent un fichier
     octet-pour-octet identique.
- Sortie : une ligne par snapshot, `OK <fichier>`, puis `SNAPSHOTS_OK`, rc=0.
  En cas d'erreur (pulse.json illisible/absent) : `SNAPSHOTS_KO`, message
  `  ERREUR: ...`, rc=1.
- Pas de dépendance à verifier.py ni à registre.json pour la génération
  (la liste des variantes est une constante du script, alignée sur
  verifier.py).

## 6. verifier.py — extension v2

Conserver intégralement tous les checks v0 et v1 existants (mêmes messages,
mêmes constantes), puis ajouter, avant le verdict final :

1. **[v2] registre version v2** : `registre.json` → `version == "v2"`.
   (Le check v1 existant `version != v1` est remplacé par celui-ci — un seul
   check de version, attendu `v2`.) Le nouveau champ `historisation` est
   vérifié : `dossier == "00_Registre/historique"`, `actif == true`.
2. **[v2] historique/ présent** : `00_Registre/historique` existe et est un
   dossier.
3. **[v2] snapshots valides** : pour chaque variante, le fichier
   `hist-<variante>-<mois_courant>.json` (mois courant calculé au moment du
   check) existe, est un JSON valide, et respecte le format §4.2 :
   `variante` correct, `mois` = mois courant, `metriques` = objet contenant
   au minimum les 3 clés `revenus_mois`, `clients_actifs`, `offres_lancees`
   de type number, `horodatage` = chaîne non vide.
- Docstring mise à jour : titre v2, liste des checks [v2], même référence
  de spec. Encodage ASCII conservé (style du fichier v1).
- Verdict inchangé : `PULSE_OK` + rc=0 si tout passe, sinon `PULSE_KO` +
  rc=1. Le sens de `PULSE_OK` devient : v0 + v1 + v2 tous verts.

## 7. Critères d'acceptation exécutables

Depuis `C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/` :

1. `python verifier.py` → sortie `PULSE_OK`, rc=0. (Check A2A complet :
   v0 + v1 + v2 verts.)
2. `python snapshot.py` → rc=0, sortie `SNAPSHOTS_OK`, 4 lignes `OK ...`.
3. Idempotence : `python snapshot.py && python snapshot.py` → rc=0 les deux
   fois, et le hash des 4 snapshots est identique entre les deux exécutions
   (aucun `horodatage` rafraîchi à tord).
4. `hist-<variante>-<AAAA-MM_courant>.json` existe pour chacune des 4
   variantes dans `00_Registre/historique/` et parse en JSON valide avec les
   champs du §4.2, `metriques` identiques au `pulse.json` courant.
5. `registre.json` : `version == "v2"`, champ `historisation` présent, 4
   variantes inchangées et dans l'ordre.
6. Aucun `pulse.json` modifié (statut reste `v1-initialise`, métriques à
   zéro) ; aucun README modifié.
7. `python snapshot.py` et `python verifier.py` fonctionnent en stdlib pur
   (aucun import tiers).

## 8. Rappels de preuve

- "Fait" = chemin vérifié + rc + lecture de retour.
- Idempotence vérifiée par hash (critère 3), pas par intention.
- Aucune question à l'opérateur : toute ambiguïté restante invalide le ruban
  et le retourne à `_INBOX`.
