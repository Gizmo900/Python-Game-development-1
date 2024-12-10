import pgzrun
TITLE = "Quiz game"
WIDTH = 800
HEIGHT = 650

scroller_box = Rect(0,0,800,80)
question_box = Rect(20,100,650,150)
a_box1 = Rect(20,270,300,150)
a_box2 = Rect(370,270,300,150)
a_box3 = Rect(20,450,300,150)
a_box4 = Rect(370,450,300,150)



def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(scroller_box,"navy")
    screen.draw.filled_rect(scroller_box,"red")
    screen.draw.filled_rect(a_box1,"yellow")
    screen.draw.filled_rect(a_box2,"yellow")
    screen.draw.filled_rect(a_box3,"yellow")
    screen.draw.filled_rect(a_box4,"yellow")


def update():
    pass
pgzrun.go()


























































































































































