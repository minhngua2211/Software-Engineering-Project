import pygame, sys
from pygame.locals import *
from bike import Bike
from gas import Gas
from background import Background
from score import Score
from obstacles import Obstacles
from gas_station import Gas_Station
from level import Level
from pygame import mixer
pygame.init()

WINDOWWIDTH = 400 
WINDOWHEIGHT = 620

X_MARGIN = 80
LANEWIDTH = 60

#Size of obstacles
OBWIDTH = 56
OBHEIGHT = 56

GASWIDTH = 40
GASHEIGHT = 40
GASIMG = pygame.image.load('image\gas_icon.png')
GASIMG = pygame.transform.scale(GASIMG, (GASWIDTH, GASHEIGHT))
TANKWIDTH = 40
TANKHEIGHT = 400
TANKIMG = pygame.image.load('image/rectangle.png')
TANKIMG = pygame.transform.scale(TANKIMG, (TANKWIDTH, TANKHEIGHT))
CONSUMELIMIT = 1000
CONSUMEWIDTH = 35
CONSUMEHEIGHT = 217 * CONSUMELIMIT/1000
CONSIMG = pygame.image.load('image/Red.png')
CONSIMG = pygame.transform.scale(CONSIMG, (CONSUMEWIDTH, CONSUMEHEIGHT))
GAS_X = 10
GAS_Y = 50

#Figures of car
BIKEWIDTH = 50
BIKEHEIGHT = 90
BIKESPEED = 5
BIKEIMG = pygame.image.load('image/motorcycle.png')
BIKEIMG = pygame.transform.scale(BIKEIMG, (BIKEWIDTH, BIKEHEIGHT))
BIKE_X = (WINDOWWIDTH-BIKEWIDTH)/2
BIKE_Y = WINDOWHEIGHT*0.8

#Other figures of obstacles
DISTANCE = 200
OBSTACLESSPEED = 3
CHANGESPEED = 0.005
OBSTACLESIMG = pygame.image.load('image/Rock Pile.png')

#Create backgound and scroll
BGSPEED = 3
BGIMG = pygame.image.load('image/background.png')
BG_X = 0
BG_Y = 0

#figure of gas_station
GAS_STATION_X = 310
GAS_STATION_Y = 0
GAS_STATION_WIDTH = 80
GAS_STATION_HEIGHT = 80
GAS_STATIONIMG = pygame.image.load("image/gas_station.png")
GAS_STATIONIMG = pygame.transform.scale(GAS_STATIONIMG, (GAS_STATION_WIDTH, GAS_STATION_HEIGHT))
GAS_DISTANCE = 7*WINDOWHEIGHT
GASICON = pygame.image.load("image/energy.png")
GASICON = pygame.transform.scale(GASICON, (50, 50))

# game window
displaysurf = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Motocycle")

FPS = 60
fpsClock = pygame.time.Clock()

background_music = mixer.Sound("sound/background_music.mp3")
background_music.set_volume(0.1)
background_music.play(-1)

#Handle collistion
def rectCollision(rect1, rect2):
    if rect1[0] <= rect2[0]+rect2[2] and rect2[0] <= rect1[0]+rect1[2] and rect1[1] <= rect2[1]+rect2[3] and rect2[1] <= rect1[1]+rect1[3]:
        return True
    return False

def is_refuel(gas_station, bike):
    if int(bike.y) <= int(gas_station.ls[0] + GAS_STATION_HEIGHT):
        return True

#Lose game
def isGameover(bike, obstacles, gas):
    if gas.CONSUMELIMIT == 0:
        return True
    bikeRect = [bike.x, bike.y, bike.width, bike.height]
    for i in range(5):
        x = int(X_MARGIN + obstacles.ls[i][0]*LANEWIDTH + (LANEWIDTH-obstacles.obwidth)/2)
        y = int(obstacles.ls[i][1])
        obstaclesRect = [x, y, obstacles.obwidth, obstacles.obheight]
        if rectCollision(bikeRect, obstaclesRect) == True:
            return True
    return False

#Build Start function
def gameStart(bg, displaysurf):
    bg.__init__(displaysurf,BGSPEED, BGIMG, BG_X, BG_Y)
    font = pygame.font.SysFont('Arial', 40)
    headingSuface = font.render('GOAT RACING GAME', True, (255, 0, 0))
    headingSize = headingSuface.get_size()
    font = pygame.font.SysFont('consolas', 20)
    creditSuface = font.render('Made by group Goat', True, (0, 0, 0))
    font = pygame.font.SysFont('consolas', 20)
    startSurface = font.render('Start', True, (0, 0, 0))
    exitSurface = font.render('Exit', True, (0, 0, 0))
    startSize = startSurface.get_size()
    exitSize = exitSurface.get_size()
    selected = "start"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == K_SPACE:
                    if selected == "start":
                        return
                    elif selected == "exit":
                        pygame.quit()
                        sys.exit()
                elif event.key == K_UP or event.key == K_DOWN:
                    if selected == "start":
                        selected = "exit"
                    elif selected == "exit":
                        selected = "start"
        bg.draw()
        displaysurf.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0])/2), 100))
        displaysurf.blit(creditSuface, (200, 600))
        if selected == "start":
            pygame.draw.rect(displaysurf, (0, 255, 0), ((int((WINDOWWIDTH - startSize[0]) / 2) - 10, 200 - 10),
                                                         (startSize[0] + 20, startSize[1] + 20)))
        else:
            pygame.draw.rect(displaysurf, (255, 255, 255), ((int((WINDOWWIDTH - startSize[0]) / 2) - 10, 200 - 10),
                                                             (startSize[0] + 20, startSize[1] + 20)))
        displaysurf.blit(startSurface, (int((WINDOWWIDTH - startSize[0]) / 2), 200))

        if selected == "exit":
            pygame.draw.rect(displaysurf, (0, 255, 0), ((int((WINDOWWIDTH - exitSize[0]) / 2) - 10, 300 - 10),
                                                         (exitSize[0] + 20, exitSize[1] + 20)))
        else:
            pygame.draw.rect(displaysurf, (255, 255, 255), ((int((WINDOWWIDTH - exitSize[0]) / 2) - 10, 300 - 10),
                                                             (exitSize[0] + 20, exitSize[1] + 20)))
        displaysurf.blit(exitSurface, (int((WINDOWWIDTH - exitSize[0]) / 2), 300))
        pygame.display.update()
        fpsClock.tick(FPS)



def gamePlay(displaysurf,bg, bike, obstacles, score, gas, gas_station, level, BGSPEED, BIKESPEED, OBSTACLESSPEED):
    bike.__init__(BIKEWIDTH, BIKEHEIGHT, displaysurf, BIKEIMG, BIKESPEED, BIKE_X, BIKE_Y)
    obstacles.__init__(displaysurf, OBWIDTH, OBHEIGHT, DISTANCE, OBSTACLESSPEED, CHANGESPEED, OBSTACLESIMG)
    bg.__init__(displaysurf, BGSPEED, BGIMG, BG_X, BG_Y)
    score.__init__(displaysurf)
    gas.__init__(displaysurf, GAS_X, GAS_Y, GASIMG, TANKIMG, CONSIMG, CONSUMELIMIT, CONSUMEHEIGHT, CONSUMEWIDTH)
    gas_station.__init__(displaysurf,  GAS_STATIONIMG, BGSPEED, GAS_DISTANCE, GASICON)
    level.__init__(displaysurf)
    background_music.stop()
    moving_sound = mixer.Sound("sound/bike_sound.wav")
    moving_sound.set_volume(0.3)
    moving_sound.play(-1)
    moveLeft = False
    moveRight = False
    brake = False
    brake_sound = mixer.Sound("sound/brake_sound.mp3")
    brake_sound.set_volume(0.2)
    while True:
        if gas.CONSUMELIMIT < BGSPEED/6:
            gas.CONSUMELIMIT = 0
        else:
            gas.CONSUMELIMIT -= BGSPEED/6
        gas.CONSUMEHEIGHT = 217 * gas.CONSUMELIMIT/1000
        gas.CONSIMG = pygame.image.load('image/Red.png')
        gas.CONSIMG = pygame.transform.scale(CONSIMG, (CONSUMEWIDTH, CONSUMEHEIGHT))
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
        if isGameover(bike, obstacles, gas):
            moving_sound.stop()
            background_music.play(-1)
            return
        if is_refuel(gas_station, bike):
            gas.CONSUMELIMIT = 1000
            gas.CONSUMEHEIGHT = 217 * gas.CONSUMELIMIT/1000
            gas.CONSIMG = pygame.image.load('image/Red.png')
            gas.CONSIMG = pygame.transform.scale(CONSIMG, (CONSUMEWIDTH, CONSUMEHEIGHT))       
        bg.draw()
        bg.update()
        bg.pump_brake(brake, BGSPEED)
        bike.draw()
        bike.update(moveLeft, moveRight)
        gas.draw()
        gas.pump_brake(brake)
        obstacles.draw()
        obstacles.update()
        obstacles.pump_brake(brake,OBSTACLESSPEED)
        score.draw()
        score.update(bg.speed)
        gas_station.draw()
        gas_station.update()
        gas_station.pump_brake(brake, BGSPEED)
        level.draw()
        level.update(score.score)
        if brake == True:
            brake_sound.play(-1)
        else:
            brake_sound.stop()
        if level.level - level.last_level == 1:
            BGSPEED += 1
            BIKESPEED += 1
            OBSTACLESSPEED += 1
            level.last_level = level.level
        pygame.display.update()
        fpsClock.tick(FPS)
# Build game over func
def gameOver(displaysurf, bg, bike, obstacles, score, gas, gas_station, level):
    font = pygame.font.SysFont('consolas', 50)
    headingSuface = font.render('GAMEOVER', True, (255, 255, 255))
    headingSize = headingSuface.get_size()
    font = pygame.font.SysFont('consolas', 30)
    scoreSurface = font.render('Your Score is: ' + str(int(score.get_score())), True, (255, 255, 255))
    scoreSize = scoreSurface.get_size()
    font = pygame.font.SysFont('consolas', 20)
    commentSuface = font.render('Press Space to return', True, (0, 0, 0))
    commentSize = commentSuface.get_size()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == K_SPACE:
                    gas.CONSUMELIMIT = 1000
                    gas.CONSUMEHEIGHT = 217 * gas.CONSUMELIMIT/1000
                    gas.CONSIMG = pygame.image.load('image/Red.png')
                    gas.CONSIMG = pygame.transform.scale(gas.CONSIMG, (gas.CONSUMEWIDTH, gas.CONSUMEHEIGHT))
                    gameStart(bg, displaysurf)
                    return
        bg.draw()
        bike.draw()
        obstacles.draw()
        score.draw()
        gas.draw()
        gas_station.draw()
        level.draw()
        displaysurf.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0])/2), 100))
        displaysurf.blit(scoreSurface, (int((WINDOWWIDTH - scoreSize[0])/2), 200))
        displaysurf.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0])/2), 400))
        pygame.display.update()

def main():
    bg = Background(displaysurf, BGSPEED, BGIMG, BG_X, BG_Y)
    bike = Bike(BIKEWIDTH, BIKEHEIGHT, displaysurf , BIKEIMG, BIKESPEED, BIKE_X, BIKE_Y)
    obstacles = Obstacles(displaysurf, OBWIDTH, OBHEIGHT, DISTANCE, OBSTACLESSPEED, CHANGESPEED, OBSTACLESIMG)
    score = Score(displaysurf)
    gas = Gas(displaysurf, GAS_X, GAS_Y, GASIMG, TANKIMG, CONSIMG, CONSUMELIMIT, CONSUMEHEIGHT, CONSUMEWIDTH)
    gas_station = Gas_Station(displaysurf,  GAS_STATIONIMG, BGSPEED, GAS_DISTANCE, GASICON)
    level = Level(displaysurf)
    gameStart(bg, displaysurf)
    while True:
        gamePlay(displaysurf, bg, bike, obstacles, score, gas, gas_station, level, BGSPEED, BIKESPEED, OBSTACLESSPEED)
        gameOver(displaysurf, bg, bike, obstacles, score, gas, gas_station, level)

if __name__ == '__main__':
    main()