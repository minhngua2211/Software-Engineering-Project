import pygame

class Level():
    def __init__(self, displaysurf):
        self.displaysurf = displaysurf
        self.level = 0
        self.last_level = 0
        self.ls = [32,61]
    def draw(self):
        font = pygame.font.SysFont('consolas', 30)
        scoreSuface = font.render('Level: '+str(int(self.level)), True, (0, 0, 0))
        self.displaysurf.blit(scoreSuface, (250, 10))
    
    def update(self, score):
        if score > self.ls[0]:
            self.level += 1
            self.ls.pop(0)
            self.ls.append(self.ls[0] + 29)
    