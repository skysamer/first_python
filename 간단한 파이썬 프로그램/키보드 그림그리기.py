import turtle as t

def turn_right():
    t.seth(0)
    t.fd(10)

def turn_up():
    t.seth(90)
    t.fd(10)

def turn_left():
    t.seth(180)
    t.fd(10)

def turn_down():
    t.seth(270)
    t.fd(10)

def black():
    t.clear()


t.shape("turtle")
t.speed(0)
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank, "Escape")
t.listen()
t.mainloop()
