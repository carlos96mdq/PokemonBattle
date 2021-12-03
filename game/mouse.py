# Clase que controla el mouse y sus colisiones

import pygame


class Mouse:
    def __init__(self):
        self.rect = pygame.Rect((pygame.mouse.get_pos()), (1, 1))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def colision(self, rect):
        return self.rect.colliderect(rect)