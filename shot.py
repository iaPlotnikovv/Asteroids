from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self,position):
        super().__init__(position.x,position.y,SHOT_RADIUS)
        self.position = pygame.Vector2(position.x,position.y)
        self.rotation = 0
        

    def draw(self,screen):
        pygame.draw.circle(screen, "red", self.position, self.radius,2)


    def update(self,dt):
        self.position += self.velocity * dt 
        
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or
               self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
               self.kill()
      