import pyray
import setup
import game
import math

class Scene():
  def __init__(self) -> None:
    self.gameBoard = game.Board()
    self.drawOnce = 0
    self.a = 0

  def play(self):
    pyray.clear_background(pyray.BLACK)
    if not self.drawOnce:
      self.deadImg = pyray.load_texture_from_image(setup.gameOverImg)
      self.gameBoard.createBoard()
      self.drawOnce = 1
    
    else:
      self.gameBoard.displayBoard()

  def gameOver(self):
    self.a += 5
    pyray.clear_background(pyray.BLACK)
    pyray.draw_text('GAME OVER', 90, 75, setup.FONT_SIZE*4, pyray.Color(255,0,0,int((255/2)+(255/2)*math.sin(self.a/(180/math.pi)))))
    pyray.draw_texture(self.deadImg, 175, 150, pyray.WHITE)
    self.restart()

  def restart(self):
    pyray.draw_text('CLICK TO RESTART', 120, 400, setup.FONT_SIZE*2, pyray.YELLOW)
    if pyray.is_mouse_button_pressed(0):
      setup.display = 'play'
      self.drawOnce = 0
      self.play()

level = Scene()
scenes = {
  'play': level.play,
  'gameOver': level.gameOver
}