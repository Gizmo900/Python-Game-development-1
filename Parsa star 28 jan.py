"""A python game using Pygame Zero(pgzrun)    
where a player controls a basket to catch falling stars"""

import pgzrun
import random

#set up the screen size
WIDTH = 800
HEIGHT = 600

# Create the basket actor and position it at the bottom center
basket = Actor("basket")

basket.pos = (WIDTH // 2, HEIGHT - 80)

# Create the star actor and start it at a random position at the top
star = Actor("star")
star.pos = (random.randint(50, WIDTH - 50), 50)   # (x, y)- Generates a random x-coordinate 
                                                 #  Within the range of 50 to WIDTH - 50

# set initial score
score = 0

# set star falling speed 
star_speed = 3

# draw function to render the screen
def draw():
    screen.clear() # clear the screen before drawing 
    screen.blit("spacebackground", (0,0)) #draw the backround image.
    basket.draw() # draw the basket actor
    star.draw() # draw the star actor
    screen.draw.text(f"Score: {score}", (10,10), fontsize = 40, color = "white") # display the score

# Update function to handle movement and collision detection
def update():
    global score

    # move the basket left and right with arrow keys.
    if keyboard.left and basket.left >0:
        basket.x -=5
    if keyboard.right and basket.right < WIDTH:
        basket.x +=5
        
    # move the star down
    star.y += star_speed # star.y refers to the vertical position of the star .
                         #if star_speed = 3 , the star moves down 3 pixels per frame    

    # Check if the star reaches the bottom
    if star.y > HEIGHT:
        reset_star()


    # check for collision with the basket
    if basket.colliderect(star):
        score +=1
        reset_star()

# Function to reset the star at the top at a new random position
def reset_star():
    star.pos = (random.randint(50,WIDTH - 50), 50)

# Run the game 
pgzrun.go()            






 
























































































