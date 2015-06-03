import pygame, math, sys, random, classes
from pygame.locals import *


# Initialise screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption('Basic Pygame program')

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

# Blit everything to the screen
screen.blit(background, (0, 0))
pygame.display.flip()

##sprite handling
sprites = pygame.sprite.Group()
ball = classes.Ball(50,50)
ball2 = classes.Ball(400,400)
sprites.add(ball,ball2)



mainloop = True
while mainloop:
    pygame.display.set_caption('fps:%f'%clock.get_fps())
    clock.tick(60)

    #event loop
    for event in pygame.event.get():
        ##print(event)
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop=False
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in classes.Unitorg.units:
                i.selection()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            for i in classes.Ball.selected:
                i.target = pygame.mouse.get_pos()
                print(ball.target)

    #updates units
    for u in classes.Unitorg.units:
        u.update()

    #updates the screen
    screen.blit(background,(0,0))
    sprites.draw(screen)
    pygame.display.flip()




##class config(object):
##    width = 800
##    height = 600
##    xtiles = 15
##    ytiles = 15
##    fps = 30
##    scrollstepx = 15
##    scrollstepy = 15
##    cornerpoint = [0,0]
##    zoomspeed = 0.01
##    zoom = 1.0
##    
##
##
##
###main game
##pygame.init()
##screen = pygame.display.set_mode((config.width,config.height))
##
###-----------------Loads-Map-Image---------------------
##themap = pygame.image.load("map_inspiration_rs.png").convert()
##
##
##mapdim = themap.get_size()
##themap_origin = themap.copy()
##background = pygame.Surface((screen.get_size()))
##backgroundrect = background.get_rect()
##background = themap.subsurface((config.cornerpoint[0],config.cornerpoint[1],
##                                config.width,config.height))
##background = background.convert()
##screen.blit(background,(0,0))
##clock = pygame.time.Clock()
##
## 
##
##allgroup = pygame.sprite.LayeredUpdates()
##
##BLACK = (0,0,0)
##WHITE = (255,255,255)
##
##
##
##
##pygame.display.update()
##
##mainloop=True
##while mainloop:
##    milliseconds = clock.tick(config.fps)  # milliseconds passed since last frame
##    seconds = milliseconds / 1000.0 # seconds passed since last frame
##
##    for event in pygame.event.get():
##        if event.type==pygame.QUIT:
##            pygame.quit()
##            sys.exit()
##        elif event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_ESCAPE:
##                mainloop=False
##                pygame.quit()
##                sys.exit()
##        if event.type == pygame.MOUSEBUTTONDOWN:
##            print (event.button)
##
##    if pygame.mouse.get_pressed()[0]:
##        Class.Unit(pygame.mouse.get_pos()) # create a new Bird at mousepos
##    
##    pygame.display.set_caption(" fps:"
##        "%.2f " % (clock.get_fps(),))
##    
##    trooporigin = [0,0]
##    scrollx = 0
##    scrolly = 0
##    pressedkeys = pygame.key.get_pressed()
##    mousepressed = pygame.mouse.get_pressed()
##    mousepos = pygame.mouse.get_pos()
##
##
##    # -----------SCROLLING------------------------
##        
##                 
##    # --- handle keys to scroll map ----
##    if pressedkeys[pygame.K_LEFT]:
##        scrollx -= config.scrollstepx
##    if pressedkeys[pygame.K_RIGHT]:
##        scrollx += config.scrollstepx
##    if pressedkeys[pygame.K_UP]:
##        scrolly -= config.scrollstepy
##    if pressedkeys[pygame.K_DOWN]:
##        scrolly += config.scrollstepy
##    # -------- scroll the visible part of the map ------
##    config.cornerpoint[0] += scrollx
##    config.cornerpoint[1] += scrolly
##
##    if config.cornerpoint[0] < 0:
##            config.cornerpoint[0] = 0
##            scrollx = 0
##    elif config.cornerpoint[0] > mapdim[0] - config.width:
##            config.cornerpoint[0] = mapdim[0] - config.width
##            scrollx = 0
##    if config.cornerpoint[1] < 0:
##            config.cornerpoint[1] = 0
##            scrolly = 0
##    elif config.cornerpoint[1] > mapdim[1] - config.height:
##            config.cornerpoint[1] = mapdim[1] - config.height
##            scrolly = 0
##
##    if scrollx == 0 and scrolly == 0:    # only necessery if there was no scrolling
##        allgroup.clear(screen, background)
##
##    else:
##        background = themap.subsurface((config.cornerpoint[0],
##                                            config.cornerpoint[1],
##                                            config.width,
##                                            config.height)) # take snapshot of bigmap
##
####--------------------ZOOM-----------(WIP)--------------------------------
####
####
####    # zoom with o and l key
####    zoomfactor = 1.0 # neither o nor l, no zooming
####    
####    if pressedkeys[pygame.K_o]:
####        zoomfactor += config.zoomspeed
####    if pressedkeys[pygame.K_l]:
####        zoomfactor -= config.zoomspeed
####    if config.zoom >= 1.2:
####        config.zoom = 1.2
####
####    if zoomfactor !=1.0:
####        config.zoom *= zoomfactor
####        print (config.zoom)
####        themap = pygame.transform.rotozoom(themap_origin,0,config.zoom).convert()
##             
##
##    screen.blit(background, (0,0))
##
##    pygame.display.flip()

