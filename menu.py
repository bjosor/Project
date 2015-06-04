import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1600, 800))
screen.fill((255,255,255))

background = pygame.Surface(screen.get_size())
background.fill((255,255,255))

playbutton = pygame.Surface((100,50))

playbutton.fill((0,255,0))


menu = True
while menu:
    
    for event in pygame.event.get():
        ##print(event)
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu = False
                pygame.quit()
                sys.exit()
                
    background.blit(screen,(0,0))
    playbutton.blit(screen, (400,300))
    
    pygame.display.flip()