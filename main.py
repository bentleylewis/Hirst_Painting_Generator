###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import turtle
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)\

# '''
# 10 by 10 dots
#
# 20 in size
#
# spaced by 50 paces
#
# '''


import turtle as t
import random

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = t.Turtle()
t.colormode(255)


t.speed("fastest")
t.hideturtle()


def turtle_start():
    tim.hideturtle()
    tim.penup()
    tim.goto(-200, -200)


'''
def turtle_across():
    for _ in range(10):
        random_color = random.choice(color_list)
        tim.pendown()
        tim.dot(20, random_color)
        tim.penup()
        tim.forward(50)
'''


'''
turtle_rows = 0
while turtle_rows < 10:
    current_y = tim.ycor()
    current_x = tim.xcor()
    turtle_across()
    new_line()
    turtle_rows += 1'''

turtle_start()
for dot_count in range(1,101):
    random_color = random.choice(color_list)
    tim.dot(20, random_color)
    tim.forward(50)

    if dot_count % 10 == 0:
        current_y = tim.ycor()
        tim.goto(-200, current_y + 50)

screen = t.Screen()
t.exitonclick()


