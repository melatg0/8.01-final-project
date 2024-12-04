from vpython import *

scene = canvas(width=400, height=400, background=vec(1, 1, 1))
earth = cylinder(pos=vec(0, 0, 0), axis=vec(0, 0, 300), color=color.yellow)
earth.rotate(angle=-pi / 2, origin=vec(0, 0, 0))

particle = sphere(pos=vec(-200, 0, 0), radius=10, color=color.yellow, make_trail=True)
velocity = vec(0.1, 0, 0)
dt = 0.1

while particle.pos.x < 400:
    rate(30)
    particle.pos += particle.pos + velocity*dt


while True:
    pass