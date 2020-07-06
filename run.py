import pygame, sys
from map import World
from player import Player


clock = pygame.time.Clock()

pygame.init()   # Initiates pygame
pygame.display.set_caption('Catonaut')

WINDOW_SIZE = (700, 600)
display = pygame.display.set_mode(WINDOW_SIZE)
font = pygame.font.SysFont('comicsans', 35, True)

world = World()

# Character initialization, add also in drawGameWindow()

player_img = pygame.image.load('sprite/cat.png')

player = Player(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2, 50, 80, player_img)   # (x, y, width, height, image) of our character
true_shift = [0, 0]


def clicks():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.move_flag[0] += player.vel
        player.right = True
        player.left = False
    if keys[pygame.K_LEFT]:
        player.move_flag[0] -= player.vel
        player.right = False
        player.left = True

    if keys[pygame.K_UP] and player.jump == False:
        player.move_flag[1] -= 10
        player.jump = True
        # jump_sound.play()
    if keys[pygame.K_DOWN]:
        player.down = True

def exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def pause_menu():
    bar = [200, 50]  # buttons size
    h = 20  # spacing between buttons
    y_bar = 100  # move menu up and down
    center_bar = int(WINDOW_SIZE[0] / 2 - bar[0] / 2)  # width center (center of the button)
    color1 = (0, 0, 0)
    color2 = (0, 120, 120)
    pause = font.render('Pause', 1, (120,120,120))
    while True:

        display.blit(pause, (int(center_bar + (bar[0] - pause.get_width()) / 2),
                               int(y_bar + -1 * (bar[1] + h) + (bar[1] - pause.get_height()) / 2)))

        # NEW GAME
        # view the button
        clicked = create_bar('Return', 0, color1, color2, center_bar, y_bar, bar, h)

        # button function
        if pygame.mouse.get_pressed()[0] and clicked:
            break
            #game_screen()

        # SAVE GAME
        clicked = create_bar('Save Game', 1, color1, color2, center_bar, y_bar, bar, h)
        if pygame.mouse.get_pressed()[0] and clicked:
            pass

        # LOAD GAME
        clicked = create_bar('Load Game', 2, color1, color2, center_bar, y_bar, bar, h)
        if pygame.mouse.get_pressed()[0] and clicked:
            pass

        # SETTING
        clicked = create_bar('Settings', 3, color1, color2, center_bar, y_bar, bar, h)
        if pygame.mouse.get_pressed()[0] and clicked:
            pass

        # EXIT/QUIT
        clicked = create_bar('Save and quit', 4, color1, color2, center_bar, y_bar, bar, h)

        if pygame.mouse.get_pressed()[0] and clicked:
            print('saving does not work yet')
            pygame.quit()
            sys.exit()



        exit()

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            break

        pygame.display.update()
        clock.tick(60)

def main_menu():
    display.fill((120,120,120))
    bar = [200, 50] # buttons size
    h = 20  # spacing between buttons
    y_bar = 20  # move menu up and down
    center_bar = int(WINDOW_SIZE[0]/2 - bar[0]/2)   # width center (center of the button)
    color1 = (0, 0, 0)
    color2 = (0, 120, 120)

    # NEW GAME
    # view the button
    clicked = create_bar('New Game', 0, color1, color2, center_bar, y_bar, bar, h)

    # button function
    if pygame.mouse.get_pressed()[0] and clicked:
        game_screen()

    # LOAD GAME
    clicked = create_bar('Load Game', 1, color1, color2, center_bar, y_bar, bar, h)
    if pygame.mouse.get_pressed()[0] and clicked:
        pass

    # SETTING
    clicked = create_bar('Settings', 2, color1, color2, center_bar, y_bar, bar, h)
    if pygame.mouse.get_pressed()[0] and clicked:
        pass

    #CREDITS
    clicked = create_bar('Credits', 3, color1, color2, center_bar, y_bar, bar, h)
    if pygame.mouse.get_pressed()[0] and clicked:
        credits(display, center_bar)

    # EXIT/QUIT
    clicked = create_bar('Quit Game', 4, color1, color2, center_bar, y_bar, bar, h)


    if pygame.mouse.get_pressed()[0] and clicked:
        pygame.quit()
        sys.exit()


def create_bar(name, number, color1, color2, center_bar, y_bar, bar, h):

    if center_bar < pygame.mouse.get_pos()[0] < bar[0] + center_bar and y_bar + number * (bar[1] + h) < pygame.mouse.get_pos()[1] < bar[1] + y_bar + number * (bar[1] + h):
        pygame.draw.rect(display, color2, (center_bar, y_bar + number * (bar[1] + h), bar[0], bar[1]))
        caption = font.render(name, 1, (250, 250, 250))
        display.blit(caption, (int(center_bar + (bar[0] - caption.get_width()) / 2), int(y_bar + number * (bar[1] + h) + (bar[1] - caption.get_height()) / 2)))
        return True
    else:
        pygame.draw.rect(display, color1, (center_bar, y_bar + number * (bar[1] + h), bar[0], bar[1]))
        caption = font.render(name, 1, (250, 250, 250))
        display.blit(caption, (int(center_bar + (bar[0] - caption.get_width()) / 2), int(y_bar + number * (bar[1] + h) + (bar[1] - caption.get_height()) / 2)))
        return False

def credits(display, center_bar):
    display.fill((0,0,0))
    credits1 = pygame.font.SysFont('comicsans', 40, True)
    credits2 = pygame.font.SysFont('comicsans', 30)
    credits3 = pygame.font.SysFont('comicsans', 15)

    created_by = credits1.render('CREATED BY', 1, (250, 250, 250))
    name = credits2.render('Mateusz Bączkowski', 1, (250, 250, 250))
    github = credits2.render('github.com/Baczas', 1, (250, 250, 250))
    escape = credits2.render('click ESC to return to the menu', 1, (120, 120, 120))
    display.blit(created_by, (center_bar , 150))
    display.blit(name, (center_bar, 250))
    display.blit(github, (center_bar, 270))
    display.blit(player.image, (center_bar - 70, 270 - 50))
    display.blit(escape, (10,10))

    pygame.display.update()
    while True:
        exit()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            break
        clock.tick(60)


def enemies():
    pass


def game_screen():
    while True:
        clicks()
        display.fill((146, 244, 255))  # set display background

        # Start screen

        true_shift[0] += (player.hit_box.x - true_shift[0] - int(WINDOW_SIZE[0] / 2 - player.hit_box.width / 2)) / 10
        true_shift[1] += (player.hit_box.y - true_shift[1] - int(WINDOW_SIZE[1] / 2 - player.hit_box.height / 2)) / 10
        # scroll = true_scroll.copy()
        shift = [int(true_shift[0]), int(true_shift[1])]

        colision_rects, platform_rects = world.draw(display, shift)
        player.move(display, colision_rects, platform_rects, shift)

        # add some text on screen later

        # Here add more characters
        enemies()
        pygame.display.update()
        clock.tick(60)
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pause_menu()

display.fill((120, 120, 120))  # set display background
while True:     # Main loop

    clicks()
    #display.fill((146, 244, 255))  # set display background
    main_menu()

    pygame.display.update()
    clock.tick(60)

