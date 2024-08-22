import turtle
import random

# Constants
GRID_SIZE = 20  # Size of each grid cell
w = 500
h = 500
food_size = GRID_SIZE
initial_delay = 150  # Increase delay to slow down the snake
delay = initial_delay

offsets = {
    "up": (0, GRID_SIZE),
    "down": (0, -GRID_SIZE),
    "left": (-GRID_SIZE, 0),
    "right": (GRID_SIZE, 0)
}

# Global variables
snake = []
snake_dir = "up"
food_position = ()
pen = None

def reset():
    global snake, snake_dir, food_position, pen, delay
    snake = [[0, 0], [0, GRID_SIZE], [0, 2 * GRID_SIZE], [0, 3 * GRID_SIZE], [0, 4 * GRID_SIZE]]
    snake_dir = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    delay = initial_delay  # Reset delay
    move_snake()

def move_snake():
    global snake_dir, delay

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_dir][0]
    new_head[1] += offsets[snake_dir][1]

    # Check for boundary collision
    if (new_head[0] >= w / 2 or new_head[0] < -w / 2 or
        new_head[1] >= h / 2 or new_head[1] < -h / 2):
        print("Game Over! The snake hit the boundary.")
        turtle.bye()
        return

    # Check for collision with self
    if new_head in snake:
        print("Game Over! The snake collided with itself.")
        turtle.bye()
        return

    snake.append(new_head)

    if not food_collision():
        snake.pop(0)

    pen.clearstamps()
    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.stamp()

    screen.update()

    # Continue with the next frame
    turtle.ontimer(move_snake, delay)

def food_collision():
    global food_position
    if get_distance(snake[-1], food_position) < GRID_SIZE:
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False

def get_random_food_position():
    while True:
        x = random.randint(-int(w / 2) // GRID_SIZE * GRID_SIZE + GRID_SIZE, int(w / 2) // GRID_SIZE * GRID_SIZE - GRID_SIZE)
        y = random.randint(-int(h / 2) // GRID_SIZE * GRID_SIZE + GRID_SIZE, int(h / 2) // GRID_SIZE * GRID_SIZE - GRID_SIZE)
        position = (x, y)
        if position not in snake:  # Ensure food is not on the snake
            return position

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"

def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"

def go_down():
    global snake_dir
    if snake_dir != "up":
        snake_dir = "down"

def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"

# Setup screen
screen = turtle.Screen()
screen.setup(w, h)
screen.title("Snake")
screen.bgcolor("blue")
screen.tracer(0)

# Setup pen
pen = turtle.Turtle("square")
pen.penup()

# Setup food
food = turtle.Turtle()
food.shape("square")
food.color("yellow")
food.shapesize(food_size / 20)
food.penup()

# Keyboard bindingsd
screen.listen()
screen.onkey(go_up, "w")    # Move up with 'W'
screen.onkey(go_right, "d") # Move right with 'D'
screen.onkey(go_down, "s")  # Move down with 'S'
screen.onkey(go_left, "a")  # Move left with 'A'

reset()
turtle.done()
