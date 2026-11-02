"""
Slime Combat 1v1 — jeu de combat 1v1 en Python (Pygame).

Module : src.main
Rôle   : application Pygame qui affiche et pilote le combat 1v1 de deux slimes.
"""

import random
import sys
import time

import pygame

from src.combat import CombatEngine
from src.slime import Slime

BLEU_JOUEUR = (180, 218, 255)
VERT_ENNEMI = (120, 230, 150)
NOIR = (30, 30, 30)
BLANC = (255, 255, 255)
FOND = (20, 18, 28)

TITRE = "Slime Combat 1v1 — combat 1v1 de slimes"
INSTR = "Espace or clic gauche = attaquer (slime de gauche)"


def creer_joueur() -> Slime:
    return Slime(color=BLEU_JOUEUR, hp=10, max_hp=10, damage=3, attack_cooldown=0.6)


def creer_ennemi() -> Slime:
    return Slime(color=VERT_ENNEMI, hp=10, max_hp=10, damage=4, attack_cooldown=1.4)


class JeuPygame:
    """
    Application Pygame du jeu de combat 1v1.

    Le joueur (slime de gauche) attaque avec Espace / clic. L'ennemi
    attaque tout seul suivant un cooldown. Le premier à atteindre 0 PV perd.
    """

    def __init__(self, largeur=820, hauteur=660):
        pygame.init()
        self.fenetre = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption(TITRE)
        self.largeur, self.hauteur = largeur, hauteur

        self.font = pygame.font.SysFont("consolas", 28)
        self.font_gros = pygame.font.SysFont("consolas", 46)

        self.joueur = creer_joueur()
        self.ennemi = creer_ennemi()
        self.moteur = CombatEngine(self.joueur, self.ennemi)

        self.longueur_joueur = largeur * 0.32

        self.dégâts = 0
        self.dégâts_vie = 1.0

        self.dernier_coup_enemy = 0
        self.cooldown_enemy = self.ennemi.attack_cooldown

        self.partie_terminee = False

        self.tps = 0

    def gerer_evenements(self):
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                self.quitter()
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if self.moteur.joueur.is_alive and pygame.mouse.get_pressed()[0]:
                    x, y = evenement.pos
                    if x < self.largeur // 2 and self._zone_slime_gauche(x, y):
                        self.attaquer_cote("joueur")
            elif evenement.type == pygame.KEYDOWN:
                if self.moteur.joueur.is_alive and evenement.key == pygame.K_SPACE:
                    self.attaquer_cote("joueur")

    def attaquer_cote(self, cote: str):
        if cote == "joueur":
            self.moteur.attaquer(self.joueur, self.ennemi)
        else:
            self.moteur.attaquer(self.ennemi, self.joueur)

    def gerer_enemy(self):
        if not self.ennemi.is_alive:
            return
        if time.time() - self.dernier_coup_enemy > self.cooldown_enemy:
            self.attaquer_cote("ennemi")
            self.dernier_coup_enemy = time.time()

    def _zone_slime_gauche(self, x: float, y: float) -> bool:
        return 40 < x < self.largeur // 2 - 40 and 330 < y < self.hauteur - 200

    def afficher(self):
        self.fenetre.fill(FOND)
        self._dessiner_piste()
        self._afficher_titres()
        self._afficher_bars_vie()
        self._afficher_slime_joueur()
        self._afficher_slime_ennemi()
        self._afficher_instruction()
        self._afficher_texte_terminus()
        self._afficher_dégâts()
        pygame.display.flip()

    def _dessiner_piste(self):
        pygame.draw.rect(
            self.fenetre, (26, 23, 36), (0, 0, self.largeur, self.hauteur - 260), border_radius=0
        )
        pygame.draw.rect(
            self.fenetre, (40, 37, 52), (20, self.hauteur - 320, self.largeur - 40, 300), border_radius=14
        )

    def _afficher_titres(self):
        titre = self.font.render(TITRE, True, BLANC, FOND)
        self.fenetre.blit(titre, (self.largeur // 2 - titre.get_width() // 2, 26))

    def _afficher_bars_vie(self):
        x_j = self.longueur_joueur / 2 - 40
        x_e = self.largeur - x_j - 20
        self._barre(x_j, self.joueur, BLEU_JOUEUR, "Joueur")
        self._barre(x_e, self.ennemi, VERT_ENNEMI, "Ennemi")

    def _barre(self, x: float, s: Slime, couleur: tuple[int, int, int], etiquette: str):
        py = self.hauteur - 180
        px = x - self.longueur_joueur / 2
        pdf = s.hp / s.max_hp
        pygame.draw.rect(self.fenetre, NOIR, (px, py, self.longueur_joueur, 16), border_radius=6)
        pygame.draw.rect(
            self.fenetre, couleur, (px, py, self.longueur_joueur * pdf, 16), border_radius=6
        )
        txt = self.font.render(f"{s.hp}  |  {etiquette}", True, BLANC)
        self.fenetre.blit(txt, (px, py + 22))

    def _afficher_slime_joueur(self):
        cx, cy = 210, self.hauteur * 0.78
        self._dessiner_slime(cx, cy, BLEU_JOUEUR)
        self._texte_illisible("Joueur", cx, cy - 40, BLANC, 26)

    def _afficher_slime_ennemi(self):
        cx, cy = self.largeur - 210, self.hauteur * 0.78
        self._dessiner_slime(cx, cy, VERT_ENNEMI)
        self._texte_illisible("Ennemi", cx, cy - 40, BLANC, 26)

    def _dessiner_slime(self, cx: float, cy: float, couleur: tuple[int, int, int]):
        r = 58
        pygame.draw.ellipse(self.fenetre, couleur, (cx - r, cy - 50, r * 2, r * 2), 0)
        pygame.draw.ellipse(self.fenetre, NOIR, (cx - 16, cy - 34, 12, 12))
        pygame.draw.ellipse(self.fenetre, NOIR, (cx + 4, cy - 34, 12, 12))
        pygame.draw.ellipse(self.fenetre, NOIR, (cx - 16, cy - 22, 10, 10))
        pygame.draw.ellipse(self.fenetre, NOIR, (cx + 9, cy - 22, 10, 10))
        pygame.draw.arc(self.fenetre, NOIR, (cx - 22, cy - 10, 44, 30), 0, 3.14, 4)

    def _texte_illisible(self, texte: str, x: float, y: float, couleur: tuple[int, int, int], taille: int):
        police = pygame.font.SysFont("consolas", taille)
        txt = police.render(texte, True, couleur)
        self.fenetre.blit(txt, (x - txt.get_width() // 2, y))

    def _afficher_instruction(self):
        txt = self.font.render(INSTR, True, (170, 180, 210))
        self.fenetre.blit(txt, (self.largeur // 2 - txt.get_width() // 2, self.hauteur - 52))

    def _afficher_texte_terminus(self):
        if not self.moteur.joueur.is_alive and not self.moteur.ennemi.is_alive:
            return
        if not self.partie_terminee:
            return
        if self.moteur.ennemi.is_alive and not self.moteur.joueur.is_alive:
            motif = "Défaite"
            couleur = NOIR
        else:
            motif = "Victoire"
            couleur = VERT_ENNEMI
        gros = self.font_gros.render("Slime Combat 1v1", True, NOIR)
        sous = self.font.render(f"{motif} !", True, couleur)
        effacer = self.font_gros.render("Slime Combat 1v1", True, (0, 0, 0, 200))
        self.fenetre.blit(gros, (self.largeur // 2 - gros.get_width() // 2, 230))
        self.fenetre.blit(sous, (self.largeur // 2 - sous.get_width() // 2, 290))
        self.fenetre.blit(effacer, (self.largeur // 2 - effacer.get_width() // 2, 240))

    def _afficher_dégâts(self):
        if self.dégâts > 0 and self.dégâts_vie > 0:
            self.dégâts_vie -= 0.03
            if self.dégâts_vie <= 0:
                self.dégâts = 0
            else:
                texte = self.font.render(f"-{self.dégâts}", True, (240, 90, 90), FOND)
                self.fenetre.blit(texte, (410, 300))
        elif self.dégâts > 0:
            self.dégâts = 0

    def quitter(self):
        pygame.quit()
        sys.exit()

    def executer(self):
        while True:
            self.gerer_evenements()
            self.gerer_enemy()
            self.afficher()
            pygame.time.wait(16)


def main():
    jeu = JeuPygame()
    jeu.executer()


if __name__ == "__main__":
    main()

