##################### Data Base #####################
from turtle import *
from base import box
from random import randrange
from time import sleep

##################### Constants #####################
snake = [[0,0], [10,0], [20,0], [30,0], [40,0], [50,0]]
apple_x = randrange(-20, 18) * 10
apple_y = randrange(-19, 19) * 10
aim_x = 0
aim_y = 10

##################### Functions #####################
def move(x,y):
    global aim_x, aim_y
    aim_x = x
    aim_y = y

def inside_snake():
    for i in range(len(snake) - 1):
        if snake[-1][0] == snake[i][0] and snake[-1][1] == snake[i][1]:
            return True
    
    return False

def inside():
    if -200 <= snake[-1][0] <= 180 and -190 <= snake[-1][1] <= 190:
        return True
    else:
        return False

def gameLoop():
    global apple_x, apple_y, aim_x, aim_y, snake
    snake.append([snake[-1][0] + aim_x, snake[-1][1] + aim_y])

    if snake[-1][0] != apple_x or snake[-1][1] != apple_y:
        snake.pop(0)
    else:
        apple_x = randrange(-20, 18) * 10
        apple_y = randrange(-19, 19) * 10

    if not inside() or inside_snake():
        box(snake[-1][0], snake[-1][1],10,"green")
        update()
        sleep(2)
        snake = [[0,0], [10,0], [20,0], [30,0], [40,0], [50,0]]
        apple_x = randrange(-20, 18) * 10
        apple_y = randrange(-19, 19) * 10
        aim_x = 0
        aim_y = 10 

    clear()
    box(-210, -200, 410, "black")
    box(-200, -190, 390, "white")
    box(apple_x, apple_y, 10, "green")
    for i in range(len(snake)):
        box(snake[i][0], snake[i][1], 10, "black")
    update()
    ontimer(gameLoop, 150)

##################### Main #####################
setup(420, 420, 0, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: move(0, 10), "w")
onkey(lambda: move(0, -10), "s")
onkey(lambda: move(-10, 0), "a")
onkey(lambda: move(10, 0), "d")
gameLoop()
done()
