import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point

#Cherry Powerups

class Food(Actor):
    """
    A tasty item that pacman likes to eat.
    
    The responsibility of Food is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "Constructs a new Food."
        super().__init__()
        self.set_text(constants.food)
        self.reset()
        
    def reset(self):
        """Selects a random position and points that the food is worth."""
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        
    def get_points(self):
        """Gets the points the food is worth.
        
        Returns:
            points (int): The points the food is worth.
        """
        return self._points