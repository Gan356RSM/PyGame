import pygame

pygame.init()

win = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

player = pygame.Rect(50, 50, 50, 50)
wall1 = pygame.Rect(0, 0, 2000, 25)
wall2 = pygame.Rect(0, 775, 2000, 25)
wall3 = pygame.Rect(775, 0, 25, 2000)
wall4 = pygame.Rect(0, 0, 25, 2000)
wall5 = pygame.Rect(350, 350, 100, 100)
wall6 = pygame.Rect(200, 200, 0, 100)
wall7 = pygame.Rect(100, 100, 100, 0)
wall8 = pygame.Rect(100, 100, 100, 0)
wall9 = pygame.Rect(100, 100, 100, 0)
walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9]

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


    win.fill((157, 250, 249))
    pygame.draw.rect(win, (31, 196, 193), player)
    for w in walls:
        pygame.draw.rect(win, (22, 122, 121), wall1)
        pygame.draw.rect(win, (22, 122, 121), wall2)
        pygame.draw.rect(win, (22, 122, 121), wall3)
        pygame.draw.rect(win, (22, 122, 121), wall4)
        pygame.draw.rect(win, (22, 122, 121), wall5)
        pygame.draw.rect(win, (22, 122, 121), wall6)
        pygame.draw.rect(win, (22, 122, 121), wall7)
        pygame.draw.rect(win, (22, 122, 121), wall8)
        pygame.draw.rect(win, (22, 122, 121), wall9)

    pygame.display.update()
    clock.tick(60)