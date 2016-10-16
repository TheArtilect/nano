import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor('black')

    donnie = turtle.Turtle()
    donnie.shape("turtle")
    donnie.color("green")
    donnie.speed(2)

    for x in range(0, 4):
        donnie.forward(100)
        donnie.right(90)

    amy = turtle.Turtle()
    amy.shape('turtle')
    amy.color("pink")
    amy.circle(60)

    kingsley = turtle.Turtle()
    kingsley.shape("turtle")
    kingsley.color("blue")

    for x in range(0, 3):
        kingsley.back(120)
        kingsley.left(120)

    window.exitonclick()

draw_shapes()
