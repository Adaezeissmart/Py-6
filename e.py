import turtle

turtle.Screen().bgcolor("blue")

sc = turtle.Screen()
sc.setup(405,305)

turtle.color("Green")

turtle.title("Welcome to my turte canvas")

board = turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)
    i = i+i