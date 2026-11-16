import pygame, math

pygame.init()

screen_width,screen_height = 512,512
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
FPS = 60
run = True
keybinds = {'up': pygame.K_w, 'left': pygame.K_a, 'down': pygame.K_s, 'right': pygame.K_d}

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,size,color):
        self.surface = pygame.Surface(size)
        self.surface.fill(color)
        self.rect = self.surface.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dirX = 0
        self.dirY = 0
        self.dx = 0
        self.dy = 0

    def movement(self):
        keys = pygame.key.get_pressed()

        match (keys[keybinds['up']],keys[keybinds['down']]):
            case (True,False):
                self.dirY = -1
            case (False,True):
                self.dirY = 1
            case (True,True) | (False,False):
                self.dirY = 0

        match (keys[keybinds['left']],keys[keybinds['right']]):
            case (True,False):
                self.dirX = -1
            case (False,True):
                self.dirX = 1
            case (True,True) | (False,False):
                self.dirX = 0

        match (self.dirX,self.dirY):
            case (-1,-1):
                self.dx = -7
                self.dy = -7
            case (-1,0):
                self.dx = -10
                self.dy = 0
            case (-1,1):
                self.dx = -7
                self.dy = 7

            case (0,-1):
                self.dx = 0
                self.dy = -10
            case (0,0):
                self.dx = 0
                self.dy = 0
            case (0,1):
                self.dx = 0
                self.dy = 10
            
            case (1,-1):
                self.dx = 7
                self.dy = -7
            case (1,0):
                self.dx = 10
                self.dy = 0
            case (1,1):
                self.dx = 7
                self.dy = 7


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