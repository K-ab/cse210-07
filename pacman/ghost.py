import pyray
import setup

#pacman ghosts

class Ghost():
  def __init__(self,x,y) -> None:
      self._x = x
      self._y = y
      self._ghostSize = setup.bSize
      self.ghostTexture = pyray.load_texture_from_image(setup.ghost)

  def displayGhost(self):
    pyray.draw_texture(self.ghostTexture, self._x, self._y, pyray.WHITE)
