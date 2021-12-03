# Clase pasdre de todos los pokemons

import pygame, os


class Pokemon(pygame.sprite.Sprite):
    def __init__(self, pokemon_info, position):
        pygame.sprite.Sprite.__init__(self)
        self.info = pokemon_info
        self.name = self.info["name"]
        self.hp_actual = self.info["hp"]
        self.hp_total = self.info["hp"]
        self.atk = self.info["atk"]
        self.defe = self.info["def"]
        self.atkx = self.info["atkx"]
        self.defx = self.info["defx"]
        self.vel = self.info["vel"]
        self.cry = pygame.mixer.Sound(os.path.join(self.info["dir"], "cry.aif"))
        self.contador = 0
        self.velocidad = 3
        self.set_front_sheet(position)

    def set_front_sheet(self, position):
        self.sheet = pygame.image.load(os.path.join(self.info["dir"], "front.png"))
        self.sheet = self.sheet.convert_alpha()
        self.width = self.info["front_w"]
        self.height = self.info["front_h"]
        self.sheet_w = self.info["front_sheet_w"]
        self.sheet_h = self.info["front_sheet_h"]
        self.frames = self.info["front_frames"]
        self.sheet.set_clip(pygame.Rect(0, 0, self.width, self.height))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.scale = 2
        self.image = pygame.transform.scale(self.image, (self.width * self.scale, self.height * self.scale))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.frame = 0
        self.sheet_x = 0
        self.sheet_y = 0

    def set_back_sheet(self, position):
        self.sheet = pygame.image.load(os.path.join(self.info["dir"], "back.png"))
        self.sheet = self.sheet.convert_alpha()
        self.width = self.info["back_w"]
        self.height = self.info["back_h"]
        self.sheet_w = self.info["back_sheet_w"]
        self.sheet_h = self.info["back_sheet_h"]
        self.frames = self.info["back_frames"]
        self.sheet.set_clip(pygame.Rect(0, 0, self.width, self.height))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.scale = 2
        self.image = pygame.transform.scale(self.image, (self.width * self.scale, self.height * self.scale))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.frame = 0
        self.sheet_x = 0
        self.sheet_y = 0

    def update(self):
        # Manejo la animación del sprite
        if self.contador == self.velocidad:
            self.contador = 0
            self.frame += 1
            self.sheet_x += self.width
            if self.sheet_x >= self.sheet_w:
                self.sheet_x = 0
                self.sheet_y += self.height
                if self.sheet_y >= self.sheet_h:
                    self.sheet_y = 0
            if self.frame == self.frames:
                self.frame = 0
                self.sheet_x = 0
                self.sheet_y = 0
            self.sheet.set_clip(pygame.Rect(self.sheet_x, self.sheet_y,
                                            self.width, self.height))
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.image = pygame.transform.scale(self.image, (self.width*self.scale, self.height*self.scale))
        else:
            self.contador += 1