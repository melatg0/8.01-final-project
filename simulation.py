from vpython import *

scene = canvas(width=400, height=400, background=vec(1, 1, 1))
earth = cylinder(pos=vec(0, 0, 0), axis=vec(100, 0, 0), color=color.yellow)
earth.rotate(angle=-pi / 2, origin=vec(0, 0, 0))

while True:
    pass