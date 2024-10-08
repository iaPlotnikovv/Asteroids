import pygame
import time
import sys
from circleshape import *
from constants import *
from shot import *


class Player(CircleShape):
    
    #hitbox
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation=0
        self.cooldown_timer = 0
    #real look
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,"green",self.triangle(),2)
    
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt        
    
    def rotate(self,dt):
        self.rotation+=PLAYER_TURN_SPEED*dt

    
    def update(self, dt):
        if self.cooldown_timer <=0 :
            self.cooldown_timer = 0
        else:
            self.cooldown_timer-= dt 
       
        keys = pygame.key.get_pressed()

        
        if keys[pygame.K_SPACE]:
             if self.cooldown_timer >0:
              pass
             else:
                 self.shoot(dt)
             
        
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        #Adding boarders
        self.position.x = max(min(self.position.x, SCREEN_WIDTH - self.radius), self.radius)
        self.position.y = max(min(self.position.y, SCREEN_HEIGHT - self.radius), self.radius)


    def shoot(self,dt): 
        shot = Shot(self.position)
        shot_vector = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_SHOT_SPEED
        shot.velocity = shot_vector 
        self.cooldown_timer = PLAYER_SHOOT_COOLDOWN

    def game_over(self,screen):
        font = pygame.font.SysFont("Arial", 52)
        screen.fill((0,0,0))
        text_surface = font.render("GAME OVER", True, (255, 0, 0), "BLACK")  # Red text
        screen.blit(text_surface, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        pygame.display.flip()
        time.sleep(3)

        pygame.quit()
        sys.exit("GAME OVER !")

    def cooldown_msg (self,screen):
        font = pygame.font.SysFont("Arial", 18)
        if self.cooldown_timer > 0:
            cooldown_text = f"      {self.cooldown_timer:.1f}s"
            text_surface = font.render(cooldown_text, True, (255, 255, 0), None)
            screen.blit(text_surface, (self.position.x, self.position.y))  # Fixed position
            pygame.display.flip()
    
    