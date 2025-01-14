"""Quiz Master (File Handling in Python, Scoring System, Making a Timer)

Game Description:
Creation of a quiz game named "Quiz Master" using the Pygame Zero library for graphics and game logic."""

import pgzrun # Imports the Pygame zero library for graphics

TITLE = "Quiz game" #Sets the title of the game window
WIDTH = 800 #Define the size of the game window in pixels
HEIGHT = 650

# Define Rectangles (Boxes)
scroller_box = Rect(0,0,800,80)# Rect(x,y, width,height)
question_box = Rect(20,100,650,150)
a_box1 = Rect(20,270,300,150)
a_box2 = Rect(370,270,300,150)
a_box3 = Rect(20,450,300,150)
a_box4 = Rect(370,450,300,150)

# New Time and Skip boxes.
time_box = Rect(700,100,80,150) # Displays the reminaing time. Position at top-right.
skip_box = Rect(700,270,80,330) # A skip button- Below the time box.

#Global Variables
score = 0 # Tracks the player's score.                                                                               
time_left = 10 #The timer for answering a question.
scroller_msg = "" #Message to display in the scrolling area
gameover = False
a_boxes = [a_box1,a_box2,a_box3,a_box4] #List of answer boxes for easier iteration.
question_count = 0 # Number of questions in the game.
question_index = 0 #Tracks the current question number.
questions = [] #List of all questions read from the file.


#Draw Function
def draw():
    screen.clear() # Clears the screen for the next frame
    screen.fill("black") # Fills the background with black.

    # Draw scroller and question boxes.
    screen.draw.filled_rect(scroller_box,"navy")
    screen.draw.filled_rect(question_box,"red")
    
    #Draw answer option boxes.
    for box in a_boxes:
    # Draw answer boxes.
        screen.draw.filled_rect(box,"yellow")
         

    # Draws the time_box and displays the remaining time in blue
    screen.draw.filled_rect(time_box, "white")
    screen.draw.textbox(str( time_left),time_box,color = "blue",shadow = (0.5,0.5),scolor = "grey")

    #Draws the skip_box with the label "Skip", rotated by 90 degrees.
    screen.draw.filled_rect(skip_box, "green")
    screen.draw.text("Skip",center = skip_box.center, fontsize = 30, color = "white",angle = -90)
    
    #Displays a scrolling message showing the current question number
    scroller_msg = f"Welcome to the quiz! Q.No.{question_index} of {question_count}"
    screen.draw.textbox(scroller_msg,scroller_box,color = "white")
    
    # Display the current quesiton and its options.
    screen.draw.textbox(question[0],question_box,color = "blue")
    
    index = 1 # Starts from the first answer option.
    for box in a_boxes:
        screen.draw.textbox(question[index],box,color = "blue")
        index+=1



#Update Function
def update():
    scroller_box.x-= 2 #Moves the scroller_box 2 pixels to the left per frame. 
    if scroller_box.right<0: #When the box moves out of the screen, 
        scroller_box.x = 800 #it resets to the right edge (x=800).




#Read Questions
def read_questions():
    global questions , question_count   
    with open("questions.txt","r") as file:#Reads questions from a file named questions.txt
        for i in file:
            questions.append(i)#Adds each question to the questions list,
            question_count+=1  #Increments question_count





# Load questions
def load_questions():
    """Loads the next question and splits it into question text and options."""
    global questons,question_index

    question_index+=1 # Moves to the next question text and options
    return questions.pop(0).split("|") # Splits the question and its options

# Game Over
def game_over():
     global question,score,gameover,time_left
     message = f"Game Over. You have scored {score}" # Game over message.
     question = [message,"-","-","-","-",5] # Placeholder question to signal game over.
     time_left = 0 # Stops the timer.
     gameover = True



# Update Time
def update_time():
    """Updates the timer and triggers game over when time runs out."""
    global time_left
    if time_left>0:
        time_left-=1 # Decreases the timer by 1 second.
    else:
        game_over() # Ends the game when the timer reaches 0.




# Initialize the Game
read_questions() #Loads questions from the file.
question = load_questions() # Loads the first question.
clock.schedule_interval(update_time,1)  # Schedules the timer to update every second.



pgzrun.go() #Starts the game loop






























   




























