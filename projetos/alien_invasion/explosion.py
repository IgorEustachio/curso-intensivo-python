import pygame
import random
from pygame.sprite import Sprite

class Explosion(Sprite):

    def __init__(self, ai_game, center):
        super().__init__()
        self.screen = ai_game.screen
        self.center = center
        self.lifetime = 20
        self.timer = 0
        self.particles = [
            [random.randint(-20, 20), random.randint(-20, 20), random.randint(3, 7)]
            for _ in range(8)
        ]
        self.image = pygame.Surface((1, 1))
        self.rect = self.image.get_rect(center=center)

    def update(self):
        self.timer += 1
        if self.timer >= self.lifetime:
            self.kill()

    def draw_explosion(self):
        progress = self.timer / self.lifetime
        for dx, dy, size in self.particles:
            x = self.center[0] + int(dx * (1 + progress * 2))
            y = self.center[1] + int(dy * (1 + progress * 2))
            g = max(0, int(180 * (1 - progress)))
            current_size = max(1, int(size * (1 - progress * 0.6)))
            pygame.draw.circle(self.screen, (255, g, 0), (x, y), current_size)
