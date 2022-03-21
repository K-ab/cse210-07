import constants
from game.casting.actor import Actor
from game.shared.point import Point

#Pacman himself

class Player(Actor):
    """
    A pacman character.
    
    The responsibility of Player is to move itself.

    Attributes:
        
    """
    def __init__(self):
        super().__init__()
        self.player = constants.p

    def move_next(self):
        #move player
        pass
