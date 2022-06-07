# RPG

import pygame
from sys import exit

def main():
    pygame.init()
    width=800
    height=600
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("RPG")
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    pygame.display.update()
    pygame.time.delay(10)


main()