from vpython import *

def ball_on_rotating_disk(g, rotation_speed, ball_mass):
    # Set up the scene
    scene = canvas()
    scene.caption = (
        "Rotate the camera by dragging with the right mouse button.\n"
        "To zoom, drag with left+right mouse buttons or use the mouse pad.\n"
        "Touch screen: pinch/extend to zoom, swipe or two-finger rotate."
    )

    # Create the rotating disk (initially not rotated)
    floor = cylinder(pos=vector(0, -8, 0), axis=vector(0, 0.01, 0), radius=10, color=color.blue)

    # Create the ball and set its initial position
    # Position the ball on the perimeter of the disk.
    # We'll place it at (floor.radius, -8, 0) so it's horizontally at the edge.
    ball = sphere(pos=vector(floor.radius, -8, 0), radius=1, color=color.red, make_trail=True)

    # Time parameters
    time = 0
    dt = 0.001
    t_f = 10  # simulate for 10 seconds
    frequency = 1/dt

    # Angular velocity vector of the disk (about the y-axis)
    rotation_speed_vec = vector(0, rotation_speed, 0)

    # Radius vector from the disk center to the ball:
    r_vector = ball.pos - floor.pos  # vector from center of disk to ball

    # Initial tangential velocity: v = ω × r
    tan_vel = cross(rotation_speed_vec, r_vector)

    # If you want to see what happens with a vertical component, uncomment below:
    # tan_vel += vector(0,1,0)  # add a vertical "kick"

    # Assign initial velocity to the ball
    ball.velocity = tan_vel

    # Define gravity vector
    g_vec = vector(0, -g, 0)

    # Initially, we consider centripetal force only. After first step, we add gravity.
    # Centripetal force is directed towards center: Fc = -m * v^2 / r * r_hat
    # where r_hat is the unit vector pointing from ball to center.
    # But since the ball should initially be in uniform circular motion,
    # we can start with that assumption and then let gravity perturb it.

    while time < t_f:
        # Rotate the disk about its center
        angle = rotation_speed * dt
        floor.rotate(angle=angle, axis=vector(0,1,0), origin=floor.pos)

        # STEP 1: Update forces and motion

        # Recompute radius vector each iteration (in case position changes)
        r_vector = ball.pos - floor.pos
        r_mag = mag(r_vector)
        r_hat = r_vector / r_mag

        # Ball speed and velocity magnitude
        v_mag = mag(ball.velocity)

        # Compute centripetal force to maintain circular motion:
        # Fc should point towards the center (negative r_hat)
        # Fc = -m (v²/r) r_hat
        Fc = -ball_mass * (v_mag**2 / r_mag) * r_hat

        # Gravity force
        Fg = ball_mass * g_vec

        # Net force
        Fnet = Fc + Fg

        # If you want to add other forces (like lift), you can do it here:
        # For example, a small upward "lift" force:
        # Flift = vector(0, 0.05, 0)
        # Fnet = Fc + Fg + Flift

        # STEP 2: Update motion
        ball.accel = Fnet / ball_mass
        ball.velocity = ball.velocity + ball.accel * dt
        ball.pos = ball.pos + ball.velocity * dt

        # Manage simulation speed
        rate(frequency)

        # Update time
        time += dt


# Call the function with gravitational acceleration and rotation speed
# Here, rotation_speed = 2π/2 means one full rotation every 2 seconds.
ball_on_rotating_disk(g=9.8, rotation_speed=2*pi/2, ball_mass=0.1)
