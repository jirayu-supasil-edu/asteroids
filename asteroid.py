from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            surface=screen,
            color="red",
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH
        )
    
    def update(self, dt:float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle: float = random.uniform(20, 50)
        radius: float = self.radius - ASTEROID_MIN_RADIUS
        x: float = self.position.x
        y: float = self.position.y
        asteroid_a = Asteroid(x, y, radius)
        asteroid_b = Asteroid(x, y, radius)

        asteroid_a.velocity = self.velocity.rotate(angle) * 1.2
        asteroid_b.velocity = self.velocity.rotate(-angle) * 1.2


