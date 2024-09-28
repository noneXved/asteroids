# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    while 1:           
        pygame.init()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.update()
        
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

if __name__ == "__main__":
    main()
