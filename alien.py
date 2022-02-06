from msilib.schema import SelfReg
from os import truncate
from shutil import register_unpack_format
import pygame
class Alien:

    def __init__(self,x,y,screen):
        self.image=pygame.image.load("Ship3.png")
        self.image=pygame.transform.scale(self.image,(150,75))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.screen=screen
        self.speed=2

    def moveme(self,DIR):
        self.rect.x+=DIR*self.speed

    def killme(self,bullet):
        if pygame.Rect.colliderect(self.rect,bullet.rect):
            return True
    def check(self,DIR):
        touched=False
        if self.rect.right>self.screen.get_rect().right:
            self.rect.right=self.screen.get_rect().right
            DIR=-1 
            touched=True
        if self.rect.left<0:
            self.rect.left=0
            DIR=1
            touched=True
        return [DIR,touched]
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def lose (self,player):
        if self.rect.bottom>=self.screen.get_rect().bottom:
            return True

