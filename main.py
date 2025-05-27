import sys
import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables  = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Player.containers = (updatables, drawables)
    Shot.containers = (updatables, drawables, shots)
    
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        clock.tick(60)
        updatables.update(dt)
        
        for drawable in drawables:
            drawable.draw(screen)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot) == True:
                    asteroid.split()
                    shot.kill()
            if player.collision(asteroid) == True:
                sys.exit("Game Over!")
        
        dt = clock.get_time() / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
