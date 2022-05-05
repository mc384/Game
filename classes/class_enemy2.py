from turtle import speed
import pygame
import random
import math
import sys
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((1920,1080))
class enemy2(object):
    walkright = [pygame.image.load('skel2.png'), pygame.image.load('skel4.png'), pygame.image.load('skel2.png'), pygame.image.load('skel4.png'), pygame.image.load('skel2.png'), pygame.image.load('skel4.png'), pygame.image.load('skel2.png'), pygame.image.load('skel4.png'), pygame.image.load('skel2.png'), pygame.image.load('skel4.png'), pygame.image.load('skel2.png')]
    walkleft = [pygame.image.load('skel1.png'), pygame.image.load('skel3.png'), pygame.image.load('skel1.png'), pygame.image.load('skel3.png'), pygame.image.load('skel1.png'), pygame.image.load('skel3.png'), pygame.image.load('skel1.png'), pygame.image.load('skel3.png'), pygame.image.load('skel1.png'), pygame.image.load('skel3.png'), pygame.image.load('skel1.png')]

    def __init__(self, x, y, length, height, start, stop):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.patrol = [start, stop]
        self.walkcount = 0
        self.speed = 3
        self.hitbox = (self.x, self.y, 28, 60)
        self.health = 10
        self.visible = True
        self.aggro = False 

    def draw(self, win):
        self.move() 
        if self.visible:
            if self.walkcount + 1 >= 33:
                self.walkcount = 0
        
            if self.speed > 0:
                win.blit(self.walkright[self.walkcount//3], (self.x,self.y))
                self.walkcount += 1
            else:
                win.blit(self.walkleft[self.walkcount//3], (self.x,self.y))
                self.walkcount += 1
            self.hitbox = (self.x, self.y, 31, 57)

    def hit(self):
        if self.health > 0:
            self.health -= 2
        else:
            self.visible = False

    def move(self):
        if self.speed > 0: #moving down
            if self.y < self.patrol[1] + self.speed: # check if its moving past the point we wanna stop at
                self.y += self.speed
            else:
                self.speed = self.speed * -1 # moving in the opposite direction
                self.y += self.speed
                self.walktimer = 0
        else: # 
            if self.y > self.patrol[0] - self.speed:
                self.y += self.speed
            else:
                self.speed = self.speed * -1
                self.y += self.speed
                self.walktimer = 0

    def chase(self):
        if self.aggro == True:
            self.x += 1.1*self.vel