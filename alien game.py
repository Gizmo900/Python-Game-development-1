


import pgzrun
from random import randint
TITLE = "Alien game"

WIDTH = 500
HEIGHT = 500


img = Actor("alien")
img.pos=100,100

msg=""
def draw():
    screen.clear()
    screen.fill("blue")
    img.draw()
    screen.draw.text(msg,center=(400,10),fontsize = 30, color="white")

def on_mouse_down(pos) :
    global msg
    if img.collidepoint(pos):
        img.x=randint(50,450)
        img.y=randint(50,450)
        msg="Good shot"
    else:
        msg="You missed"
    
pgzrun.go()
