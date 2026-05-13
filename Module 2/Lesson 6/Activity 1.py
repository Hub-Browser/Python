import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(800,600)
t=turtle.Turtle()

no_s=6
s_l=70
a=360/no_s

for i in range(no_s):
    t.forward(s_l)
    t.right(a)