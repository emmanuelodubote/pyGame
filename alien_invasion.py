

import sys
import pygame
# import settings                                    #------1 below
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    

    def __init__(self):
        
        """Initialize the game, and create game resources."""
        pygame.init()

        # self.settings = settings.Settings()       #------1 above
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((1200, 800))                                              #-----2 below Surface (Setting.py Class)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  #-----2 above Surface (Setting.py Class)
        
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)                            #------self is AlienInvasion, the game
        
        # # Set the background color.
        # self.bg_color = (230, 230, 230)


    def run_game(self):
        """Start the main loop for the game."""

        while True:                                   #--------???
            
            # # Watch for keyboard and mouse events.        #-----3 below (all 4lines)
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:       #------why mtd w/o () ???
            #         sys.exit()


            self._check_events()                            #-----3 above
            self._update_screen()                                        #-----4 below (all 5lines)
            

            # # Redraw the screen during each pass through the loop.     #-----4 below (all 5lines)
            # self.screen.fill(self.settings.bg_color)

            # self.ship.blitme()                       #-------draw the ship on the screen

            # # Make the most recently drawn screen visible.
            # pygame.display.flip()                      


    def _check_events(self):                              #-----3 above
        """Respond to keypresses and mouse events."""

        # Watch for keyboard and mouse events.            #-----3 above (all 4lines)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:     
                sys.exit()


    def _update_screen(self):                                            #-----4 above (all 5lines)
        """Update images on the screen, and flip to the new screen."""
        
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()




if __name__ == '__main__':                           #--------???
        # Make a game instance, and run the game.
        ai = AlienInvasion()
        ai.run_game()











