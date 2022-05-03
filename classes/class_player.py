from turtle import speed
import pygame
import random
import math
import sys
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((1920,1080))

moveStill = [pygame.image.load('tile002.png')]
moveRight = [pygame.image.load('tile067.png'), pygame.image.load('tile071.png'), pygame.image.load('tile067.png'), pygame.image.load('tile071.png'), pygame.image.load('tile067.png'), pygame.image.load('tile071.png'), pygame.image.load('tile067.png'), pygame.image.load('tile071.png'), pygame.image.load('tile067.png')]
moveLeft = [pygame.image.load('tile077.png'), pygame.image.load('tile081.png'), pygame.image.load('tile077.png'), pygame.image.load('tile081.png'), pygame.image.load('tile077.png'), pygame.image.load('tile081.png'), pygame.image.load('tile077.png'), pygame.image.load('tile081.png'), pygame.image.load('tile077.png')]

class player(object):
    def __init__(self, x, y, length, height, health, damage):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.health = health
        self.speed = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.standing = False
        self.Timer = 0
        self.hitbox = (self.x + 20, self.y, self.length, self.height)
        self.damage = damage

    def draw(self, win):

        if self.Timer + 1 >= 36:
            self.Timer = 0
        
        if self.standing == False:
            if self.left:  
                window.blit(moveLeft[self.Timer//4], (self.x,self.y))
                self.Timer += 1                          
            elif self.right:
                window.blit(moveRight[self.Timer//4], (self.x,self.y))
                self.Timer += 1
            
        else:
            window.blit(moveStill[0], (self.x, self.y))
        self.hitbox = (self.x + 20, self.y + 10, 29, 52)

    def hit(self):
        self.walkCount = 0
        font1 = pygame.font.SysFont('arial', 100)
        pygame.display.update()


    def death(self):
        self.x = 400
        self.y = 410
        self.walkCount = 0
        font2 = pygame.font.SysFont('arial', 100)
        text2 = font2.render('Vanquished...', 1, (255,0,0))
        window.blit(text2, (900, 500))
        pygame.display.update()
        i = 0
        while i < 400:
            pygame.time.delay(10)
            i += 1
        if i == 400:
            pygame.quit()
            sys.exit()
