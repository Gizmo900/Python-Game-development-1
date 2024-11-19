""" The game initiaises a fixed number of spaceship images at random 
positions on the screen and displays them along with their numbering.
It also calculate and displays the time taken since the game started."""

#import the  pygame zero library.
import pgzrun
from random import randint
from time import time

#screen dimentions. 
WIDTH = 600
HEIGHT = 600

tot_spaceship = 10

#record the start time of the game
start_time = time()

# Store actors
spaceships = [] # list to store spaceship actors

# creates the spaceship
for i in range(tot_spaceship):
    spaceship = Actor("spaceship")
    # Random positions within boundaries
    spaceship.pos = (randint(50, 550), randint(50, 550))
    #add the spaceship to the list.
    spaceships.append(spaceship)

def draw():
    # Draw the background
    screen.blit("spacebackground", (0, 0))

    # Draw spaceships and their numbers
    #the emumerate function adds a counter(index).
    for number, spaceship in enumerate(spaceships, start=1):
        spaceship.draw()
        screen.draw.text(
            str(number), (spaceship.pos[0], spaceship.pos[1] + 20), color="white"
        )

    # Calculate and display elapsed time
    total_time = time() - start_time
    screen.draw.text(
        str(total_time),(10,10), fontsize = 30
    )

def update():
    pass

pgzrun.go()






