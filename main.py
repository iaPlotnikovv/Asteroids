import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
         open_window(screen)

def open_window(screen):
        screen.fill("black")
        pygame.display.flip()

#This line ensures the main() function is only called when this file is run directly; it won't run if it's imported as a module.
if __name__ == "__main__":
    main()