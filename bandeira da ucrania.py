import turtle

t=turtle.Turtle("turtle")
ecra=turtle.getscreen()
for i in range(2):
    t.begin_fill()
    t.color("black","blue")
    t.forward(250)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.end_fill()
t.begin_fill()
t.color("black","yellow")
for i in range(1):
    t.right(270)
    t.forward(70)
    t.left(270)
    t.forward(250)
    t.left(270)
    t.forward(70)
t.end_fill()
#Esquecer informação
t.penup()
t.forward(1000)
t.pendown()
ecra.mainloop()