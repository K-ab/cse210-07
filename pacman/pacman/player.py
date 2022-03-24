import pyray
import setup
from collisions import Collisions

#creates a player

class Player:
  def __init__(self,x,y) -> None:
    self._x = int(x+(setup.bSize-setup.playerSize)/2)
    self._y = int(y+(setup.bSize-setup.playerSize)/2)
    self._size = setup.playerSize
    self.playerTexture = pyray.load_texture_from_image(setup.player)
    self.vel = pyray.Vector2(0,0)
    self.speed = setup.speed
    self.collide = Collisions()

  def createPlayer(self):
    pyray.draw_texture(self.playerTexture, self._x, self._y, pyray.WHITE)
  
  def movePlayer(self):
    self.prev = pyray.Vector2(self._x, self._y)

    if pyray.is_key_pressed(pyray.KEY_D): #right
      self.vel = pyray.Vector2(self.speed, 0)
    if pyray.is_key_pressed(pyray.KEY_A): #left
      self.vel = pyray.Vector2(-self.speed, 0)
    
    self._x += int(self.vel.x)
    self.collideH()
    if pyray.is_key_pressed(pyray.KEY_S): #down
      self.vel = pyray.Vector2(0,self.speed)
    if pyray.is_key_pressed(pyray.KEY_W): #up
      self.vel = pyray.Vector2(0, -self.speed)

    self._y += int(self.vel.y)
    self.collideV()

    # for i in range(len(setup.coins)-1,0,-1):
    #   if(self.collide.collide(self, setup.coins[i])):
    #     setup.coins.pop(i)


  def collideV(self):
    for i in range(len(setup.blocks)):
      if self.collide.collide(self, setup.blocks[i]):
        b = setup.blocks[i]
        self._y = b._y - self._size if self.prev.y < b._y else b._y + b._size
        self.vel = pyray.Vector2(0,0)

  def collideH(self):
    for i in range(len(setup.blocks)):
      if self.collide.collide(self, setup.blocks[i]):
        b = setup.blocks[i]
        self._x = b._x - self._size if self.prev.x < b._x else b._x + b._size
        self.vel = pyray.Vector2(0,0)