import pygame

class Gas():
    def __init__(self, displaysurf, gasX, gasY, GASIMG, TANKIMG, CONSIMG, CONSUMELIMIT, CONSUMEHEIGHT, CONSUMEWIDTH):
        self.displaysurf = displaysurf
        self.x = gasX
        self.y = gasY
        self.gasimg = GASIMG
        self.tankimg = TANKIMG
        self.consimg = CONSIMG
        self.CONSUMELIMIT = CONSUMELIMIT
        self.CONSUMEHEIGHT = CONSUMEHEIGHT
        self.CONSUMEWIDTH = CONSUMEWIDTH
    def draw(self):
        self.displaysurf.blit(self.gasimg,(self.x, self.y))
        self.displaysurf.blit(self.tankimg, (self.x, self.y - 13))
        self.displaysurf.blit(self.consimg,(self.x + 3, self.y + 80))
    def pump_brake(self, brake):
        if brake == True:
            if self.CONSUMELIMIT < 2:
                self.CONSUMELIMIT = 0
            else:
                self.CONSUMELIMIT -= 2
        self.CONSUMEHEIGHT = 217*self.CONSUMELIMIT/1000
        self.consimg = pygame.image.load("image/Red.png")
        self.consimg = pygame.transform.scale(self.consimg, (self.CONSUMEWIDTH, self.CONSUMEHEIGHT))