from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import KIRBY_TYPE, KIRBY

class Kirby(PowerUp):
    def __init__(self):
        self.image = KIRBY
        self.type = KIRBY_TYPE
        # Reduciremos la velocidad
        # self.slowdown_dino = 0.5 # Quitaremos la mitad
        super().__init__(self.image, self.type)