import pygame
import sys
from constants import WHITE, BLACK, SCREEN_SIZE

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Pokemon Card Battle!!')
clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    pygame.draw.line(screen, BLACK, (SCREEN_SIZE[0]//4, 0), (SCREEN_SIZE[0]//4, SCREEN_SIZE[1]), 1)
    pygame.draw.line(screen, BLACK, (SCREEN_SIZE[0]*3//4, 0), (SCREEN_SIZE[0]*3//4, SCREEN_SIZE[1]), 1)

    pygame.draw.line(screen, BLACK, (0, 300), (SCREEN_SIZE[0]//4, 300), 1)
    pygame.draw.line(screen, BLACK, (SCREEN_SIZE[0]*3//4, 300), (SCREEN_SIZE[0], 300), 1)

    pygame.draw.rect(screen, BLACK, (100, 100, 200, 150))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
