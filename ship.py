

import pygame



class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings


        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        # self.image = pygame.image.load('images/brick.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom        #----?? midbottom mtd? why no ()

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False


    def blitme(self):
        """Draw the ship at its current location."""
        
        self.screen.blit(self.image, self.rect)   


    def update(self):
        """Update the ship's position based on the movement flag"""

        # if self.moving_right:                                                 #----- 2 below (limiting ship range)
        if self.moving_right and self.rect.right < self.screen_rect.right:      #----- 2 above (limiting ship range)  # --- ??
            # self.rect.x += 1          #------ 1 below

            # Update the ship's x value, not the rect.      
            self.x += self.settings.ship_speed          #------ 1 above

        # if self.moving_right:                                                 #----- 2 below (limiting ship range)
        if self.moving_left and self.rect.left > 0:     # --- ??                         #----- 2 above (limiting ship range)
            # self.rect.x -= 1          #------ 1 below

            self.x -= self.settings.ship_speed          #------ 1 above

        # Update rect object from self.x
        self.rect.x = self.x





