import pygame
import GenerateTiling

pygame.init()

width = 600
height = 600
scale = 50

screen = pygame.display.set_mode((width, height))

colors = [[255, 255, 255],
          [255, 000, 000],
          [000, 255, 000],
          [000, 000, 255]]


def isometricCoords(x, y, z):
    coords = [width/2, height/2]
    coords[0] += x * scale * 0.866
    coords[0] -= y * scale * 0.866
    coords[1] += x * scale * 0.5
    coords[1] += y * scale * 0.5
    coords[1] -= z * scale
    return [int(coords[0]), int(coords[1])]


def drawTops(screen, heights):
    for x in range(len(heights)):
        for y in range(len(heights[x])):
            coords = isometricCoords(x, y, heights[x][y])
            rect = (coords[0]-10, coords[1]-10, 20, 20)
            pygame.draw.rect(screen, colors[1], rect)


heights = GenerateTiling.randomConfig()

screen.fill((colors[0]))
drawTops(screen, heights)

flag = True

while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                flag = False

    pygame.display.flip()

pygame.quit()
