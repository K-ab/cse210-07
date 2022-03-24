import pyray
import game
import setup

pyray.set_target_fps(60)

pyray.init_window(setup.MAX_X, setup.MAX_Y, setup.CAPTION)
gameBoard = game.Board()
gameBoard.createBoard()

while not pyray.window_should_close():
  pyray.begin_drawing()
  pyray.clear_background(pyray.BLACK)
  gameBoard.displayBoard()
  pyray.end_drawing()

pyray.close_window()