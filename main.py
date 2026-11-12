import pygame

pygame.init()

screen_width,screen_height = 512,512
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
FPS = 60
run = True

while run:

    screen.fill((145,142,133))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(FPS)