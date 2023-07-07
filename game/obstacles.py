import pygame
import random

X_MARGIN = 80
LANEWIDTH = 60
OBWIDTH = 56
OBHEIGHT = 56
DISTANCE = 200
OBSTACLESSPEED = 3
CHANGESPEED = 0.005
WINDOWHEIGHT = 620
OBSTACLESIMG = pygame.image.load('game/image/Rock Pile.png')

class Obstacles():
    def __init__(self, display_surf):
        self.display_surf = display_surf
        self.width = OBWIDTH
        self.height = OBHEIGHT
        self.distance = DISTANCE
        self.speed = OBSTACLESSPEED
        self.changeSpeed = CHANGESPEED
        self.ls = []
        for i in range(5):
            y = -OBHEIGHT-i*self.distance
            lane = random.randint(0, 3)
            self.ls.append([lane, y])
    
    def draw(self):
        for i in range(5):
            x = int(X_MARGIN + self.ls[i][0]*LANEWIDTH + (LANEWIDTH-self.width)/2)
            y = int(self.ls[i][1])
            self.display_surf.blit(OBSTACLESIMG, (x, y))
    
    def update(self):
        for i in range(5):
            self.ls[i][1] += self.speed
        self.speed += self.changeSpeed
        if self.ls[0][1] > WINDOWHEIGHT:
            self.ls.pop(0)
            y = self.ls[3][1] - self.distance
            lane = random.randint(0, 3)
            self.ls.append([lane, y])
    
    def pump_brake(self, brake):
        if brake == True:
            self.speed = OBSTACLESSPEED * 0.5
        if brake == False:
            self.speed = OBSTACLESSPEED
