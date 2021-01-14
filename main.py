import pygame
from start_screen import start_screen


class Cube():
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        # гг
        self.x = 200
        self.y = 441
        self.wight = 40
        self.heigt = 40
        self.speed = 3
        self.cubeSet = 0
        self.isJump = False
        self.jumpCount = 12
        self.main_cube = pygame.image.load('data\Main_cube\skin1.png')
        self.main_cube = pygame.transform.scale(self.main_cube, (40, 40))

        # вращение
        self.rot = 0
        self.rot_speed = 18
        self.last_update = pygame.time.get_ticks()
        self.rect = self.main_cube.get_rect()
        self.pos_rot = 0  # проверка позиции после вращения
        self.checker_rot = 0  # проверка того что вращение куба произошло 1 раз

    def action(self, keys):
        """
        Отработка прыжка
        """
        if not self.isJump:
            if keys[pygame.K_SPACE]:
                self.isJump = True
                if self.pos_rot == 0:
                    self.pos_rot = 1
                else:
                    self.pos_rot = 0
                    self.checker_rot = 0
        else:
            if self.jumpCount >= -12:
                if self.jumpCount < 0:
                    self.y += (self.jumpCount ** 2) // 4 - 1
                else:
                    self.y -= (self.jumpCount ** 2) // 4 - 1
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 12
                self.y -= 1
        pygame.display.update()

    def draw_character(self):
        if not self.isJump:
            if self.pos_rot == 0:
                self.screen.blit(self.main_cube, (self.x, self.y))
            elif self.pos_rot == 1:
                self.screen.blit(self.main_cube, (self.x, self.y))
                if self.checker_rot == 0:
                    self.main_cube = pygame.transform.rotate(self.main_cube, 180)
                    self.checker_rot = 1
        else:
            self.rotate()
        pygame.display.update()

    def rotate(self):
        """
        Вращение куба во время прыжка
        """
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot - self.rot_speed) % 360
            image = pygame.transform.rotate(self.main_cube, self.rot)
            screen.blit(image, (self.x, self.y))

            old_center = self.rect.center
            new_image = image
            self.rect = new_image.get_rect()
            self.rect.center = old_center
        pygame.display.update()

    def coordinate(self):
        return self.y


class Location():
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        # гг
        self.x = 200
        self.y = 441
        self.wight = 40
        self.heigt = 40
        # земля
        self.g_w, self.g_h = self.size
        self.bg = pygame.transform.smoothscale(pygame.image.load('data\Grounds\gr1.jpg'), (self.g_w, self.g_h))
        self.pos_xg = 0
        self.speed = 3

        # фон
        self.bg_w, self.bg_h = 800, self.y + self.heigt
        self.g = pygame.transform.smoothscale(pygame.image.load('data\ofon.jpg'), (self.bg_w, self.bg_h))
        self.pos_xbg = 0
        self.speed_bg = 5

    def draw_bg(self):
        """
        Отрисовка заднего фона
        """
        self.pos_xbg -= self.speed_bg

        x_rel = self.pos_xbg % self.bg_w
        x_part2 = x_rel - self.bg_w if x_rel > 0 else x_rel + self.bg_w

        screen.blit(self.bg, (x_rel, 0))
        screen.blit(self.bg, (x_part2, 0))
        self.draw_ground()

    def draw_ground(self):
        """
        Отрисовка землии
        """
        self.pos_xg -= self.speed

        x_rel = self.pos_xg % self.g_w
        x_part2 = x_rel - self.g_w if x_rel > 0 else x_rel + self.g_w

        screen.blit(self.g, (x_rel, 0))
        screen.blit(self.g, (x_part2, 0))


class Block():
    def __init__(self):
        self.w_bl, self.h_nl = 40, 40
        self.bl = pygame.transform.smoothscale(pygame.image.load('data\Enemys\E0.png'), (self.w_bl // 2, self.h_nl))
        self.pos_xbl = 800
        self.speed = 5
        self.isStart = True

    def generate_blocK(self):
        if self.pos_xbl <= 0 or self.isStart:
            self.spawn_block()
            self.isStart = False
        else:
            self.move_block()

    def spawn_block(self):
        screen.blit(self.bl, (self.pos_xbl, 441))
        pygame.display.update()
        self.pos_xbl = 800

    def move_block(self):
        self.pos_xbl -= self.speed
        screen.blit(self.bl, (self.pos_xbl, 440))
        pygame.display.update()

    def coordinate(self):
        return self.pos_xbl


def end_no():
    bl_x = blck.coordinate()
    bl_y = 441
    cb_x = 200
    cb_y = cub.coordinate()
    if ((bl_x + 40 == cb_x or bl_x == cb_x) or (bl_x + 40 == cb_x + 20 or bl_x == cb_x + 20))\
            and ((bl_y + 40 == cb_y or bl_y == cb_y) or bl_y == cb_y or bl_y == cb_y):
        return True


def start():
    """
    Запуск игры и др ее компонентов
    """
    cub.action(keys)
    loc.draw_bg()
    cub.draw_character()
    blck.generate_blocK()
    # render()
    # screen.fill((0, 0, 0))


def render():
    """
    Отрисовка сетки для отладки(для разработчика)
    """
    global screen
    for y in range(600 // 40):
        for x in range(800 // 40):
            pygame.draw.rect(screen, (255, 255, 255), (40 * x, 40 * y, 40, 40), 1)
    pygame.display.update()


if __name__ == "__main__":
    clock = pygame.time.Clock()
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    cub = Cube(screen, size)
    loc = Location(screen, size)
    blck = Block()
    restart = True
    if start_screen(screen, clock):
        while restart:
            run = True
            while run:
                clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                if end_no():
                    run = False
                keys = pygame.key.get_pressed()
                start()

            pygame.quit()
