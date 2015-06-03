import pygame, math, sys, random
from pygame.locals import *


class Ball(pygame.sprite.Sprite):
    selected = []
    img = [pygame.image.load('blue_dot.png'),pygame.image.load('blue_dot_sel.png'),
           pygame.image.load('red_dot.png')]

    ## Contains the base information of the instance
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = Ball.img[0]
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        Unitorg.units.append(self)
        self.target = None
        self.pos = (self.rect[0],self.rect[1])

    ##used each frame to update the state of the instance
    def update(self):

        #if a target has been set, move towards it and stop when reached
        if  self.target != None:
            steps_number = max( abs(self.target[0]-self.rect[0]), abs(self.target[1]-self.rect[1]) )
            stepx = float(self.target[0]-self.rect[0])/steps_number
            stepy = float(self.target[1]-self.rect[1])/steps_number
            self.rect.move_ip(int(stepx), int(stepy))
            if self.rect[0] == self.target[0] and self.rect[1] == self.target[1]:
                self.target = None

            
                
            
        

    def calcnewpos(self,target):
        i = 0
        steps_number = max( abs(target[0]-self.rect[0]), abs(target[1]-self.rect[1]) )
        stepx = float(target[0]-self.rect[0])/steps_number
        stepy = float(target[1]-self.rect[1])/steps_number
        self.rect.move(int(self.rect[1] + stepx*i), int(self.rect[1] + stepy*i))
        i += 1

    ## marks a unit as selected if clicked on, and deselects it if you click elsewhere
    def selection(self):
        if self.rect.collidepoint((pygame.mouse.get_pos())):
            if not self in Ball.selected:
                Ball.selected.append(self)
                self.image = Ball.img[1]
                print(Ball.selected)
            

        elif not self.rect.collidepoint((pygame.mouse.get_pos())):
            if self in Ball.selected:
                Ball.selected.remove(self)
                self.image = Ball.img[0]
                print(Ball.selected)


##Class to keep track of units created
class Unitorg(object):

    units = []
    

