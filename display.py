import pygame
import pygame as pg
import pymunk.pygame_util

import animation
import movable_objects as mo
from movable_objects import Lover

if __name__ == '__main__':
    RES = WIDTH, HEIGHT = 800, 620
    FPS = 60
    pg.init()
    surface = pg.display.set_mode(RES)
    clock = pg.time.Clock()
    draw_options = pymunk.pygame_util.DrawOptions(surface)
    # настройки pymunk
    space = pymunk.Space()
    space.gravity = 0, 8000

    man = mo.Lover(mo.Gender.M, space, surface)
    woman = mo.Lover(mo.Gender.W, space, surface)

    meeting = animation.Meeting('Images/Anim_DonutAndLollipop')
    anim = animation.Animation('blow')
    while True:
        surface.fill(pg.Color('black'))
        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit()
            if i.type == pg.MOUSEBUTTONDOWN:
                if i.button == 1:
                    pass
            if i.type == pygame.USEREVENT:
                pass
        for char in (man, woman):
            char.change_pos(surface)
        #mo.check_distance(man, woman)
        pg.display.flip()
        clock.tick(FPS)