import pygame

GASWIDTH = 40
GASHEIGHT = 40
GASIMG = pygame.image.load('game/image/gas-station.png')
GASIMG = pygame.transform.scale(GASIMG, (GASWIDTH, GASHEIGHT))
TANKWIDTH = 40
TANKHEIGHT = 400
TANKIMG = pygame.image.load('game/image/rectangle.png')
TANKIMG = pygame.transform.scale(TANKIMG, (TANKWIDTH, TANKHEIGHT))
CONSUMELIMIT = 1000
CONSUMEWIDTH = 35
CONSUMEHEIGHT = 217 * CONSUMELIMIT/1000
CONSIMG = pygame.image.load('game/image/Red.png')
CONSIMG = pygame.transform.scale(CONSIMG, (CONSUMEWIDTH, CONSUMEHEIGHT))

class Gas():
    def __init__(self, display_surf):
        self.display_surf = display_surf
        self.gasX = 10
        self.gasY = 50
        self.gas_limit = CONSUMELIMIT
    
    def draw(self):
        self.display_surf.blit(GASIMG, (self.gasX, self.gasY))
        self.display_surf.blit(TANKIMG, (self.gasX, self.gasY - 13))
        self.display_surf.blit(CONSIMG, (self.gasX + 3, self.gasY + 80))
    
    def pump_brake(self, brake):
        if brake == True:
            global CONSUMELIMIT, CONSUMEHEIGHT, CONSUMEWIDTH, CONSIMG
            CONSUMELIMIT -= 2
            CONSUMEHEIGHT = 217 * CONSUMELIMIT/1000
            CONSIMG = pygame.image.load('game/image/Red.png')
            CONSIMG = pygame.transform.scale(CONSIMG, (CONSUMEWIDTH, CONSUMEHEIGHT))
