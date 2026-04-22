import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Levels")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_COLOR = (34, 110, 40)
RED = (200, 0, 0)
GRAY = (40, 40, 40)
BLUE = (0, 0, 255)


class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (CELL_SIZE, 0)
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0] 
        dx, dy = self.direction 
        new_head = (head_x + dx, head_y + dy) 

        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop() 
        else:
            self.grow = False  
            

    def change_direction(self, dx, dy):
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)

    def draw(self): 
        for block in self.body:
            pygame.draw.rect(screen, BLUE, (*block, CELL_SIZE, CELL_SIZE))  

    def check_self_collision(self):
        return self.body[0] in self.body[1:] 

    def check_wall_collision(self):
        x, y = self.body[0]
        return x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT 
    

class Food:
    def __init__(self, snake_body):
        self.position = self.generate_position(snake_body)  

    def generate_position(self, snake_body):
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE

            if (x, y) not in snake_body:
                return (x, y)

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, CELL_SIZE, CELL_SIZE))


snake = Snake()
food = Food(snake.body)

score = 0
level = 1
foods_per_level = 3
speed = 8


running = True
while running:
    screen.fill(BG_COLOR)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(0, CELL_SIZE)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(CELL_SIZE, 0)

  
    snake.move()

   
    if snake.body[0] == food.position:  
        snake.grow = True
        score += 1
        food = Food(snake.body)

       
        if score % foods_per_level == 0:
            level += 1
            speed += 2

    
    if snake.check_self_collision() or snake.check_wall_collision():  
        running = False

   
    snake.draw()
    food.draw()

   
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

   
    pygame.display.update()
    clock.tick(speed)

pygame.quit()
sys.exit()