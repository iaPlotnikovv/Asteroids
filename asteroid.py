from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):

    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "black", self.position, self.radius,2)


    def update(self,dt):
        self.position += self.velocity * dt 
        if (self.position.x < 0 or self.position.x > 2*SCREEN_WIDTH or
               self.position.y < 0 or self.position.y > 2*SCREEN_HEIGHT):
               self.kill()

      

    def split(self):

        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        angle = random.uniform(20,90)

        first_vector = self.velocity.rotate(angle)
        second_vector =self.velocity.rotate(-angle)

        first_asteroid = Asteroid(self.position.x,self.position.y, new_radius) 
        second_asteroid = Asteroid(self.position.x,self.position.y, new_radius)

        first_asteroid.velocity, second_asteroid.velocity = first_vector*1.5, second_vector*1.5
    