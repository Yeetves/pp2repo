import pygame
import sys
import math
from collections import deque
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 1200, 700
TOOLBAR_H = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Modern Paint")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE  = (0, 0, 255)
YELLOW = (255, 220, 0)
PURPLE = (180, 0, 255)
BG    = (245, 245, 245)
PANEL = (225, 225, 225)
BTN   = (250, 250, 250)
BTN_ON = (120, 170, 255)
BORDER = (170, 170, 170)

PALETTE = [BLACK, RED, GREEN, BLUE, YELLOW, PURPLE]
BRUSH_SIZES = {"small": 2, "medium": 5, "large": 10}

MODES = ["draw", "line", "rect", "circle", "erase", "fill",
         "text", "square", "r_triangle", "e_triangle", "rhombus"]
LABELS = {
    "draw": "Pencil", "line": "Line", "rect": "Rect",
    "circle": "Circle", "erase": "Erase", "fill": "Fill",
    "text": "Text", "square": "Square", "r_triangle": "R-Tri",
    "e_triangle": "E-Tri", "rhombus": "Rhomb"
}

# Precompute button rects so we don't recalculate in draw AND in events
MODE_RECTS = {
    m: pygame.Rect(350 + (i % 6) * 110, 10 + (i // 6) * 45, 100, 35)
    for i, m in enumerate(MODES)
}
SIZE_RECTS = {
    "small":  pygame.Rect(30,  65, 55, 28),
    "medium": pygame.Rect(100, 65, 55, 28),
    "large":  pygame.Rect(170, 65, 55, 28),
}

canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_H))
canvas.fill(WHITE)

font = pygame.font.SysFont("Arial", 28)
small_font = pygame.font.SysFont("Arial", 18)

# App state
cur_color = BLACK
brush_size = BRUSH_SIZES["medium"]
mode = "draw"
drawing = False
start_pos = last_pos = None
text_mode = False
text_pos = (0, 0)
text_input = ""


def flood_fill(surface, x, y, new_color):
    old_color = surface.get_at((x, y))
    if old_color == (*new_color, 255):
        return
    w, h = surface.get_size()
    q = deque([(x, y)])
    while q:
        px, py = q.popleft()
        if not (0 <= px < w and 0 <= py < h):
            continue
        if surface.get_at((px, py)) != old_color:
            continue
        surface.set_at((px, py), new_color)
        q.extend([(px+1, py), (px-1, py), (px, py+1), (px, py-1)])


def save_canvas():
    name = f"painting_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
    pygame.image.save(canvas, name)
    print(f"Saved: {name}")


def draw_shape(surf, shape, start, end, color, thick):
    sx, sy = start
    ex, ey = end

    if shape == "line":
        pygame.draw.line(surf, color, start, end, thick)

    elif shape == "rect":
        pygame.draw.rect(surf, color,
                         pygame.Rect(sx, sy, ex - sx, ey - sy), thick)

    elif shape in ("circle", "square"):
        size = min(abs(ex - sx), abs(ey - sy))
        x = sx - size if ex < sx else sx
        y = sy - size if ey < sy else sy
        r = pygame.Rect(x, y, size, size)
        if shape == "circle":
            pygame.draw.ellipse(surf, color, r, thick)
        else:
            pygame.draw.rect(surf, color, r, thick)

    elif shape == "r_triangle":
        pygame.draw.polygon(surf, color, [start, (sx, ey), end], thick)

    elif shape == "e_triangle":
        size = min(abs(ex - sx), abs(ey - sy))
        x = sx - size if ex < sx else sx
        y = sy - size if ey < sy else sy
        pts = [(x + size//2, y), (x, y + size), (x + size, y + size)]
        pygame.draw.polygon(surf, color, pts, thick)

    elif shape == "rhombus":
        cx = (sx + ex) // 2
        cy = (sy + ey) // 2
        hw = abs(ex - sx) // 2
        hh = abs(ey - sy) // 2
        pygame.draw.polygon(surf, color,
                            [(cx, cy-hh), (cx+hw, cy), (cx, cy+hh), (cx-hw, cy)], thick)


def draw_ui():
    pygame.draw.rect(screen, PANEL, (0, 0, WIDTH, TOOLBAR_H))

    for i, color in enumerate(PALETTE):
        cx = 30 + i * 50
        pygame.draw.circle(screen, color, (cx, 35), 15)
        if color == cur_color:
            pygame.draw.circle(screen, WHITE, (cx, 35), 20, 3)

    for m, rect in MODE_RECTS.items():
        c = BTN_ON if mode == m else BTN
        pygame.draw.rect(screen, c, rect, border_radius=10)
        pygame.draw.rect(screen, BORDER, rect, 2, border_radius=10)
        lbl = small_font.render(LABELS[m], True, BLACK)
        screen.blit(lbl, lbl.get_rect(center=rect.center))

    for name, rect in SIZE_RECTS.items():
        c = BTN_ON if brush_size == BRUSH_SIZES[name] else BTN
        pygame.draw.rect(screen, c, rect, border_radius=8)
        pygame.draw.rect(screen, BORDER, rect, 2, border_radius=8)
        key = {"small": "1", "medium": "2", "large": "3"}[name]
        screen.blit(small_font.render(key, True, BLACK), (rect.x + 22, rect.y + 5))

    screen.blit(small_font.render("Ctrl+S = Save", True, BLACK), (1100, 15))


# Main loop
running = True
while running:
    screen.fill(BG)
    screen.blit(canvas, (0, TOOLBAR_H))
    draw_ui()

    # Live shape preview
    shape_modes = {"line", "rect", "circle", "square",
                   "r_triangle", "e_triangle", "rhombus"}
    if drawing and start_pos and mode in shape_modes:
        preview = canvas.copy()
        mx, my = pygame.mouse.get_pos()
        draw_shape(preview, mode, start_pos, (mx, my - TOOLBAR_H),
                   cur_color, brush_size)
        screen.blit(preview, (0, TOOLBAR_H))

    if text_mode:
        ts = font.render(text_input, True, cur_color)
        screen.blit(ts, (text_pos[0], text_pos[1] + TOOLBAR_H))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                save_canvas()
            if event.key == pygame.K_1: brush_size = BRUSH_SIZES["small"]
            if event.key == pygame.K_2: brush_size = BRUSH_SIZES["medium"]
            if event.key == pygame.K_3: brush_size = BRUSH_SIZES["large"]

            if text_mode:
                if event.key == pygame.K_RETURN:
                    canvas.blit(font.render(text_input, True, cur_color), text_pos)
                    text_input = ""
                    text_mode = False
                elif event.key == pygame.K_ESCAPE:
                    text_input = ""
                    text_mode = False
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            for i, color in enumerate(PALETTE):
                if math.hypot(x - (30 + i*50), y - 35) <= 15:
                    cur_color = color

            for name, rect in SIZE_RECTS.items():
                if rect.collidepoint(event.pos):
                    brush_size = BRUSH_SIZES[name]

            for m, rect in MODE_RECTS.items():
                if rect.collidepoint(event.pos):
                    mode = m

            if y > TOOLBAR_H:
                canvas_pos = (x, y - TOOLBAR_H)
                if mode == "fill":
                    flood_fill(canvas, *canvas_pos, cur_color)
                elif mode == "text":
                    text_mode, text_pos, text_input = True, canvas_pos, ""
                else:
                    drawing = True
                    start_pos = last_pos = canvas_pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end = (event.pos[0], event.pos[1] - TOOLBAR_H)
                if mode in shape_modes:
                    draw_shape(canvas, mode, start_pos, end, cur_color, brush_size)
            drawing = False

        elif event.type == pygame.MOUSEMOTION and drawing:
            if event.pos[1] > TOOLBAR_H:
                cur = (event.pos[0], event.pos[1] - TOOLBAR_H)
                if mode == "draw":
                    pygame.draw.line(canvas, cur_color, last_pos, cur, brush_size)
                elif mode == "erase":
                    pygame.draw.line(canvas, WHITE, last_pos, cur, brush_size * 2)
                last_pos = cur

    pygame.display.flip()
    clock.tick(144)

pygame.quit()
sys.exit()
