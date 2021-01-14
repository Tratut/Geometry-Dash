import pygame

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

bg_w, bg_h = 40, 40
main_cube = pygame.image.load('data\Main_cube\skin1.png')
main_cube = pygame.transform.scale(main_cube, (40, 40))
pos_rot = 0


def rotate():
    global pos_rot
    global main_cube
    if pos_rot == 0:
        screen.blit(main_cube, (300, 300))
    elif pos_rot == 1:
        screen.blit(main_cube, (300, 300))
        main_cube = pygame.transform.rotate(main_cube, 180)
    pygame.display.update()


done = False
while not done:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if pos_rot == 0:
        pos_rot = 1
    else:
        pos_rot = 0
    rotate()
