import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        # Initialize the module
        pygame.init()                           

        # To create a display window
        self.settings = Settings() 
        # self.screen = pygame.display.set_mode((
        #     self.settings.screen_width,self.settings.screen_height)) 
       
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        # Initialize the name of the window
        pygame.display.set_caption("Alien Invasion") 

        # display the ship
        self.ship = Ship(self)               
            
        """ 
        The object assigned to self.screen is called a surface. 
        A surface in Pygame is a part of the screen where a game element can be displayed.
        It gets updated the the elements get added and removed.

        """
                      
    
    def run_game(self):
        """Start the main loop for the game."""

        while True:
            self._check_events() # helper to check the actions. 
            self.ship.update()
            self._update_screen() # helper to draw the screen and update that. 

            # Redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():           # To access the events 
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        # changing the color (equal mix of RGB) 
        self.screen.fill(self.settings.bg_color)
        #  draw the ship on the screen
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()