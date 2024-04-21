import pygame

pygame.init()

win = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()

class Enemy():
    def __init__(self, x, y, moves):
        self.rect = pygame.Rect(x, y, 25, 25)
        self.color = (255, 0, 0)
        self.moves = moves
        self.idx = 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def update(self):
        move = self.moves[self.idx]
        if move == 'l':
            self.rect.x -= 1
        elif move == 'r':
            self.rect.x += 1
        elif move == 'u':
            self.rect.y -= 1
        elif move == 'd':
            self.rect.y += 1
        self.idx += 1
        if self.idx >= len(self.moves):
            self.idx = 0


class Food():
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Level1():
    def __init__(self):
        self.next = None
        self.player = pygame.Rect(100, 100, 25, 25)
        self.wall1 = pygame.Rect(0, 0, 500, 25)
        self.wall2 = pygame.Rect(0, 0, 25, 400)
        self.wall3 = pygame.Rect(475, 0, 25, 400)
        self.wall4 = pygame.Rect(0, 375, 500, 25)
        e1 = Enemy(100, 300, 10 * 'l' + 10 * 'r')
        e2 = Enemy(100, 200, 10 * 'l' + 10 * 'r')
        self.enemies = [e1, e2]
        f1 = Food(100, 100, (25, 255, 200))
        f2 = Food(200, 200, (25, 255, 200))
        self.food = [f1, f2]
        

    def draw(self, surface):
        surface.fill((255, 255, 200))
        pygame.draw.rect(surface, (200, 255, 200), self.player)
        for e in self.enemies:
            e.draw(surface)
        for f in self.food:
            f.draw(surface)

    def update(self, events, keys):
        if keys[pygame.K_a]:
            self.player.x -= 1
        if keys[pygame.K_d]:
            self.player.x += 1
        if keys[pygame.K_w]:
            self.player.y -= 1
        if keys[pygame.K_s]:
            self.player.y += 1
        for e in self.enemies:
            e.update()
        for f in self.food:
                if len(self.food) == 0:
                    game_over = True
                    final_msg = win_msg
        if player.colliderect(f.rect):
            self.food.remove(f)
            
        

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

player = pygame.Rect(50, 50, 25, 25)

fnt = pygame.font.Font(None, 16)
lose_msg = fnt.render("You Lose!", True, (0, 0, 0))
win_msg = fnt.render("You Win!", True, (0, 0, 0))
final_msg = lose_msg
game_over = False
level = Level1()

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    
    if level.next != None:
        level = level.next

    level.update(events, keys)
    level.draw(win)
    
    #if not game_over:
        #if e.rect.colliderect(player):
            #game_over = True
            #final_msg = lose_msg

    pygame.display.update()
    clock.tick(120)