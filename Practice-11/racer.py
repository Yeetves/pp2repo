import pygame
import random
import sys

pygame.init()


WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")


clock = pygame.time.Clock()
FPS = 60


WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)
RED = (255, 0, 0)


bg = pygame.image.load("images/background.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

car_img = pygame.image.load("images/car.png")
player_width = 50
player_height = 80
player_img = pygame.transform.scale(car_img, (player_width*1.25, player_height*1.25))

player = pygame.Rect(WIDTH // 2, HEIGHT - 100, player_width, player_height)
player_speed = 6

car2_img = pygame.image.load("images/enemy.png")
enemy_width = 50
enemy_height = 80
enemy_img = pygame.transform.scale(car2_img, (enemy_width*1.25, player_height*1.25))

enemy = pygame.Rect(random.randint(50, WIDTH - 100), -100, enemy_width, enemy_height)
enemy_speed = 5


coin_size = 20
coins = []
coin_spawn_timer = 0


score = 0
font = pygame.font.SysFont("Arial", 24)


def spawn_coin():
    x = random.randint(50, WIDTH - 50)
    weight = random.choice([1, 3])
    coin = pygame.Rect(x, -20, coin_size, coin_size) 
    coins.append({
        "rect": coin,
        "weight": weight
    })


def draw_coins():
    for coin in coins:
        rect = coin["rect"]
        weight = coin["weight"]

        # Small coin
        if weight == 1:
            radius = 10

        # Big coin
        else:
            radius = 16

        pygame.draw.circle(screen, YELLOW, rect.center, radius)



def move_coins():
    global coins
    for coin in coins:
        coin["rect"].y += 5

    coins = [
    c for c in coins   
    if c["rect"].y < HEIGHT]


def reset_enemy():
    enemy.x = random.randint(50, WIDTH - 100)
    enemy.y = -100



running = True
while running:
    clock.tick(FPS)
    screen.blit(bg, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed


    coin_spawn_timer += 1
    if coin_spawn_timer > 40:
        spawn_coin()
        coin_spawn_timer = 0

    move_coins()


    for coin in coins[:]:
        if player.colliderect(coin["rect"]): 
            coins.remove(coin)
            score += coin["weight"]

    enemy.y += enemy_speed

    # Reset enemy if it leaves screen
    if enemy.y > HEIGHT:
        reset_enemy()

    enemy_speed = 5 + (score // 10)

    if player.colliderect(enemy):

        # Game over screen
        game_over = font.render("GAME OVER", True, RED)
        screen.blit(game_over, (WIDTH // 2 - 80, HEIGHT // 2))

        pygame.display.flip()

        pygame.time.delay(2000)

        running = False

    screen.blit(player_img, (player.x, player.y))
    draw_coins()
    screen.blit(enemy_img, (enemy.x, enemy.y))
    
    score_text = font.render(f"Coins: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH - 130, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()