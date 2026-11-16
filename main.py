import pygame, math, json

pygame.init()

screen_width,screen_height = 512,512
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
FPS = 60
run = True
keybinds = {'up': pygame.K_w, 'left': pygame.K_a, 'down': pygame.K_s, 'right': pygame.K_d}

class Player():
    def __init__(self,world,pos,size,color):
        self.surface = pygame.Surface(size)
        self.surface.fill(color)
        self.rect = self.surface.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dirX = 0
        self.dirY = 0
        self.dx = 0
        self.dy = 0
        self.speed = 5
        self.speedDiag = self.speed / math.sqrt(2)

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
                self.dx = -1 * self.speedDiag
                self.dy = -1 * self.speedDiag
            case (-1,0):
                self.dx = -1 * self.speed
                self.dy = 0
            case (-1,1):
                self.dx = -1 * self.speedDiag
                self.dy = self.speedDiag

            case (0,-1):
                self.dx = 0
                self.dy = -1 * self.speed
            case (0,0):
                self.dx = 0
                self.dy = 0
            case (0,1):
                self.dx = 0
                self.dy = self.speed
            
            case (1,-1):
                self.dx = self.speedDiag
                self.dy = -1 * self.speedDiag
            case (1,0):
                self.dx = self.speed
                self.dy = 0
            case (1,1):
                self.dx = self.speedDiag
                self.dy = self.speedDiag


    def collision(self):
        if self.rect.right + self.dx >= world.rect.right:
            self.rect.right = world.rect.right
        elif self.rect.left + self.dx <= world.rect.left:
            self.rect.left = world.rect.left
        else:
            self.rect.x += self.dx

        if self.rect.bottom + self.dy >= world.rect.bottom:
            self.rect.bottom = world.rect.bottom
        elif self.rect.top + self.dy <= world.rect.top:
            self.rect.top = world.rect.top
        else:
            self.rect.y += self.dy

    def update(self):
        screen.blit(self.surface, self.rect)
        player.movement()
        player.collision()


class World():
    def __init__(self,origin=(0,0)):
        with open("data\\rooms\\starting.json", encoding="utf-8") as room:
            data = json.load(room)

        self.width = data["bounds"]["width"]
        self.height = data["bounds"]["height"]
        self.surface = pygame.Surface((self.width,self.height))
        self.surface.fill((145,142,133))
        self.rect = self.surface.get_rect()
        self.rect.x = origin[0]
        self.rect.y = origin[1]

        if data["doors"]["south"]:
            self.S_door = pygame.sprite.Sprite
            self.S_door.surface = pygame.Surface((32,8))
            self.S_door.surface.fill((0,255,0))
            self.S_door.rect = self.S_door.surface.get_rect()
            self.S_door.rect.x = origin[0] + data["doors"]["south"]["x"] - 16
            self.S_door.rect.y = origin[1] + data["doors"]["south"]["y"] - 4

    def update(self):
        screen.blit(self.surface, self.rect)
        screen.blit(self.S_door.surface, self.S_door.rect)


world = World()
player = Player(world,(200,200),(25,25),(255,0,0))

while run:
    screen.fill((50,50,50))

    world.update()
    player.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(FPS)