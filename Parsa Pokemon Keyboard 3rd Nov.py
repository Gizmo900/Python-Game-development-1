"""This program is a simple game where the player controls an actor called "Ash" 
to move around the screen. The goal is to collide with a "Pokemon" actor 
as many times as possible to increase the score. After each collision, 
the "Pokemon" moves to a random location. The game ends after 60 seconds, 
at which point the screen displays "Game Over" along with the final score. """



import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 600

score = 0 

game_over = False

Pokemon = Actor("pokemon")
Pokemon.pos = 100, 200

Ash = Actor("ash")
Ash.pos = 150, 200

def draw():
    if game_over: #  check if the game is over
        screen.fill("sky blue")
        screen.draw.text("Game over! You have scored: " + str(score), color="green", fontsize=40, center=(WIDTH // 2, HEIGHT // 2))
    else:
        screen.blit("backgroundc", (0, 0)) # draw the backround image
        Ash.draw()
        Pokemon.draw()
        screen.draw.text("Score: " + str(score), color="red", topleft=(10, 10))

def update():
    global score # A variable that can be used by any part of the program
    if not game_over:
        if keyboard.left:
            Ash.x -= 3 #Moves Ash 3pixels to the left
        if keyboard.right:
            Ash.x += 3
        if keyboard.up:
            Ash.y -= 3
        if keyboard.down:
            Ash.y += 3

        if Ash.colliderect(Pokemon):# Check if ash collides with the pokemon
            score += 1# Increases  the score by 1.
            Pokemon.pos = randint(50, 500), randint(50, 500)#Moves the pokemon to a random spot on the screen

def timer():
    global game_over
    game_over = True

clock.schedule(timer, 60) #you have 60 seconds to catch as many pokemon as possible.
pgzrun.go() # Starts the game with a loop.
























