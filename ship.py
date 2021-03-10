import pygame

class Ship:
    """Class to manage the ship"""

    def __init__(self, ai_game): # ref. to current instance of AI class
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        #Use get_rect method and assign to self.screen_rect (this allows to us to place the ship in the corect location on the screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect(rectangles)
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)


        #At def__init(self, ai_game) this will give ship access to all the game         resources defined in AlienInvasion