import pygame
import sys
import math

pygame.init()

# =================================================
# SCREEN SETTINGS
# =================================================
WIDTH, HEIGHT = 1000, 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Modern Paint")

clock = pygame.time.Clock()

# =================================================
# COLORS
# =================================================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)

BG = (245, 245, 245)

PANEL = (225, 225, 225)
BUTTON = (250, 250, 250)
BUTTON_ACTIVE = (120, 170, 255)

BORDER = (170, 170, 170)

colors = [BLACK, RED, GREEN, BLUE]

current_color = BLACK

# =================================================
# DRAWING SETTINGS
# =================================================
mode = "draw"

brush_size = 6

drawing = False

start_pos = None

# Fill background
screen.fill(BG)

# =================================================
# DRAW USER INTERFACE
# =================================================
def draw_ui():

    # Top panel
    pygame.draw.rect(screen, PANEL, (0, 0, WIDTH, 90))

    # ---------- COLOR BUTTONS ----------
    for i, color in enumerate(colors):

        x = 30 + i * 50
        y = 30

        pygame.draw.circle(
            screen,
            color,
            (x, y),
            15
        )

        # Highlight selected color
        if color == current_color:

            pygame.draw.circle(
                screen,
                WHITE,
                (x, y),
                19,
                3
            )

    # ---------- MODE BUTTONS ----------
    font = pygame.font.SysFont("Arial", 18)

    modes = [
        "draw",
        "rect",
        "circle",
        "erase",
        "square",
        "r_triangle",
        "e_triangle",
        "rhombus"
    ]

    labels = {
        "draw": "Draw",
        "rect": "Rect",
        "circle": "Circle",
        "erase": "Erase",
        "square": "Square",
        "r_triangle": "R-Tri",
        "e_triangle": "E-Tri",
        "rhombus": "Rhomb"
    }

    for i, m in enumerate(modes):

        button_x = 260 + i * 85
        button_y = 20

        # Active mode button
        if mode == m:
            color = BUTTON_ACTIVE
        else:
            color = BUTTON

        # Button body
        pygame.draw.rect(
            screen,
            color,
            (button_x, button_y, 75, 40),
            border_radius=12
        )

        # Button border
        pygame.draw.rect(
            screen,
            BORDER,
            (button_x, button_y, 75, 40),
            2,
            border_radius=12
        )

        # Button text
        text = font.render(labels[m], True, BLACK)

        text_rect = text.get_rect(
            center=(button_x + 37, button_y + 20)
        )

        screen.blit(text, text_rect)

# =================================================
# MAIN LOOP
# =================================================
running = True

while running:

    draw_ui()

    for event in pygame.event.get():

        # ---------------- QUIT ----------------
        if event.type == pygame.QUIT:
            running = False

        # =================================================
        # MOUSE BUTTON DOWN
        # =================================================
        if event.type == pygame.MOUSEBUTTONDOWN:

            drawing = True

            start_pos = event.pos

            x, y = event.pos

            # ---------- COLOR SELECTION ----------
            for i, color in enumerate(colors):

                circle_x = 30 + i * 50
                circle_y = 30

                distance = (
                    (x - circle_x) ** 2
                    +
                    (y - circle_y) ** 2
                ) ** 0.5

                if distance <= 15:

                    current_color = color

            # ---------- MODE SELECTION ----------
            modes = [
                "draw",
                "rect",
                "circle",
                "erase",
                "square",
                "r_triangle",
                "e_triangle",
                "rhombus"
            ]

            for i, m in enumerate(modes):

                button_x = 260 + i * 85
                button_y = 20

                if (
                    button_x < x < button_x + 75
                    and
                    button_y < y < button_y + 40
                ):

                    mode = m

        # =================================================
        # MOUSE BUTTON UP
        # =================================================
        if event.type == pygame.MOUSEBUTTONUP:

            drawing = False

            end_pos = event.pos

            # -------------------------------------------------
            # RECTANGLE
            # -------------------------------------------------
            if mode == "rect":

                rect = pygame.Rect(
                    start_pos,
                    (
                        end_pos[0] - start_pos[0],
                        end_pos[1] - start_pos[1]
                    )
                )

                pygame.draw.rect(
                    screen,
                    current_color,
                    rect,
                    4
                )

            # -------------------------------------------------
            # CIRCLE
            # -------------------------------------------------
            if mode == "circle":

                # Square size
                size = min(
                    abs(end_pos[0] - start_pos[0]),
                    abs(end_pos[1] - start_pos[1])
                )

                # Determine drawing direction
                x = start_pos[0]
                y = start_pos[1]

                if end_pos[0] < start_pos[0]:
                    x -= size

                if end_pos[1] < start_pos[1]:
                    y -= size

                # Bounding square
                rect = pygame.Rect(x, y, size, size)

                # Draw circle inside square
                pygame.draw.ellipse(
                    screen,
                    current_color,
                    rect,
                    4
                )

            # -------------------------------------------------
            # SQUARE
            # -------------------------------------------------
            if mode == "square":

                side = min(
                    abs(end_pos[0] - start_pos[0]),
                    abs(end_pos[1] - start_pos[1])
                )

                rect = pygame.Rect(
                    start_pos[0],
                    start_pos[1],
                    side,
                    side
                )

                pygame.draw.rect(
                    screen,
                    current_color,
                    rect,
                    4
                )

            # -------------------------------------------------
            # RIGHT TRIANGLE
            # -------------------------------------------------
            if mode == "r_triangle":

                points = [
                    start_pos,
                    (start_pos[0], end_pos[1]),
                    end_pos
                ]

                pygame.draw.polygon(
                    screen,
                    current_color,
                    points,
                    4
                )

            # -------------------------------------------------
            # EQUILATERAL TRIANGLE
            # -------------------------------------------------
            if mode == "e_triangle":

    # Square size
                size = min(
                    abs(end_pos[0] - start_pos[0]),
                    abs(end_pos[1] - start_pos[1])
                )

                # Determine direction
                x = start_pos[0]
                y = start_pos[1]

                if end_pos[0] < start_pos[0]:
                    x -= size

                if end_pos[1] < start_pos[1]:
                    y -= size

                # Triangle points inside square
                points = [
                    (x + size // 2, y),           # top
                    (x, y + size),                # bottom left
                    (x + size, y + size)          # bottom right
                ]

                pygame.draw.polygon(
                    screen,
                    current_color,
                    points,
                    4
                )

            # -------------------------------------------------
            # RHOMBUS
            # -------------------------------------------------
            if mode == "rhombus":

                center_x = (start_pos[0] + end_pos[0]) // 2
                center_y = (start_pos[1] + end_pos[1]) // 2

                width = abs(end_pos[0] - start_pos[0])
                height = abs(end_pos[1] - start_pos[1])

                points = [
                    (center_x, center_y - height // 2),
                    (center_x + width // 2, center_y),
                    (center_x, center_y + height // 2),
                    (center_x - width // 2, center_y)
                ]

                pygame.draw.polygon(
                    screen,
                    current_color,
                    points,
                    4
                )

        # =================================================
        # DRAW / ERASE
        # =================================================
        if event.type == pygame.MOUSEMOTION and drawing:

            # Prevent drawing over UI panel
            if event.pos[1] > 90:

                # Free drawing
                if mode == "draw":

                    pygame.draw.circle(
                        screen,
                        current_color,
                        event.pos,
                        brush_size
                    )

                # Eraser
                if mode == "erase":

                    pygame.draw.circle(
                        screen,
                        BG,
                        event.pos,
                        brush_size * 4
                    )

    # Update screen
    pygame.display.flip()

    # FPS
    clock.tick(200)

pygame.quit()
sys.exit()