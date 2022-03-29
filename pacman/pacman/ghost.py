import pyray
import setup
import random
from collisions import Collisions

#pacman ghosts

class Ghost():
  def __init__(self,x,y) -> None:
      self._x = x
      self._y = y
      self._size = setup.ghostSize
      self.eyeTexture = [pyray.load_texture_from_image(i) for i in setup.ghostEyes]
      self.currentTexture = random.choice(self.eyeTexture)
      self.blank = pyray.load_texture_from_image(setup.ghostBlank)
      self.prevSides = []
      self.speed = 2
      self.vel = pyray.Vector2(1,0)
      self.collide = Collisions()
      self.colors = setup.colors[len(setup.ghosts)-1]

  def displayGhost(self):
    pyray.draw_texture(self.blank, self._x, self._y, self.colors)
    pyray.draw_texture(self.currentTexture, self._x+setup.eyesOffsetW, self._y+setup.eyesOffsetH, pyray.WHITE)

  def move(self):
    self.prev = pyray.Vector2(self._x, self._y)    
    self._x += int(self.vel.x)
    self.collideH()
    self._y += int(self.vel.y)
    self.collideV()
    self.checkSides()

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

  def checkSides(self):
    self.sides = [] 
    self.a = pyray.Vector2(self._x, self._y)
    id = setup.board[setup.lvl]

    if (id[ int(self.a.y /  setup.bSize)][ int(self.a.x /  setup.bSize) - 1]  == "b") :
      pass
    else :
      self.sides.append("Left") 
     
    if (id[ int(self.a.y /  setup.bSize)][ int(self.a.x /  setup.bSize) + 1]  == "b") :
      pass
    else :
      self.sides.append("Right") 
     
    if (id[ int(self.a.y /  setup.bSize) - 1][ int(self.a.x /  setup.bSize)]  == "b") :
      pass
    else :
      self.sides.append("Up") 
     
    if (id[ int(self.a.y /  setup.bSize) + 1][ int(self.a.x /  setup.bSize)]  == "b") :
      pass
    else :
      self.sides.append("Down") 
     
    direction = self.sides 

    if (
      set(self.sides) != set(self.prevSides) or
      set([self._x, self._y]) == set([self.prev.x,self.prev.y])
    ): 
      
      self.dir = direction[(random.randint(0,len(direction)-1))] 
      if (self.dir == "Left"):
          self.vel = pyray.Vector2(-self.speed,0)
          self.currentTexture = self.eyeTexture[1]
      elif self.dir == "Right":
          self.vel = pyray.Vector2(self.speed,0)
          self.currentTexture = self.eyeTexture[0]
      elif self.dir == 'Up':
          self.vel = pyray.Vector2(0,-self.speed)
          self.currentTexture = self.eyeTexture[2]
      elif self.dir == "Down":
          self.vel = pyray.Vector2(0,self.speed)
          self.currentTexture = self.eyeTexture[3]

    s = self.prevSides 
    self.prevSides = self.sides 
    return [direction, self.sides, s] 
   

