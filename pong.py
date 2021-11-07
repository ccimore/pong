# Old School Pong
# By Chris Cimorelli 11-7-21

# Imports
import turtle               # Imports library to create ball and paddle objects
import winsound             # Imports sound library for collisions

# Window Setup
wn = turtle.Screen()                         # creates a window
wn.title("Old School Pong!!! by CMC")        # Title
wn.bgcolor("black")                          # Background Color   
wn.setup(width =800, height =600)            # Size of window - Width and Height
wn.tracer(0)                                 # Stops window from updating - allows us to speed up games

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()                             # Creates Turtle object
paddle_a.speed(0)                                      # Speed of animation
paddle_a.shape("square")                               # Turtle shape
paddle_a.color("white")                                # Turtle color
paddle_a.shapesize(stretch_wid=5, stretch_len=1)       # Stretches turtle 5 * (20) wide, length = 1 * (20) is default
paddle_a.penup()                                       # Turtles, by definition, draw a line.  We don't want that here
paddle_a.goto(-350, 0)                                 # Turtle starting point (x coor, y coor)

# Paddle B
paddle_b = turtle.Turtle()                             # Creates Turtle object
paddle_b.speed(0)                                      # Speed of animation
paddle_b.shape("square")                               # Turtle shape
paddle_b.color("white")                                # Turtle color
paddle_b.shapesize(stretch_wid=5, stretch_len=1)       # Stretches turtle 5 * (20) wide, length = 1 * (20) is default
paddle_b.penup()                                       # Turtles, by definition, draw a line.  We don't want that here
paddle_b.goto(350, 0)                                  # Turtle starting point (x coor, y coor)

# Ball
ball = turtle.Turtle()                             # Creates Turtle object
ball.speed(0)                                      # Speed of animation
ball.shape("square")                               # Turtle shape
ball.color("white")                                # Turtle color
ball.penup()                                       # Turtles, by definition, draw a line.  We don't want that here
ball.goto(0, 0)                                    # Turtle starting point (x coor, y coor)
ball.dx = .08                                      # Delta x - provides movement along y coordinate (in pixels)
ball.dy = .08                                      # Delta y - provides movement along y coordinate (in pixels)

# Pen - scoring
pen = turtle.Turtle()               # Creates pen Turtle
pen.speed(0)                        # Speed of animation
pen.color("white")                  # Turtle color
pen.penup()                         # Turtles, by definition, draw a line.  We don't want that here
pen.hideturtle()                    # This is a Turtle we do not want to see, just the text it writes
pen.goto(0, 260)                    # Places score at top middle of screen
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 24, "normal"))       # Displays score of 0 for both players at start of game

# Function
def paddle_a_up():                              # Move Turtle up function
    y = paddle_a.ycor()                         # Returns y coordinate to y coordinate variable
    y += 20                                     # Adds 20 pixels to y coordinate variable
    paddle_a.sety(y)                            # Sets new y coordinate value for Turtle

def paddle_a_down():                            # Move Turtle down function
    y = paddle_a.ycor()                         # Returns y coordinate to y coordinate variable
    y -= 20                                     # Subtracts 20 pixels from y coordinate variable
    paddle_a.sety(y)                            # Sets new y coordinate value for Turtle

def paddle_b_up():                              # Move Turtle up function
    y = paddle_b.ycor()                         # Returns y coordinate to y coordinate variable
    y += 20                                     # Adds 20 pixels to y coordinate variable
    paddle_b.sety(y)                            # Sets new y coordinate value for Turtle

def paddle_b_down():                            # Move Turtle down function
    y = paddle_b.ycor()                         # Returns y coordinate to y coordinate variable
    y -= 20                                     # Subtracts 20 pixels from y coordinate variable
    paddle_b.sety(y)                            # Sets new y coordinate value for Turtle

# Keyboard binding - Details how function is called
wn.listen()                               # Listens for keyboard input while in window
wn.onkeypress(paddle_a_up, "w")           # When user presses input key - paddle_a_up function called
wn.onkeypress(paddle_a_down, "s")         # When user presses input key - paddle_a_down function called
wn.onkeypress(paddle_b_up, "Up")           # When user presses input key - paddle_b_up function called
wn.onkeypress(paddle_b_down, "Down")         # When user presses input key - paddle_b_down function called

# Main Game Loop
while True:                                 # While loop - creates continuous loop
    wn.update()                             # Window updates every time loop runs

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)        # Moves ball from start position with delta x velocity
    ball.sety(ball.ycor() + ball.dy)        # Moves ball from start position with delta y velocity

    # Border checking
    if ball.ycor() > 290:                   # Checks for ball beyond top of window
        ball.sety(290)                      # Sets ball at top of window
        ball.dy *= -1                       # Reverses y velocity of ball
        winsound.Beep(370, 100)             # Sound of ball collision

    if ball.ycor() < -290:                   # Checks for ball beyond bottom of window
        ball.sety(-290)                      # Sets ball at bottom of window
        ball.dy *= -1                        # Reverses y velocity of ball
        winsound.Beep(370, 100)              # Sound of ball collision

    if ball.xcor() > 390:                    # Checks for ball beyond right border of window
        ball.goto(0, 0)                      # Sets ball back at center
        ball.dx *= -1                        # Reverses x velocity of ball
        score_a += 1                         # Increments Player A score by 1
        pen.clear()                          # Clears previous score
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))      # Updates score for Player A
        winsound.Beep(370, 100)              # Sound of ball collision

    if ball.xcor() < -390:                   # Checks for ball beyond left border of window
        ball.goto(0, 0)                      # Sets ball back at center
        ball.dx *= -1                        # Reverses x velocity of ball
        score_b += 1                         # Increments Player B score by 1
        pen.clear()                          # Clears previous score
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))      # Updates score for Player B
        winsound.Beep(370, 100)              # Sound of ball collision
       
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):   # Describes position of ball and right paddle at collision
        ball.setx(340)                 # Sets ball in front of right paddle
        ball.dx *= -1                  # Reverses x velocity of ball
        winsound.Beep(370, 100)        # Sound of ball collision

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):   # Describes position of ball and left paddle at collision
        ball.setx(-340)                # Sets ball in front of left paddle
        ball.dx *= -1                  # Reverses x velocity of ball
        winsound.Beep(370, 100)        # Sound of ball collision

  


    



