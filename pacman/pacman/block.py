import setup
import pyray

#creates the blocks

class Block:
  def __init__(self, x, y) -> None:
    self._x = x
    self._y = y
    self._size = setup.bSize

  def displayBlock(self):
    pyray.draw_rectangle(self._x, self._y, self._size, self._size, setup.blockColor)

