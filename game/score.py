import pygame

class Score():
    def __init__(self, display_surf):
        self.display_surf = display_surf
        self.score = 0
    
    def draw(self):
        font = pygame.font.SysFont('consolas', 30)
        scoreSuface = font.render('Score: '+str(int(self.score)), True, (0, 0, 0))
        self.display_surf.blit(scoreSuface, (10, 10))
    
    def update(self):
        self.score += 0.02
