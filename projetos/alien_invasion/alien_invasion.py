import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion():

    def __init__(self):
        #inicializa e cria recursos do jogo
        pygame.init()  
        
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')


        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def _check_events(self):
            #responde aos eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        #responde a teclas pressionadas (keydown)
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        #responde a teclas soltas (keyup)
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        #cria um novo projétil e o adiciona ao grupo projéteis
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        #atualiza a posição dos projéteis e descarta os projéteis antigos
        #atualiza as posições dos projéteis
        self.bullets.update()

        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)


    def _update_screen(self):
        #redesenha a tela durante cada passagem pelo loop
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        # Deixa a tela desenhada mais recente visível
        pygame.display.flip()

    def run_game(self):
        #inicializa o loop principal do jogo

        while True:
            #observa eventos de teclado e mouse
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

            

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()