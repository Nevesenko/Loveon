import pygame as pg
import os
import display
class Meeting(pg.sprite.Sprite):
    def __init__(self, directory):
        pg.sprite.Sprite.__init__(self)
        length = len([file for file in os.listdir(directory) if os.path.isfile(str(directory+file))])
        self.shots = []
        self.count = 0
        for i in range(1, length, 2):
            filename = f'{directory}/shot_{i}'
            img = pg.image.load(filename)
            self.shots.append(img)

    def rescale(self, k = 1.2 ):
        for item in self.shots:
            pg.transform.scale(item, (80*k,110*k))

    def update(self, coordinates):
        for item in self.shots:
            display.surface.blit(item)
        Meeting.kill()

##############################

import pygame as pg
import os


class Animation():
    def __init__(self, param):
        self.collect = []
        path = str() #спросить у Дани
        match param:
            case 'blow':
                path = 'C:/Users/Lenovo/Downloads/Спрайты/Анимация Для пончика и леденца/'
            case 'another':
                pass

        for file in os.listdir(path):
            image = pg.image.load(path + file)
            self.collect.append(image)
    def transform(self ):
        for item in self.collect:
            item = pg.transform.scale(item, (80,80))
        self.gen = (display.surface.blit(i) for i in self.collect)
    def generate_blow(self):
        yield self.gen




