"""
Slime — données du personnage (équipement minimal).

Module : src.slime
Rôle   : décrit un slime (couleur, HP, dégâts, vitesse d'attaque).
"""

from dataclasses import dataclass


@dataclass
class Slime:
    """Un personnage de slime dans le combat 1v1."""

    # Garde l'affichage de l'image (couleur, dans la phase 1).
    color: tuple[int, int, int]

    # Points de vie (0 = éliminé).
    hp: int

    # Points de vie maximum.
    max_hp: int

    # Dégâts bruts infligés lors d'un coup normal.
    damage: int

    # Délai minimum entre deux attaques (en secondes).
    attack_cooldown: float = 1.2

    def __post_init__(self):
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    @property
    def is_alive(self) -> bool:
        """Un slime est en vie tant que ses PV sont strictement positifs."""
        return self.hp > 0
