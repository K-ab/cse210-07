#makes the collisions
class Collisions:
  def __init__(self) -> None:
      pass

  def collide(self,a,b):
    return (
      a._x - b._x < b._size and 
      b._x - a._x < a._size and 
      a._y - b._y < b._size and 
      b._y - a._y < a._size  
    )