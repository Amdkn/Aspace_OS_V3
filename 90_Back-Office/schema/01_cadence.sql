-- =====================================================================
-- A'Space OS — la cadence, en relations
--
-- POURQUOI CE SCHEMA EXISTE
-- Le RDF dit ce qui est vrai ; il ne dit pas bien ce qui est *emboite* et
-- ce qui est *compte*. « 5 Scrums font 1 Sprint » est une contrainte
-- d'integrite, pas une assertion : elle doit pouvoir etre VIOLEE et
-- signalee, ce qu'un triplet ne sait pas faire.
--
-- Ce schema est donc la vue simplifiee d'apres-distillation : ce qu'on
-- regarde quand on veut savoir ou en est une vague, pas ce qu'on
-- interroge pour savoir pourquoi elle existe.
--
-- Cible : SQLite (aucun serveur, le fichier vit a cote du depot).
-- =====================================================================

PRAGMA foreign_keys = ON;

-- ---------------------------------------------------------------------
-- LES DEUX ETAGES ET LEURS COUCHES
-- L1 Life OS gouverne, L2 Business OS execute. Une couche appartient a
-- un etage et a exactement un rang.
-- ---------------------------------------------------------------------
CREATE TABLE etage (
  code        TEXT PRIMARY KEY,          -- 'L1' | 'L2'
  nom         TEXT NOT NULL,
  -- L'asymetrie temporelle est une PROPRIETE DE L'ETAGE, pas un reglage
  -- par vague. Business OS est comprime ; Life OS ne l'est pas, pour que
  -- l'arbitrage humain reste observable. Voir vague.duree_machine_s.
  compressible INTEGER NOT NULL CHECK (compressible IN (0,1))
);

CREATE TABLE couche (
  code      TEXT PRIMARY KEY,            -- A0..A3, B1..B3
  etage     TEXT REFERENCES etage(code),
  rang      INTEGER NOT NULL,            -- 1 = le plus haut de l'etage
  nom       TEXT NOT NULL,
  cadence   TEXT NOT NULL                -- 'quotidien'..'annuel'
);

-- ---------------------------------------------------------------------
-- L'EMBOITEMENT
-- La plus petite unite est la vague de Scrum. Tout le reste est un
-- agregat, et chaque agregat porte SA REGLE DE COMPTE.
--
--   5 Scrums (B3, quotidien)  = 1 Sprint
--   4 Sprints (B2, hebdo)     = 1 Rock
--   3 Rocks  (B1, mensuel)    = 1 Cycle 12WY   -> conseils A3, trimestriel
--   4 Cycles 12WY             = 1 annee civile -> vaisseaux A2, garde annuelle
--
-- `attendu` est ecrit en dur ici parce que c'est une decision du
-- proprietaire, pas une moyenne observee. Un agregat qui s'en ecarte doit
-- se voir (vue v_agregat_incomplet), pas se normaliser en silence.
-- ---------------------------------------------------------------------
CREATE TABLE genre_agregat (
  code        TEXT PRIMARY KEY,   -- 'scrum','sprint','rock','cycle','annee'
  contient    TEXT REFERENCES genre_agregat(code),
  attendu     INTEGER,            -- combien d'enfants font un parent
  couche      TEXT REFERENCES couche(code)
);

INSERT INTO etage (code, nom, compressible) VALUES
  ('L1', 'Life OS',     0),
  ('L2', 'Business OS', 1);

INSERT INTO couche (code, etage, rang, nom, cadence) VALUES
  ('A0','L1',0,'Amadeus — hors boucle de revue','—'),
  ('A1','L1',1,'Morty — Watcher, gatekeeper de complexite','annuel'),
  ('A2','L1',2,'Vaisseaux — garde de l''annee en cours','annuel'),
  ('A3','L1',3,'Conseils — coachs des cycles 12WY','trimestriel'),
  ('B1','L2',1,'Direction — Rocks','mensuel'),
  ('B2','L2',2,'Domaines — Sprints','hebdomadaire'),
  ('B3','L2',3,'Execution — Scrums','quotidien');

INSERT INTO genre_agregat (code, contient, attendu, couche) VALUES
  ('scrum',  NULL,     NULL, 'B3'),
  ('sprint', 'scrum',  5,    'B2'),
  ('rock',   'sprint', 4,    'B1'),
  ('cycle',  'rock',   3,    'A3'),
  ('annee',  'cycle',  4,    'A2');

-- ---------------------------------------------------------------------
-- LA VAGUE — l'unite reelle
-- Une vague est une execution datee. `parent` la range dans son agregat.
-- ---------------------------------------------------------------------
CREATE TABLE vague (
  id               INTEGER PRIMARY KEY,
  genre            TEXT NOT NULL REFERENCES genre_agregat(code),
  parent           INTEGER REFERENCES vague(id),
  libelle          TEXT NOT NULL,
  dossier          TEXT NOT NULL,   -- chemin relatif a la racine du depot
  ouverte_le       TEXT NOT NULL,   -- ISO 8601
  fermee_le        TEXT,
  -- Le temps machine reel. C'est LUI qui rend la compression mesurable au
  -- lieu de postulee : si une vague de Scrum tient sous 3600 s, le Sprint
  -- tient en 4-5 h. On ne le decrete pas, on le constate.
  duree_machine_s  INTEGER,
  statut           TEXT NOT NULL DEFAULT 'ouverte'
                   CHECK (statut IN ('ouverte','livree','revue','acceptee','rejetee'))
);

CREATE INDEX idx_vague_parent ON vague(parent);
CREATE INDEX idx_vague_genre  ON vague(genre, statut);

-- ---------------------------------------------------------------------
-- CE QUE LA REVUE REGARDE : dettes, avancees, apprentissages
-- Trois natures, une seule table : elles partagent le meme cycle de vie
-- et la meme page de revue. Les separer obligerait a trois requetes la
-- ou la page en fait une.
-- ---------------------------------------------------------------------
CREATE TABLE constat (
  id        INTEGER PRIMARY KEY,
  vague     INTEGER NOT NULL REFERENCES vague(id) ON DELETE CASCADE,
  nature    TEXT NOT NULL CHECK (nature IN ('dette','avancee','apprentissage')),
  titre     TEXT NOT NULL,
  detail    TEXT,
  -- Un constat sans preuve est une opinion. `preuve` porte le chemin d'une
  -- capture, d'un diff, d'un log ou d'une sortie reproductible — les 4
  -- formes du contrat de preuve B3.
  preuve    TEXT,
  poids     INTEGER NOT NULL DEFAULT 1 CHECK (poids BETWEEN 1 AND 5),
  ouvert    INTEGER NOT NULL DEFAULT 1 CHECK (ouvert IN (0,1))
);

CREATE INDEX idx_constat_vague ON constat(vague, nature);

-- ---------------------------------------------------------------------
-- L'ESCALADE DE REVUE — A3 -> A2 -> A1 -> le proprietaire
-- A0 n'y figure pas : il SORT de la boucle. Son absence de cette table
-- est la facon dont le schema fait respecter cette decision.
-- ---------------------------------------------------------------------
CREATE TABLE palier_revue (
  rang      INTEGER PRIMARY KEY,
  acteur    TEXT NOT NULL,
  porte     TEXT NOT NULL
);

INSERT INTO palier_revue (rang, acteur, porte) VALUES
  (1, 'A3', 'conseils — accepte le cycle 12WY ou renvoie le Rock'),
  (2, 'A2', 'vaisseaux — garde l''alignement de l''annee en cours'),
  (3, 'A1', 'Morty — gatekeeper de complexite, dernier filtre machine'),
  (4, 'human:amdkn', 'le proprietaire — seul a pouvoir apposer le verdict');

CREATE TABLE revue (
  id         INTEGER PRIMARY KEY,
  vague      INTEGER NOT NULL REFERENCES vague(id) ON DELETE CASCADE,
  palier     INTEGER NOT NULL REFERENCES palier_revue(rang),
  acteur     TEXT NOT NULL,
  verdict    TEXT NOT NULL CHECK (verdict IN ('accepte','renvoye','escalade')),
  motif      TEXT,
  au         TEXT NOT NULL,
  UNIQUE (vague, palier, acteur)
);

-- ---------------------------------------------------------------------
-- LA JONCTION VERS LE CORPUS OKF
-- Le SQL ne duplique pas les concepts : il pointe vers eux. Dupliquer
-- ferait deux sources de verite, et celle qui derive en silence est
-- toujours celle qu'on regarde.
-- ---------------------------------------------------------------------
CREATE TABLE concept_lie (
  vague     INTEGER NOT NULL REFERENCES vague(id) ON DELETE CASCADE,
  chemin    TEXT NOT NULL,          -- relatif a la racine du depot
  confiance TEXT NOT NULL CHECK (confiance IN ('non_verifie','machine','humain')),
  PRIMARY KEY (vague, chemin)
);

-- =====================================================================
-- VUES — ce que les pages HTML consomment
-- =====================================================================

-- Un agregat dont le compte d'enfants s'ecarte de la regle. C'est la
-- premiere chose qu'une page de revue doit montrer : non pas « tout va
-- bien », mais « voici ce qui ne ferme pas ».
CREATE VIEW v_agregat_incomplet AS
SELECT p.id, p.genre, p.libelle, g.attendu,
       COUNT(e.id) AS observe,
       COUNT(e.id) - g.attendu AS ecart
FROM vague p
JOIN genre_agregat g ON g.code = p.genre
LEFT JOIN vague e ON e.parent = p.id
WHERE g.attendu IS NOT NULL
GROUP BY p.id
HAVING COUNT(e.id) <> g.attendu;

-- La compression, mesuree et non postulee. Une vague de Scrum sous 3600 s
-- rend la commodite temporelle vraie pour son Sprint parent.
CREATE VIEW v_compression AS
SELECT v.id, v.genre, v.libelle, v.duree_machine_s,
       e.compressible,
       CASE
         WHEN v.duree_machine_s IS NULL          THEN 'non mesure'
         WHEN e.compressible = 0                 THEN 'non comprime (delibere)'
         WHEN v.genre = 'scrum'
              AND v.duree_machine_s < 3600       THEN 'commodite atteinte'
         ELSE 'sous le seuil'
       END AS verdict_temporel
FROM vague v
JOIN genre_agregat g ON g.code = v.genre
JOIN couche c ON c.code = g.couche
JOIN etage e ON e.code = c.etage;

-- L'etat de revue d'une vague : ou en est l'escalade, et ce qui bloque.
-- Les agregats sont calcules en sous-requetes correlees et NON par un
-- GROUP BY sur une double jointure : joindre `revue` et `constat` a la
-- fois multiplierait les lignes et gonflerait le compte de dettes par le
-- nombre de paliers franchis. Un tableau de bord qui exagere la dette est
-- aussi faux qu'un tableau de bord qui la cache.
CREATE VIEW v_escalade AS
SELECT v.id, v.libelle, v.statut,
       (SELECT MAX(r.palier) FROM revue r
         WHERE r.vague = v.id AND r.verdict <> 'renvoye') AS palier_atteint,
       (SELECT p.acteur FROM palier_revue p
         WHERE p.rang = COALESCE(
                 (SELECT MAX(r.palier) FROM revue r
                   WHERE r.vague = v.id AND r.verdict <> 'renvoye'), 0) + 1)
         AS prochain_acteur,
       (SELECT COUNT(*) FROM constat c
         WHERE c.vague = v.id AND c.nature = 'dette' AND c.ouvert = 1)
         AS dettes_ouvertes
FROM vague v;

-- La dette de revue du corpus : combien de concepts attendent encore un
-- humain. C'est le chiffre que le tableau de bord A3 doit afficher en
-- premier, parce que c'est le seul goulot qu'aucun agent ne peut lever.
CREATE VIEW v_dette_revue AS
SELECT confiance, COUNT(*) AS n
FROM concept_lie
GROUP BY confiance;
