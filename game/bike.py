class Bike():
    def __init__(self, BIKEWIDTH, BIKEHEIGHT, DISPLAYSURF , BIKEIMG, BIKESPEED, bike_x, bike_y):
        self.width = BIKEWIDTH
        self.height = BIKEHEIGHT
        self.displaysurf = DISPLAYSURF
        self.img = BIKEIMG
        self.speed = BIKESPEED
        self.x = bike_x
        self.y = bike_y
        self.X_MARGIN = 80
        self.WINDOWWIDTH = 400
        self.WINDOWHEIGHT = 620
    
    def draw(self):
        self.displaysurf.blit(self.img, (self.x, self.y))
    
    def update(self, moveLeft, moveRight):
        if moveLeft == True:
            self.x -= self.speed
        if moveRight == True:
            self.x += self.speed        
        if self.x < self.X_MARGIN:
            self.x = self.X_MARGIN
        if self.x + self.width > self.WINDOWWIDTH - self.X_MARGIN:
            self.x = self.WINDOWWIDTH - self.X_MARGIN - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height > self.WINDOWHEIGHT :
            self.y = self.WINDOWHEIGHT - self.height       
