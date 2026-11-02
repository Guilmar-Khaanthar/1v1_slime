# Slime Combat 1v1

Jeu de combat **1v1 de slimes** conçu pour être joué sur **PC, macOS et Linux**
(le cœur est multiplateforme, et la route vers **Android et iOS** est
prévue en finalisation, avec Kivy). Ce projet est écrit en **Python** avec
**Pygame** pour le PC, et partage la logique de combat côté mobile.

---

## Objectif du jeu

- Deux slimes s'affrontent en **1v1**.
- Chacun a **10 vies**.
- Le premier à atteindre **0 vie perd**.
- Format de **match** en 3 manches (prévoir).

---

## Tech stack

| Élément          | Choix                             |
| ---------------- | --------------------------------- |
| Langage          | Python 3.10+                      |
| Moteur (PC)      | Pygame (stabilisé, sans compilation) |
| Moteur (mobile)  | Kivy (route de finalisation)      |
| Build Android    | Buildozer (lors de la phase mobile) |
| Build iOS        | Beebox (Mac, lors de la phase mobile) |
| Interface        | Clavier/souris (PC) + tactile (mobil) |

---

## Structure rapide

```
src/          # Code source du jeu
  main.py     # Application Pygame + boucle de jeu
  slime.py    # Données du slime (couleur, PV, dégâts)
  combat.py   # Moteur de combat (vies, attaques, tour)
docs/         # Documentation (règles, architecture, installation)
assets/       # Images, sons, sprites
tests/        # Tests automatisés
```

---

## Installation rapide (PC)

```bash
# 1. Créer l'environnement virtuel
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer le jeu
python -m src.main
```

---

## Dépôt

- Nom GitHub : `jeu mobil1v1`
- Pour les instructions de push, voir la section suivante.

---

## Licence

Projet personnel / formation. À préciser plus tard.
