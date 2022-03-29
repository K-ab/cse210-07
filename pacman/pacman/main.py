import pyray
import setup
from scene import scenes

pyray.set_target_fps(60)

pyray.init_window(setup.MAX_X, setup.MAX_Y, setup.CAPTION)

while not pyray.window_should_close():
  pyray.begin_drawing()
  pyray.clear_background(pyray.BLACK)
  scenes[setup.display]()
  pyray.end_drawing()

pyray.close_window()