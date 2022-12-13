import pygame
import math
from vector import Vector
import time
BLACK = (0,0,0)
color = (255,255,255)
pygame.init()
GRAVITY = 1

#finds size of computer display and creates pygame window
infoObject = pygame.display.Info()
width = int(infoObject.current_w)
height = int((infoObject.current_h - 60))
DISPLAY = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Grapling hook sim')

click = False
position = Vector(100,100)#location of the player
velocity = Vector(2,0)    #velocity of the player
acceleration = Vector(0,1)#acceleration of the player
gravity = Vector(0,1)     #gravity accel
hook = Vector(0,0)        #location that had been hooked
points = []

while True:
    time.sleep(0.1)
    #allows user to quit if program is taking to long
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        #allowing mouse interfacing
        if event.type == pygame.MOUSEBUTTONUP:
            click = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
            hook = hook.set(pygame.mouse.get_pos())

    #calculating the acceleration of the player
    acceleration += gravity
    if click:
        acceleration += ((hook-position).unit()) * (velocity.mag()^2/(hook-position).mag())
        

    #makes display
    DISPLAY.fill(BLACK)
    pygame.draw.rect(DISPLAY,color,(position.get()[0] -10,position.get()[1] -10,20,20))
    #pygame.draw.lines(DISPLAY, (0,0,255), False, points)
    if click:
        pygame.draw.line(DISPLAY,color, position.get(), hook.get())
    pygame.display.update()