""" The game initiaises a fixed number of spaceship images at random 
positions on the screen and displays them along with their numbering.
It also calculate and displays the time taken since the game started.

The player needs to click on spaceships in numerical order to connect
them with lines. The goal is to connect all spaceships within 20 seconds. 
The time it takes to complete the task will be displayed as "Final Time" 
when the game ends."""


#import the pygame zero library.
import pgzrun
from random import randint
from time import time

#screen dimensions.
WIDTH=600
HEIGHT=600

tot_spaceship=10

#record the start time of the game
start_time=time()
completion_time= None # Variable to track the time when all lines are connected.

#Store actors
spaceships=[] #list to store spaceship actors
current_sat= 0
lines=[]

game_over=False # Sets the game_over flag to False to start the game.

#create the spaceships
for i in range(tot_spaceship):
    spaceship= Actor ("spaceship")
    #random positions within boundaries
    spaceship.pos=(randint (50,550),randint(50,550))
    # add the spaceship to the list.
    spaceships.append(spaceship)

def draw():
    #draw the background
    screen.blit("spacebackground", (0,0))

    if not game_over:
        #draw spaceships and their numbers
        for number, spaceship in enumerate(spaceships, start=1):
            spaceship.draw()
            screen.draw.text(
                str(number), (spaceship.pos[0], spaceship.pos[1]+20),color="white"
            )

        # claulate and display elapsed time
        total_time=round(time()-start_time, 2) # rounded to 2 decimal places
        screen.draw.text(f"time: {total_time}s", (10,10), fontsize= 30)

        #draw lines
        for i in lines:
            screen.draw.line(i[0], i[1], "red")
    else:
        #display game over messge and final time
        if completion_time is not None:
            total_time= round(completion_time-start_time,2) #time to complete lines
        else:
            total_time= round(time()-start_time,2) # fallback to elapsed time

        screen.draw.text("Game Over", (WIDTH//2-100, HEIGHT//2-50),fontsize=50,color="red")
        screen.draw.text(f"Final Time:{total_time}s", (WIDTH//2-100, HEIGHT// 2+10), fontsize=30, color="white")

def update():
    pass

def on_mouse_down(pos):
    global current_sat, tot_spaceship, lines, game_over, completion_time
    if not game_over: # allow input only if the game is not over
        if current_sat< tot_spaceship:
            if spaceships[current_sat].collidepoint(pos):
                if current_sat:
                    lines.append((spaceships[current_sat-1].pos, spaceships[current_sat].pos)) # drawing a line between the previously clicked spaceship and the currently clicked spaceship.
                current_sat += 1
                # check if all lines are connected
                if current_sat == tot_spaceship:
                    completion_time=time() # record the time of completion
                    game_over= True # End the game when all lines are connected

            else:
                lines=[]
                current_sat=0

def timer():
    global game_over
    if not game_over:
        game_over= True # ends the game if the timer finishes before completion.

clock.schedule(timer,20) # schedules the timer function to rund after 20 seconds

pgzrun.go() #start the game
        