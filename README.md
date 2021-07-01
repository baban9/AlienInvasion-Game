# AlienInvasion-Game

In Alien Invasion, the player controls a rocket ship that appears at the bottom center of the screen. 
The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar. 
When the game begins, a fleet of aliens fills the sky and moves across and down the screen. 
The player shoots and destroys the aliens.
    If the player shoots all the aliens, a new fleet appears that moves faster than the previous fleet. 
    If any alien hits the player’s ship or reaches the bottom of the screen, the player loses a ship. 
    If the player loses three ships, the game ends.

Further Details : 
The game is controlled by the run_game() method. 
This method contains a while loop that runs continually. 
The while loop contains an event loop and code that manages screen updates. 
An event is an action that the user performs while playing the game, such as pressing a key or moving the mouse. 
To make our program respond to events, we write this event loop to listen for events 
and perform appropriate tasks depending on the kinds of events that occur. 
The for loop is an event loop.

Playing Details in code : 
Each event is picked up by the pygame.event.get() method. 
We need to specify in our _check_events() method what kind of events we want the game to check for. 
Each keypress is registered as a KEYDOWN event.
When Pygame detects a KEYDOWN event, 
    - we need to check whether the key that was pressed is one that triggers a certain action.

