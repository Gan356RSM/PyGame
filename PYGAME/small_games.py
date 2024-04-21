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


f1 = Food(100, 100, (25, 255, 200))
f2 = Food(200, 200, (25, 255, 200))
food = [f1, f2]


player = pygame.Rect(50, 50, 25, 25)

w1 = pygame.Rect(0, 0, 500, 25)
w2 = pygame.Rect(0, 0, 25, 400)
w3 = pygame.Rect(475, 0, 25, 400)
w4 = pygame.Rect(0, 375, 500, 25)
walls = [w1, w2, w3, w4]

fnt = pygame.font.Font(None, 16)
lose_msg = fnt.render("You Lose!", True, (0, 0, 0))
win_msg = fnt.render("You Win!", True, (0, 0, 0))
final_msg = lose_msg
game_over = False

e1 = Enemy(100, 300, 10 * 'l' + 10 * 'r')
e2 = Enemy(100, 200, 10 * 'l' + 10 * 'r')
enemies = [e1, e2]

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_a]:
            player.x -= 1
            for w in walls:
                while w.colliderect(player):
                    player.x += 1

        if keys[pygame.K_d]:
            player.x += 1
            for w in walls:
                while w.colliderect(player):
                    player.x -= 1

        if keys[pygame.K_w]:
            player.y -= 1
            for w in walls:
                while w.colliderect(player):
                    player.y += 1
                    
        if keys[pygame.K_s]:
            player.y += 1
            for w in walls:
                while w.colliderect(player):
                    player.y -= 1

    for f in food:
        if player.colliderect(f.rect):
            food.remove(f)
            if len(food) == 0:
                game_over = True
                final_msg = win_msg

    if not game_over:
        for e in enemies:
            e.update()
            if e.rect.colliderect(player):
                game_over = True
                final_msg = lose_msg

    win.fill((255, 255, 200))
    for w in walls:
        pygame.draw.rect(win, (200, 255, 255), w)
    pygame.draw.rect(win, (200, 255, 200), player)
    for f in food:
        f.draw(win)
    for e in enemies:
        e.draw(win)
    if game_over:
        win.blit(final_msg, (0, 0))


    pygame.display.update()
    clock.tick(120)