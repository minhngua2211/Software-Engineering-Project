import pygame, sys
from pygame.locals import *
from background import Background
from obstacles import Obstacles
from gas import Gas
from bike import Bike
from score import Score
from game_functions import *

pygame.init()

WINDOWWIDTH = 400
WINDOWHEIGHT = 620
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Goat Motoracing Game')

def main():
    bg = Background(DISPLAYSURF)
    bike = Bike(DISPLAYSURF)
    obstacles = Obstacles(DISPLAYSURF)
    score = Score(DISPLAYSURF)
    gas = Gas(DISPLAYSURF)
    gameStart(DISPLAYSURF, bg)
    while True:
        gamePlay(DISPLAYSURF, bg, bike, obstacles, score, gas)
        gameOver(DISPLAYSURF, bg, bike, obstacles, score, gas)

if __name__ == '__main__':
    main()
