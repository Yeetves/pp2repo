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


coin_size = 20
coins = []
coin_spawn_timer = 0


score = 0
font = pygame.font.SysFont("Arial", 24)


def spawn_coin():
    x = random.randint(50, WIDTH - 50)
    coin = pygame.Rect(x, -20, coin_size, coin_size) 
    coins.append(coin)


def draw_coins():
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, coin.center, coin_size // 2)


def move_coins():
    global coins
    for coin in coins:
        coin.y += 5

    coins = [
    c for c in coins   
    if c.y < HEIGHT]



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
        if player.colliderect(coin): 
            coins.remove(coin)
            score += 1

    screen.blit(player_img, (player.x, player.y))
    draw_coins()

    
    score_text = font.render(f"Coins: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH - 130, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()