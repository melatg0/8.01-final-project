from vpython import *

scene = canvas(width=400, height=400, background=vec(1, 1, 1))
earth = ellipsoid(pos=vec(0, 0, 0), length=100, height=10, width=100, color=color.blue)
earth.rotate(axis=vec(0, 1, 0), angle=pi / 3, origin=vec(0, 0, 0))

while True:
    pass