import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.kirby import Kirby
from dino_runner.utils.constants import POWER_UP_SOUND

# Aqui se van a gestionar los poderes que apareceran en el mapa
class PowerUpManager:
    """
    Eliminare las listas las seteare de una manera distinta
    self.power_ups[]
    self.options_numbers = list(range(1, 10))
    
    el chiste es ir reemplazando las listas para que no salgan
    juntas
    """
    def __init__(self):
     self.current_power_up = None # No hay un power Up - Variable de instanci
     """
     una variable de instancia o miembro de dato es una variable que se relaciona con una única instancia de una clase
     """
     self.points = 0
     self.when_appears = 0
     self.power_up_sound = POWER_UP_SOUND
    
    def generate_power_ups(self,points):
        self.points = points
        
        """if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                print("Generating power up")
                # Va a ir alternando en las puntuaciones
                self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                self.power_ups.append(Shield())
                self.power_ups.append(Kirby())"""
        if self.current_power_up is not None: # Ya tenemos algo
            return[self.current_power_up] # Devuelve que ya tenemos algo
        
        if self.when_appears == self.points:
            print("Generating power up")
            self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
            
            # Vamos a hacer una lista para ir alternando una de ellas
            power_up_option = [Shield(), Hammer(), Kirby()]
            # Ahora usaremos random para alternas nustros power ups
            new_power_up = random.choice(power_up_option) # choice devuelve algo al azar de una lista u una tupla

            # Ahora guardaremos nuestra variable instanciada con un valor
            self.current_power_up = new_power_up
            return [new_power_up] # Nos devolvera el nuevo power up para ser usado
        
        return [] #Nos devuelve una lista vacia para volver a iniciar en caso de que no se genere algo nuevo
    
        """return self.power_ups -  le daremos un uso ahora con """
    
    def update(self, points, game_speed, player):
        self.generate_power_ups(points)
        """for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)"""
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
        # En lugar de iterar un bucle solo mandamos a llamar al metodo draw en el objeto actual que este en la lista
        if self.current_power_up is not None:
            self.current_power_up.draw(screen)