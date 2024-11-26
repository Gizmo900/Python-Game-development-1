
#import the  pygame zero library.
import pgzrun,random


#screen dimentions. 
WIDTH = 800
HEIGHT = 600

total_levels = 4
speed = 10
items = ["bag","battery","bottle","chips"]

win = False
lose = False

current_level = 1

def draw():
    screen.blit("backroundenv",(0,0))
    if lose: 
        screen.draw.text("Game over :0"fontsize = 60, center = (WIDTH//2,HEIGHT//2), color = blue)
    elif win:
        screen.draw.text("YOU WON! :)"fontsize = 60, center = (WIDTH//2,HEIGHT//2), color = blue)
    else:
        for i in items:
            i.draw()

def item_creator(number_items):
    #items to be loaded at each level
    items_to_create = item_decider(number_items)
    #passing the actor function for each items
    actor_items = image_creator( items_to_create)
    #deciding the layout of the items
    layout_items(actor_items)
    #animating the items
    animate_items(actor_items)

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

             



