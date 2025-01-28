import pgzrun
import random
HEIGHT = 800
WIDTH = 1000

ship = Actor('galaga')
bug = Actor('bug')
score = 0
GO = False

ship.pos = (WIDTH//2,HEIGHT-60)
enemies = []
bullets = []

direction = 1

for i in range (5):
    for j in range (3):
        enemies.append(Actor("bug"))
        enemies[-1].x = 100 + 50*i # initial postionis  100 and add 50 each time
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

def gameOver():
    global GO
    GO = True
    screen.draw.text("GAME OVER",(400,500))

def update():
    global score,direction 
    moveDown = False


    if keyboard.left:
        ship.x-=5
        if ship.x<=0:
            ship.x = 0

    elif keyboard.right:
        ship.x+=5
        if ship.x>= WIDTH:
            ship.x = WIDTH

    # move the bullets
    for bullet in bullets:
        bullet.y-=10
        if bullet.y<=0:
            bullets.remove(bullet)

        


    if len(enemies)>0 and (enemies[-1].x>WIDTH or enemies [0].x<0):
         moveDown = True
         direction*=-1
    for enemy in enemies:
        enemy.x+=4*direction
        if moveDown==True:
             enemy.y+=100

        for bullet in bullets:
          if enemy.colliderect(bullet):
            score+=1
            enemies.remove(enemy)
            bullets.remove(bullet)
            if len (enemies)==0:
                gameOver() 

        if enemy.colliderect(ship):
            gameOver()
def draw():
    screen.clear() 
    screen.fill('red')  
    screen.draw.text(str(score),(50,30))
    if GO==False:
        for i in bullets:
            i.draw()
        for i in enemies:
            i.draw()
        ship.draw()





pgzrun.go()
























