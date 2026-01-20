import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    #Classe para representar um único alienígena na frota

    def __init__(self, ai_game):
        #Inicializa o alienígena e define sua posição inicial
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #.Carrega a imagem do alienígena e define seu atributo rect
        self.image = pygame.image.load('projetos/alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        #inicia cada alienígena novo perto do canto superior esquerdo da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #armazena a posição horizontal exata do alienígena
        self.x = float(self.rect.x)

    def update(self):
        #move o alien para direita
        self.x = self.settings.alien_speed 
        self.rect.x = self.x