import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.utils.constants import POWER_UP_SOUND

# Aqui se van a gestionar los poderes que apareceran en el mapa
class PowerUpManager:
    
    def __init__(self):
     self.power_ups = []
     self.points = 0
     self.when_appears = 0
     self.options_numbers = list(range(1, 10))
     self.power_up_sound = POWER_UP_SOUND
        
    
    def generate_power_ups(self,points):
        self.poins = points
        
        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                print("Generating power up")
                # Va a ir alternando en las puntuaciones
                self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                self.power_ups.append(Shield())
        
        return self.power_ups
    
    def update(self, points, game_speed, player):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            
            if player.dino_rect.colliderect(power_up.rect):
                player.shield = True
                self.power_up_sound.play()
                player.type = power_up.type
                start_time = pygame.time.get_ticks()
                time_random = random.randrange(5, 8)
                player.shield_time_up = start_time + (time_random * 1000)
                
                self.power_ups.remove(power_up)
    
    def draw(self, screen):
        for powerup in self.power_ups:
            powerup.draw(screen)