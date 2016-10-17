import turtle

def square(turt):
    for x in range(0,4):
        turt.forward(100)
        turt.right(90)


def draw_shapes():
    window = turtle.Screen()
    window.bgcolor('black')

    donnie = turtle.Turtle()
    donnie.shape("turtle")
    donnie.color("green")
    donnie.speed(2)

    for x in range(0, 36):
        square(donnie)
        donnie.right(10)

    window.exitonclick()

'''
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

'''



draw_shapes()
