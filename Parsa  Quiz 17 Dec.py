
"""Quiz Master (File Handling in Python, Scoring System, Making a Timer)

Game Description:

Creation of a quiz game named "Quiz Master" using the Pygame Zero library for graphics and game logic."""
import pgzrun

TITLE = "Quiz game"
WIDTH = 800
HEIGHT = 650

# Define all boxes
scroller_box = Rect(0,0,800,80)# Rect(x,y, width,height)
question_box = Rect(20,100,650,150)
a_box1 = Rect(20,270,300,150)
a_box2 = Rect(370,270,300,150)
a_box3 = Rect(20,450,300,150)
a_box4 = Rect(370,450,300,150)

# New Time and Skip boxes.
time_box = Rect(700,100,80,150) # Position at top-right.
skip_box = Rect(700,270,80,330) # Below the time box.


score = 0                                                                                
time_left = 10
scroller_msg = ""
gameover = False
a_boxes = [a_box1,a_box2,a_box3,a_box4]
question_count = 0
question_index = 0
questions = []



def draw():
    screen.clear()
    screen.fill("black")

    # Draw scroller and question boxes.
    screen.draw.filled_rect(scroller_box,"navy")
    screen.draw.filled_rect(question_box,"red")
    
    for box in a_boxes:
    # Draw answer boxes.
        screen.draw.filled_rect(box,"yellow")
         

    # Draw time and skip boxes.
    screen.draw.filled_rect(time_box, "white")
    screen.draw.textbox(str( time_left),time_box,color = "blue",shadow = (0.5,0.5),scolor = "grey")


    screen.draw.filled_rect(skip_box, "green")
    screen.draw.text("Skip",center = skip_box.center, fontsize = 30, color = "white",angle = -90)

    scroller_msg = f"Welcome to the quiz! Qno.{question_index} of {question_count}"
    screen.draw.textbox(scroller_msg,scroller_box,color = "white")


def read_questions():
    global questions , question_count   
    with open("questions.txt","r") as file:
        for i in file:
            questions.append(i)
            question_count+=1









def update():
    scroller_box.x-= 2
    if scroller_box.right<0:
        scroller_box.x = 800

read_questions()
print(questions)


pgzrun.go()