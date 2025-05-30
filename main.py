import sys
import pygame
import pygame_menu
import pygame_widgets
from pygame_widgets.progressbar import ProgressBar
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
#from startmenu import StartMenu

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print(f"======== Game Start ========")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg = pygame.image.load("Images/galaxy_background.jpg")
    clock = pygame.time.Clock()
    dt = 0

    game_running = True
    player = None
    points = 0
    charge = 0

    font = pygame.font.SysFont("monospace", 15)

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
            raise Exception("game_running set to False")
            player = None
            Player.containers = ()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            screen.blit(bg, (0, 0))
            clock.tick(60)
            updatables.update(dt)

            for drawable in drawables:
                drawable.draw(screen)

            menu = StartMenu("Asteroids!", SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4, theme=pygame_menu.themes.THEME_DARK)
            menu.mainloop(screen)

            dt = clock.get_time() / 1000
            pygame.display.flip()

        elif game_running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            screen.blit(bg, (0, 0))
            clock.tick(60)
            updatables.update(dt)

            points_text = font.render(f"Points: {points}", 1, (255,255,255))
            screen.blit(points_text, (50, 50))

            if charge >= 50:
                ultimate_text = font.render("Ultimate Ready!", 1, (0,200,0))
                screen.blit(ultimate_text, (50, 75))

            Player.containers = (updatables, drawables)
            if player == None:
                player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        
            for drawable in drawables:
                drawable.draw(screen)
            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collision(shot) == True:
                        asteroid.split()
                        points += 10
                        charge += 1
                        shot.kill()
                if player.collision(asteroid) == True:
                    print(f"Your got {points} points!")
                    points = 0
                    sys.exit("======== Game Over! ========")
                    #game_running = False
        
            dt = clock.get_time() / 1000
            pygame.display.flip()



    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
