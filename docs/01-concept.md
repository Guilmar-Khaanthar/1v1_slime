# Concept — Slime Combat 1v1

Jeu de combat 1v1 en temps réel. Deux slug (slimes) se battent sur un « canal ».
Le but : être le premier à épuiser son adversaire.

---

## Règles principales

- **Format** : match de 3 rounds (1v1).
- **Chaque round** : le premier à toucher l'autre gagne le round.
- **Quand un joueur a 0 PV** : il est éliminé, l'autre gagne le match.
- **Vies initiales** : 10 (paramétrable).
- **Attaques** : coups normaux, coups puissants, attaque spéciale.

---

## Moteur de combat (prévoir)

| Élément | Description |
|---|---|
| Vie (PV) | Nombre entier par joueur, 0 = éliminé |
| Attack power | Dégâts infligés par un coup |
| Crit | Septième chance de dégât double |
| Vitesse | Qui attaque en premier dans un round |
| Écran | Affichage d'une barre de vie simple |

---

## Évolutions prévues

- [ ] Animation simple des sprites
- [ ] Effets de particules légers
- [ ] Jauge de coup critique
- [ ] Bruitages d'impact
- [ ] Pause pendant le combat
- [ ] Sauvegarde du score

---
