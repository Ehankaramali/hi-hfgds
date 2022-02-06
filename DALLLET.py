import pygame

class BALLET:
    def __init__(self,x,y,screen):
        self.image=pygame.image.load("ball.png")
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.screen=screen
    def update_position(self):
        self.rect.y-=5
    def blit_me(self):
      self.screen.blit(self.image,self.rect)
