print('Classes Programming Puzzles')
print('''
''')
print('#1 The Giraffe Shuffle')

class Animate:
    pass
class Animals(Animate):
    pass
class Mammals(Animals):
    def dance(self):
        print('''
        left foot forward
        left foot back
        right foot forward
        right foot back
        left foot back
        right foot back
        right foot forward
        left foot forward''')
class Giraffes(Mammals):
    def _init_(self, dance):
        self.giraffe_dance = dance
    
reginald = Giraffes()
print('Do the Reginald Dance!!')
reginald.dance()

print('''
''')
print('#2 The Turtle Pitchfork')

import turtle
q = turtle.Pen()
w = turtle.Pen()
e = turtle.Pen()
r = turtle.Pen()
q.backward(30)
q.forward(90)
w.forward(70)
e.forward(70)
r.forward(60)
q.left(90)
q.forward(60)
q.right(90)
q.forward(100)
w.left(90)
w.forward(35)
w.right(90)
w.forward(45)
r.right(90)
r.forward(60)
r.left(90)
r.forward(100)
e.right(90)
e.forward(35)
e.left(90)
e.forward(45)
