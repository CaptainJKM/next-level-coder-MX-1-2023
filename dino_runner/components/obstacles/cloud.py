import random

from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH

class Cloud():
    def  __init__(self):
        self.image = CLOUD
        self.width = self.image.get_width()    
        
        self.x = SCREEN_WIDTH + random.randint(1, 1000)
        self.y = random.randint(30, 90)
        
        self.game_speed = 4
    
    def update(self):
        self.x -= self.game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(1, 1000)
            self.y = random.randint(10, 60)
        
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    