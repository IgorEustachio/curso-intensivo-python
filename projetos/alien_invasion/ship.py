import pygame

class Ship():
    #classe da espaçonave

    def __init__(self,ai_game): # ai = alien invasion
        #inicializa a espaçonave e define sua posição inicial
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() #rect = rectangle

        #faz upload da imagem e obtém seu rect
        self.image = pygame.image.load('projetos/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        #começa cada espaçonave nova no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # Armazena um float para a posição horizontal exata da espaçonave
        self.x = float(self.rect.x)

        #flag de movimento; começa com uma espaçonave que não está se movendo
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #atualiza a posição da nave com base na flag de movimento
        #atualiza o valor x da espaçonave, nao o rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #atualiza o objeto rect de self.x
        self.rect.x = self.x
    
    def blitme(self): #blit = block transfer
        #desenha a espaçonave em sua localização atual 
        self.screen.blit(self.image, self.rect)