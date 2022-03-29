import pyray
from raylib import ImageResize

board = [
      [
        'bbbbbbbbbbbbb',
        'bgcccccccccgb',
        'bcbbcbbbcbbcb',
        'bcbcccccccbcb',
        'bcccbbcbbcccb',
        'bcbcbcccbcbcb',
        'bcbcccpcccbcb',
        'bcbcbcccbcbcb',
        'bcccbbcbbcccb',
        'bcbcccccccbcb',
        'bcbbcbbbcbbcb',
        'bgcccccccccgb',
        'bbbbbbbbbbbbb'
      ]]
lvl = 0

bSize = 40
coinSize = int(bSize * 0.8)
playerSize = int(bSize * 0.8)
ghostSize = int(bSize * 0.8)

speed = 2
display = 'play'

gameOverImg = pyray.load_image(r'cse210-06\pacman\imgs\gameOver.png')
pyray.image_resize(gameOverImg, 200, 200)

coinImg = pyray.load_image(r'cse210-06\pacman\imgs\coin.png')
pyray.image_resize(coinImg, coinSize, coinSize)

player = pyray.load_image(r'cse210-06\pacman\imgs\pacman.png')
pyray.image_resize(player, playerSize, playerSize)

ghostEyes = [
  pyray.load_image(r'cse210-06\pacman\imgs\eyesRight.png'),
  pyray.load_image(r'cse210-06\pacman\imgs\eyesLeft.png'),
  pyray.load_image(r'cse210-06\pacman\imgs\eyesUp.png'),
  pyray.load_image(r'cse210-06\pacman\imgs\eyesDown.png')
]

ghostBlank = pyray.load_image(r'cse210-06\pacman\imgs\blankGhost.png')
pyray.image_resize(ghostBlank, ghostSize, ghostSize)

eyesOffsetW = int((ghostSize - int(ghostSize*0.64))/2)
eyesOffsetH = int((ghostSize - int(ghostSize*0.32))/3)

for i in ghostEyes:
  pyray.image_resize(i, int(ghostSize * 0.64), int(ghostSize * 0.32))

colors = [
  pyray.Color(255, 13, 174, 255),
  pyray.Color(0, 184, 125, 255),
  pyray.Color(51, 204, 255, 255),
  pyray.Color(255, 0, 0, 255)
]

blockColor = pyray.Color(41, 117, 39, 255)

blocks = []
coins = []
pacman = []
ghosts = []

FONT_SIZE = 16
COLUMNS = 40
ROWS = 20
MAX_X = 520
MAX_Y = 520
FRAME_RATE = 15
CAPTION = "PAC_MAN"
