"""Genere un tableau d'arbitrage HTML pour les contradictions de CONSOLIDE.json.

POURQUOI
204 contradictions ne se traitent pas en prose : il faut voir, filtrer, trancher
et exporter. Ce script produit un fichier HTML autonome (aucun serveur, aucune
dependance) que l'on ouvre dans un navigateur.

CE QU'IL FAIT
1. Charge CONSOLIDE.json, fusionne les sujets identiques (46 doublons sur 204).
2. Range chaque contradiction dans une FAMILLE DE CAUSE -- le canon du poste dit
   de decouper par cause, pas par surface : cinq causes expliquaient la moitie
   des defauts visuels de Coach OS.
3. Marque le STATUT VERIFIE quand une mesure a ete faite sur le corpus actuel.
   Le catalogue date du 2026-08-13 : plusieurs familles sont deja mortes, et les
   presenter comme vivantes ferait perdre du temps sur des decisions inutiles.
4. Ecrit un HTML avec filtres, choix par contradiction, compteurs et export.

L'export rend un JSON de decisions + un markdown lisible, telecharges par le
navigateur. Rien n'est ecrit sur le disque par ce script en dehors du HTML.

    python generer_arbitrage.py
"""

import json
import pathlib
import re
from collections import OrderedDict

RACINE = pathlib.Path(__file__).resolve().parent
SOURCE = RACINE / "CONSOLIDE.json"
SORTIE = RACINE / "ARBITRAGE_CONTRADICTIONS.html"

# --- Familles de cause -------------------------------------------------------
# Ordre important : la premiere regle qui matche gagne. Les regles les plus
# specifiques sont donc en tete.
FAMILLES = [
    ("sales-g2", "Domaine Sales / G2 — archetype et 8e domaine",
     r"john\s?jones|manhunter|sales b2|illuminati|nombre de (business )?domain|domaines business wheel|8 domaines|map count|sales.*cognition|sales kr"),
    ("commandement", "Deux ontologies de commandement (B1/B2/B3 vs T1/T2/T3)",
     r"summers.*omk|b1/b2/b3|t1/t2/t3|triptyque|sob \(b0\)|b0 self-operating|b1/b2 vs 12wy|b1 vs 12wy"),
    ("horizons", "Horizons des officiers (Saru / Book / Picard, H1/H3/H10)",
     r"saru|book.*h1|h10|horizon|picard h"),
    ("cycle", "Duree du cycle 12WY (84 jours, 12 semaines, W13)",
     r"w1-w12|84 jours|21 jours|w13|cycle length|cycle court"),
    ("rosters", "Taille des escouades B3 (4 vs 6 vs 8 membres)",
     r"roster|squad|swarm_config|members|topology"),
    ("mesures", "Mesures datees (drift, pas contradiction)",
     r"compte de|count des|nombre de pages|volume|conformite description|14 ?951|14 ?613|jonctions"),
    ("typos", "Coquilles, encodage et casse",
     r"coquille|creatry|caractere chinois|caracteres chinois|cerriros|orthographe|double espace|casse des|template variable|inconsistante|no space"),
    ("slots", "Numerotation des slots et doublons de dossier",
     r"05_legal|08_legal|slot canon|04_finance|doublons de folder|folder naming|nom de folder"),
    ("adr", "ADR manquants, index et collisions d'identifiant",
     r"\badr\b|meta-006|id collision|index l2 count"),
    ("seuils", "Seuils et niveaux (YELLOW, sommeil, capital)",
     r"yellow|seuil|sleep|niveaux"),
    ("devise", "Devise EUR vs USD",
     r"eur|usd|pricing"),
    # --- familles tirees de l'inspection du fourre-tout « divers » ---
    ("statut", "Statuts perimes (fait / en cours / retrograde)",
     r"stale|status|statut|en cours vs construit|retrograded|runtime actif|closure|coverage j03"),
    ("vides", "Artefacts vides ou incomplets (gabarits jamais remplis)",
     r"empty|vide|incomplet|placeholder|non rempli|non reclassifi|manquant"),
    ("projets", "Divergences entre projets BOS (ABC / marina / RILCOT / Alikaly)",
     r"02 abc|05 marina|03 rilcot|04 alikaly|priority_domains|prioritaires|jtbd growth|frontmatter"),
    ("compagnons", "Perimetre des compagnons et officiers (Nardole, Bill, Donna, Tendi)",
     r"nardole|companion|\bbill\b|tendi|rutherford|cerritos|curie|donna"),
    ("jerry", "Jerry — divergences de doctrine entre ses variantes",
     r"jerry"),
    ("doctrine", "Doctrines concurrentes (Paperclip, Solarpunk, AaaS, GO)",
     r"paperclip|solarpunk|aaas|go perpetuel|go triennal|hospital planet|doctrine"),
    ("principes", "Comptes de principes et de KPI (off-by-one, versions)",
     r"principles|principes|\bpe\d|\bkpi|f13-f18|persona"),
    ("jumeaux", "Dossiers jumeaux, clones et prototypes concurrents",
     r"sister|jumeau|clone|prototype|rilcot-os-v2|geordi 0|variant"),
    ("plateformes", "Source de verite entre plateformes (Notion, ClickUp, Airtable, Hermes)",
     r"notion|clickup|airtable|symphony|hermes|tri-plateforme"),
    ("evidence", "Niveau de preuve et bibliographies",
     r"bibliograph|evidence|hypothesis|d6 nuance|d1 verified|calibration"),
    ("owner", "Proprietaires et mappings (LD <-> domaine, owner)",
     r"owner|mapping|ancre ld|driver b1|parent_a2|constitution|tier 1|lead lag|muse|format des kr"),
]

# --- Statuts verifies sur le corpus actuel ------------------------------------
# Renseigne uniquement quand une mesure a ete faite. Ne jamais deviner ici :
# un statut suppose vaut moins que pas de statut du tout.
VERIFIE = {
    "sales-g2": {
        "statut": "resolu",
        "note": ("Mesure 2026-08-29 : `John Jones` rend ZERO occurrence dans le PARA. "
                 "Les cinq projets portent `02_Sales_MartianManhunter_Illuminati` en B2 et B3. "
                 "Le renommage W40 V4 est propage, fichiers ET contenu. "
                 "Reste un seul ecart reel : `01-omk-business-os` n'a que 6 domaines "
                 "(Growth et Sales absents) quand les quatre autres en ont 8."),
    },
    "slots": {
        "statut": "resolu",
        "note": ("Mesure 2026-08-29 : `07_People_GreenLantern_XMen` et `08_Legal_Aquaman_Eternals` "
                 "sont unanimes sur les cinq projets, conformes a ONTOLOGIE_V2 (G7 People, G8 Legal). "
                 "La variante `05_Legal` n'existe plus."),
    },
    "typos": {
        "statut": "partiel",
        "note": ("Mesure 2026-08-29 : `Creatry` et `CERRIROS` rendent ZERO occurrence -- corriges. "
                 "Les caracteres chinois et les variantes Alykaly n'ont PAS ete reverifies "
                 "(sonde interrompue par depassement de delai)."),
    },
    "mesures": {
        "statut": "hors-sujet",
        "note": ("Ce ne sont pas des contradictions mais des mesures prises a des dates "
                 "differentes sur un corpus qui bouge. Les arbitrer n'a pas de sens : "
                 "il faut redater, pas trancher."),
    },
}

STATUT_LIBELLE = {
    "resolu": "deja resolu",
    "partiel": "partiellement resolu",
    "hors-sujet": "hors sujet",
    "vivant": "a verifier",
}


def sans_accents(s):
    """Normalisation grossiere pour que les regles matchent malgre les accents."""
    table = str.maketrans("àâäéèêëîïôöùûüçÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ'’", "aaaeeeeiioouuucAAAEEEEIIOOUUUC  ")
    return s.translate(table).lower()


def famille_de(sujet):
    s = sans_accents(sujet)
    for cle, libelle, motif in FAMILLES:
        if re.search(motif, s):
            return cle, libelle
    return "divers", "Divers — sans famille identifiee"


def main():
    donnees = json.loads(SOURCE.read_text(encoding="utf-8", errors="ignore"))
    brutes = donnees["contradictions"]

    # Fusion des sujets identiques : on garde toutes les paires de chemins.
    fusion = OrderedDict()
    for x in brutes:
        sujet = (x.get("sujet") or "").strip()
        if not sujet:
            continue
        entree = fusion.setdefault(sujet, {"sujet": sujet, "occurrences": 0, "paires": []})
        entree["occurrences"] += 1
        paire = {
            "a": (x.get("chemin_a") or "").strip(),
            "da": (x.get("date_a") or "").strip(),
            "b": (x.get("chemin_b") or "").strip(),
            "db": (x.get("date_b") or "").strip(),
        }
        if paire not in entree["paires"]:
            entree["paires"].append(paire)

    items = []
    for i, e in enumerate(fusion.values(), 1):
        cle, libelle = famille_de(e["sujet"])
        v = VERIFIE.get(cle, {})
        items.append({
            "id": "C%03d" % i,
            "sujet": e["sujet"],
            "occurrences": e["occurrences"],
            "paires": e["paires"],
            "famille": cle,
            "famille_libelle": libelle,
            "statut": v.get("statut", "vivant"),
            "note": v.get("note", ""),
        })

    familles = OrderedDict()
    for it in items:
        f = familles.setdefault(it["famille"], {
            "cle": it["famille"], "libelle": it["famille_libelle"],
            "n": 0, "statut": it["statut"], "note": it["note"],
        })
        f["n"] += 1

    charge = {
        "genere_le": donnees.get("genere"),
        "total_brut": len(brutes),
        "total_fusionne": len(items),
        "couverture": donnees.get("couverture"),
        "familles": list(familles.values()),
        "items": items,
        "libelles_statut": STATUT_LIBELLE,
    }

    html = GABARIT.replace("/*__DONNEES__*/", json.dumps(charge, ensure_ascii=False))
    SORTIE.write_text(html, encoding="utf-8")
    print("ecrit : %s" % SORTIE)
    print("  %d contradictions brutes -> %d apres fusion des doublons" % (len(brutes), len(items)))
    print("  familles :")
    for f in sorted(familles.values(), key=lambda z: -z["n"]):
        print("    %-13s %3d  [%s]" % (f["cle"], f["n"], STATUT_LIBELLE.get(f["statut"], f["statut"])))


GABARIT = r"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Arbitrage des contradictions — A'Space OS</title>
<style>
:root{
  --fond:#0f1115; --carte:#171a21; --carte2:#1d2129; --bord:#2a2f3a;
  --texte:#e6e8ee; --doux:#9aa3b2; --accent:#7aa2f7;
  --ok:#7dcfa0; --attention:#e0af68; --mort:#6b7280; --vif:#f7768e;
}
*{box-sizing:border-box}
body{margin:0;background:var(--fond);color:var(--texte);
     font:15px/1.55 ui-sans-serif,system-ui,"Segoe UI",Roboto,sans-serif}
header{position:sticky;top:0;z-index:20;background:rgba(15,17,21,.96);
       border-bottom:1px solid var(--bord);padding:14px 20px;backdrop-filter:blur(8px)}
h1{margin:0 0 4px;font-size:17px;letter-spacing:.2px}
.sous{color:var(--doux);font-size:12.5px}
.barre{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:10px}
.filtre{background:var(--carte2);border:1px solid var(--bord);color:var(--texte);
        padding:5px 11px;border-radius:999px;cursor:pointer;font-size:12.5px}
.filtre.on{background:var(--accent);color:#0b0d11;border-color:var(--accent);font-weight:600}
/* Bloc de familles pliable : 23 puces occupaient la moitie de l'ecran et
   repoussaient les contradictions hors de vue. Replie par defaut. */
.plieur{display:flex;align-items:center;gap:9px;margin-top:10px;flex-wrap:wrap}
.bouton-plier{background:var(--carte2);border:1px solid var(--bord);color:var(--texte);
              padding:5px 12px;border-radius:7px;cursor:pointer;font-size:12.5px;
              display:inline-flex;align-items:center;gap:7px}
.bouton-plier:hover{border-color:var(--accent)}
.chevron{display:inline-block;transition:transform .15s ease;font-size:10px;opacity:.75}
.ouvert .chevron{transform:rotate(90deg)}
.actif{font-size:12.5px;color:var(--doux)}
.actif b{color:var(--accent);font-weight:650}
#filtres{max-height:0;overflow:hidden;opacity:0;transition:max-height .2s ease,opacity .15s ease;
         margin-top:0}
#filtres.deplie{max-height:60vh;overflow:auto;opacity:1;margin-top:10px}
.espace{flex:1}
button.action{background:var(--accent);color:#0b0d11;border:0;padding:8px 15px;
              border-radius:7px;font-weight:650;cursor:pointer;font-size:13px}
button.fant{background:transparent;color:var(--texte);border:1px solid var(--bord)}
main{padding:18px 20px 90px;max-width:1180px;margin:0 auto}
.fam{margin:22px 0 10px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.fam h2{margin:0;font-size:14.5px;font-weight:650}
.puce{font-size:11px;padding:2px 9px;border-radius:999px;border:1px solid var(--bord);color:var(--doux)}
.puce.resolu{color:var(--ok);border-color:#2c4a3a}
.puce.partiel{color:var(--attention);border-color:#4a3f2c}
.puce.hors-sujet{color:var(--mort);border-color:#333}
.puce.vivant{color:var(--vif);border-color:#4a2c33}
.note{width:100%;color:var(--doux);font-size:12.5px;background:var(--carte);
      border-left:3px solid var(--bord);padding:9px 12px;border-radius:0 6px 6px 0;margin-top:4px}
.item{background:var(--carte);border:1px solid var(--bord);border-radius:9px;
      padding:13px 15px;margin-bottom:9px}
.item.trancheA{border-color:#2f6f4f}
.item.trancheB{border-color:#2f5a8f}
.item.ignore{opacity:.42}
.tete{display:flex;gap:10px;align-items:flex-start}
.ref{color:var(--doux);font:12px ui-monospace,SFMono-Regular,Menlo,monospace;flex:0 0 auto;padding-top:2px}
.sujet{font-weight:600;font-size:14px;flex:1}
.mult{font-size:11px;color:var(--attention);border:1px solid #4a3f2c;padding:1px 7px;border-radius:999px}
.paires{margin:10px 0 0;display:grid;gap:7px}
.paire{display:grid;grid-template-columns:1fr 1fr;gap:9px}
.cote{background:var(--carte2);border:1px solid var(--bord);border-radius:7px;padding:8px 10px;
      font:11.5px/1.5 ui-monospace,SFMono-Regular,Menlo,monospace;color:#c8cddb;
      word-break:break-word;overflow-wrap:anywhere}
.cote .eti{display:block;color:var(--doux);font-size:10px;letter-spacing:.6px;margin-bottom:3px;
           font-family:ui-sans-serif,system-ui}
.choix{display:flex;gap:7px;flex-wrap:wrap;margin-top:11px;align-items:center}
.choix label{font-size:12.5px;background:var(--carte2);border:1px solid var(--bord);
             padding:5px 11px;border-radius:7px;cursor:pointer;user-select:none}
.choix input{margin-right:5px;vertical-align:-1px}
.choix label:has(input:checked){border-color:var(--accent);background:#1b2231}
.motif{margin-top:9px;width:100%;background:var(--carte2);border:1px solid var(--bord);
       color:var(--texte);border-radius:7px;padding:7px 10px;font-size:12.5px;font-family:inherit}
footer{position:fixed;bottom:0;left:0;right:0;background:rgba(15,17,21,.97);
       border-top:1px solid var(--bord);padding:11px 20px;display:flex;gap:12px;
       align-items:center;backdrop-filter:blur(8px);z-index:20}
.compteur{font-size:13px;color:var(--doux)}
.compteur b{color:var(--texte)}
.vide{color:var(--doux);padding:30px;text-align:center}
</style>
</head>
<body>
<header>
  <h1>Arbitrage des contradictions — A'Space OS</h1>
  <div class="sous" id="entete"></div>
  <div class="plieur" id="plieur">
    <button class="bouton-plier" onclick="plier()">
      <span class="chevron">&#9654;</span><span id="etiq_plier">Familles</span>
    </button>
    <span class="actif" id="filtre_actif"></span>
  </div>
  <div class="barre" id="filtres"></div>
  <div class="barre">
    <button class="action" onclick="exporter('json')">Exporter les décisions (JSON)</button>
    <button class="action fant" onclick="exporter('md')">Exporter en Markdown</button>
    <button class="action fant" onclick="toutIgnorerResolus()">Marquer « déjà résolu » les familles vérifiées</button>
    <span class="espace"></span>
    <button class="action fant" onclick="reinit()">Réinitialiser</button>
  </div>
</header>
<main id="corps"></main>
<footer>
  <span class="compteur" id="compteur"></span>
  <span class="espace"></span>
  <span class="compteur" id="avis_stockage"></span>
</footer>
<script>
const D = /*__DONNEES__*/;
const CLE = "arbitrage_contradictions_v1";

// localStorage LEVE sur une origine opaque : un fichier ouvert en file:// ou
// servi en data: n'a pas de stockage. Sans ce garde, l'exception avortait tout
// le script et la page restait VIDE, entete et corps compris. Paye le
// 2026-08-29 en verifiant la page au lieu de la livrer sans la regarder.
const STOCK = (function(){
  try { const t="__t"; localStorage.setItem(t,"1"); localStorage.removeItem(t); return localStorage; }
  catch(e){ return null; }
})();
let etat = {};
try { if(STOCK) etat = JSON.parse(STOCK.getItem(CLE) || "{}"); } catch(e){ etat = {}; }
let filtre = "tout";

function sauver(){
  try { if(STOCK) STOCK.setItem(CLE, JSON.stringify(etat)); } catch(e){}
  majCompteur();
}

function majCompteur(){
  const n = D.items.length;
  const d = Object.values(etat).filter(x => x && x.choix).length;
  document.getElementById("compteur").innerHTML =
    "<b>" + d + "</b> / " + n + " contradictions tranchées";
}

let deplie = false;
try { if(STOCK) deplie = STOCK.getItem(CLE+"_deplie") === "1"; } catch(e){}

function plier(){
  deplie = !deplie;
  appliquerPli();
  try { if(STOCK) STOCK.setItem(CLE+"_deplie", deplie ? "1" : "0"); } catch(e){}
}
function appliquerPli(){
  document.getElementById("filtres").classList.toggle("deplie", deplie);
  document.getElementById("plieur").classList.toggle("ouvert", deplie);
  document.getElementById("etiq_plier").textContent = deplie ? "Masquer les familles" : "Familles";
}
function libelleDe(cle){
  if(cle==="tout") return "Tout";
  const f = D.familles.find(x=>x.cle===cle);
  return f ? f.libelle : cle;
}
function majFiltreActif(){
  const n = filtre==="tout" ? D.items.length
          : (D.familles.find(x=>x.cle===filtre)||{n:0}).n;
  document.getElementById("filtre_actif").innerHTML =
    "Filtre : <b>" + esc(libelleDe(filtre)) + "</b> — " + n + " contradiction" + (n>1?"s":"");
}

function rendreFiltres(){
  const c = document.getElementById("filtres");
  const fams = [{cle:"tout", libelle:"Tout", n:D.items.length, statut:""}].concat(
    D.familles.slice().sort((a,b)=>b.n-a.n));
  c.innerHTML = fams.map(f =>
    `<button class="filtre ${f.cle===filtre?'on':''}" onclick="setFiltre('${f.cle}')">`+
    `${esc(f.libelle)} <span style="opacity:.7">${f.n}</span></button>`).join("");
  majFiltreActif();
}
// Choisir une famille replie le bloc : on veut voir les contradictions,
// pas la liste des familles qu'on vient de quitter.
function setFiltre(f){
  filtre=f; rendreFiltres(); rendre();
  if(deplie) plier();
  window.scrollTo({top:0, behavior:"smooth"});
}

function choisir(id, val){
  etat[id] = etat[id] || {};
  etat[id].choix = val;
  sauver();
  const el = document.getElementById("i_"+id);
  el.className = "item" + (val==="A" ? " trancheA" : val==="B" ? " trancheB"
                 : (val==="ignore"||val==="resolu") ? " ignore" : "");
}
function motif(id, v){ etat[id]=etat[id]||{}; etat[id].motif=v; sauver(); }

function rendre(){
  const corps = document.getElementById("corps");
  const vus = filtre==="tout" ? D.items : D.items.filter(i=>i.famille===filtre);
  if(!vus.length){ corps.innerHTML='<div class="vide">Rien dans ce filtre.</div>'; return; }
  const parFam = {};
  vus.forEach(i => (parFam[i.famille]=parFam[i.famille]||[]).push(i));
  let h = "";
  for(const cle in parFam){
    const f = D.familles.find(x=>x.cle===cle) || {libelle:cle, statut:"vivant", note:""};
    h += `<div class="fam"><h2>${f.libelle}</h2>`+
         `<span class="puce ${f.statut}">${D.libelles_statut[f.statut]||f.statut}</span>`+
         `<span class="puce">${parFam[cle].length}</span>`+
         (f.note ? `<div class="note">${f.note}</div>` : "")+`</div>`;
    parFam[cle].forEach(i => { h += carte(i); });
  }
  corps.innerHTML = h;
}

function carte(i){
  const e = etat[i.id] || {};
  const cls = e.choix==="A" ? " trancheA" : e.choix==="B" ? " trancheB"
            : (e.choix==="ignore"||e.choix==="resolu") ? " ignore" : "";
  const paires = i.paires.map(p => `
    <div class="paire">
      <div class="cote"><span class="eti">VERSION A ${p.da?("· "+p.da):""}</span>${esc(p.a)||"—"}</div>
      <div class="cote"><span class="eti">VERSION B ${p.db?("· "+p.db):""}</span>${esc(p.b)||"—"}</div>
    </div>`).join("");
  const opt = (v,t)=>`<label><input type="radio" name="ch_${i.id}" value="${v}"
      ${e.choix===v?"checked":""} onchange="choisir('${i.id}','${v}')">${t}</label>`;
  return `<div class="item${cls}" id="i_${i.id}">
    <div class="tete"><span class="ref">${i.id}</span>
      <span class="sujet">${esc(i.sujet)}</span>
      ${i.occurrences>1?`<span class="mult">${i.occurrences}× au catalogue</span>`:""}</div>
    <div class="paires">${paires}</div>
    <div class="choix">
      ${opt("A","A fait foi")}${opt("B","B fait foi")}
      ${opt("fusion","Fusionner les deux")}
      ${opt("resolu","Déjà résolu")}
      ${opt("ignore","Sans objet")}
    </div>
    <input class="motif" placeholder="Motif de la décision (facultatif, mais c'est lui qui vaudra dans six mois)"
      value="${esc(e.motif||"")}" oninput="motif('${i.id}',this.value)">
  </div>`;
}
function esc(s){ return (s||"").replace(/[&<>"]/g, c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c])); }

function toutIgnorerResolus(){
  const fams = D.familles.filter(f=>f.statut==="resolu"||f.statut==="hors-sujet").map(f=>f.cle);
  D.items.filter(i=>fams.includes(i.famille)).forEach(i=>{
    etat[i.id]=etat[i.id]||{};
    if(!etat[i.id].choix) etat[i.id].choix = i.statut==="resolu" ? "resolu" : "ignore";
  });
  sauver(); rendre();
}
function reinit(){ if(confirm("Effacer toutes les décisions ?")){ etat={}; sauver(); rendre(); } }

function exporter(fmt){
  const lignes = D.items.map(i=>({
    id:i.id, famille:i.famille, sujet:i.sujet,
    statut_verifie:i.statut, decision:(etat[i.id]||{}).choix||null,
    motif:(etat[i.id]||{}).motif||"", paires:i.paires
  }));
  let contenu, nom, type;
  if(fmt==="json"){
    contenu = JSON.stringify({source:"CONSOLIDE.json", genere_le:D.genere_le,
      total_brut:D.total_brut, total_fusionne:D.total_fusionne, decisions:lignes}, null, 2);
    nom="decisions_contradictions.json"; type="application/json";
  } else {
    let m = "# Arbitrage des contradictions\n\n";
    m += "Source `CONSOLIDE.json` du " + D.genere_le + " — " + D.total_brut +
         " entrées, " + D.total_fusionne + " après fusion des doublons.\n\n";
    const tranchees = lignes.filter(l=>l.decision);
    m += "**" + tranchees.length + " tranchées sur " + lignes.length + ".**\n\n";
    D.familles.forEach(f=>{
      const s = lignes.filter(l=>l.famille===f.cle && l.decision);
      if(!s.length) return;
      m += "## " + f.libelle + "\n\n";
      s.forEach(l=>{
        m += "- **" + l.id + "** — " + l.sujet + "\n";
        m += "  - décision : `" + l.decision + "`\n";
        if(l.motif) m += "  - motif : " + l.motif + "\n";
      });
      m += "\n";
    });
    contenu=m; nom="decisions_contradictions.md"; type="text/markdown";
  }
  const b=new Blob([contenu],{type:type+";charset=utf-8"});
  const a=document.createElement("a");
  a.href=URL.createObjectURL(b); a.download=nom; a.click();
  URL.revokeObjectURL(a.href);
}

document.getElementById("entete").textContent =
  "Source CONSOLIDE.json du " + D.genere_le + " — " + D.total_brut +
  " entrées, " + D.total_fusionne + " après fusion des doublons. Couverture du corpus : " +
  (D.couverture ? D.couverture.pct + " %" : "inconnue") + ".";
document.getElementById("avis_stockage").textContent = STOCK
  ? "Les décisions sont conservées dans ce navigateur jusqu'à l'export."
  : "⚠ Pas de stockage local ici : exportez avant de fermer, sinon les décisions sont perdues.";

appliquerPli(); rendreFiltres(); rendre(); majCompteur();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
