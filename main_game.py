from turtle import speed
import pygame
import random
import math
pygame.init()
pygame.font.init()
from class_chest import chest
from class_player import player
from class_enemy import enemy
from class_enemy2 import enemy2
import sys

window = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Dungeon Slayer")

moveStill = [pygame.image.load('tile002.png')]
moveRight = [pygame.image.load('tile067.png'), pygame.image.load('tile071.png'), pygame.image.load('tile067.png'), pygame.image.load('tile071.png'), pygame.image.load('tile067.png'), pygame.image.load('tile071.png'), pygame.image.load('tile067.png'), pygame.image.load('tile071.png'), pygame.image.load('tile067.png')]
moveLeft = [pygame.image.load('tile077.png'), pygame.image.load('tile081.png'), pygame.image.load('tile077.png'), pygame.image.load('tile081.png'), pygame.image.load('tile077.png'), pygame.image.load('tile081.png'), pygame.image.load('tile077.png'), pygame.image.load('tile081.png'), pygame.image.load('tile077.png')]
attackRight = [pygame.image.load('tile043.png'), pygame.image.load('tile043.png'), pygame.image.load('tile043.png'), pygame.image.load('tile047.png'), pygame.image.load('tile047.png'), pygame.image.load('tile047.png'), pygame.image.load('tile051.png'), pygame.image.load('tile051.png'), pygame.image.load('tile051.png')]
attackLeft = [pygame.image.load('tile033.png'), pygame.image.load('tile033.png'), pygame.image.load('tile033.png'), pygame.image.load('tile041.png'), pygame.image.load('tile041.png'), pygame.image.load('tile041.png'), pygame.image.load('tile057.png'), pygame.image.load('tile057.png'), pygame.image.load('tile057.png')]

background = pygame.image.load('dungeon10.png')
background = pygame.transform.scale(background, (1920, 1080))
char = pygame.image.load('tile030.png')

chestclosed = pygame.image.load('chest2.png')
chestopened = pygame.image.load('chest4.png')

x = 500
y = 300
length = 40
height = 60
speed = 5

clock = pygame.time.Clock()

left = False
right = False

attacking = False

def visuals():
    window.blit(background, (0,0))
    text = font.render('HP: ' + str(hero.health), 1, (255, 0, 0))
    window.blit(text, (1500, 100))
    keybinds = font.render('Spacebar = Attack ', 1, (255, 0, 0))
    window.blit(keybinds, (1500, 130))
    keybinds2 = font.render('Arrow keys = Move ', 1, (255, 0, 0))
    window.blit(keybinds2, (1500, 160))
    goblin.draw(window) # Use win as the argument, not bg for enemy
    goblin2.draw(window)
    goblin3.draw(window)
    chest1.draw(background) 
    hero.draw(window)
    pygame.display.update() 


font = pygame.font.SysFont('arial', 30, True)

run = True
hero = player(300, 410, 64, 64, 250, 2)
goblin = enemy(250, 300, 64, 64, 250, 1000)
goblin2 = enemy(650, 700, 64, 64, 650, 1400)
goblin3 = enemy2(450, 200, 64, 64, 200, 800)
chest1 = chest(950,300, 64, 64, 'closed')
enemies = [goblin, goblin2, goblin3]

while run:
    clock.tick(36)

    for i in enemies:
        if abs(hero.x - i.x) < 10 and abs(hero.y - i.y) < 10 and i.visible == True:

            hero.hit()
            hero.health -= 5
    
        
    if hero.health <= 0:
        hero.death()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in enemies:
        if abs(hero.y - goblin.y) < 100:
            if goblin.x < hero.x:
                goblin.aggro = True
                goblin.chase()
                goblin.find_player(hero)
            else:
                goblin.aggro = True
                goblin.find_player(hero)

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_e] and abs(hero.x - chest1.x) < 50 and abs(hero.y - chest1.y) < 50:
        chest1.state = 'opened'
        hero.health += 20
        chest1.open(background)
        
    for i in enemies:
        if keys[pygame.K_SPACE]:
            if abs(hero.y - i.y) < 10 or abs(hero.x - i.x) < 10:
                i.hit()


    if keys[pygame.K_UP] and hero.y - hero.speed > 100:
        hero.y -= speed
        hero.up = True
        hero.down = False
        hero.standing = False

    if keys[pygame.K_DOWN] and hero.y + hero.speed + hero.height < 980:
        hero.y += speed
        hero.up = False
        hero.down = True
        hero.standing = False

    if keys[pygame.K_LEFT] and hero.x - hero.speed > 200: 
        hero.x -= speed
        hero.left = True
        hero.right = False
        hero.up = False
        hero.down = False
        hero.standing = False

    elif keys[pygame.K_RIGHT] and hero.x + speed + length < 1700:  
        hero.x += speed
        hero.left = False
        hero.right = True
        hero.up = False
        hero.down = False
        hero.standing = False
        
    else: 
        hero.standing = True
        hero.walkCount = 0
        
        
          
    visuals() 
    

pygame.quit()