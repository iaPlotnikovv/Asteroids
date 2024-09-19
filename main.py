import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps= pygame.time.Clock()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers =(updatable)
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

         pygame.display.flip()
        #limit 60 FPS
         dt=fps.tick(60)/1000
         
         


#This line ensures the main() function is only called when this file is run directly; it won't run if it's imported as a module.
if __name__ == "__main__":
    main()