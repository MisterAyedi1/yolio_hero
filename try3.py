import turtle
import time

# Set up the screen
win = turtle.Screen()
win.title("Ping Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  # Stops the window from updating automatically

# Difficulty and Speed Configuration
difficulty = win.textinput("Choose Difficulty", "Enter difficulty (easy, medium, hard): ").strip().lower()
if difficulty == "easy":
    ball_speed = 0.1
elif difficulty == "medium":
    ball_speed = 0.2
else:
    ball_speed = 0.3  # Hard mode has the fastest speed

# Get Player Names
player_a_name = win.textinput("Player A Name", "Enter Player A's name: ")
player_b_name = win.textinput("Player B Name", "Enter Player B's name: ")

# Paddle A (left paddle)
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B (right paddle)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = ball_speed  # Ball movement in x direction based on difficulty
ball.dy = -ball_speed  # Ball movement in y direction based on difficulty

# Score
score_a = 0
score_b = 0

# Display the score and player names
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"{player_a_name}: 0  {player_b_name}: 0", align="center", font=("Courier", 24, "normal"))

# Function to update the score
def update_score():
    score_display.clear()
    score_display.write(f"{player_a_name}: {score_a}  {player_b_name}: {score_b}", align="center", font=("Courier", 24, "normal"))

# Functions to move paddles
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
        paddle_b.sety(y)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Display start message
start_message = turtle.Turtle()
start_message.speed(0)
start_message.color("yellow")
start_message.penup()
start_message.hideturtle()
start_message.goto(0, 0)
start_message.write("Get Ready!", align="center", font=("Courier", 36, "normal"))
time.sleep(2)
start_message.clear()

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking (top and bottom)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Border checking (left and right)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = ball_speed if ball.dx > 0 else -ball_speed  # Reset ball speed
        ball.dy = ball_speed if ball.dy > 0 else -ball_speed
        score_a += 1
        update_score()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = ball_speed if ball.dx > 0 else -ball_speed  # Reset ball speed
        ball.dy = ball_speed if ball.dy > 0 else -ball_speed
        score_b += 1
        update_score()

    # Paddle and ball collision
    if (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
