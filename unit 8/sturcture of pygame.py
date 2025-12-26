#structure of pygame

import pygame

pygame.init() #initilaize game

clock=pygame.time.Clock() #setup frame rate

while True: #loop of updating images
    clock.tick(30) #run at 30FPS
    for event in pygame.event.get(): #exit when window is closed
        if event.type==pygame.QUIT:
            exit()


#do stuff here (here is where you write your game)

pygame.display.update() #update the screen

screen.fill(black) #erase the screen

#always need two lines to draw a box
rectl=pygame.Rect(x,y,width,height)
pygame.draw.rect(screen, black, rectl) 

(x,y) #starting point of rectangle
(width, height) #width and height of the rectangle


#example of setting up a game
red=(255, 0, 0)
black=(0, 0, 0)
width=800
height=600
box_x=50
box_y=200
screen=pygame.display.set_mode((width, height))