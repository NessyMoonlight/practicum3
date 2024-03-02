import turtle
pen= turtle.Turtle()
pen.color("blue", "blue")
pen.begin_fill()

pen.circle(-100, 120)
position = pen.pos()
pen.goto(0, -100)

pen.end_fill()

pen.penup()
pen.goto(position[0] + 20, position[1] + 85)
pen.pendown()
pen.write("A", move=False, align="left", font=("Arial", 8, "normal"))


pen.penup()
pen.goto(position)
pen.pendown()


pen.color("red", "red")
pen.begin_fill()
pen.circle(-100, 100)
position = pen.pos()
pen.goto(0, -100)

pen.end_fill()

pen.penup()
pen.goto(position[0] + 85, position[1] - 40)
pen.pendown()
pen.write("B", move=False, align="left", font=("Arial", 8, "normal"))


pen.penup()
pen.goto(position)
pen.pendown()


pen.color("orange", "orange")
pen.begin_fill()
pen.circle(-100, 80)
position = pen.pos()
pen.goto(0, -100)

pen.end_fill()

pen.penup()
pen.goto(position[0] - 40, position[1] - 80)
pen.pendown()
pen.write("C", move=False, align="left", font=("Arial", 8, "normal"))


pen.penup()
pen.goto(position)
pen.pendown()


pen.color("green", "green")
pen.begin_fill()
pen.circle(-100, 40)
position = pen.pos()
pen.goto(0, -100)

pen.end_fill()

pen.penup()
pen.goto(position[0] - 40, position[1] - 10)
pen.pendown()
pen.write("D", move=False, align="left", font=("Arial", 8, "normal"))


pen.penup()
pen.goto(position)
pen.pendown()


pen.color("purple", "purple")
pen.begin_fill()
pen.circle(-100, 20)
position = pen.pos()
pen.goto(0, -100)

pen.end_fill()

pen.penup()
pen.goto(position[0] - 20, position[1] + 10)
pen.pendown()
pen.write("E", move=False, align="left", font=("Arial", 8, "normal"))


pen.penup()
pen.goto(100, 100)

input()