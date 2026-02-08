class Player:
    def __init__ (self):
        self.energie = 3
        self.alive = True
    def blessure (self):
        self.energie = self.energie - 1
        if energie <= 0 :
            self.alive = False
    def soin (self):
        if energie > 0 :
           self.energie = self.energie + 1
    
    