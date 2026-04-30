import pygame
import random
import sys

pygame.init()

# ---------------- SCREEN SETTINGS ----------------
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Levels")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# ---------------- COLORS ----------------
WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

# Background color
BG_COLOR = (34, 110, 40)

# Grid is now only SLIGHTLY darker
GRID_COLOR = (28, 95, 34)

RED = (200, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 215, 0)

# =================================================
# SNAKE CLASS
# =================================================
class Snake:

    def __init__(self):

        self.body = [(100, 100), (80, 100), (60, 100)]

        # Current direction
        self.direction = (CELL_SIZE, 0)

        # Next direction
        # Prevents instant double turns bug
        self.next_direction = self.direction

        self.grow = False

    # -------------------------------------------------
    # Move snake
    # -------------------------------------------------
    def move(self):

        # Apply next direction ONLY once per frame
        self.direction = self.next_direction

        head_x, head_y = self.body[0]

        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)

        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()

        else:
            self.grow = False

    # -------------------------------------------------
    # Change direction
    # Fixes fast-keypress self collision bug
    # -------------------------------------------------
    def change_direction(self, dx, dy):

        # Check against CURRENT direction only
        if (dx, dy) != (-self.direction[0], -self.direction[1]):

            self.next_direction = (dx, dy)

    # -------------------------------------------------
    # Draw snake
    # -------------------------------------------------
    def draw(self):

        for block in self.body:

            pygame.draw.rect(
                screen,
                BLUE,
                (*block, CELL_SIZE, CELL_SIZE)
            )

    # -------------------------------------------------
    # Check self collision
    # -------------------------------------------------
    def check_self_collision(self):

        return self.body[0] in self.body[1:]

    # -------------------------------------------------
    # Check wall collision
    # -------------------------------------------------
    def check_wall_collision(self):

        x, y = self.body[0]

        return (
            x < 0 or
            x >= WIDTH or
            y < 0 or
            y >= HEIGHT
        )

# =================================================
# FOOD CLASS
# =================================================
class Food:

    def __init__(self, snake_body):

        self.position = self.generate_position(snake_body)

        # Three food types
        self.type = random.choice([
            "yellow",
            "red",
            "poison"
        ])

        # Timer
        self.spawn_time = pygame.time.get_ticks()

        # Food lifetime
        self.lifetime = random.randint(4000, 7000)

    # -------------------------------------------------
    # Generate position
    # -------------------------------------------------
    def generate_position(self, snake_body):

        while True:

            x = random.randint(
                0,
                (WIDTH // CELL_SIZE) - 1
            ) * CELL_SIZE

            y = random.randint(
                0,
                (HEIGHT // CELL_SIZE) - 1
            ) * CELL_SIZE

            if (x, y) not in snake_body:
                return (x, y)

    # -------------------------------------------------
    # Draw food
    # -------------------------------------------------
    def draw(self):

        x, y = self.position

        center = (
            x + CELL_SIZE // 2,
            y + CELL_SIZE // 2
        )

        # Small yellow food
        if self.type == "yellow":

            pygame.draw.circle(
                screen,
                YELLOW,
                center,
                5
            )

        # Bigger red food
        elif self.type == "red":

            pygame.draw.circle(
                screen,
                RED,
                center,
                8
            )

        # Poison food
        elif self.type == "poison":

            pygame.draw.rect(
                screen,
                BLACK,
                (
                    x + 4,
                    y + 4,
                    CELL_SIZE - 8,
                    CELL_SIZE - 8
                )
            )

    # -------------------------------------------------
    # Check if food expired
    # -------------------------------------------------
    def expired(self):

        current_time = pygame.time.get_ticks()

        return (
            current_time - self.spawn_time
            > self.lifetime
        )

# =================================================
# DRAW GRID
# =================================================
def draw_grid():

    for x in range(0, WIDTH, CELL_SIZE):

        pygame.draw.line(
            screen,
            GRID_COLOR,
            (x, 0),
            (x, HEIGHT)
        )

    for y in range(0, HEIGHT, CELL_SIZE):

        pygame.draw.line(
            screen,
            GRID_COLOR,
            (0, y),
            (WIDTH, y)
        )

# =================================================
# GAME VARIABLES
# =================================================
snake = Snake()

food = Food(snake.body)

score = 0
level = 1

foods_per_level = 3

speed = 8

# =================================================
# MAIN GAME LOOP
# =================================================
running = True

while running:

    screen.fill(BG_COLOR)

    draw_grid()

    # ---------------- EVENTS ----------------
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

    # ---------------- MOVE SNAKE ----------------
    snake.move()

    # ---------------- FOOD TIMER ----------------
    if food.expired():

        food = Food(snake.body)

    # ---------------- EAT FOOD ----------------
    if snake.body[0] == food.position:

        snake.grow = True

        # Yellow food
        if food.type == "yellow":

            score += 1

        # Red food
        elif food.type == "red":

            score += 3

        # Poison
        elif food.type == "poison":

            score -= 2

        # Prevent negative score
        if score < 0:
            score = 0

        # Generate new food
        food = Food(snake.body)

        # Increase level and speed
        if score >= level * foods_per_level:

            level += 1
            speed += 1

    # ---------------- COLLISION CHECK ----------------
    if (
        snake.check_self_collision()
        or
        snake.check_wall_collision()
    ):

        running = False

    # ---------------- DRAW OBJECTS ----------------
    snake.draw()

    food.draw()

    # ---------------- DRAW TEXT ----------------
    score_text = font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    level_text = font.render(
        f"Level: {level}",
        True,
        WHITE
    )

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    # ---------------- UPDATE SCREEN ----------------
    pygame.display.update()

    # Control FPS
    clock.tick(speed)

pygame.quit()
sys.exit()