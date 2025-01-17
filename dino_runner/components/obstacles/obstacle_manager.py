import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.grunt import Grunt
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, CRASH_SOUND, PUNCH_SOUND, GRUNT

class ObstacleManager():

    def __init__(self):
        self.obstacles = []
        self.crash_sound = CRASH_SOUND
        self.punch = PUNCH_SOUND
        
        
    def update(self, game_speed, game):

        if len(self.obstacles) == 0:
            type = random.randint(0, 3)
            match type:
                case 0:
                    self.obstacles.append(Grunt(GRUNT)) 
                case 1:
                    self.obstacles.append(Cactus(SMALL_CACTUS))
                case 2:
                    self.obstacles.append(Cactus(LARGE_CACTUS))
                case 3:
                    self.obstacles.append(Bird(BIRD))
                     
                
    
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            
            # Si tiene el escudo agregar una condicional y un tiempo para traspasar
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    game.heart_manager.reduce_heart()
                if game.heart_manager.heart_count < 1:
                    pygame.time.delay(300)
                    game.playing = False
                    break
                else:
                    self.obstacles.remove(obstacle)
                    self.crash_sound.play()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)