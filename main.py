import colorgram
import turtle as t
import random

# # Extract colors from an image.
# colors = colorgram.extract('image.jpg', 30)
#
# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t.colormode(255)

tim = t.Turtle()
tim.hideturtle()
tim.speed("fastest")

# Variables
origin = (-200, -200)
dot_size = 20
dot_space = 50
num_dots_per_line = 10

def draw_dots_in_line():
    for n in range(num_dots_per_line):
        tim.dot(dot_size, random.choice(color_list))
        if n != num_dots_per_line - 1:
            tim.penup()
            tim.forward(dot_space)
            tim.pendown()

def reset_pos():
    tim.penup()
    tim.setheading(90)
    tim.forward(dot_space)
    tim.setheading(180)
    tim.setx(origin[0])
    tim.setheading(0)

# Set starting point
tim.penup()
tim.setpos(origin)

# Draw
for n in range(num_dots_per_line):
    draw_dots_in_line()
    if n != num_dots_per_line - 1:
        reset_pos()

screen = t.Screen()
screen.exitonclick()
