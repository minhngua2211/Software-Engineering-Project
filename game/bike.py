import pygame

BIKEWIDTH = 50
BIKEHEIGHT = 90
BIKESPEED = 5
WINDOWWIDTH = 400
WINDOWHEIGHT = 620
X_MARGIN = 80
BIKEIMG = pygame.image.load('game/image/motorcycle.png')
BIKEIMG = pygame.transform.scale(BIKEIMG, (BIKEWIDTH, BIKEHEIGHT))

class Bike():
    def __init__(self, display_surf):
        self.display_surf = display_surf
        self.width = BIKEWIDTH
        self.height = BIKEHEIGHT
        self.x = (WINDOWWIDTH - self.width) / 2
        self.y = (WINDOWHEIGHT - self.height) / 0.25
        self.speed = BIKESPEED
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
    
    def draw(self):
        self.display_surf.blit(BIKEIMG, (int(self.x), int(self.y)))
    
    def update(self, moveLeft, moveRight):
        if moveLeft == True:
            self.x -= self.speed
        if moveRight == True:
            self.x += self.speed        
        if self.x < X_MARGIN:
            self.x = X_MARGIN
        if self.x + self.width > WINDOWWIDTH - X_MARGIN:
            self.x = WINDOWWIDTH - X_MARGIN - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height > WINDOWHEIGHT :
            self.y = WINDOWHEIGHT - self.height
