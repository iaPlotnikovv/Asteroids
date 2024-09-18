import pygame
from constants import *
from player import *


def main():
    pygame.init()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    fps= pygame.time.Clock()
    dt = 0

    while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
         game_window(screen,player)
         dt=fps.tick(60)/1000
        

def game_window(screen, player):
        screen.fill("purple")
        player.draw(screen)
        pygame.display.flip()

#This line ensures the main() function is only called when this file is run directly; it won't run if it's imported as a module.
if __name__ == "__main__":
    main()