import pygame


def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


class Player():
    def __init__(self, x, y, width, heigth, image):
        self.image = image
        # self.image = [pygame.image.load('sprite/cat.png'), pygame.image.load('sprite/walk1.png'), pygame.image.load('sprite/walk2.png')]
        self.hit_box = pygame.Rect(x, y, 25, heigth)
        self.vel = 5
        self.move_flag = [0, 0]
        self.left = False
        self.right = True
        self.jump = False
        self.down = False
        self.feet = pygame.Rect(x, y, 25, 2)

    def move(self, display, colision_rects, platform_rects, shift):
        # self.hit_box, collisions = move(self.hit_box, self.move_flag, colision_rects)
        # player_rect,  collisions = move(player_rect,  player_movement, tile_rects)
        # def move(rect,movement,tiles):

        #collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}

        self.move_flag[1] += 0.2 * 1  # 3 is the gravity
        if self.move_flag[1] > 10:
            self.move_flag[1] = 10

        self.hit_box.y += self.move_flag[1]

        self.hit_box.x -= shift[0]
        self.hit_box.y -= shift[1]

        if self.move_flag[1] > 0:   # this two lines turning off jump when you walk off from the tile
            self.jump = True

        hit_list = collision_test(self.hit_box, colision_rects)

        for tile in hit_list:
            if self.move_flag[1] > 0:
                self.hit_box.bottom = tile.top
                #collision_types['bottom'] = True
                self.move_flag[1] = 0
                self.jump = False
            elif self.move_flag[1] < 0:
                self.hit_box.top = tile.bottom
                #collision_types['top'] = True
                self.move_flag[1] = 0

        self.hit_box.x += self.move_flag[0]

        self.feet.x = self.hit_box.x
        self.feet.y = self.hit_box.y + self.hit_box.height - 2

        hit_list = collision_test(self.hit_box, colision_rects)
        for tile in hit_list:
            if self.move_flag[0] > 0:
                self.hit_box.right = tile.left
                #collision_types['right'] = True
            elif self.move_flag[0] < 0:
                self.hit_box.left = tile.right
                #collision_types['left'] = True


        platform_list = collision_test(self.feet, platform_rects)
        for tile in platform_list:
            if self.move_flag[1] > 0:
                self.hit_box.bottom = tile.top
                # collision_types['bottom'] = True
                self.move_flag[1] = 0
                self.jump = False
            elif self.down:
                self.hit_box.bottom += 10
                print(self.down)
        self.down = False








        # return rect, collision_types

        if self.left:
            display.blit(
                pygame.transform.scale(pygame.transform.flip(self.image, True, False), (50, 80)), (self.hit_box.x-5, self.hit_box.y))
        if self.right:
            display.blit(pygame.transform.scale(self.image, (50, 80)), (self.hit_box.x-19, self.hit_box.y))
        pygame.draw.rect(display, (255, 0, 0), self.hit_box, 2)  # Show player rectangle hit box
        #self.feet.y = self.hit_box.y + 78
        pygame.draw.rect(display, (0, 0, 250), self.feet, 2)  # Show player rectangle hit box

        self.move_flag[0] = 0
        self.hit_box.x += shift[0]
        self.hit_box.y += shift[1]