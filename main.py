from random import random
from turtle import Turtle, Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import snake

screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("white")
screen.title("Snake Game 𓉸𓆗 ")
screen.tracer(0)




snake = snake() 
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "Down")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "d")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
#Detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
#Teleport food to random position without touching snkes body



#Detect collision with wall

    if snake.head.xcor() > 450 or snake.head.xcor() < -450 or snake.head.ycor() > 450 or snake.head.ycor() < -450:
        game_is_on = False
        scoreboard.game_over()

#Detect collision with tail

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()








screen.update() 

    
    

  

        
        


















screen.exitonclick()