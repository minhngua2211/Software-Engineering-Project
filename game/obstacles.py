import random 

class Obstacles():
    def __init__(self, displaysurf, OBWIDTH, OBHEIGHT, DISTANCE, OBSTACLESSPEED, CHANGESPEED, OBSTACLESIMG):
        self.displaysurf = displaysurf
        self.obwidth = OBWIDTH
        self.obheight = OBHEIGHT
        self.distance = DISTANCE
        self.speed = OBSTACLESSPEED
        self.changespeed = CHANGESPEED
        self.img = OBSTACLESIMG
        self.ls = []
        self.X_MARGIN = 80
        self.LANEWIDTH = 60
        for i in range(5):
            y = - self.obheight - i*self.distance
            lane = random.randint(0,3) 
            self.ls.append([lane, y])
    def draw(self):
        for i in range(5):
            x = int(self.X_MARGIN + self.ls[i][0]*self.LANEWIDTH + (self.LANEWIDTH-self.obwidth)/2)
            y = int(self.ls[i][1])
            self.displaysurf.blit(self.img, (x, y))
    def update(self):
        for i in range(5):
            self.ls[i][1] += self.speed
        self.speed += self.changespeed
        if self.ls[0][1] > 620:
            self.ls.pop(0)
            y = self.ls[3][1] - self.distance
            lane = random.randint(0, 3)
            self.ls.append([lane, y])
    def pump_brake(self, brake, OBSTACLESSPEED):
        if brake == True:
            self.speed = OBSTACLESSPEED/2
        if brake == False:
            self.speed = OBSTACLESSPEED