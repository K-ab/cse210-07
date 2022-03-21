from constants import *
board = [
  [b,b,b,b,b,b,b,b,b,],
  [b,g,c,c,c,c,c,g,b],
  [b,c,b,b,c,b,b,c,b],
  [b,c,b,c,c,c,b,c,b],
  [b,c,c,c,p,c,c,c,b],
  [b,c,b,c,c,c,b,c,b],
  [b,c,b,b,c,b,b,c,b],
  [b,g,c,c,c,c,c,g,b],
  [b,b,b,b,b,b,b,b,b],
]
for i in range(len(board)):
  for j in range(len(board[i])):
    id = board[i][j]
    if id == b:
      blocks.append(Block(j*bSize, i*bSize))
    elif id == c:
      coins.append(Coin(j*bSize, i*bSize))
    elif id == g:
      ghost.append(Ghost(j*bSize, i*bSize))
    elif id == p:
      player.append(Player(j*bSize,i*bSize))