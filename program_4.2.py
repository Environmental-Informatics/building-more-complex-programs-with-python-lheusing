# =============================================================================
# # ABE 651 
# # 1/29/2020
# # Logan Heusinger
# # EX 4.2
# # Draw 3 flowers as shown in the book
# see think python 2 section 4 for addition code help
#==============================================================================




from __future__ import print_function, division #imports
import turtle
import math



def polyline(t,n,length,angle): #create a line at angles
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t,r,angle): #using polyline change the line  into arcs
    arc_length = 2 * math.pi * r * angle /360
    n = int(arc_length/ 3 ) + 1
    step_length = arc_length / n
    step_angle = float(angle) /n
    polyline(t,n,step_length,step_angle)


def petal(t, r, angle): # arcs back to back for petal
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    """Draws a flower with n petals.

    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)


def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()


logan = turtle.Turtle()


move(logan, -100)
flower(logan, 7, 60.0, 60.0)

move(logan, 100)
flower(logan, 10, 40.0, 80.0)

move(logan, 100)
flower(logan, 20, 140.0, 20.0)

logan.hideturtle()
turtle.mainloop()

