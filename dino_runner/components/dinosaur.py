import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import (
    RUNNING, 
    DUCKING, 
    JUMPING,
    DEFAULT_TYPE,
    SHIELD_TYPE,
    KIRBY_TYPE,
    RUNNING_SHIELD,
    DUCKING_SHIELD,
    JUMPING_SHIELD,
    HAMMER_TYPE,
    RUNNING_HAMMER,
    JUMPING_HAMMER,
    DUCKING_HAMMER,
    JUMP_SOUND)

class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310
    POS_Y_DUCKING = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.run_img = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, KIRBY_TYPE: RUNNING}
        self.duck_img = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, KIRBY_TYPE: DUCKING}
        self.jump_img = { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, KIRBY_TYPE: JUMPING}
        self.type =  DEFAULT_TYPE        
        self.image = self.run_img[self.type][0]
        
        
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.setup_states()
        
        # Codigo nuevo
        self.jump_sound = JUMP_SOUND
        

    def setup_states(self):
        self.has_power_up = False
        self.shield =  False
        self.shield_time_up = 0

    def update(self, user_input):
        # Llama a los metodos para hacer las modificaciones de Animacion
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()

        # and not self.dino_jump da prioridad a evitar a hacer multiples acciones
        # Aqui se hacen las comprobaciones del teclado
        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
            
        elif user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
            self.jump_sound.play()
            
            # Si no toca nada entonces vuelve a correr
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False
        
        # Resetea la animacion en 0 para asegurar que se muestre todo correctamente
        if self.step_index >= 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, self.dino_rect)

    #Todos estos se llaman al update
    def run(self):
        self.image = self.run_img[self.type][self.step_index // 5]
        
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y
        self.step_index += 1
    def duck(self):
        self.image = self.duck_img[self.type][self.step_index // 5]
        
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y_DUCKING
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img[self.type]
        # Hace referencia para ser llamado arriba
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4 # Salto
            self.jump_vel -= 0.8 # Salto, cuando llega a negativo, baja
        # Ejecuta la logica para bajar al dinosario otra vez
        if self.jump_vel < -self.JUMP_VEL: # Cuando llega a JUMP_VEL en negativo, este se detiene
            self.dino_rect.y = self.POS_Y
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL
            
    # Revisar invesibility
    
    def check_invincibility(self):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 1000, 2)
            
            if not time_to_show >= 0:
                self.shield = False
                self.update_to_default(SHIELD_TYPE)
    
    def update_to_default(self, current_type):
        if self.type == current_type:
            self.type =  DEFAULT_TYPE