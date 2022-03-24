import pyray
from raylib import ImageResize

bSize = 40
coinSize = int(bSize * 0.8)
playerSize = int(bSize * 0.8)

speed = 2

coinImg = pyray.load_image('pacman\imgs\coin.png')
pyray.image_resize(coinImg, coinSize, coinSize)

player = pyray.load_image('pacman\imgs\pacman.png')
pyray.image_resize(player, playerSize, playerSize)

ghost = pyray.load_image('pacman\imgs\ghost.png')
pyray.image_resize(ghost, bSize, bSize)

blocks = []
coins = []
pacman = []
ghosts = []

FONT_SIZE = 15
COLUMNS = 40
ROWS = 20
MAX_X = 520
MAX_Y = 520
FRAME_RATE = 15
CAPTION = "PAC_MAN"
