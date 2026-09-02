---
titre: Spec quiz-nexus.html — page quiz Nexus standalone
spec: doctor12_l2
date: 2026-09-02
work: L2
parent_a2: 30_Business_OS/10_Projects/coach-os-app
---

# Ruban - quiz nexus : page quiz standalone dans coach-os-app

## Verifie reellement (etat du repo au 2026-09-02)

Mesure directe :
- `30_Business_OS/10_Projects/coach-os-app/public/` existe (servi statiquement par Vite).
- Le quiz canon 4 questions vit dans `src/apps/welcome/landing/canvases/DemoCanvas.tsx`
  (section `data-anchor="quiz"`, questions : « Combien de clients payants as-tu signé ? »,
  « Qu... » [Q2], « Tu utilises déjà des outils (Notion, Drive, Slack) ? »,
  « Si tu avais ton vendredi soir à toi, tu ferais quoi ? », note « On n'enregistre rien · on ne te maille pas »).
- Le dépôt historique `omk/repos/omk-services-nexus-quiz/quiz.html` cité par
  `09_Blueprints/coach-os-refonte/analyses/N3_projets.md` N'EXISTE PLUS sur disque
  (vérifié 2026-09-02, arbre complet sans node_modules). Le quiz Nexus n'a donc
  aucun artefact standalone servi.

## Objectif

Creer `public/quiz-nexus.html` : page HTML autonome (zero dependance, zéro build),
quiz 4 questions Nexus aligné sur la niche canon ADR-ICP-NEXUS-001
(coachs / consultants seniors, facturation 500-2000 EUR/h), conservant les
4 questions canon de DemoCanvas.tsx verbatim.

## Livrable

`C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os-app/public/quiz-nexus.html`

Contraintes :
- HTML5 + CSS + JS inline dans le fichier unique. Aucun CDN, aucun import externe.
- Les 4 questions de DemoCanvas.tsx reprises verbatim (Q2 lue directement depuis
  le fichier source par le constructeur — ne pas inventer).
- Scoring 0-12 (0-3 par question), 3 bandes : Strong fit (>=9) / Partial fit (5-8) / Low fit (<=4),
  conforme au pattern onboarding historique.
- Banniere « On n'enregistre rien · on ne te maille pas » (zero PII, pattern Zero-PII seal).
- CTA finale vers la niche : « Réservation audit Nexus — coaching premium 500-2000 EUR/h ».

## Perimetre

- Ecrire : `public/quiz-nexus.html` UNIQUEMENT.
- Ne pas modifier : `DemoCanvas.tsx`, toute autre source, `package.json`, config Vite.

## Critere d'acceptation

- N1 : le fichier existe, taille > 2000 octets, et contient les 3 questions canon verbatim (« Combien de clients payants as-tu signé ? », « Tu utilises déjà des outils (Notion, Drive, Slack) ? », « Si tu avais ton vendredi soir à toi, tu ferais quoi ? »). Verification : `python -c "import os;s=open(r'C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os-app/public/quiz-nexus.html',encoding='utf-8').read();print(os.path.getsize(r'C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os-app/public/quiz-nexus.html')>2000 and all(q in s for q in ['Combien de clients payants as-tu signé ?','Tu utilises déjà des outils (Notion, Drive, Slack) ?','Si tu avais ton vendredi soir à toi, tu ferais quoi ?']))"` -> True
- N2 : Q2 du fichier == Q2 verbatim de DemoCanvas.tsx. Verification (exit 0) : `python -c "import re;d=open(r'C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os-app/src/apps/welcome/landing/canvases/DemoCanvas.tsx',encoding='utf-8').read();h=open(r'C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os-app/public/quiz-nexus.html',encoding='utf-8').read();qs=re.findall(r'q:\\s*[\\\"\\'\\`]([^\\\"\\'\\`]+)[\\\"\\'\\`]',d);assert len(qs)==4;print(qs[1] in h)"` -> True
- N3 : scoring et bandes presents (Strong fit / Partial fit / Low fit + banniere zero-PII + CTA). Verification : `python -c "s=open(r'C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os-app/public/quiz-nexus.html',encoding='utf-8').read();print(all(t in s for t in ['Strong fit','Partial fit','Low fit','On n\'enregistre rien','Réservation audit Nexus']))"` -> True
- N4 : aucune reference externe (http/https src ou href hors ancres internes autorisees). Verification (exit 0) : `python -c "import re;s=open(r'C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os-app/public/quiz-nexus.html',encoding='utf-8').read();ext=[u for u in re.findall(r'(?:src|href)=[\\\"\\'](http[^\\\"\\']+)',s)];print(ext)"` -> []

## Interdits

- Prononcer `done` : seul le 11e Docteur detache, depuis `review`.
- Modifier un fichier autre que `public/quiz-nexus.html`.
- Inventer la Q2 (la lire depuis DemoCanvas.tsx).
- Copier un secret ou une cle API dans la page.
- Cumuler Build et Review.
