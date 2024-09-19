import pygame
import time
import sys
from circleshape import *
from constants import *


class Player(CircleShape):
    #hitbox
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation=0
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
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

    def game_over(self,screen):
        font = pygame.font.SysFont("Arial", 52)
        screen.fill((0,0,0))
        text_surface = font.render("GAME OVER", True, (255, 0, 0), "BLACK")  # Red text
        screen.blit(text_surface, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        pygame.display.flip()
        time.sleep(3)

        pygame.quit()
        sys.exit("GAME OVER !")