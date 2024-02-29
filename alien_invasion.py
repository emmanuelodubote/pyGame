

import sys
import pygame
# import settings                                    #------1 below
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    

    def __init__(self):
        
        """Initialize the game, and create game resources."""
        pygame.init()

        # self.settings = settings.Settings()       #------1 above
        self.settings = Settings()

        self.screen = pygame.display.set_mode((1200, 800))                                              #-----2 below Surface (Setting.py Class)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  #-----2 above Surface (Setting.py Class)       #------7 below
        
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)                                                                                 #------7 above (all 3 lines)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)                            #------self is AlienInvasion, the game
        
        self.bullets = pygame.sprite.Group()            #----called a group rather than an attribute, why??

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
            self.ship.update()
            self.bullets.update()               #----calls for each bullet we place in the bullet group above
            
            # Get rid of bullets that have disappeared
            for bullet in self.bullets.copy():      #----??
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            # print(len(self.bullets))

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

            elif event.type == pygame.KEYDOWN:     #---- keypress down
                # if event.key == pygame.K_RIGHT:           #---- 6 below (all 6lines)

                #     # # Move the ship to the right      #--------5 below
                #     # self.ship.rect.x += 1

                #     self.ship.moving_right = True       #--------5 above
                
                # elif event.key == pygame.K_LEFT:
                #     self.ship.moving_left = True

                self._check_keydown_events(event)           #---- 6 above & below

            elif event.type == pygame.KEYUP:        #----?? keypress release
                # if event.key == pygame.K_RIGHT:           #---- 6 below (all 4lines)
                #     self.ship.moving_right = False

                # elif event.key == pygame.K_LEFT:
                #     self.ship.moving_left = False
                
                self._check_keyup_events(event)             #---- 6 above & below


    def _check_keydown_events(self, event):                 #---- 6 above
        """Respond to keypresses."""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # elif event.key == pygame.K_UP:
        #     self.ship.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):                    #---- 6 above
        """Respond to key releases."""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        # elif event.key == pygame.K_UP:
        #     self.ship.moving_up = False


    def _update_screen(self):                                            #-----4 above (all 5lines)
        """Update images on the screen, and flip to the new screen."""
        
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():       #------FOR statement, why?
            bullet.draw_bullet()

        pygame.display.flip()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)               #----instance of a bullet
            self.bullets.add(new_bullet)            #----adding to bullet group with add() mtd (similar to append)


if __name__ == '__main__':                           #--------???
        # Make a game instance, and run the game.
        ai = AlienInvasion()
        ai.run_game()











