import pygame
import math
import time
BLACK = (0,0,0)
color = (255,255,255)
pygame.init()

#finds size of computer display and creates pygame window
infoObject = pygame.display.Info()
width = int(infoObject.current_w)
height = int((infoObject.current_h - 60))
DISPLAY = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Grapling hook sim')


position = [100,100]
velocity = [0,0]
anchor = [0,0]
points = [(100,100)]
click = False
rclick = False
while True:
    time.sleep(0.001)
    #allows user to quit if program is taking to long
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        #allowing mouse interfacing
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                rclick = False
            else:
                click= False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                rclick= True
            else:
                click= True
                (x,y) = pygame.mouse.get_pos()
                anchor = [x,y]
                Maxlength = math.dist(anchor,position)
                length= [anchor[0] - position[0],anchor[1] - position[1]]
                angle = math.atan2(length[1],length[0])
                vangle = math.atan2(velocity[1],velocity[0])
                vangle -= angle
                if vangle >= 2*math.pi:
                    vangle -= 2*math.pi
                if vangle <= 0:
                    vangle += 2*math.pi
                if math.cos(vangle) <=0:
                    vtotal= math.sqrt(velocity[1]**2 + velocity[0]**2) *math.sin(vangle)
                    vangle = angle + math.pi/2
                    velocity = [vtotal * math.cos(vangle),vtotal * math.sin(vangle)]
                
    forces = []

    #adds gravity force
    forces.append([0,0])

    #adds centripital force
    if click:
        dif = math.dist(anchor,position) - Maxlength
        if dif >= 0:
            length= [anchor[0] - position[0],anchor[1] - position[1]]
            angle = math.atan2(length[1],length[0])
            forces.append([dif*math.cos(angle),dif*math.sin(angle)])

    #adds reel force
    if rclick and click:
        Maxlength = math.dist(anchor,position)
        length= [anchor[0] - position[0],anchor[1] - position[1]]
        angle = math.atan2(length[1],length[0])
        forces.append([2*math.cos(angle),2*math.sin(angle)])

    #updates velocity and position
    totalForce = [0,0]
    for i in forces:
        totalForce[0] += i[0]
        totalForce[1] += i[1]
    if math.sqrt((totalForce[0]* totalForce[0])+(totalForce[1]* totalForce[1]) ) >= 10:
        color = (255,0,0)
        if math.sqrt((totalForce[0]* totalForce[0])+(totalForce[1]* totalForce[1]) ) >= 40:
            click= False
    else:
        color = (255,255,255)

    velocity[0] += totalForce[0]
    velocity[1] += totalForce[1]

    #drag
    velocity[0] -= velocity[0]/10000
    velocity[1] -= velocity[1]/10000

    position[0] += velocity[0]/1000
    position[1] += velocity[1]/1000

    points.append((position[0],position[1]))

    #makes display
    DISPLAY.fill(BLACK)
    pygame.draw.rect(DISPLAY,color,(position[0] -10,position[1] -10,20,20))
    pygame.draw.lines(DISPLAY, (0,0,255), False, points)
    if click:
        pygame.draw.line(DISPLAY,color, position, anchor)
    pygame.display.update()