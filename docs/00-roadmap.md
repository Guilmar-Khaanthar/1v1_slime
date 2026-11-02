# Roadmap du projet — jeu de combat 1v1 de slime

Ce document décrit la feuille de route complète du projet :
**PC / Mac / Linux / Android / iOS**, avec un focus mobile dès le départ.

---

## Cible finale

| Plateforme | État | Moteur / outils |
|---|---|---|
| PC (Windows/macOS/Linux) | **Priorité 1 : en cours** | Pygame (clair, sans compilation) |
| Android | Priorité 2 | Kivy + Buildozer (route de finalisation) |
| iOS | Priorité 3 | Kivy + Beebox (Mac) |

> Note : Python est un langage interprété. Pour Android/iOS, Kivy encapsule
> le code dans une application native via `buildozer` (Android) et `beebox`
> (iOS). C'est la phase de finalisation, quand le PC fonctionne.

---

## Phases de développement

### Phase 0 — Préparation (en cours)
- [x] Créer le dépôt GitHub `jeu mobil1v1` (structure + docs)
- [x] Environnement Python + Pygame installés (window lance sans erreur)
- [x] Documenter la stack (PC = Pygame, mobile = Kivy + Buildozer/Beebox)
- [ ] Mettre à jour la documentation au fur et à mesure

### Phase 1 — Combat 1v1 (en cours)
- [x] Fenêtre Pygame s'ouvre correctement
- [x] Deux slimes (Joueur + Ennemi) rendus sur l'écran
- [x] Barres de vie pour chaque camp
- [x] Attaque avec Espace / clic (dégâts affichés)
- [x] Automate d'attaque de l'ennemi
- [ ] La partie est clairement terminée (message de victoire/défaite)

### Phase 2 — Détails de jeu
- [ ] Attaque spéciale / coup critique (optionnel)
- [ ] Sons d'impact (pygame.mixer)
- [ ] Boucle de match (3 manches)
- [ ] Sauvegarde du score / highscore

### Phase 3 — Multi-plateforme
- [ ] Build Pygame pour PC/macOS/Linux (console + exécutables)
- [ ] Préparation Kivy pour Android (Buildozer)
- [ ] Préparation Kivy pour iOS (Beebox / Xcode)

### Phase 4 — Fin de projet
- [ ] Menu principal simplifié (bouton pour commencer)
- [ ] Pause, règles affichées à l'écran
- [ ] Sons et effets de fin de partie
- [ ] Documentation finale publiée
- [ ] Publication du dépôt

---

## Conventions de documentation

- **README.md** : présentation courte + installation + roadmap.
- **docs/**
  - `01-projet.md` : concept + règles du jeu
  - `02-architecture.md` : structure des fichiers
  - `03-install.md` : guide d'installation
  - `04-multiplateforme.md` : guide de build Android/iOS
- **Doc « au fur et à mesure »** : on ajoute une section à la fin
  de la documentation avant chaque nouvelle version.
