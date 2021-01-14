import pygame


def start_screen(screen, clock):
    pygame.init()
    text = ["Geometry dash",
            "", "", "", "", "", "", "", "", "", "", "",
            "Нажмите кнопкy для продолжения"]
    background = pygame.image.load('data\ofon.jpg')
    background = pygame.transform.scale(background, (800, 600))
    screen.blit(background, (0, 0))

    pygame.font.init()
    font = pygame.font.Font(None, 40)
    text_coord = 50
    for line in text:
        string = font.render(line, 1, pygame.Color("white"))
        string_rect = string.get_rect()
        text_coord += 10
        string_rect.top = text_coord
        string_rect.x = 150
        text_coord += string_rect.height
        screen.blit(string, string_rect)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return True
        pygame.display.flip()
        clock.tick(60)
