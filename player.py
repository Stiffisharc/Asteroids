import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
            if self.position.x < 0:
                self.position.x = 1300
            if self.position.x > 1300:
                self.position.x = 0
            if self.position.y < 0:
                self.position.y = 750
            if self.position.y > 750:
                self.position.y = 0
        if keys[pygame.K_s]:
            self.move(-dt)
            if self.position.x < 0:
                self.position.x = 1300
            if self.position.x > 1300:
                self.position.x = 0
            if self.position.y < 0:
                self.position.y = 750
            if self.position.y > 750:
                self.position.y = 0
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN
        if keys[pygame.K_LALT]:
            #ultimate attack goes here
            pass

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position[0], self.position[1])
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.timer = 100

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
        self.position += self.velocity * dt
        if self.position.x < 0:
            self.position.x = 1300
        if self.position.x > 1300:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = 750
        if self.position.y > 750:
            self.position.y = 0
