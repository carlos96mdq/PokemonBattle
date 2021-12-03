# Menu principal de jugador en batalla

import pygame, os
from .info import battle
from .config import *

class Battlemenu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Parámetros del battlemenu
        self.font = pygame.font.Font(FONT_GB, 14)
        self.scale = battle["scale"]
        self.width = battle["battlemenu_w"]
        self.height = battle["battlemenu_h"]
        self.image = pygame.image.load(os.path.join(DIR_IMG_BATT, "battlemenu.png"))
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (800, self.height * self.scale))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 528)
        # Movsmenu
        self.movesmenu = pygame.image.load(os.path.join(DIR_IMG_BATT, "movesmenu.png"))
        self.movesmenu = self.movesmenu.convert_alpha()
        self.movesmenu = pygame.transform.scale(self.movesmenu, (battle["movesmenu_w"] * self.scale, battle["movesmenu_h"] * self.scale))
        # Moves
        self.move_1 = self.font.render("ATACAR", False, BLACK)
        self.move_1_rect = self.move_1.get_rect()
        self.move_1_rect.center = (90, 50)
        self.movesmenu.blit(self.move_1, self.move_1_rect)
        self.image.blit(self.movesmenu, (0, 0)) # Necesito hacerlo en este orden, sino no dibuja

    def update(self):
        pass
    # Modifico contenido de la Battlebox
    # Redibujo contenido de la Battlebox