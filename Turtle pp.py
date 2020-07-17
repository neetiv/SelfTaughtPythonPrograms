import turtle
t = turtle.Pen()

print(''' Turtle Programming Puzzles
''')



print('''#1: Drawing an Octagon:
''')


def myoctagon(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(0,8):
        t.forward(size)
        t.left(45)
    if filled == True:
        t.end_fill()

myoctagon(100, False)


print('''#2: Drawing a Filled Octagon:
''')

t.reset()

def myoctagon(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(0,8):
        t.forward(size)
        t.left(45)
    if filled == True:
        t.end_fill()
        
t.color(0.898, 0.169, 0.314)
myoctagon(100, True)

t.color(0,0,0)
myoctagon(100, False)



print('''#3: Another Star Drawing Function:
''')


t.reset()
def draw_star(size, points, angle, filled):
    if filled == True:
        t.begin_fill()
    for x in range(0, points):
        t.forward(size)
        t.left(angle)
    if filled == True:
        t.end_fill()

t.color(0.502, 0.094, 0.094)
draw_star(100, 8, 225, True)

t.color(1, 1, 1)
draw_star(100, 8, 225, False)
    


