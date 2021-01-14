import pygame


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


class Game():
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        # гг
        self.x = 200
        self.y = 441
        self.wight = 40
        self.heigt = 40

        self.cubeSet = 0

        self.isJump = False
        self.jumpCount = 10

        self.main_cube = pygame.image.load('data\Main_cube\skin1.png')
        self.main_cube = pygame.transform.scale(self.main_cube, (40, 40))
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

        # вращение
        self.rot = 0
        self.rot_speed = 18
        self.last_update = pygame.time.get_ticks()
        self.rect = self.main_cube.get_rect()

        # блоки
        self.w_bl, self.h_nl = 40, 40
        self.bl = pygame.transform.smoothscale(pygame.image.load('data\Grounds\gr1.jpg'), (self.w_bl, self.h_nl))
        self.pos_xbl = 500
        self.x_rel = 800

    def action(self, keys):
        if not self.isJump:
            if keys[pygame.K_SPACE]:
                self.isJump = True
        else:
            if self.jumpCount >= -10:
                if self.jumpCount < 0:
                    self.y += (self.jumpCount ** 2) // 4 - 1
                else:
                    self.y -= (self.jumpCount ** 2) // 4 - 1
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
                self.y -= 1
        pygame.display.update()

    def draw_character(self):
        if not self.isJump:
            self.screen.blit(self.main_cube, (self.x, self.y))
        else:
            self.rotate()

        pygame.display.update()

    def draw_bg(self):
        self.pos_xbg -= self.speed_bg

        x_rel = self.pos_xbg % self.bg_w
        x_part2 = x_rel - self.bg_w if x_rel > 0 else x_rel + self.bg_w

        screen.blit(self.bg, (x_rel, 0))
        screen.blit(self.bg, (x_part2, 0))
        self.draw_ground()

    def draw_ground(self):
        self.pos_xg -= self.speed

        x_rel = self.pos_xg % self.g_w
        x_part2 = x_rel - self.g_w if x_rel > 0 else x_rel + self.g_w

        screen.blit(self.g, (x_rel, 0))
        screen.blit(self.g, (x_part2, 0))

    def rotate(self):
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

    def block(self):
        self.pos_xbl -= self.speed
        self.x_rel -= self.pos_xbl % self.w_bl
        screen.blit(self.bl, (self.x_rel, 440))


class Blocks():
    pass


def start():
    game.action(keys)
    game.draw_bg()
    game.draw_character()
    game.block()
    # render()
    # screen.fill((0, 0, 0))


def render():
    global screen
    for y in range(600 // 40):
        for x in range(800 // 40):
            pygame.draw.rect(screen, (255, 255, 255), (40 * x, 40 * y, 40, 40), 1)
    pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    game = Game(screen, size)
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        start()

    pygame.quit()
