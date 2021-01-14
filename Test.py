import pygame

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

bg_w, bg_h = 40, 40
image_orig = pygame.image.load('data\Main_cube\skin1.png')
image_orig = pygame.transform.scale(image_orig, (40, 40))

rot = 0
rot_speed = 15
last_update = pygame.time.get_ticks()
rect = image_orig.get_rect()


def rotate():
    global image_orig
    global last_update
    global rot
    global screen
    global rect
    screen.fill((0, 0, 0))
    now = pygame.time.get_ticks()
    if now - last_update > 50:
        last_update = now
        rot = (rot - rot_speed) % 360
        image = pygame.transform.rotate(image_orig, rot)
        screen.blit(image, (150, 150))

        old_center = rect.center
        new_image = image
        rect = new_image.get_rect()
        rect.center = old_center
    pygame.display.update()



done = False
while not done:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    rotate()

