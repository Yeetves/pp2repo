import pygame
import random
import sys
import json
import psycopg2

pygame.init()

# Database
conn = psycopg2.connect(
    dbname="SnakePlayers",
    user="postgres",
    password="Skyisover12!",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS players(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS game_sessions(
    id SERIAL PRIMARY KEY,
    player_id INTEGER REFERENCES players(id),
    score INTEGER NOT NULL,
    level_reached INTEGER NOT NULL,
    played_at TIMESTAMP DEFAULT NOW()
)
""")

conn.commit()

# Settings
DEFAULT_SETTINGS = {
    "snake_color": [70, 120, 255],
    "grid": True
}

try:

    with open("settings.json", "r") as file:

        settings = json.load(file)

except:

    settings = DEFAULT_SETTINGS

    with open("settings.json", "w") as file:

        json.dump(settings, file, indent=4)

# Screen
WIDTH, HEIGHT = 800, 600

CELL = 20

PADDING = 2

TOP_PANEL = CELL * 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Calibri", 30)

small_font = pygame.font.SysFont("Calibri", 20)

# Colors
BG = (235, 235, 235)

GRID_LIGHT = (220, 220, 220)

GRID_DARK = (210, 210, 210)

TEXT = (40, 40, 40)

BLUE = (70, 120, 255)

RED = (220, 80, 80)

GREEN = (70, 170, 120)

YELLOW = (255, 200, 70)

POISON = (120, 70, 70)

OBSTACLE_COLOR = (90, 90, 90)

POWER_SPEED = (80, 200, 255)

POWER_SLOW = (255, 180, 80)

POWER_SHIELD = (180, 180, 255)

# Database functions
def get_or_create_player(username):

    cur.execute(
        "SELECT id FROM players WHERE username=%s",
        (username,)
    )

    result = cur.fetchone()

    if result:

        return result[0]

    cur.execute(
        "INSERT INTO players(username) VALUES(%s) RETURNING id",
        (username,)
    )

    conn.commit()

    return cur.fetchone()[0]


def save_game(player_id, score, level):

    cur.execute(
        """
        INSERT INTO game_sessions(
            player_id,
            score,
            level_reached
        )
        VALUES(%s,%s,%s)
        """,
        (player_id, score, level)
    )

    conn.commit()


def get_best(player_id):

    cur.execute(
        """
        SELECT MAX(score)
        FROM game_sessions
        WHERE player_id=%s
        """,
        (player_id,)
    )

    result = cur.fetchone()[0]

    return result if result else 0


def get_top10():

    cur.execute("""
    SELECT
        username,
        score
    FROM game_sessions
    JOIN players
    ON players.id = game_sessions.player_id
    ORDER BY score DESC
    LIMIT 10
    """)

    return cur.fetchall()

# Draw
def draw_text(text, x, y, color=TEXT):

    rendered = font.render(text, True, color)

    screen.blit(rendered, (x, y))


def draw_background():

    for row in range(HEIGHT // CELL):

        for col in range(WIDTH // CELL):

            color = (
                GRID_LIGHT
                if (row + col) % 2 == 0
                else GRID_DARK
            )

            rect = pygame.Rect(
                col * CELL,
                row * CELL,
                CELL,
                CELL
            )

            pygame.draw.rect(screen, color, rect)

            if settings["grid"]:

                pygame.draw.rect(
                    screen,
                    (200, 200, 200),
                    rect,
                    1
                )

# Random free cell
def random_position(snake, obstacles):

    while True:

        x = random.randint(
            0,
            WIDTH // CELL - 1
        ) * CELL

        y = random.randint(
            2,
            HEIGHT // CELL - 1
        ) * CELL

        pos = (x, y)

        if (
            pos not in snake
            and
            pos not in obstacles
        ):

            return pos

# Food
class Food:

    def __init__(self, snake, obstacles):

        self.position = random_position(
            snake,
            obstacles
        )

        self.type = random.choice([
            "yellow",
            "red",
            "poison"
        ])

        self.spawn_time = pygame.time.get_ticks()

        self.lifetime = random.randint(5000, 9000)

    def draw(self):

        x, y = self.position

        center = (
            x + CELL // 2,
            y + CELL // 2
        )

        if self.type == "yellow":

            pygame.draw.circle(
                screen,
                YELLOW,
                center,
                5
            )

        elif self.type == "red":

            pygame.draw.circle(
                screen,
                RED,
                center,
                8
            )

        elif self.type == "poison":

            pygame.draw.rect(
                screen,
                POISON,
                (
                    x + 5,
                    y + 5,
                    CELL - 10,
                    CELL - 10
                )
            )

    def expired(self):

        return (
            pygame.time.get_ticks()
            - self.spawn_time
            > self.lifetime
        )

# Snake
class Snake:

    def __init__(self):

        self.body = [
            (100, 100),
            (80, 100),
            (60, 100)
        ]

        self.direction = (CELL, 0)

        self.next_direction = self.direction

        self.grow = False

    def move(self):

        self.direction = self.next_direction

        head_x, head_y = self.body[0]

        dx, dy = self.direction

        new_head = (
            head_x + dx,
            head_y + dy
        )

        self.body.insert(0, new_head)

        if not self.grow:

            self.body.pop()

        else:

            self.grow = False

    def change_direction(self, dx, dy):

        if (
            (dx, dy)
            !=
            (-self.direction[0], -self.direction[1])
        ):

            self.next_direction = (dx, dy)

    def draw(self):

        color = tuple(settings["snake_color"])

        for block in self.body:

            pygame.draw.rect(
                screen,
                color,
                (
                    block[0] + PADDING,
                    block[1] + PADDING,
                    CELL - PADDING * 2,
                    CELL - PADDING * 2
                )
            )

    def self_collision(self):

        return self.body[0] in self.body[1:]

    def wall_collision(self):

        x, y = self.body[0]

        return (
            x < 0
            or
            x >= WIDTH
            or
            y < TOP_PANEL
            or
            y >= HEIGHT
        )

# Username screen
def username_screen():

    username = ""

    while True:

        screen.fill(BG)

        draw_text(
            "Enter Username",
            260,
            220
        )

        draw_text(
            username,
            260,
            280,
            BLUE
        )

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

            if event.type == pygame.KEYDOWN:

                if (
                    event.key == pygame.K_RETURN
                    and
                    username
                ):

                    return username

                elif event.key == pygame.K_BACKSPACE:

                    username = username[:-1]

                else:

                    username += event.unicode

        pygame.display.flip()

# Main menu
def main_menu():

    options = [
        "Play",
        "Leaderboard",
        "Settings",
        "Quit"
    ]

    selected = 0

    while True:

        screen.fill(BG)

        title = font.render(
            "Snake",
            True,
            TEXT
        )

        screen.blit(title, (350, 120))

        for i, option in enumerate(options):

            color = (
                BLUE
                if i == selected
                else TEXT
            )

            text = font.render(
                option,
                True,
                color
            )

            screen.blit(
                text,
                (340, 220 + i * 55)
            )

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:

                    selected = (
                        selected - 1
                    ) % len(options)

                if event.key == pygame.K_DOWN:

                    selected = (
                        selected + 1
                    ) % len(options)

                if event.key == pygame.K_RETURN:

                    return options[selected]

        pygame.display.flip()

# Leaderboard
def leaderboard_screen():

    data = get_top10()

    while True:

        screen.fill(BG)

        draw_text(
            "Leaderboard",
            280,
            60
        )

        headers = ["#", "Name", "Score"]

        x_positions = [120, 260, 520]

        for i, header in enumerate(headers):

            draw_text(
                header,
                x_positions[i],
                140,
                BLUE
            )

        for i, row in enumerate(data):

            username, score = row

            values = [
                str(i + 1),
                username,
                str(score)
            ]

            for j, value in enumerate(values):

                text = small_font.render(
                    value,
                    True,
                    TEXT
                )

                screen.blit(
                    text,
                    (
                        x_positions[j],
                        190 + i * 35
                    )
                )

        draw_text(
            "ESC - Back",
            300,
            540
        )

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

            if (
                event.type == pygame.KEYDOWN
                and
                event.key == pygame.K_ESCAPE
            ):

                return

        pygame.display.flip()

# Settings
def settings_screen():

    options = [
        "Grid",
        "Snake Color",
        "Save & Back"
    ]

    selected = 0

    colors = [
        [70, 120, 255],
        [255, 80, 80],
        [70, 170, 120],
        [255, 180, 70]
    ]

    while True:

        screen.fill(BG)

        values = [
            str(settings["grid"]),
            str(settings["snake_color"]),
            ""
        ]

        for i, option in enumerate(options):

            color = (
                BLUE
                if i == selected
                else TEXT
            )

            draw_text(
                f"{option} {values[i]}",
                180,
                200 + i * 70,
                color
            )

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:

                    selected = (
                        selected - 1
                    ) % 3

                if event.key == pygame.K_DOWN:

                    selected = (
                        selected + 1
                    ) % 3

                if event.key == pygame.K_RETURN:

                    if selected == 0:

                        settings["grid"] = (
                            not settings["grid"]
                        )

                    elif selected == 1:

                        current = settings["snake_color"]

                        index = colors.index(current)

                        settings["snake_color"] = colors[
                            (index + 1)
                            % len(colors)
                        ]

                    elif selected == 2:

                        with open(
                            "settings.json",
                            "w"
                        ) as file:

                            json.dump(
                                settings,
                                file,
                                indent=4
                            )

                        return

        pygame.display.flip()

# Powerups
def spawn_powerup(snake, obstacles):

    if random.random() < 0.01:

        power = random.choice([
            "speed",
            "slow",
            "shield"
        ])

        position = random_position(
            snake,
            obstacles
        )

        return power, position

    return None, None

# Game over
def game_over_screen(score, level, best):

    options = [
        "Retry",
        "Menu"
    ]

    selected = 0

    while True:

        screen.fill(BG)

        draw_text(
            "Game Over",
            280,
            120,
            RED
        )

        draw_text(
            f"Score: {score}",
            280,
            220
        )

        draw_text(
            f"Level: {level}",
            280,
            270
        )

        draw_text(
            f"Best: {best}",
            280,
            320
        )

        for i, option in enumerate(options):

            color = (
                BLUE
                if i == selected
                else TEXT
            )

            draw_text(
                option,
                320,
                420 + i * 60,
                color
            )

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:

                    selected = (
                        selected - 1
                    ) % 2

                if event.key == pygame.K_DOWN:

                    selected = (
                        selected + 1
                    ) % 2

                if event.key == pygame.K_RETURN:

                    return options[selected]

        pygame.display.flip()

# Game
def game(player_id, best_score):

    snake = Snake()

    score = 0

    level = 1

    base_speed = 8

    speed = base_speed

    obstacles = []

    food = Food(
        snake.body,
        obstacles
    )

    shield_active = False

    powerup = None

    power_pos = None

    power_spawn = 0

    effect = None

    effect_end = 0

    while True:

        draw_background()

        pygame.draw.rect(
            screen,
            BG,
            (0, 0, WIDTH, TOP_PANEL)
        )

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:

                    snake.change_direction(0, -CELL)

                elif event.key == pygame.K_DOWN:

                    snake.change_direction(0, CELL)

                elif event.key == pygame.K_LEFT:

                    snake.change_direction(-CELL, 0)

                elif event.key == pygame.K_RIGHT:

                    snake.change_direction(CELL, 0)

        snake.move()

        head = snake.body[0]

        collision = (
            snake.wall_collision()
            or
            snake.self_collision()
            or
            head in obstacles
        )

        if collision:

            if shield_active:

                shield_active = False

            else:

                save_game(
                    player_id,
                    score,
                    level
                )

                return score, level

        if food.expired():

            food = Food(
                snake.body,
                obstacles
            )

        if head == food.position:

            if food.type == "yellow":

                snake.grow = True

                score += 1

            elif food.type == "red":

                snake.grow = True

                score += 3

            elif food.type == "poison":

                if len(snake.body) <= 2:

                    save_game(
                        player_id,
                        score,
                        level
                    )

                    return score, level

                snake.body = snake.body[:-2]

            if score >= level * 5:

                level += 1

                speed += 2

                if level >= 3:

                    for _ in range(3):

                        obstacle = random_position(
                            snake.body,
                            obstacles
                        )

                        obstacles.append(obstacle)

            food = Food(
                snake.body,
                obstacles
            )

        if powerup is None:

            powerup, power_pos = spawn_powerup(
                snake.body,
                obstacles
            )

            if powerup:

                power_spawn = pygame.time.get_ticks()

        if (
            powerup
            and
            pygame.time.get_ticks()
            - power_spawn
            > 8000
        ):

            powerup = None

        if powerup and head == power_pos:

            if powerup == "speed":

                speed += 5

                effect_end = (
                    pygame.time.get_ticks()
                    + 5000
                )

            elif powerup == "slow":

                speed = max(5, speed - 4)

                effect_end = (
                    pygame.time.get_ticks()
                    + 5000
                )

            elif powerup == "shield":

                shield_active = True

            effect = powerup

            powerup = None

        if (
            effect
            and
            pygame.time.get_ticks()
            > effect_end
        ):

            speed = (
                base_speed
                + (level - 1) * 2
            )

            effect = None

        snake.draw()

        food.draw()

        for obstacle in obstacles:

            pygame.draw.rect(
                screen,
                OBSTACLE_COLOR,
                (
                    obstacle[0],
                    obstacle[1],
                    CELL,
                    CELL
                )
            )

        if powerup:

            color = {
                "speed": POWER_SPEED,
                "slow": POWER_SLOW,
                "shield": POWER_SHIELD
            }[powerup]

            pygame.draw.rect(
                screen,
                color,
                (
                    power_pos[0] + 4,
                    power_pos[1] + 4,
                    CELL - 8,
                    CELL - 8
                )
            )

        score_text = small_font.render(
            f"Score: {score}",
            True,
            TEXT
        )

        level_text = small_font.render(
            f"Level: {level}",
            True,
            TEXT
        )

        best_text = small_font.render(
            f"Best: {best_score}",
            True,
            TEXT
        )

        screen.blit(score_text, (10, 10))

        screen.blit(level_text, (130, 10))

        screen.blit(best_text, (240, 10))

        pygame.display.flip()

        clock.tick(speed)

# Main
username = username_screen()

player_id = get_or_create_player(
    username
)

while True:

    best_score = get_best(player_id)

    choice = main_menu()

    if choice == "Play":

        score, level = game(
            player_id,
            best_score
        )

        action = game_over_screen(
            score,
            level,
            max(best_score, score)
        )

        if action == "Retry":

            continue

    elif choice == "Leaderboard":

        leaderboard_screen()

    elif choice == "Settings":

        settings_screen()

    elif choice == "Quit":

        break

pygame.quit()

sys.exit()