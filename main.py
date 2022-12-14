import pygame
import math
from vector import Vector
import time
BLACK = (0,0,0)
pygame.init()
GRAVITY = 1

#finds size of computer display and creates pygame window
infoObject = pygame.display.Info()
width = int(infoObject.current_w)
height = int((infoObject.current_h - 60))
DISPLAY = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Grapling hook sim')

click = False
position = Vector(100,100)  #location of the player
velocity = Vector(0,0)      #velocity of the player
acceleration = Vector(0,0)#acceleration of the player
gravity = Vector(0,1)       #gravity accel
hook = Vector(0,0)          #location that had been hooked
points = [position.get()]
radius = 0
while True:
    points.append(position.get())
    if len(points) >= 100:
        points.pop(0)
    acceleration = Vector(0,0)
    time.sleep(0.01)
    #allows user to quit if program is taking to long
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        #allowing mouse interfacing
        if event.type == pygame.MOUSEBUTTONUP:
            click = False
            radius = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
            hook.set(pygame.mouse.get_pos())

    #calculating the acceleration of the player
    acceleration += gravity
    if click:
        hookUnit = ((hook-position).unit())#direction to the hook point
        hookPerp = Vector(1,-hookUnit.get()[0]/hookUnit.get()[1])
        angularVel = velocity.projectedOnto(hookPerp)
        centripital =  hookUnit * (((angularVel.mag())**2)/((hook-position).mag()))
        if velocity.angle(centripital) >=(math.pi/2):
            acceleration += centripital#adds centripital force if neccisarry
        if gravity.angle(centripital) >=(math.pi/2):
            acceleration -= gravity.projectedOnto(centripital)#adds normal force if neccisary
    position += (velocity * 0.5) + (0.5*0.5 *0.5* acceleration)
    velocity += (acceleration * 0.5)
    #makes display
    DISPLAY.fill(BLACK)
    pygame.draw.rect(DISPLAY,(255,100,20),(position.get()[0] -10,position.get()[1] -10,20,20))
    pygame.draw.lines(DISPLAY, (0,200,200), False, points)
    if click:
        pygame.draw.line(DISPLAY,(255,255,255), position.get(), hook.get())
    pygame.display.update()