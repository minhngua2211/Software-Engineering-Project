class Background():
    def __init__(self, displaysurf, BGSPEED, BGIMG, BG_X, BG_Y):
        self.displaysurf = displaysurf
        self.speed = BGSPEED
        self.img = BGIMG
        self.x = BG_X
        self.y = BG_Y
        self.height = self.img.get_height()
        self.width = self.img.get_width()
    def draw(self):
        self.displaysurf.blit(self.img, (int(self.x) , int(self.y)))
        self.displaysurf.blit(self.img, (int(self.x), int(self.y - self.height)))
    def update(self):
        self.y += self.speed
        if self.y > self.height:
            self.y -= self.height
    def pump_brake(self, brake, BGSPEED):
        if brake == True:
            self.speed = BGSPEED/2
        if brake == False:
            self.speed = BGSPEED
