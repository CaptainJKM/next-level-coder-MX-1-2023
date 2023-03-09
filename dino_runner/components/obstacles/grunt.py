import random
from dino_runner.components.obstacles.obstacle import Obstacle


class Grunt(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,7)
        super().__init__(image, self.type)
        self.rect.y = 325
        self.index = 0
    
    def draw(self, screen):
        
        if self.index >= 10:
            self.index = 0
            # "self.index < 5" devuelve True si el valor de "index" es menor que 5
        screen.blit(self.image[self.index < 5], self.rect)
        self.index += 1