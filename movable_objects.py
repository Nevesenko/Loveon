import pygame as pg
import pygame.time
import pymunk
from enum import Enum
import asyncio
import pandas as pd
import animation




class Gender(Enum):
    M = 1
    W = 2

class Lover():
    def __init__(self, gender: Gender, space, surface):
        #pg.Surface.__init__(self, (80,80))
        def choose_by_gender( g: Gender) -> object:
            if g == Gender.M:
                path = 'Images/lollipop.png'
                SIZE = (80, 120)
            elif g == Gender.W:
                path = 'Images/donut.png'
                SIZE = (85, 85)
            #image = pg.image.load(path)
            #pg.transform.scale(image,(image.get_width()/10, image.get_height()/10))
            return path
        self.img = pg.image.load(choose_by_gender(gender))
        self.img = pg.transform.scale(self.img, (self.img.get_width()/10, self.img.get_height()/10))
        #self.img = choose_by_gender(gender)
        self.delta = 2
        self.rect = self.img.get_rect()

        if gender == Gender.M:
            self.pos = [600,100]
            self.delta = -self.delta
        else:
            self.pos = [100,100]
        surface.blit(self.img, (self.pos))
        #self.blit(self.img, (0,0))
    def change_pos(self, surface):
        self.pos[0] = self.pos[0]+self.delta
        surface.blit(self.img, self.pos)


def check_distance(x1: Lover, x2: Lover):
    distance = abs(x1.pos[0] - x2.pos[0])
    print(distance)
    if distance < 4:
       return pygame.time.set_timer(pygame.USEREVENT, 2, 0)


