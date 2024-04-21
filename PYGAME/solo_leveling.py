import pygame

class Level1():
    def __init__(self):
        self.player = pygame.Rect(100, 100, 25, 25)
        self.w = pygame.Rect(200, 100, 25, 25)
        self.next = None

    def draw(self, surface):
        surface.fill((255, 255, 200))
        pygame.draw.rect(surface, (200, 255, 200), self.player)
        pygame.draw.rect(surface, (200, 200, 200), self.w)

    def update(self, events, keys):
        if keys[pygame.K_a]:
            self.player.x -= 1
        if keys[pygame.K_d]:
            self.player.x += 1
        if keys[pygame.K_w]:
            self.player.y -= 1
        if keys[pygame.K_s]:
            self.player.y += 1

        if self.player.colliderect(self.w):
            self.next = Level2()

class Level2():
    def __init__(self):
        self.player = pygame.Rect(225, 175, 25, 25)
        self.w = pygame.Rect(0, 0, 25, 25)
        self.next = None

    def draw(self, surface):
        surface.fill((255, 255, 200))
        pygame.draw.rect(surface, (200, 255, 200), self.player)
        pygame.draw.rect(surface, (200, 200, 200), self.w)

    def update(self, events, keys):
        if keys[pygame.K_a]:
            self.player.x -= 1
        if keys[pygame.K_d]:
            self.player.x += 1
        if keys[pygame.K_w]:
            self.player.y -= 1
        if keys[pygame.K_s]:
            self.player.y += 1

        if self.player.colliderect(self.w):
            self.next = Level3()

class Level3():
    def __init__(self):
        self.player = pygame.Rect(225, 175, 25, 25)
        self.w = pygame.Rect(0, 0, 25, 25)
        self.next = None

    def draw(self, surface):
        surface.fill((255, 255, 200))
        pygame.draw.rect(surface, (200, 255, 200), self.player)
        pygame.draw.rect(surface, (200, 200, 200), self.w)

    def update(self, events, keys):
        if keys[pygame.K_a]:
            self.player.x -= 1
        if keys[pygame.K_d]:
            self.player.x += 1
        if keys[pygame.K_w]:
            self.player.y -= 1
        if keys[pygame.K_s]:
            self.player.y += 1

        if self.player.colliderect(self.w):
            self.next = None


pygame.init()
win = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()
run = True
level = Level1()
while run:
    events = pygame.event.get()
    keys = pygame.key.get_pressed()

    for e in events:
        if e.type == pygame.QUIT:
            run = False
    
    if level.next != None:
        level = level.next
            
    level.update(events, keys)
    level.draw(win)

    pygame.display.update()
    clock.tick(120)