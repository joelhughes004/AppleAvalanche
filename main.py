#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif"  # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file

apple = trtl.Turtle()
drawer = trtl.Turtle()
drawer2 = trtl.Turtle()
drawer3 = trtl.Turtle()
drawer.penup()
drawer2.penup()
drawer3.penup()
apple_size = 2
apple.shapesize(apple_size)

apple_shape = "circle"
apple.shape(apple_shape)

apple_fill_color = "pink"
apple.fillcolor(apple_fill_color)

wn.bgpic("background.gif")
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

# This call to the onkeypress function sets draw_an_A as the function
# that will be called when the "a" key is pressed.

wn.listen()


def draw_apple(active_apple):
    letter_placement_x = 0
    letter_placement_y = 0
    active_apple.shape(apple_image)
    letter_placement_x = active_apple.xcor()
    letter_placement_y = active_apple.ycor()
    drawer.penup()
    drawer.hideturtle()
    drawer.goto(letter_placement_x - 15, letter_placement_y - 35)
    drawer.pendown()
    drawer.showturtle()
    drawer.color("white")
    drawer.write("A" , font=("Arial", 35, "bold"))
    drawer.penup()
    drawer.hideturtle()


    wn.update()


def apple_fall():
    apple.setheading(270)

    distance = 160 + apple.ycor()
    y = apple.ycor()
    drawer.clear()
    while (y >= -150):
        apple.forward(10)
        #apple.xcor()

        print("y values is:", apple.ycor())
        y = y - 10
    new_x = rand.randint(-120,120)
    new_y = rand.randint(0,120)
    apple.clear()
    apple.penup()
    apple.hideturtle()
    apple.goto(new_x,new_y)
    apple.showturtle()






def reset_apple():
    rand_x = rand.randint(90, -91)
    rand_y = rand.randint(0, 151)


#-----function calls-----

draw_apple(apple)

wn.onkeypress(apple_fall, "a")

wn.listen()

wn.mainloop()
