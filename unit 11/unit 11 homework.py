import pygame

pygame.init()
pygame.font.init()

#colours
green=(0,255,0)
blue=(0,0,255)
pink=(255, 105, 180)
black=(0,0,0)
white=(255,255,255)

#screen measurements
width=800
height=600
screen=pygame.display.set_mode((width, height))

#boxes' coordinates
green_box_x=400
green_box_y=300
pink_box_x=0
pink_box_y=0

#boxes' measurements
green_box_width=30
green_box_height=30
pink_box_width=30
pink_box_height=30

#framerate
clock=pygame.time.Clock()
speed=10

pink_box_x_change=0
pink_box_y_change=0

#loop of updating images
while True:
    clock.tick(30) #run at 30FPS 

    screen.fill(black) #erase the screen

    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            exit()

        #direction depending on which keys are pressed
        elif event.type == pygame. KEYDOWN:
            if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                pink_box_x_change-=speed
            if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                pink_box_x_change+=speed
            if event.key == pygame.K_UP or event.key==pygame.K_w:
                pink_box_y_change-=speed
            if event.key == pygame. K_DOWN or event.key==pygame.K_s:
                pink_box_y_change+=speed

        elif event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                pink_box_x_change=0
            if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                pink_box_x_change=0
            if event.key == pygame.K_UP or event.key==pygame.K_w:
                pink_box_y_change=0
            if event.key == pygame. K_DOWN or event.key==pygame.K_s:
                pink_box_y_change=0
        
    pink_box_x+=pink_box_x_change
    pink_box_y+=pink_box_y_change

    #border protection
    if pink_box_x<0: #means box is left outside screen
        pink_box_x=0
    if pink_box_y<0: #means box is right outside screen
        pink_box_y=0
    if pink_box_x>width-pink_box_width: #means box is top outside screen
        pink_box_x=width-pink_box_width
    if pink_box_y>height-pink_box_height: #means box is bottom outside screen
        pink_box_y=height-pink_box_height

    #drawing rectangle 
    pink_rectl=pygame.Rect(pink_box_x, pink_box_y, pink_box_width, pink_box_height)
    green_rectl=pygame.Rect(green_box_x,green_box_y,green_box_width,green_box_height)
    pygame.draw.rect(screen, pink, pink_rectl)
    pygame.draw.rect(screen, green, green_rectl)

    #collision detection
    if pink_rectl.colliderect(green_rectl):
        myfont=pygame.font.SysFont("Times New Roman", 30)
        font=myfont.render("Overlapped", False, white)
        screen.blit(font, (350,250))
        green=blue

    #updating the screen
    pygame.display.update()