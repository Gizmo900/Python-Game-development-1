""" This is a simple click-and-catch game made with Pygame Zero. Here's how it works:

Objective:

Click on the falling items.
Look for the "Red Star" item—clicking it moves you to the next level.
If you click the wrong item or miss the "Red Star," it's game over.
Game Levels:

There are 4 levels.
Each level has more falling items and faster speed.
Winning/Losing:

Win: Click all the "Red Stars" items in every level.
Lose: Click the wrong item or miss a "Red Star."  """

#import the Pygame Zero and random library
import pgzrun, random  # Pygame Zero is used to make games, and random is used to pick random items.

# screen dimensions
WIDTH = 800  # Width of the game window.
HEIGHT = 600  # Height of the game window.

# game variables
total_levels = 4  # Total number of levels in the game.
speed = 10  # Base speed of falling items (higher is slower).
items = ["ostar", "bstar", "ystar", "gstar"]  # List of non-paper items to fall.
win = False  # Tracks if the player has won.
lose = False  # Tracks if the player has lost.
current_level = 1  # The current game level.
animations = []  # List to keep track of animations.
item_level = []  # Items currently on the screen.

def draw():
    """Handles everything that appears on the screen."""
    global item_level, current_level, win, lose
    screen.clear()  # Clear the screen before drawing anything.
    screen.blit("backgroundenv", (0, 0))  # Set the background image.
    if lose: 
        # Show "Game Over" text if the player loses.
        screen.draw.text("Game over :(", fontsize=60, center=(WIDTH//2, HEIGHT//2), color="blue")
    elif win:
        # Show "You Won!" text if the player wins.
        screen.draw.text("YOU WON! :)", fontsize=60, center=(WIDTH//2, HEIGHT//2), color="blue")
    else:
        # Draw all items on the screen.
        for i in item_level:
            i.draw()

def update():
    """Updates the game state on each frame."""
    global item_level
    if len(item_level) == 0:  # If there are no items on the screen...
        item_level = item_creator(current_level)  # Create new items for the current level.

def item_creator(number_items):
    """Creates items for the current level."""
    items_to_create = item_decider(number_items)  # Decide which items will fall.
    actor_items = image_creator(items_to_create)  # Convert item names to Actor objects.
    layout_items(actor_items)  # Arrange items horizontally across the screen.
    animate_items(actor_items)  # Animate items so they fall.
    return actor_items  # Return the list of falling items.

def item_decider(number_items):
    """Chooses the items that will fall, always including at least one 'paper'."""
    items_to_create = ["paper"]  # Always include a "paper" item.
    for i in range(number_items):  # Add a random selection of other items.
        option = random.choice(items)
        items_to_create.append(option)
    return items_to_create

def image_creator(items_to_create):
    """Turns item names into Actor objects for the game."""
    actor_items = []
    for i in items_to_create:  # Create an Actor object for each item.
        img = Actor(i)
        actor_items.append(img)
    return actor_items

def layout_items(items):
    """Places the items evenly across the screen."""
    num_gaps = len(items) + 1  # Calculate gaps between items.
    gap_size = WIDTH / num_gaps  # Width of each gap.
    for num, item in enumerate(items, 1):  # Position each item.
        xpos = num * gap_size
        item.x = xpos  # Set the x position for each item.

def animate_items(items):
    """Animates the items to fall from the top to the bottom of the screen."""
    for i in items:
        timetaken = speed - current_level  # Calculate fall speed based on the level.
        animation = animate(i, duration=timetaken, on_finished=game_over, y=HEIGHT)
        animations.append(animation)  # Add animation to the list.

def game_over():
    """Triggers game over when the player fails."""
    global lose
    lose = True

def on_mouse_down(pos):
    """Checks if the player clicks on an item."""
    global item_level
    for i in item_level:
        if i.collidepoint(pos):  # If the player clicks an item...
            if "paper" in i.image:  # Check if the clicked item is "paper".
                game_complete()  # Progress to the next level.
                return
            else:
                game_over()  # End the game if the wrong item is clicked.
                return
    # If no item is clicked:
    game_over()

def game_complete():
    """Handles what happens when the player completes a level."""
    global win, item_level, animations, current_level
    stop_animation(animations)  # Stop any ongoing animations.
    if current_level == total_levels:  # If the last level is completed...
        win = True  # Player wins.
    else:
        current_level += 1  # Move to the next level.
        item_level = item_creator(current_level)  # Create new items for the next level.
        animations = []

def stop_animation(items):
    """Stops all animations."""
    for i in items:
        i.stop()  # Stop each animation.

pgzrun.go()  # Start the game.
