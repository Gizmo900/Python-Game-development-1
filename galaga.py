import pgzrun
import random
HEIGHT = 800
WIDTH = 1000

ship = Actor('galaga')
bug = Actor('bug')
score = 0
ship.pos = (WIDTH//2,HEIGHT-60)
enemies = []
bullets = []


for i in range (5):
    for j in range (3):
        enemies.append(Actor("bug"))
        enemies[-1].x = 100 + 50*i
        enemies[-1].y = 80+50*j        

def draw():
    screen.clear()
    screen.fill('cyan')
    for i in enemies:
        i.draw()
    ship.draw()

def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor('bullet'))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50
def update():
    if keyboard.left:
        ship.x-=5
        if ship.x<=0:
            ship.x = 0

    elif keyboard.right:
        ship.x+=5
        if ship.x>= WIDTH:
            ship.x = WIDTH





pgzrun.go()
























