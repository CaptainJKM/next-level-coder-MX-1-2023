import random

from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH


class PowerUp(Sprite):
    
    def __init__(self, image, type):
        self.image = image 
        self.type = type # Tipo que nos llega
        self.rect = self.image.get_rect()
        # Haremos que aparezcan en diferentes lados
        self.rect.y = random.randint(125, 150)
        self.rect.x = SCREEN_WIDTH # Lo mismo que con los obstaculos
        
        self.start = 0
        self.width = self.image.get_width()
        
    def update(self, game_speed, powerups):
        self.rect.x -= game_speed
        
        if self.rect.x < 0:
            powerups.pop()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)