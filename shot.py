import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)  # Call parent with only x, y, radius
        self.velocity = velocity  # Set velocity after parent init
    
    def update(self, dt):  # Implement required update method
        self.position += self.velocity * dt
    
    def draw(self, screen):  # Implement required draw method
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)