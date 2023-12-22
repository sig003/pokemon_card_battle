import pygame
from constants import WHITE, BLACK, SCREEN_SIZE, GREY

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Pokemon Card Battle!!')
clock = pygame.time.Clock()

img1 = pygame.image.load('images/1.png')
img1 = pygame.transform.scale(img1, (370, 600))

img2 = pygame.image.load('images/2.png')
img2 = pygame.transform.scale(img2, (300, 550))

while True:
    screen.fill(WHITE)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    pygame.draw.line(screen, BLACK, (SCREEN_SIZE[0]//4, 0), (SCREEN_SIZE[0]//4, SCREEN_SIZE[1]), 1)
    pygame.draw.line(screen, BLACK, (SCREEN_SIZE[0]*3//4, 0), (SCREEN_SIZE[0]*3//4, SCREEN_SIZE[1]), 1)

    pygame.draw.line(screen, BLACK, (0, 300), (SCREEN_SIZE[0]//4, 300), 1)
    pygame.draw.line(screen, BLACK, (SCREEN_SIZE[0]*3//4, 300), (SCREEN_SIZE[0], 300), 1)

    #screen.blit(img1, (40, 400))
    screen.blit(img1, (0, 350))
    screen.blit(img2, (1170, 370))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
