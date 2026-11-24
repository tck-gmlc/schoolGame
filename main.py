import pygame, math, json

pygame.init()

screen_width,screen_height = 512,512
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
FPS = 60
run = True
keybinds = {'up': pygame.K_w, 'left': pygame.K_a, 'down': pygame.K_s, 'right': pygame.K_d}
rCount = 0


class Room():
    def __init__(self, pos, id, color=(145,142,133)):
        global rCount

        with open(f"./data/rooms/{id}.json", encoding="utf-8") as room:
                    data = json.load(room)
        self.data=  data
        rCount += 1
        self.rID = rCount
        self.width = data["bounds"]["width"]
        self.height = data["bounds"]["height"]
        self.surface = pygame.Surface((self.width,self.height))
        self.surface.fill(color)
        self.rect = self.surface.get_rect()
        self.pos = pos
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        screen.blit(self.surface, self.rect)



class Player():
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


    def collision(self, room):

        self.rect.x += self.dx
        self.rect.y += self.dy

        for collider in room.data["colliders"]:
            if room.data["colliders"][collider]["type"] == "xConst":
                x = room.data["colliders"][collider]["x"] + room.pos[0]
                start = room.data["colliders"][collider]["start"] + room.pos[1]
                stop = room.data["colliders"][collider]["stop"] + room.pos[1]
                
                if self.rect.bottom > start and self.rect.top < stop:
                    if self.dx > 0 and self.rect.right >= x and self.rect.left < x:
                        self.rect.right = x
                    elif self.dx < 0 and self.rect.left <= x and self.rect.right > x:
                        self.rect.left = x

            if room.data["colliders"][collider]["type"] == "yConst":
                            y = room.data["colliders"][collider]["y"] + room.pos[1]
                            start = room.data["colliders"][collider]["start"] + room.pos[0]
                            stop = room.data["colliders"][collider]["stop"] + room.pos[0]
                            
                            if self.rect.right > start and self.rect.left < stop:
                                if self.dy > 0 and self.rect.bottom >= y and self.rect.top < y:
                                    self.rect.bottom = y
                                elif self.dy < 0 and self.rect.top <= y and self.rect.bottom > y:
                                    self.rect.top = y

                        



    def update(self,room):
        screen.blit(self.surface, self.rect)
        player.movement()
        player.collision(room)
        

room1 = Room((128,128), "starting")
player = Player((10,10),(25,25),(255,0,0))


while run:
    screen.fill((50,50,50))

    room1.update()
    player.update(room1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(FPS)