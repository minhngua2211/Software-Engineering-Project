class Gas_Station():
    def __init__(self, displaysurf, GAS_STATIONIMG, BGSPEED, GAS_DISTANCE, GASICON):
            self.displaysurf = displaysurf
            self.x = 320
            self. y = 0
            self.img = GAS_STATIONIMG
            self.speed = BGSPEED
            self.distance = GAS_DISTANCE
            self.icon = GASICON
            self.ls = []
            for i in range(1,3):
                 y = - i*self.distance
                 self.ls.append(y)
    def draw(self):
            for i in range(2):
                 self.y = int(self.ls[i])
                 self.displaysurf.blit(self.img, (self.x, self.y))
                 self.displaysurf.blit(self.icon, (self.x - 55, self.y + 30))
                 self.displaysurf.blit(self.icon, (self.x - 115, self.y + 30))
                 self.displaysurf.blit(self.icon, (self.x - 175, self.y + 30))
                 self.displaysurf.blit(self.icon, (self.x - 235, self.y + 30))
    def update(self):
        for i in range(2):
            self.ls[i] += self.speed
        if self.ls[0] > 620:
            self.ls.pop(0)
            y = self.ls[0] - self.distance
            self.ls.append(y)
    def pump_brake(self, brake, BGSPEED):
        if brake == True:
            self.speed = BGSPEED/2
        if brake == False:
            self.speed = BGSPEED
         
