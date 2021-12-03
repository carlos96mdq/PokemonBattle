# Clase que pinta el fondo y ubica imagenes (no sprites)

import pygame, os


class Fondo:
    def __init__(self, color=None, imagen=None, imagen_dir=None, imagen_x_y=(0, 0)):
        self.color = color
        if imagen is not None:
            self.image = pygame.image.load(os.path.join(imagen_dir, imagen))
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.centerx = imagen_x_y[0]
            self.rect.centery = imagen_x_y[1]
        else: self.image = None


    def dibujar(self, pantalla):
        pantalla.fill(self.color)
        if self.image is not None:
            pantalla.blit(self.image, self.rect)
