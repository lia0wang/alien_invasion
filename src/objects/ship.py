from sys import flags
from time import sleep
import pygame

class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        # Assign the screen
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Get the background rect, as to place the ship
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image
        self.image = pygame.image.load('images/ship.bmp')
        # Get the image as a rect as to place the ship
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
    
        # Store a float value for the ship's horizontal position.
        self.horizon = float(self.rect.x)
        self.vertical = float(self.rect.y)

        # Movement flag, default False
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.horizon += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.horizon -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.vertical += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.vertical -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.horizon
        self.rect.y = self.vertical

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.horizon = float(self.rect.x)
        self.vertical = float(self.rect.y)