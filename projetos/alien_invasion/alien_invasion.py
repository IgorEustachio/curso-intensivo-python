import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button

class AlienInvasion():

    def __init__(self):
        #inicializa e cria recursos do jogo
        pygame.init()  
        
        # Inicializa Invasão Alienígena em um estado inativo
        self.game_active = False

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        
        self.ship = Ship(self)
        self.stats = GameStats(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        #cria o botão Play
        self.play_button = Button(self, "Play") #"Play" corresponde ao parâmetro msg

        self._create_fleet()    

        # Desenha o botão Play se o jogo estiver inativo
        if not self.game_active:
            self.play_button.draw_button()

    def _check_events(self):
            #responde aos eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        #inicia um jogo novo quando o jogador clica em play
        #cria o botão Play
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            #redefine as estatísticas do jogo
            self.stats.resets_stats()
            self.game_active = True

            #descarta quaisquer projéteis e alienígenas restantes
            self.bullets.empty()
            self.aliens.empty()
            #cria uma frota nova e centraliza a espaçonave
            self._create_fleet()
            self.ship.center_ship()

            #oulta o cursor do mouse
            pygame.mouse.set_visible(False)

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
        
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        #verifica se algum projétil atingiu um alienígena, se sim remove o projétil e o alienígena
        collisions = pygame.sprite.groupcollide(
        self.bullets, self.aliens, True, True)

        if not self.aliens:
            #destrói os projéteis existentes e cria uma frota nova
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
    #cria a frota de alienígenas
    #cria um alienígena e continua adicionando alienígenas até que não haja mais espaço disponível.
    #o espaçamento entre os alienígenas é de uma largura de alienígena e uma altura de alienígena.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finalizou uma linha; redefine o valor de x
            # e incrementa o valor de y.
            current_x = alien_width
            current_y += 2 * alien_height


    def _create_alien(self, x_position, y_position):
        """Cria um alienígena e o posiciona na frota."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        #atualiza as posições de todos os alienígenas na frota
        self.aliens.update()
        self._check_fleet_edges()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print('espaçonave danificada!')
            self._ship_hit()

    def _check_fleet_edges(self):
        #responde se algum alien atingiu  a borda  
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        #faz toda a frota descer e mudar de direção
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
            
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        #responde a espaçonave sendo abatida por um alien
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            #exlue qualquer alien ou bala que esteja na tela
            self.aliens.empty()
            self.bullets.empty()

            #cria uma nova frota e re-centraliza a nave
            self._create_fleet()
            self.ship.center_ship()

            #pausa 
            sleep(0.5)
        
        else:
            self.game_active = False
            pygame.mouse.set_visible(True) #deixa o mouse visivel

    def _check_aliens_bottom(self):
        #Verifica se algum alienígena chegou à parte inferior da tela
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #trata isso como se a espaçonave tivesse sido abatida
                self._ship_hit()
                break   

    def _update_screen(self):
        #redesenha a tela durante cada passagem pelo loop
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Deixa a tela desenhada mais recente visível
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def run_game(self):
        #inicializa o loop principal do jogo

        while True:
            #observa eventos de teclado e mouse
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
        
            self._update_screen()
            self.clock.tick(60)
            

            

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()