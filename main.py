import sys
import pygame
import pygame_menu
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from startmenu import StartMenu

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg = pygame.image.load("Images/galaxy_background.jpg")
    clock = pygame.time.Clock()
    dt = 0

    game_running = False
    player = None

    updatables  = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, shots)
    
    asteroidfield = AsteroidField()

    while True:

        if game_running == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            screen.blit(bg, (0, 0))
            clock.tick(60)
            updatables.update(dt)

            menu = StartMenu("Asteroids!", SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4, theme=pygame_menu.themes.THEME_DARK)
            menu.mainloop(screen)

            for asteroid in asteroids:
                asteroid.draw(screen)

            dt = clock.get_time() / 1000
            pygame.display.flip()

        elif game_running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            screen.blit(bg, (0, 0))
            clock.tick(60)
            updatables.update(dt)

            if game_running == True:
                Player.containers = (updatables, drawables)
                if player == None:
                    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        
            for drawable in drawables:
                drawable.draw(screen)
            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collision(shot) == True:
                        asteroid.split()
                        shot.kill()
                if player.collision(asteroid) == True:
                    #sys.exit("Game Over!")
                    game_running = False
        
            dt = clock.get_time() / 1000
            pygame.display.flip()



    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
