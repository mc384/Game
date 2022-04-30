import pygame
import random
import math
pygame.init()
pygame.font.init()

chestclosed = pygame.image.load('chest2.png')
chestopened = pygame.image.load('chest4.png')

class chest(object):
    def __init__(self, x, y, width, height, state):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.state = state

    def draw(self, win):
        if self.state == 'closed':
            win.blit(chestclosed, (self.x, self.y))

    def open(self, win):
        if True:
            win.blit(chestopened, (self.x, self.y))