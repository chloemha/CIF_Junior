#get the airplane to the destination game

import pygame

pygame.init() #initilaize game
pygame.font.init()

#colours
green=(0,255,0)
blue=(0,0,255)
pink=(255, 105, 180)
black=(0,0,0)
white=(255,255,255)
brown=(150,75,0)
red=(255,0,0)

#screen measurements
width=800
height=600
screen=pygame.display.set_mode((width, height))

#images
sky=pygame.image.load('blue_sky.jpg').convert()
airplane=pygame.image.load('airplane.png').convert()
airplane=pygame.transform.scale(airplane, (40, 40))
raindrop=pygame.image.load('raindrop.jpeg').convert()
raindrop=pygame.transform.scale(raindrop, (40, 40))

#airplane and raindrops' coordinates
airplane_x=0
airplane_y=600
raindrop_x=[100, 200, 300, 400, 500, 600, 700]
raindrop_y=[-60, -120, -180, -240, -180, -120, -60]
end_x=760
end_y=0

#airplane and raindrops' measurements
raindrop_width=40
raindrop_height=40
airplane_width=40
airplane_height=40
end_width=40
end_height=40

#framerate
clock=pygame.time.Clock()
speed=10
raindrops_speed=10

airplane_x_change=0
airplane_y_change=0

game_continue=True

#loop of updating images
while True:
    clock.tick(30) #run at 30FPS 

    screen.fill(black) #erase the screen

    screen.blit(sky, (0, 0))
    screen.blit(airplane, (airplane_x, airplane_y))

    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            exit()

        #direction depending on which keys are pressed
        if game_continue:
            if event.type == pygame. KEYDOWN:
                if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                    airplane_x_change-=speed
                if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                    airplane_x_change+=speed
                if event.key == pygame.K_UP or event.key==pygame.K_w:
                    airplane_y_change-=speed
                if event.key == pygame. K_DOWN or event.key==pygame.K_s:
                    airplane_y_change+=speed

            elif event.type==pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                    airplane_x_change=0
                if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                    airplane_x_change=0
                if event.key == pygame.K_UP or event.key==pygame.K_w:
                    airplane_y_change=0
                if event.key == pygame. K_DOWN or event.key==pygame.K_s:
                    airplane_y_change=0

    if game_continue:
        airplane_x+=airplane_x_change
        airplane_y+=airplane_y_change

    #border protection
    if airplane_x<0: #means box is left outside screen
        airplane_x=0
    if airplane_y<0: #means box is right outside screen
        airplane_y=0
    if airplane_x>width-airplane_width: #means box is top outside screen
        airplane_x=width-airplane_width
    if airplane_y>height-airplane_height: #means box is bottom outside screen
        airplane_y=height-airplane_height

    #drawing end point
    end_rectl=pygame.Rect(end_x, end_y, end_width, end_height)
    pygame.draw.rect(screen, red, end_rectl)
    airplane_rectl=pygame.Rect(airplane_x,airplane_y,airplane_width,airplane_height)

    #collision detection
    if airplane_rectl.colliderect(end_rectl):
        screen.blit(sky, (0, 0))
        screen.blit(airplane, (airplane_x, airplane_y))

        for i in range(len(raindrop_x)):
            screen.blit(raindrop, (raindrop_x[i], raindrop_y[i]))
        
        myfont=pygame.font.SysFont("Times New Roman", 80)
        font=myfont.render("You Win!", False, green)
        screen.blit(font, (250,250))

    #moving raindrops
    for i in range(len(raindrop_x)):
        raindrop_rectl=pygame.Rect(raindrop_x[i], raindrop_y[i], raindrop_width, raindrop_height)

        #if didn't lose yet
        if game_continue:
            raindrop_y[i]+=raindrops_speed
            if raindrop_y[i]>height:
                raindrop_y[i]= -raindrop_height

        #another collision detection
        if airplane_rectl.colliderect(raindrop_rectl):
            game_continue=False

        screen.blit(raindrop,(raindrop_x[i],raindrop_y[i]))

    if not game_continue:
        screen.blit(sky, (0, 0))
        screen.blit(airplane, (airplane_x, airplane_y))

        for i in range(len(raindrop_x)):
            screen.blit(raindrop, (raindrop_x[i], raindrop_y[i]))

        myfonts=pygame.font.SysFont("Times New Roman", 80)
        fonts=myfonts.render("You Lost!", False, red)
        screen.blit(fonts, (250, 250))
    
    pygame.display.update()
