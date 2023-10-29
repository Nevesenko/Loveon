import pygame as pg
import pymunk
from enum import Enum
import asyncio




class Gender(Enum):
    M = 1
    W = 2

class Lover:
    def _add_image(self, g :Gender) -> object:
        if g == Gender.M:
            path = 'Images/lollypop.png'
            SIZE = (80,120)
        elif g == Gender.W:
            path = 'Images/donut.png'
            SIZE = (85,85)
        else:
            return ValueError
        self.image = pg.image.load(path)

        return pg.transform.scale(self.image,SIZE)
    def __init__(self, gender: Gender, space, surface):
        self.obj = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.delta = 0.5
        if gender == Gender.M:
            self.pos = [600,100]
            self.delta = -self.delta
        else:
            self.pos = [100,100]
        self.pic = self._add_image(gender)
        space.add(self.obj)
        surface.blit(self.pic, (self.pos))

    def change_pos(self, surface):
        self.pos[0] += self.delta
        self.obj.position = self.pos
        surface.blit(self.pic, (self.pos))

def check_distance(x1: Lover, x2: Lover):
    distance = abs(x1.obj.position[0] - x2.obj.position[0])
    print(distance)
    if distance < 4:
        pass