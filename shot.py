from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, 5)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
