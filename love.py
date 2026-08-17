import math
import turtle

# Setup screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()


# Parametric equations for a perfect mathematical heart
def heart_x(t):
  return 16 * (math.sin(t) ** 3)


def heart_y(t):
  return (
      13 * math.cos(t)
      - 5 * math.cos(2 * t)
      - 2 * math.cos(3 * t)
      - math.cos(4 * t)
  )


# Set color (Crimson border, Solid Vibrant Red fill)
pen.color("#D32F2F", "#FF0000")
pen.pensize(3)

# 1. Move to the starting point of the curve without drawing
pen.up()
start_x = heart_x(0) * 15
start_y = heart_y(0) * 15
pen.goto(start_x, start_y)
pen.down()

# 2. Begin filling and plot the mathematical curve
pen.begin_fill()
for i in range(0, 629):  # 0 to ~2*pi (6.28 radians)
  t = i / 100
  x = heart_x(t) * 15  # 15 is the scale factor
  y = heart_y(t) * 15
  pen.goto(x, y)
pen.end_fill()

turtle.done()