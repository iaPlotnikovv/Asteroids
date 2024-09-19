import pygame
import sys
import time
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps= pygame.time.Clock()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers =(updatable)
    Shot.containers = (shots,updatable,drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asterfield = AsteroidField()
  


    dt = 0

    while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
         screen.fill("purple")

         for obj in drawable:
             obj.draw(screen)

         for obj in updatable:
             obj.update(dt)
            
         for asteroid in asteroids:
           if asteroid.collider_check(player):
               player.game_over(screen)
               
            
         pygame.display.flip()
        #limit 60 FPS
         dt=fps.tick(60)/1000
         
         



#This line ensures the main() function is only called when this file is run directly; it won't run if it's imported as a module.
if __name__ == "__main__":
    main()