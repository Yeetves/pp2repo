import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BG = (237, 235, 235)

colors = [BLACK, RED, GREEN, BLUE]
current_color = BLACK


mode = "draw" #initial mode


brush_size = 7

drawing = False
start_pos = None


screen.fill(BG)

def draw_ui():
    for i, color in enumerate(colors):
        pygame.draw.rect(screen, color, (10 + i*40, 10, 30, 30))

    font = pygame.font.SysFont(None, 24)

    modes = ["draw", "rect", "circle", "erase"]
    for i, m in enumerate(modes):
        text = font.render(m, True, BLACK)
        screen.blit(text, (10 + i*80, 50))


running = True
while running:
    draw_ui()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

            x, y = event.pos

            for i, color in enumerate(colors):
                if 10 + i*40 < x < 40 + i*40 and 10 < y < 40:   
                    current_color = color

            modes = ["draw", "rect", "circle", "erase"]
            for i, m in enumerate(modes):
                if 10 + i*80 < x < 70 + i*80 and 50 < y < 80:
                    mode = m

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            if mode == "rect":
                end_pos = event.pos
                rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))  
                pygame.draw.rect(screen, current_color, rect, 4)

            if mode == "circle":
                end_pos = event.pos
                radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2) ** 0.5) 
                pygame.draw.circle(screen, current_color, start_pos, radius, 4)

        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "draw":
                pygame.draw.circle(screen, current_color, event.pos, brush_size) 

            if mode == "erase":
                pygame.draw.circle(screen, BG, event.pos, brush_size * 4)

    pygame.display.flip()
    clock.tick(200)

pygame.quit()
sys.exit()