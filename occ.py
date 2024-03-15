import turtle
import time
import random
import os
import winsound

# Variables
score = 0
high_score = 0
delay = 0.15
lives = 3
average_score = 0
name = ""
trash_shapes = ["t1.gif", "t2.gif", "t3.gif", "t4.gif", "t5.gif"]

# Functions

# Creates file if none are found
if not os.path.exists("score.txt"):
    with open("score.txt", "w") as file:
        file.write(f"Name HighScore\n")

# Clears termimal 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Header
def header():
    print("=========================================")
    print("Welcome to the Ocean Clean-up Challenge!")
    print("=========================================\n")

# Ask players for name
def player_Names():
    global name
    while True:
        header()
        name = input("Enter Player Name: ").capitalize()
        if name.isalpha():
            print(f"Hi {name}, Let's get started!")
            return name
        else:
            print("Please enter alphabetic characters only. No spaces allowed")
            input("Press enter to continue...")
            clear_screen()

# Functions to start game
def start_game():
    menu.goto(1000, 1000)
    # Set up game elements
    start_sub()
    start_trash()
    start_waste()
    scoreboard.goto(0, 260)
    scoreboard.write(f"Score: {score}     High Score:{high_score}     Lives: {lives}", align="center",
                 font=("Verdana", 16, "normal"))
    instruction.hideturtle()

def start_sub():
    sub.showturtle()

def start_trash():
    trash.showturtle()

def start_waste():
    waste.showturtle()

def inst():
    instruction.showturtle()
    menu.hideturtle()

def score_quit():
    window.bye()
    read_score()

def quit():
    instruction.hideturtle()
    menu.hideturtle()
    window.bye()
    post_game()

# Functions to move the submarine in different directions
def go_up():
    if sub.direction != "down":
        sub.direction = "up"

def go_down():
    if sub.direction != "up":
        sub.direction = "down"

def go_left():
    if sub.direction != "right":
        sub.direction = "left"

def go_right():
    if sub.direction != "left":
        sub.direction = "right"

def move():
    if sub.direction == "up":
        sub.shape("w.gif")
        y = sub.ycor()
        sub.sety(y + 20)
    if sub.direction == "down":
        sub.shape("s.gif")
        y = sub.ycor()
        sub.sety(y - 20)
    if sub.direction == "left":
        sub.shape("a.gif")
        x = sub.xcor()
        sub.setx(x - 20)
    if sub.direction == "right":
        sub.shape("d.gif")
        x = sub.xcor()
        sub.setx(x + 20)

# Append player score to text file
def file_handling():
    with open("score.txt", "a") as file:
        file.write(f"{name} {high_score}\n")

# Show scores in decreasing scores
def read_score():
    with open('score.txt', 'r') as file:
        scores = {}
        header()
        print('Name\tHigh Score')
        for i, line in enumerate(file):
            if i == 0: 
                continue
            name, score = line.strip().split()
            score = int(score)
            scores[name] = score

        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        for name, score in sorted_scores:
            print(f"{name}\t{score}")

        #Option to delete scores
        while True:
            choice = input("Would you like to delete scores?(Y/N): ").lower()
            if choice == "y":
                delete_score()
            elif choice == "n":
                post_game()
            else:
                print("Please enter Y or N.")

# Delete name and score from text file
def delete_score():
    with open('score.txt', 'r') as file:
        lines = file.readlines()

    player_to_delete = input("Enter the name of the player whose score you want to delete: ").capitalize()
    found = False

    with open('score.txt', 'w') as file:
        for line in lines:
            if player_to_delete in line:
                found = True
                break
                
    if found:
        with open('score.txt', 'w') as file:
            for line in lines:
                if player_to_delete not in line:
                    file.write(line)
        print(f"Score for {player_to_delete} has been deleted.")
        clear_screen()
        read_score()
    else:
        print(f"No score found for {player_to_delete}.")    

# Function to spawn waste objects

def spawn_waste(num_waste):
    global waste_list

    for _ in range(num_waste):
        waste = turtle.Turtle()
        waste.speed(0)
        waste.penup()
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        waste.goto(x, y)
        waste.shape("toxic.gif")
        waste.direction = "stop"
        waste_list.append(waste)

# Function for post game

def post_game():
    while True:
        clear_screen()
        header()
        print("View High Scores [1] Quit [2]")
        try:
            choice = int(input("What would you like to do?: "))
            if choice == 1:
                clear_screen()
                read_score()
                break
            elif choice == 2:
                print(f'''Thank your for playing, {name}!!! We hope you enjoyed the Ocean Cleanup Challenge.
Your dedication to cleaning up our virtual oceans is commendable, but remember, 
the real challenge lies in making a difference in our planet's oceans.
Together, we can work towards a cleaner and healthier ocean by 
reducing plastic use, recycling, participating in beach clean-ups, and supporting 
organizations dedicated to ocean conservation. Your actions today can create a 
positive impact on the oceans for generations to come. Have a wonderful day!!!''')
                time.sleep(3)
                exit()
            else:
                print("Invalid Input.")
        except ValueError:
            print("Invalid Input. Please Choose from the Choices")

# Function to remove waste

def remove_waste():
    global waste_list
    if waste_list:  
        waste_to_remove = random.choice(waste_list)
        waste_list.remove(waste_to_remove)
        waste_to_remove.hideturtle()

player_Names()

# Registering custom shapes for game elements
turtle.register_shape("start.gif")
turtle.register_shape("inst.gif")
turtle.register_shape("w.gif")
turtle.register_shape("a.gif")
turtle.register_shape("s.gif")
turtle.register_shape("d.gif")
turtle.register_shape("t1.gif")
turtle.register_shape("t2.gif")
turtle.register_shape("t3.gif")
turtle.register_shape("t4.gif")
turtle.register_shape("t5.gif")
turtle.register_shape("toxic.gif")
turtle.register_shape("gl.gif")
turtle.register_shape("ty.gif")


def main_Game():
    # Play background music
    
    winsound.PlaySound("bggmusic.wav",winsound.SND_ASYNC)
    global window, menu, instruction, exit, sub, trash, waste_list, last_waste_spawn,scoreboard, write, leave

    window = turtle.Screen()    # Initialize game window and elements
    window.title("Ocean Cleanup Challenge")
    window.bgpic("asd.png")
    window.setup(width=600, height=600)
    window.tracer(0)

    menu = turtle.Turtle()  # Menu setup
    menu.shape("start.gif")
    menu.penup()
    menu.goto(0,0)
    window.listen()
    window.onkeypress(start_game, "p")
    window.onkeypress(score_quit, "h")

    instruction = turtle.Turtle() # Instruction setup
    instruction.shape("inst.gif")
    instruction.hideturtle()
    window.onkeypress(inst, "i")

    window.onkeypress(quit, "l")    # Quit Setup

    # Submarine Setup
    sub = turtle.Turtle()
    sub.speed(0)
    sub.shape("d.gif")
    sub.penup()
    sub.goto(0,0)
    sub.speed(6)
    sub.hideturtle()
    sub.direction = "stop"

    # Trash Setup
    trash = turtle.Turtle()
    trash.speed(0)
    for shape in trash_shapes:
        turtle.register_shape(shape)
    trash.penup()
    trash_shape = random.choice(trash_shapes)
    trash.shape(trash_shape)
    trash.goto(0, 150)
    trash.hideturtle()

    # List to hold wastes
    waste_list = []
    last_waste_spawn = 0

    # Toxic waste setup
    waste = turtle.Turtle()
    waste.shape("toxic.gif")
    waste.hideturtle()
    waste.speed(0)
    waste.penup()
    waste.goto(0,200)
    waste.direction = "stop"

    waste_list.append(waste)

    # Scoreboard setup
    scoreboard = turtle.Turtle()
    scoreboard.speed(0)
    scoreboard.penup()
    scoreboard.hideturtle()

    # Losing message setup
    write = turtle.Turtle()
    write.speed(0)
    write.hideturtle()

    # Keyboard setup
    window.listen()
    window.onkeypress(go_up, "w")
    window.onkeypress(go_down, "s")
    window.onkeypress(go_left, "a")
    window.onkeypress(go_right, "d")

main_Game()


# Main game loop

while True:
    window.update()

# In-game event logic

    # Resets game speed every 500 score
    if score % 500 == 0:
        delay = 0.15

    # Increases game speed every 50 score (except for the last waste spawn)
    if score % 50 == 0 and score != last_waste_spawn:
        num = random.randint(1, 3)
        spawn_waste(num)
        remove_waste()
        last_waste_spawn = score
        delay -= 0.01

    # Border collission game logic
    if sub.xcor() > 260 or sub.xcor() < -260 or sub.ycor() > 235 or sub.ycor() < -260:
        time.sleep(1.5)
        sub.goto(0, 0)
        sub.direction = "stop"
        lives -= 1

        average_score += score
        score = 0
        delay = 0.1

        scoreboard.clear()
        scoreboard.write(f"Score: {score}     High Score: {high_score}     Lives: {lives}", align="center",
                         font=("Verdana", 16, "normal"))

    # Trash collission game logic
    if sub.distance(trash) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 225)
        trash.goto(x, y)

        delay -= 0.001
        score += 10

        if score > high_score:
            high_score = score
        scoreboard.clear()
        scoreboard.write(f"Score: {score}     High Score: {high_score}     Lives: {lives}", align="center",
                         font=("Verdana", 16, "normal"))

        trash_shape = random.choice(trash_shapes)
        turtle.register_shape(trash_shape)
        trash.shape(trash_shape)

    # Toxic waste collission and spawn game logic
    for waste in waste_list:
        if sub.distance(waste) < 20:
            x1 = random.randint(-250, 250)
            y1 = random.randint(-250, 230)
            waste.goto(x1, y1)
            time.sleep(1)
            sub.goto(0, 0)
            sub.direction = "stop"
            lives -= 1
            delay += 0.001
            average_score += score
            score = 0

            if score > high_score:
                high_score = score
            scoreboard.clear()
            scoreboard.write(f"Score: {score}     High Score: {high_score}     Lives: {lives}", align="center",
                             font=("Verdana", 16, "normal"))

            trash_shape = random.choice(trash_shapes)
            turtle.register_shape(trash_shape)
            trash.shape(trash_shape)
   
    # Game over condition
    if lives == 0:
        window.clearscreen()
        leave = turtle.Turtle()
        leave.shape("gl.gif")
        leave.goto(0,0)
        window.onkeypress(quit, "l")
        write.goto(0,-50)
        write.write(f"Fantastic work, {name}!\nYour commitment to tackling\nocean pollutions are truly inspiring!\nWith every action you take,\nyou're contributing to a healthier marine environment.\nRemember, it's not just about cleaning virtual oceans,\nbut also making a difference in the real world.\nAverage Score: {(average_score / 3):.0f}\nPress 'L' to continue your journey towards\na cleaner and safer ocean for all.", align="center", font=("Verdana", 16, "normal"))
        file_handling()
        turtle.done()
        post_game()
        
        
        break

    window.update()

    move()  # Moves the submarine
    time.sleep(delay) # Pauses the game

# End of main game loop
window.mainloop()
