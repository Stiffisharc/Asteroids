import sys
import pygame
import pygame_menu
from pygame_menu import themes
from asteroid import Asteroid

class StartMenu(pygame_menu.Menu):
    def __init__(self, title, width, height, theme):
        super().__init__(title, width, height, True, None, 0, 1, True, True, True, theme)
        self.add.button("Play", self.start)
        self.add.button("Quit", pygame_menu.events.EXIT)
        #pygame_menu kept giving me errors for various undefined variables so I manually entered them here. Any suggestions for why that was happening would be appreciated.

    def start(self):
        game_running = True
        #for asteroid in asteroids:
        #    asteroid.kill()
        return
