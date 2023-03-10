import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.kirby import Kirby
from dino_runner.utils.constants import POWER_UP_SOUND

# Aqui se van a gestionar los poderes que apareceran en el mapa
class PowerUpManager:
    def __init__(self):
     self.current_power_up = None # No hay un power Up - Variable de instancia
     self.points = 0
     self.when_appears = 0
     self.power_up_sound = POWER_UP_SOUND
    
    def generate_power_ups(self,points):
        self.points = points
        
        if self.current_power_up is not None: # Ya tenemos algo
            return[self.current_power_up] # Devuelve que ya tenemos algo
        
        if self.when_appears == self.points:
            print("Generating power up")
            self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
            
            # Vamos a hacer una lista para ir alternando una de ellas
            power_up_option = [Shield(), Hammer(), Kirby()]
            # Ahora usaremos random para alternas nustros power ups
            new_power_up = random.choice(power_up_option) 

            
            self.current_power_up = new_power_up
            return [new_power_up] 
        
        return [] 
    
        """return self.power_ups -  le daremos un uso ahora con """
    
    def update(self, points, game_speed, player):
        self.generate_power_ups(points)
        if self.current_power_up is not None: 
            self.current_power_up.update(game_speed, self.current_power_up)
                        
            if player.dino_rect.colliderect(self.current_power_up.rect):
                player.shield = True
                self.power_up_sound.play()
                player.type = self.current_power_up.type
                start_time = pygame.time.get_ticks()
                time_random = random.randrange(5, 8)
                player.shield_time_up = start_time + (time_random * 1000)
            
                self.current_power_up = None # Nos volvemos a asegurar de tener un powerup luego de tener el juego
                
    
    def draw(self, screen):
        if self.current_power_up is not None:
            self.current_power_up.draw(screen)