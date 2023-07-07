from pygame.locals import *
from gas import *
from obstacles import *
from bike import *
import sys

CONSUMELIMIT = 1000
FPS = 60
fpsClock = pygame.time.Clock()

def rectCollision(rect1, rect2):
    if rect1[0] <= rect2[0] + rect2[2] and rect2[0] <= rect1[0] + rect1[2] and rect1[1] <= rect2[1] + rect2[3] and rect2[1] <= rect1[1] + rect1[3]:
        return True
    return False

def isGameover(car, obstacles):
    global CONSUMELIMIT
    if CONSUMELIMIT == 0:
        return True
    carRect = [car.x, car.y, car.width, car.height]
    for i in range(5):
        x = int(X_MARGIN + obstacles.ls[i][0] * LANEWIDTH + (LANEWIDTH - obstacles.width) / 2)
        y = int(obstacles.ls[i][1])
        obstaclesRect = [x, y, obstacles.width, obstacles.height]
        if rectCollision(carRect, obstaclesRect) == True:
            return True
    return False

def gameStart(display_surf, bg):
    bg.__init__(display_surf)
    font = pygame.font.SysFont('consolas', 60)
    headingSuface = font.render('RACING', True, (255, 0, 0))
    headingSize = headingSuface.get_size()
    font = pygame.font.SysFont('consolas', 20)
    commentSuface = font.render('Press "space" to play', True, (0, 0, 0))
    commentSize = commentSuface.get_size()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == K_SPACE:
                    return
        bg.draw()
        display_surf.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0]) / 2), 100))
        display_surf.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0]) / 2), 400))
        pygame.display.update()
        fpsClock.tick(FPS)

def gamePlay(display_surf, bg, bike, obstacles, score, gas):
    bike.__init__(display_surf)
    obstacles.__init__(display_surf)
    bg.__init__(display_surf)
    score.__init__(display_surf)
    gas.__init__(display_surf)
    moveLeft = False
    moveRight = False
    brake = False
    while True:
        global CONSUMELIMIT
        global CONSUMEHEIGHT
        global CONSUMEWIDTH
        global CONSIMG
        CONSUMELIMIT -= 0.5
        CONSUMEHEIGHT = 217 * CONSUMELIMIT / 1000
        CONSIMG = pygame.image.load('game/image/Red.png')
        CONSIMG = pygame.transform.scale(CONSIMG, (CONSUMEWIDTH, CONSUMEHEIGHT))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    moveLeft = True
                if event.key == K_RIGHT:
                    moveRight = True
                if event.key == K_DOWN:
                    brake = True
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    moveLeft = False
                if event.key == K_RIGHT:
                    moveRight = False
                if event.key == K_DOWN:
                    brake = False
        if isGameover(bike, obstacles):
            return
        bg.draw()
        bg.update()
        bg.pump_brake(brake)
        bike.draw()
        bike.update(moveLeft, moveRight)
        gas.draw()
        gas.pump_brake(brake)
        obstacles.draw()
        obstacles.update()
        obstacles.pump_brake(brake)
        score.draw()
        score.update()
        pygame.display.update()
        fpsClock.tick(FPS)

def gameOver(display_surf, bg, bike, obstacles, score, gas):
    global CONSUMELIMIT
    font = pygame.font.SysFont('consolas', 60)
    headingSuface = font.render('GAMEOVER', True, (255, 0, 0))
    headingSize = headingSuface.get_size()

    font = pygame.font.SysFont('consolas', 20)
    commentSuface = font.render('Press "space" to replay', True, (0, 0, 0))
    commentSize = commentSuface.get_size()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == K_SPACE:
                    CONSUMELIMIT = 1000
                    CONSUMEHEIGHT = 217 * CONSUMELIMIT / 1000
                    CONSIMG = pygame.image.load('game/image/Red.png')
                    CONSIMG = pygame.transform.scale(CONSIMG, (CONSUMEWIDTH, CONSUMEHEIGHT))
                    return
        bg.draw()
        bike.draw()
        obstacles.draw()
        score.draw()
        gas.draw()
        display_surf.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0]) / 2), 100))
        display_surf.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0]) / 2), 400))
        pygame.display.update()
        fpsClock.tick(FPS)
