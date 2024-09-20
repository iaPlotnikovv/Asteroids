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
    background_image = pygame.image.load('back.jpg')
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
            
         for obj in updatable:
             obj.update(dt)  
         
         
         for asteroid in asteroids:
           if asteroid.collider_check(player):
               player.game_over(screen)
           for shot in shots:
               if asteroid.collider_check(shot):
                   asteroid.split()
                   shot.kill()
               


        #  screen.fill("purple")
           screen.blit(background_image,(0,0))

         for obj in drawable:
             obj.draw(screen)

         player.cooldown_msg(screen)

        #  print(player.cooldown_timer)   
         pygame.display.flip()
        #limit 60 FPS
         dt=fps.tick(60)/1000
         
         



#This line ensures the main() function is only called when this file is run directly; it won't run if it's imported as a module.
if __name__ == "__main__":
    main()