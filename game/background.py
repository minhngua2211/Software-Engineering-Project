import pygame

BGSPEED = 3
BGIMG = pygame.image.load('game/image/background.png')

class Background():
    def __init__(self, display_surf):
        self.display_surf = display_surf
        self.x = 0
        self.y = 0
        self.speed = BGSPEED
        self.img = BGIMG
        self.width = self.img.get_width()
        self.height = self.img.get_height()
    
    def draw(self):
        self.display_surf.blit(self.img, (int(self.x), int(self.y)))
        self.display_surf.blit(self.img, (int(self.x), int(self.y - self.height)))
    
    def update(self):
        self.y += self.speed
        if self.y > self.height:
            self.y -= self.height
    
    def pump_brake(self, brake):
        if brake == True:
            self.speed = BGSPEED * 0.5
        if brake == False:
            self.speed = BGSPEED
