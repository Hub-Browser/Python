import turtle
turtle.Screen().bgcolor("lightblue")
t=turtle.Turtle()
l=0

while True:
  t.forward(l)
  t.left(90)
  l+=5
t.done()