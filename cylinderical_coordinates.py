from vpython import *

cylinder(pos=vector(0,0,0), axis = vector(4, 0, 0), radius = 0.06, color =color.white)

i = arrow(pos=vector(0,0,0), axis = vector(2,0,0), color=color.red)
label(pos=vector(4,0.5,0), text='x', opacity=0, box=False, color=color.black)
label(pos=vector(2,0.5, 0), text='i', opacity=0, box=False, color=color.red)

