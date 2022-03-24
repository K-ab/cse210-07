import setup
import pyray
from collisions import Collisions as c

#creates the coins

class Coins():
  def __init__(self, x, y) -> None:
    self._x = int(x+(setup.bSize-setup.coinSize)/2)
    self._y = int(y+(setup.bSize-setup.coinSize)/2)
    self._size = setup.coinSize
    self.texture = pyray.load_texture_from_image(setup.coinImg)

  def displayCoins(self):
    pyray.draw_texture(self.texture, self._x, self._y, pyray.WHITE)
  
  def collected(self):
    for i in range(len(setup.pacman)):
      if c().collide(self,setup.pacman[i]):
        return True
      
    return False