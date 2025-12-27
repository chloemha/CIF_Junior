#controllable box

import pygame

pygame.init() #initilaize game

#colours
black=(0,0,0)
colour=(255,255,255) #white
pink=(255, 192, 203)

#starting coordinates of box
box_x=0
box_y=0

#box measurements
box_width=30
box_height=30

box_x_change=0
box_y_change=0

speed=10

#screen measurements
width=600
height=400
screen=pygame.display.set_mode((width, height))

clock=pygame.time.Clock() #setup frame rate

frame=0

#loop of updating images
while True:
    clock.tick(30) #run at 30FPS 
    
    frame+=1 #counting the number of frames passed

    screen.fill(black) #erase the screen

    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            exit()
    
        elif event.type == pygame. KEYDOWN:
            if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                box_x_change-=speed
            if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                box_x_change+=speed
            if event.key == pygame.K_UP or event.key==pygame.K_w:
                box_y_change-=speed
            if event.key == pygame. K_DOWN or event.key==pygame.K_s:
                box_y_change+=speed

        elif event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                box_x_change=0
            if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                box_x_change=0
            if event.key == pygame.K_UP or event.key==pygame.K_w:
                box_y_change=0
            if event.key == pygame. K_DOWN or event.key==pygame.K_s:
                box_y_change=0
        
    box_x+=box_x_change
    box_y+=box_y_change

    #border protection
    if box_x<0: #means box is left outside screen
        box_x=0
    elif box_y<0: #means box is right outside screen
        box_y=0
    elif box_x>width-box_width: #means box is top outside screen
        box_x=width-box_width
    elif box_y>height-box_height: #means box is bottom outside screen
        box_y=height-box_height

    #drawing rectangle 
    rectl=pygame.Rect(box_x, box_y, box_width, box_height)
    
    pygame.draw.rect(screen, colour, rectl) 

    if frame>=60:
        frame=0
        if colour ==(255, 255, 255):
            colour=pink
        else:
            colour=(255,255,255)

    pygame.display.update() #update the screen