import turtle 

def flower(t, n ,r, angle):
    for i in range(n):
        for i in range (2):
            t.circle(r,angle)
            t.left(180-angle)
        t.left(360/n)

def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()

b = turtle.Pen()
b.hideturtle()
b.color("red")
b.speed(0)


for n in range(3):
    b.pu()
    b.goto(-200,200-(n*100))
    b.pd()
    for i in range(1,5):
        if i == 2 :
            b.color("blue")
        else:
            b.color("red")
        flower(b,4+n,10,180)
        if i == 4:
           break
        move(b,100)
    
