import pygame
import sys
import random

pygame.init()


size = width, height = 500, 500

screen = pygame.display.set_mode(size)

class Ball():
    pos = []
    vel = [0, 0]


c = [[[100, 100, 100] for i in range(11)] for j in range(11)]

rate_of_change = 7
mode = 2



while True:
    screen.fill([255, 255, 255])

    for i in range(11):
        for j in range(11):
            for k in range(3):
                val = c[i][j][k]
                val += random.randint(-rate_of_change, rate_of_change)
                if val > 255:
                    val = 255
                if val < 0:
                    val = 0
                c[i][j][k] = val
            
            if mode > 3:
                pygame.draw.line(screen, c[(13 + i)%10][(7+j)%10], [i*50, j*50+24], [i*50+49, j*50+24], 50)
            if mode > 2:
                pygame.draw.circle(screen, c[10-i][j], [i*50+25, j*50], 25, 1)
                pygame.draw.circle(screen, c[i][10-j], [i*50, j*50+25], 25, 1)
            if mode > 1:
                pygame.draw.circle(screen, c[10-i][10-j], [i*50+25, j*50+25], 25, 1)
            if mode > 0:
                pygame.draw.circle(screen, c[i][j], [i*50, j*50], 25, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key >= pygame.K_0 and event.key <= pygame.K_9:
                mode = event.key - pygame.K_0
    
    pygame.display.flip()