# Clase que maneja al cuadrado con toda la info del pokemon durante la batalla

import pygame, os
from .config import *
from .info import battle


class Battlebox(pygame.sprite.Sprite):
    def __init__(self, pokemon, npc=False):
        pygame.sprite.Sprite.__init__(self)
        # Paramétros del battlebox
        self.pokemon = pokemon
        self.scale = battle["scale"]
        self.width = battle["battlebox_w"]
        self.height = battle["battlebox_h"]
        self.pokemon_name = self.pokemon.name
        self.pokemon_hp_total = self.pokemon.hp_total
        self.pokemon_hp_actual = self.pokemon.hp_actual
        self.font = pygame.font.Font(FONT_GB, 14)
        self.font.set_bold(True)
        self.font_num = pygame.font.Font(FONT_GB, 16)
        # Cargo imagen del BB
        self.image = pygame.image.load(os.path.join(DIR_IMG_BATT, "battlebox.png"))
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width * self.scale, self.height * self.scale))
        self.rect = self.image.get_rect()
        if npc:
            self.rect.center = (200, 100)
        else:
            self.rect.center = (600, 400)
        # Le agrego a la battlebox su contenido
        self.name = self.font.render(self.pokemon_name, False, BLACK)  # nombre

        self.hp_actual = self.font_num.render(str(self.pokemon_hp_actual), False, BLACK)  # hp actual

        self.hp_total = self.font_num.render("/" + str(self.pokemon_hp_total), False, BLACK)  # hp total

        self.hp_bar = pygame.image.load(os.path.join(DIR_IMG_BATT, "hpbar.png"))  # barra de hp
        self.hp_bar = self.hp_bar.convert_alpha()
        self.hp_bar = pygame.transform.scale(self.hp_bar, (battle["hpbar_w"] * self.scale, battle["hpbar_h"] * self.scale))


    def update(self):
        # Modifico contenido de la Battlebox
        self.pokemon_hp_actual = self.pokemon.hp_actual
        self.hp_actual = self.font_num.render(str(self.pokemon_hp_actual), False, BLACK)
        # Redibujo contenido de la Battlebox
        self.image = pygame.image.load(os.path.join(DIR_IMG_BATT, "battlebox.png"))
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width * self.scale, self.height * self.scale))
        self.image.blit(self.name, (20, 10))
        self.image.blit(self.hp_actual, (130, 55))
        self.image.blit(self.hp_total, (165, 55))
        self.image.blit(self.hp_bar, (50, 40))
