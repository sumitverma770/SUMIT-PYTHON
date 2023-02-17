from turtle import*
fillcolor('yellow')
pencolor('green')
speed(0)
side = 6
for i in range(side):
    fd(200)
    for i in range(side):
        fd(50)
        begin_fill()
        for i in range(side):
            fd(25)
            dot(10)
            for i in range(side)
            fd(25)
            lt(360/side)
            rt(360/side)
        end_fill()
        it(360/side)
    rt(360/side)


hideturtle()
mainloop()
