
#import the  pygame zero library.
#import the pygame zero library
import pgzrun
import random

# screen dimensions
WIDTH = 800
HEIGHT = 600

# game variables
total_levels = 4
speed = 10
items = ["bag", "battery", "bottle", "chips"]
win = False
lose = False
current_level = 1
animations = []
item_level = []


def draw():
    screen.blit("backgroundenv",(0,0))
    if lose: 
        screen.draw.text("Game over :(",fontsize = 60, center = (WIDTH//2,HEIGHT//2), color = "blue")
    elif win:
        screen.draw.text("YOU WON! :)",fontsize = 60, center = (WIDTH//2,HEIGHT//2), color = "blue")
    else:
        for i in item_level:
            i.draw()
def update():
    if len(item_level) == 0:
        item_creator(current_level)


def item_creator(number_items):
    #items to be loaded at each level
    items_to_create = item_decider(number_items)
    #passing the actor function for each items
    actor_items = image_creator( items_to_create)
    #deciding the layout of the items
    layout_items(actor_items)
    #animating the items
    animate_items(actor_items)
    return actor_items


def item_decider(number_items):
    items_to_create = ["paper"]
    for i in range(number_items):
        option = random.choice(items)
        items_to_create.append(option)
    return items_to_create
def image_creator(items_to_create):
    actor_items = []
    for i in items_to_create:
        img = Actor(i)
        actor_items.append(img)
    return actor_items
    
def layout_items(items):
    num_gaps = len(items)+ 1
    gap_size = WIDTH/num_gaps
    for num,item in enumerate(items,1):
        xpos = num*gap_size
        item.x = xpos

def animate_items(items):
    for i in items:
        timetaken = speed - current_level
        i.anchor = ("center","bottom")
        animation = animate(i,duration = timetaken,on_finished=game_over,y = HEIGHT)
        animations.append(animation)

def game_over():
    global lose
    lose = True         

def on_mouse_down(pos):
    for i in item_level:
        if i.collidepoint(pos):
            if "paper"in i.image:
                game_complete()
        else:
            game_over()
            

def game_complete():
    global win,item_level
    stop_animation(animations)
    if current_level == total_levels:
        win = True
    else:
        current_level += 1
        item_level = []
        animations = []

def stop_animation(items):
    for i in items:
        if i.running:
            i.stop()

pgzrun.go()