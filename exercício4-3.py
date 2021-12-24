import turtle
import math


def polyline(t, n, length, angle):
    '''Desenha n segmentos de reta com o comprimento dado e 
    ângulo (em graus) entre eles. t é um turtle.
    '''
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        
        
def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)
    

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)

def circle(t, r)    :
    arc(t, r, 360)    
    
bob = turtle.Turtle()

#arc(bob, 100, 100)
#circle(bob, 100)
for i in range(3, 10):
    polygon(bob, i, 100)        

turtle.mainloop()
