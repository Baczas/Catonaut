import pygame, json
from random import randint

class World():

    def __init__(self):
        self.world_number = 1
        self.move_flag = [0,0]
        self.gravity = 1
        self.grass_img = pygame.image.load('sprite/grass.png')
        self.dirt_img = pygame.image.load('sprite/dirt.png')
        self.metal_floor_img = pygame.image.load('sprite/floor_metal.png')
        self.game_map = self.load_map(self.world_number)
        self.ts = 32  # Tile size
        self.counter = 0
        self.fire_img = [pygame.image.load('sprite/fire1.png').convert(),
                         pygame.image.load('sprite/fire2.png').convert(),
                         pygame.image.load('sprite/fire3.png').convert()]
        for l in range(len(self.fire_img)):
            self.fire_img[l].set_colorkey((255, 255, 255))


    def load_map(self, number):
        with open( 'maps/map_' + str(number) + '.json') as json_file:
            game_map = json.load(json_file)
            # width = len(blocks)
            # print(width)
            # height = len(blocks[0])
            # print(height)

        return game_map

    def draw(self, display, shift):
        colision_rects = []
        platform_rects = []
        #shift = [0,0]

        for x in range(len(self.game_map)):
            for y in range(len(self.game_map[0])):
                tile = self.game_map[x][y]
                if tile == 2:
                    pygame.draw.rect(display, (120, 250, 0), (x * self.ts - shift[0], y * self.ts - shift[1], self.ts, self.ts))
                    display.blit(self.dirt_img, (x * self.ts - shift[0], y * self.ts - shift[1]))
                if tile == 1:
                    pygame.draw.rect(display, (250, 0, 120), (x * self.ts - shift[0], y * self.ts - shift[1], self.ts, self.ts))
                    display.blit(self.grass_img, (x * self.ts - shift[0], y * self.ts - shift[1]))
                if tile != 0 and tile != 'X' and tile != 'F' and tile != 4:
                    if tile == 3:
                        colision_rects.append(pygame.Rect(x * self.ts - shift[0], y * self.ts - shift[1], self.ts, self.ts/2))
                    else:
                        colision_rects.append(pygame.Rect(x * self.ts - shift[0], y * self.ts - shift[1], self.ts, self.ts))

                if tile == 'W':
                    pygame.draw.rect(display, (120, 120, 120), (x * self.ts - shift[0], y * self.ts - shift[1], self.ts, self.ts))
                if tile == 3:
                    display.blit(self.metal_floor_img, (x * self.ts - shift[0], y * self.ts - shift[1]))
                if tile == 4:
                    pygame.draw.rect(display, (120,120,120),(x * self.ts - shift[0], y * self.ts - shift[1], self.ts, 5))
                    platform_rects.append(pygame.Rect(x * self.ts - shift[0], y * self.ts - shift[1], self.ts, 5))
                if tile == 'F':
                    self.fire_draw(display, x * self.ts - shift[0], y * self.ts - shift[1], shift)


        self.counter += 1
        return colision_rects, platform_rects

    def fire_draw(self, display, x, y, shift):

        fire_number = 0
        #world.fire_hit_box.append(pygame.Rect(x * world.ts, y * world.ts, world.ts, world.ts))
        #if self.counter % 10 == 0:
            #fire_number = randint(0, 3)
        display.blit(pygame.transform.scale(self.fire_img[fire_number], (self.ts, self.ts)), (x, y))
        #else: