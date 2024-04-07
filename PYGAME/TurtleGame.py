import pygame

pygame.init()

win = pygame.display.set_mode((800, 700))
clock = pygame.time.Clock()

player = pygame.Rect(50, 50, 50, 50)
wall1 = pygame.Rect(0, 0, 2000, 25)
wall2 = pygame.Rect(0, 675, 2000, 25)
wall3 = pygame.Rect(775, 0, 25, 2000)
wall4 = pygame.Rect(0, 0, 25, 2000)
wall5 = pygame.Rect(350, 300, 100, 100)
walls = [wall1, wall2, wall3, wall4, wall5]

class Fruit():
    def __init__(self, x, y, w, h, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


blueberry = Fruit(25, 25, 25, 25, (100, 140, 255))
strawberry = Fruit(25, 650, 25, 25, (255, 140, 140))
melon = Fruit(750, 25, 25, 25, (100, 220, 100))
grapes = Fruit(750, 650, 25, 25, (255, 0, 255))

fruits = [blueberry, strawberry, melon, grapes]

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= 2
        for w in walls:
            while w.colliderect(player):
                player.x += 1
    if keys[pygame.K_d]:
        player.x += 2
        for w in walls:
            while w.colliderect(player):
                player.x -= 1
    if keys[pygame.K_w]:
        player.y -= 2
        for w in walls:
            while w.colliderect(player):
                player.y += 1
    if keys[pygame.K_s]:
        player.y += 2
        for w in walls:
            while w.colliderect(player):
                player.y -= 1

    for berries in fruits:
        if berries.rect.colliderect(player):
            fruits.remove(berries)

    win.fill((157, 250, 249))
    pygame.draw.rect(win, (31, 196, 193), player)
    for w in walls:
        pygame.draw.rect(win, (22, 122, 121), w)

    for berries in fruits:
        berries.draw(win)

    pygame.display.update()
    clock.tick(60)
