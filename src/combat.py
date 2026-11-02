"""
Moteur de combat — résume le flux de jeu.

Module : src.combat
Rôle   : orchestre les tours, les dégâts, le compte à rebours et le
         vainqueur. Séparé de la fenêtre de dessin pour garder le code
         testable sans écran.
"""

import random
import time

from src.slime import Slime


class CombatEngine:
    """
    Moteur de combat 1v1.

    Chaque tour : une des deux équipes attaque (selon ce qui est demandé).
    Le joueur attaque avec la flèche gauche, l'adversaire (CPU) attaque de
    son côté. Les dégâts sont tirés aléatoirement dans [damage // 2 .. damage].
    """

    def __init__(self, joueur: Slime, ennemi: Slime):
        self.joueur = joueur
        self.ennemi = ennemi
        self.round = 1

    def attaquer(self, attaquant: Slime, cible: Slime) -> int:
        """
        Fait frapper *attaquant* sur *cible* et retourne les dégâts.
        """
        if not attaquant.is_alive or not cible.is_alive:
            return 0

        # Limite de série (rareté) — la moitié du temps, un coup critique.
        is_crit = random.random() < 0.5
        degats = self._calcul_dégâts(attaquant, is_crit)

        cible.hp = max(0, cible.hp - degats)  # ne descend pas en dessous de 0

        # Message interne (rempli plus tard par la fenêtre) — on le garde simple.
        return degats

    def _calcul_dégâts(self, attaquant: Slime, is_crit: bool) -> int:
        """Calcule les dégâts réels avec eventuellement un coup critique."""
        base = attaquant.damage
        if is_crit:
            return int(base * 2.2)  # 120% d'incrément de critique
        return random.randint(int(base * 0.5), base)

    def tour(self, attaquant: Slime, cible: Slime) -> int:
        """
        Lance un tour complet : attaque puis pause léger, retourne les PV restants
        du cible (utile à l'interface).
        """
        date_debut = time.time()
        degats = self.attaquer(attaquant, cible)
        # Petit délai de recharge (simulé) pour ressentir la vitesse.
        self.attaquant_cooldown_estime(attaquant, date_debut)
        return degats

    def attaquant_cooldown_estime(self, attaquant: Slime, date_debut: float):
        """Simule une pause de recharge conforme au cooldown de l'attaquant."""
        temps_attente = attaquant.attack_cooldown - (time.time() - date_debut)
        if temps_attente > 0:
            time.sleep(temps_attente)

    @property
    def joueur_gagne(self) -> bool:
        return self.joueur.is_alive and not self.ennemi.is_alive

    @property
    def ennemi_gagne(self) -> bool:
        return self.ennemi.is_alive and not self.joueur.is_alive

    @property
    def match_nul(self) -> bool:
        return not self.joueur.is_alive and not self.ennemi.is_alive
