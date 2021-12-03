# Donde se maneja el juego y está el loop principal

import pygame, os, sys
from pygame.locals import *
from .config import *
from .fondo import Fondo
from .mouse import Mouse
from .info import *
from .pokemon import Pokemon
from .battlebox import Battlebox
from .battlemenu import Battlemenu


class Game:
    def __init__(self):
        # Inicializo pygame y la pantalla
        # Posiciono la ventana
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (S_X, S_Y)
        # Inicializo pygame
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        pygame.mixer.init()
        # Creo pantalla
        self.pantalla = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
        pygame.display.set_caption("Pokemon entrenamiento de Batalla")
        # Cargo el clock
        self.clock = pygame.time.Clock()
        # Cargo mouse
        self.mouse_obj = Mouse()
        # Cargo variables varias
        self.dir = os.path.dirname(__file__)
        self.dt = 0
        self.menu_running = False
        self.batalla_running = False
        self.jugador = None
        self.npc = None

    # Métodos para realizar acciones
    def draw(self, fondo, sprites):
        self.fondo_menu.dibujar(self.pantalla)
        self.sprites.draw(self.pantalla)
        pygame.display.flip()

    # Métodos de etapas del juego
    def start(self):
        self.menu_start()

    # Inicializo los objetos, el fondo del menu y la musica
    def menu_start(self):
        self.fondo_menu = Fondo(WHITE, "logo.png", DIR_IMG_FONDO, (400, 150))
        self.pokemon_1 = Pokemon(bulbasaur, (200, 300))
        self.pokemon_2 = Pokemon(squirtle, (400, 300))
        self.pokemon_3 = Pokemon(charmander, (600, 300))
        self.sprites = pygame.sprite.Group((self.pokemon_1, self.pokemon_2, self.pokemon_3))
        pygame.mixer.music.load(os.path.join("game\\audios\\musica", "menu.mp3"))
        self.menu_run()

    def menu_run(self):
        self.menu_running = True
        pygame.mixer.music.play(loops=-1)
        while self.menu_running:
            # Medir tiempo 60 fps
            self.dt = self.clock.tick(FPS)
            # Updates
            self.mouse_obj.update()
            self.sprites.update()
            # Reviso eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # La X de la ventana
                    sys.exit(0)
                # Controlo la salida del juego
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit(0)
                    elif event.key == K_SPACE:
                        self.menu_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.mouse_obj.colision(self.pokemon_1.rect):
                        self.pokemon_1.cry.play()
                        # Asigno jugadores, se debe tener en cuenta que en una clase el operador = no crea una nueva
                        # instancia, sino que ahora self.jugador y self.pokemon_1 hacen referencia a la misma
                        # instancia. Si modifico uno entonces se modifica el otro
                        self.player = self.pokemon_1
                        self.npc = self.pokemon_3
                        self.pokemon_2.kill()
                        self.menu_running = False
                    elif self.mouse_obj.colision(self.pokemon_2.rect):
                        self.pokemon_2.cry.play()
                        self.player = self.pokemon_2
                        self.npc = self.pokemon_1
                        self.pokemon_3.kill()
                        self.menu_running = False
                    elif self.mouse_obj.colision(self.pokemon_3.rect):
                        self.pokemon_3.cry.play()
                        self.player = self.pokemon_3
                        self.npc = self.pokemon_2
                        self.pokemon_1.kill()
                        self.menu_running = False
            # Dibujo los elementos en pantalla
            self.draw(self.fondo_menu, self.sprites)
        # Paso al siguiente menu
        pygame.mixer.music.fadeout(1000)
        self.batalla_start()

    def batalla_start(self):
        pygame.mixer.music.load(os.path.join("game\\audios\\musica", "Battle! (Trainer Battle).mp3"))
        self.fondo_menu = Fondo(WHITE)
        # Reasigno la sprite sheet del jugador de espalda
        self.player.set_back_sheet((200, 400))
        self.npc.rect.center = (600, 100)
        self.sprites = pygame.sprite.Group((self.player, self.npc))
        # Creo los battlebox
        self.battlebox_pla = Battlebox(self.player)
        self.battlebox_npc = Battlebox(self.npc, npc=True)
        self.sprites.add((self.battlebox_pla, self.battlebox_npc))
        # Creo el battlemenu
        self.battlemenu_pla = Battlemenu()
        self.sprites.add(self.battlemenu_pla)
        # Paso a la siguiente etapa
        self.batalla_run()


    def batalla_run(self):
        self.batalla_running = True
        pygame.mixer.music.play(loops=-1)
        while self.batalla_running:
            # Medir tiempo 60 fps
            self.dt = self.clock.tick(FPS)
            # Updates
            self.mouse_obj.update()
            self.sprites.update()
            # Reviso eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # La X de la ventana
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.mouse_obj.colision(self.battlemenu_pla.move_1_rect.move(self.battlemenu_pla.rect.x, self.battlemenu_pla.rect.y)):
                        self.npc.hp_actual -= 5
            # Dibujo los elementos en pantalla
            self.draw(self.fondo_menu, self.sprites)