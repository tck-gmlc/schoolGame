import pygame, keyboard

pygame.init()

screen_width,screen_height = 512,512
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
FPS = 60
run = True
keybinds = {'up': 'w', 'left': 'a', 'down': 's', 'right': 'd'}

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,size,color):
        self.surface = pygame.Surface(size)
        self.surface.fill(color)
        self.rect = self.surface.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = [1,1]
        self.dx = 0
        self.dy = 0

    def movement(self):
        if keyboard.is_pressed(keybinds.get('up')):
            self.dy = -10
        elif keyboard.is_pressed(keybinds.get('down')):
            self.dy = 10
        else:
            self.dy = 0
        if keyboard.is_pressed(keybinds.get('left')):
            self.dx = -10
        elif keyboard.is_pressed(keybinds.get('right')):
            self.dx = 10
        else:
            self.dx = 0


        self.rect.x += self.dx
        self.rect.y += self.dy

    def update(self):
        screen.blit(self.surface, self.rect)
        player.movement()


player = Player((200,200),(50,50),(255,0,0))

while run:
    screen.fill((145,142,133))

    player.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(FPS)