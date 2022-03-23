import setup
from block import Block
from coins import Coins
from player import Player
from ghost import Ghost

#creates the boards

class Board: 
  def __init__(self) -> None:
    self.board = [
      [
        'bbbbbbbbbbbbb',
        'bgcccccccccgb',
        'bcbbcbbbcbbcb',
        'bcbcccccccbcb',
        'bcccccccccccb',
        'bcbcccccccbcb',
        'bcbcccpcccbcb',
        'bcbcccccccbcb',
        'bcccccccccccb',
        'bcbcccccccbcb',
        'bcbbcbbbcbbcb',
        'bgcccccccccgb',
        'bbbbbbbbbbbbb'
      ]]
    self.level = 0

  def createBoard(self):
    print(self.board[self.level])
    for i in range(len(self.board[self.level])):
      for j in range(len(self.board[self.level][i])):
        id = self.board[self.level][i][j]
        if id == 'b':
          setup.blocks.append(Block(j*setup.bSize, i*setup.bSize))
        elif id == 'c':
          setup.coins.append(Coins(j*setup.bSize, i*setup.bSize))
        elif id == 'g':
          setup.ghosts.append(Ghost(j*setup.bSize, i*setup.bSize))
        elif id == 'p':
          setup.pacman.append(Player(j*setup.bSize,i*setup.bSize))

  def displayBoard(self):
    for i in range(len(setup.blocks)):
      setup.blocks[i].displayBlock()
    
    for i in range(len(setup.coins)):
      setup.coins[i].displayCoins()
    
    for i in range(len(setup.pacman)):
      setup.pacman[i].movePlayer()
      setup.pacman[i].createPlayer()

    for i in range(len(setup.ghosts)):
      setup.ghosts[i].displayGhost()
