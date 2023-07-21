import pygame

class Score():
    def __init__(self, displaysurf):
        self.displaysurf = displaysurf
        self.score = 0 

    def draw(self):
        font = pygame.font.SysFont('consolas', 30)
        scoreSuface = font.render('Score: '+str(int(self.score)), True, (0, 0, 0))
        self.displaysurf.blit(scoreSuface, (10, 10))

    def update(self, BGSPEED):
        self.score += 2*BGSPEED/300
        
    def get_score(self):
        return self.score