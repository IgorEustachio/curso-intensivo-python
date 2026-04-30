import pygame
import random
from pygame.sprite import Sprite

class Powerup(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        ship_image = pygame.image.load("./images/ship.png")

        #pega o tamanho da nave
        ship_width, ship_height = ship_image.get_size()

        #carrega o powerup
        powerup_image = pygame.image.load("./images/powerup.bmp")

        #redimensiona o powerup para o mesmo tamanho da nave
        self.image = pygame.transform.scale(
            powerup_image,
            (ship_width, ship_height)
        )

        self.rect = self.image.get_rect()

        self.rect.bottomleft = self.screen_rect.bottomleft

        #gerar uma posição aleatória para o powerup
        self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)

        self.x = float(self.rect.x)

        # Timer para aparição aleatória do powerup
        self.spawn_timer = 0
        self.spawn_interval = self._generate_random_interval()
        self.active = False

    def blitme_powerup(self):
        if self.active:
            self.screen.blit(self.image, self.rect)

    def position_powerup(self):
        self.active = False
        self.spawn_timer = 0
        self.spawn_interval = self._generate_random_interval()

    def _activate_powerup(self):
        self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
        self.x = float(self.rect.x)
        self.active = True

    def _generate_random_interval(self):
        return random.randint(1800, 3600)

    def update(self):
        if not self.active:
            self.spawn_timer += 1
            if self.spawn_timer >= self.spawn_interval:
                self._activate_powerup()
        