import pygame, sys

pygame.init()



class maptile(pygame.sprite.Sprite):

    tileimg = [pygame.image.load("watertile.png"),pygame.image.load("grasstile.png")]

    def __init__(self, tileID, posx, posy)
        pygame.sprite.Sprite.__init__(self)
        self.image = tileimg[tileID]
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
