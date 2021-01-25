class Settings(object):

    def __init__(self):
        self.height= 600
        self.width = 1200
        self.bgcolor = (0,0,230)
        self.bullet_width = 5
        self.bcolor = (60,60,60)
        self.bullet_height = 20
        self.bulletlimit = 3
        self.ship_limit = 3
        self.speedupscale = 1.1
        self.alien_points = 5
        self.dynamic_setttings()
        self.scorescale = 1.5

    def dynamic_setttings(self):
        self.speed = 2
        self.alienspeed = 1
        self.fleetdropspeed = 10
        self.fleetdirection = 1
        self.bspeed = 4

    def increase_speed(self):
        self.speed *= self.speedupscale
        self.alienspeed *= self.speedupscale
        self.bspeed *= self.speedupscale
        self.alien_points = int(self.alien_points * self.scorescale)


