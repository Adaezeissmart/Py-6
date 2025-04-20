import turtle

turtle.Screen().bgcolor("blue")

sc = turtle.Screen()
sc.setup(405,305)

turtle.color("Green")

turtle.title("Welcome to my turte canvas")

board = turtle.Turtle()

for i in range(7):
    board.forward(120)
    board.left(70)
    i = i+i