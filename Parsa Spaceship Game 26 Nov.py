""" The game initiaises a fixed number of spaceship images at random 
positions on the screen and displays them along with their numbering.
It also calculate and displays the time taken since the game started.

The player needs to click on spaceships in numerical order to connect
them with lines. The goal is to connect all spaceships within 20 seconds. 
The time it takes to complete the task will be displayed as "Final Time" 
when the game ends."""


 # Import the pygame zero library
import pgzrun
from random import randint
from time import time

# Screen dimensions
WIDTH = 600  # Width of the game window
HEIGHT = 600  # Height of the game window

# Total number of spaceships in the game
tot_spaceship = 10

# Start the timer
start_time = time()
completion_time = None  # To record the time when the game ends

# List to hold all spaceships
spaceships = []
current_sat = 0  # To track which spaceship we are clicking
lines = []  # To store lines connecting the spaceships

game_over = False  # To check if the game has ended

# Create spaceships at random positions
for i in range(tot_spaceship):
    spaceship = Actor("spaceship")  # Load the spaceship image
    spaceship.pos = (randint(50, 550)), randint(50, 550)  # Place it randomly
    spaceships.append(spaceship)  # Add the spaceship to the list


# This function is called to draw everything on the screen
def draw():
    # Draw the space background
    screen.blit("spacebackground", (0, 0))

    if not game_over:
        # Draw each spaceship and its number
        for number, spaceship in enumerate(spaceships, start=1):
            spaceship.draw()  # Draw the spaceship
            screen.draw.text(
                str(number), (spaceship.pos[0], spaceship.pos[1] + 20), color="white"
            )  # Show the spaceship's number below it

        # Show the timer at the top-left corner
        total_time = round(time() - start_time, 2)
        screen.draw.text(f"Time: {total_time}s", (10, 10), fontsize=30)

        # Draw the red lines connecting clicked spaceships
        for i in lines:
            screen.draw.line(i[0], i[1], "red") # Draws a line between the start and end points 
    else:
        # If the game is over, calculate the final time
        if completion_time is not None:
            total_time = round(completion_time - start_time, 2)
        else:
            total_time = round(time() - start_time, 2)

        # Display "GAME OVER" and the final time
        screen.draw.text("GAME OVER", (WIDTH // 2 - 100, HEIGHT // 2 - 50), fontsize=50, color="red")
        screen.draw.text(f"Final Time: {total_time}s", (WIDTH // 2 - 100, HEIGHT // 2 + 10), fontsize=30, color="white")


# This function runs when you click the mouse.
def on_mouse_down(pos):
    """
    Checks clicks, connects spaceships, and ends the game if done in order.
    """
    global current_sat, tot_spaceship, lines, game_over, completion_time

    # Only allow actions if the game is not over
    if not game_over:
        # Check if there are more spaceships to click
        if current_sat < tot_spaceship:
            # Check if the player clicked the correct spaceship
            if spaceships[current_sat].collidepoint(pos):
                # If this isn't the first spaceship, draw a line from the previous one
                if current_sat > 0:
                    lines.append((spaceships[current_sat - 1].pos, spaceships[current_sat].pos)) #It draws a line from the previous spaceship to the current one.

                # Move to the next spaceship
                current_sat += 1

                # If all spaceships are clicked, end the game
                if current_sat == tot_spaceship:
                    completion_time = time()  # Record the time the game ends
                    game_over = True
            else:
                # If the wrong spot is clicked, reset the game progress
                lines = []  # Clear all lines
                current_sat = 0  # Start from the first spaceship again


# This function ends the game after 30 seconds
def timer():
    global game_over
    if not game_over:  # Only end the game if it isn't already over
        game_over = True


# Schedule the timer to trigger after 30 seconds
clock.schedule(timer, 30)

# Start the game
pgzrun.go()
       
