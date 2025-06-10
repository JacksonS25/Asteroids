from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, vector):
        super().__init__(0, 0, SHOT_RADIUS)

        self.position = vector

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255, 255, 255), self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt