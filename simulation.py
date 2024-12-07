from vpython import *

scene = canvas(width=400, height=400, background=vec(1, 1, 1))

earth_cylinder = cylinder(pos=vec(0, 0, 0), axis=vec(0, 1, 0), radius=10, length=10, color=color.yellow)

earth_ball = sphere(pos=earth_cylinder.pos + earth_cylinder.axis * earth_cylinder.length, radius=5, color=color.blue)

earth = compound([earth_cylinder, earth_ball])

particle = sphere(pos=vec(-200, 0, 0), radius=10, color=color.yellow, make_trail=True)
velocity = vec(0.1, 0, 0)
dt = 0.1

while particle.pos.x < 800:
    rate(30)
    particle.pos += particle.pos + velocity*dt


while True:
    rate(10)
    earth.rotate(angle=0.05, axis=earth_cylinder.axis, origin=earth_cylinder.pos)  # Rotate around its own axis
