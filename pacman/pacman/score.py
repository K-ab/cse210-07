import pyray
import setup

class Score:
  def __init__(self) -> None:
    self.score = 0

  def resetScore(self):
    self.score = 0
  
  def addPoints(self):
    self.score += 1
  
  def displayScore(self):
    pyray.draw_text(f'Score: {str(self.score)}', 420, 10, setup.FONT_SIZE, pyray.WHITE)