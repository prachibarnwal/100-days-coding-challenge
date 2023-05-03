import turtle
t = turtle.Turtle()
t.begin_fill()
t.screen.bgcolor("CYAN")
k = 0
col = ['black','brown','navy','violet','indigo','blue','purple','cyan','darkgreen','green','lightgreen','yellow','gold','pink','magenta','orange','red','chocolate','silver']
t.goto(0,-200)
for i in range(190,0,-10):
    t.begin_fill()
    t.color(col[k])
    k += 1
    t.circle(i)
    t.end_fill()
t
turtle.done()
