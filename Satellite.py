import pgzrun
from random import randint
from time import time
WIDTH = 600
HEIGHT = 600

tot_sat = 10
start_time = 0
total_time = 0
current_sat = 0
satellites = []
lines = []

for i in range (tot_sat):
    satelite = Actor ("satellite")
    satelite.pos = randint (50,550),randint(50,550)
    satellites.append(satelite)

start_time = time()
def draw():
    screen.blit("backround",(0,0))
    number = 1
    for i in satellites:
        i.draw()
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        number = number + 1
        
    if current_sat < tot_sat:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time)),(10,10),fontsize = 30)  

def update():
    pass
pgzrun.go() 




























































































