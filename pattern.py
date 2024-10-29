import turtle
t = turtle.Turtle()
t.shape(name="turtle")
t.speed(0)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

for i in range(500):
  t.forward(i)
  t.left(500)
