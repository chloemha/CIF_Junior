#green and pink boxes moving

import pygame

pygame.init() #initilaize game

#colours
green=(0, 255, 0)
pink=(255, 192, 203)
black=(0, 0, 0)

#width and height of the screen
width=800
height=600

#starting coordinates of the green box
box_x=0
box_y=300
rectl=pygame.Rect(box_x, box_y, 30, 30)

#starting coordinates of pink box
box2_x=800
box2_y=400
rectll=pygame.Rect(box2_x, box2_y, 30, 30)

#create screen
screen=pygame.display.set_mode((width, height))

clock=pygame.time.Clock() #setup frame rate

while True: #loop of updating images
    clock.tick(30) #run at 30FPS
    for event in pygame.event.get(): #exit when window is closed
        if event.type==pygame.QUIT:
            exit()

    #make the green box move to the right
    box_x+=5
    rectl=pygame.Rect(box_x, box_y, 30, 30)
    pygame.draw.rect(screen, green, rectl) 

    #make the pink box move to the left
    box2_x-=5
    rectll=pygame.Rect(box2_x, box2_y, 30, 30)
    pygame.draw.rect(screen, pink, rectll)

    #update screen and erase prior instances
    pygame.display.update()
    screen.fill(black)