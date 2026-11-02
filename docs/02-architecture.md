# Architecture — structure des fichiers

Ce projet est organisé en modules séparés pour rester lisible et évolutif,
tout en restant léger sur les plateformes mobiles (jeu simple, peu de fichiers).

---

## Arborescence

```
jeu-mobil1v1/
├── README.md              # Présentation courte + installation
├── requirements.txt       # Dépendances Python (Pygame + Kivy pour mobile)
├── .gitignore             # Fichiers ignorés par Git
│
├── src/                   # Code source principal
│   ├── __init__.py
│   ├── main.py            # Point d'entrée (fenêtre Pygame + boucle)
│   ├── slime.py           # Données du personnage (Slime)
│   ├── combat.py          # Moteur de combat (vies, attaques, tour)
│   └── tests/
│       └── __init__.py
│
├── docs/                  # Documentation
│   ├── 00-roadmap.md
│   ├── 01-concept.md
│   ├── 02-architecture.md
│   ├── 03-install.md
│   └── 04-multiplateforme.md
│
├── assets/                # Images, sons, sprites (non versionnés)
├── tests/                 # Tests automatisés (valeurs, logique)
└── builds/                # Artefacts générés (APKs, exécutables)
```

---

## Cœur du jeu

```
Moteur (combat.py)   ← calcule : vies, tours, dégâts, gagnant
      ↑
Personnages (slime.py)  ← données du slime (couleur, PV, dégâts)
      ↑
Interface (main.py)  ← fenêtre Pygame, barres de vie, clics
```

L'**engine** est séparé de l'**interface** : c'est ce qui permet de
tester la logique (tests) sans avoir besoin d'afficher le jeu.
