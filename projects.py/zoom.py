import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My new PyGame")

clock = pygame.time.Clock()

x = 50
y = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break
        if event.type == pygame.KEYDOWN:
            # Move on the Y-Axis (Up/Down)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y += 10
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                y -= 10

            # Move on X-Axis (Left/Right)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x -= 10
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x += 10

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 50, 50))
    pygame.display.flip()

    clock.tick(60)