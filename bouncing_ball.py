from vpython import *

def bouncing_ball_restitution(g, e, vy):
    # Define sphere dimensions and initial conditions
    R = 1
    m = 0.1
    r0 = vector(0, 7.0, 0)
    v0 = vector(0, vy, 0)

    # Set up the scene
    scene = canvas()
    scene.caption = (
        "Rotate the camera by dragging with the right mouse button.\n"
        "To zoom, drag with left+right mouse buttons or use the mouse pad.\n"
        "Touch screen: pinch/extend to zoom, swipe or two-finger rotate."
    )

    # Draw the sphere and disk
    ball = sphere(pos=r0, radius=R, color=color.red)
    ball.velocity = v0

    # Create a disk-shaped surface using a cylinder
    floor = cylinder(pos=vector(0, -8, 0), axis=vector(0, 0.01, 0), radius=10, color=color.blue)

    # Physical parameters
    Fg = m * vector(0.0, -g, 0.0)
    time = 0
    dt = 0.01
    t_f = 10
    frequency = 100

    # Define rotation speed for the disk
    rotation_speed = 2 * pi / 2  # Rotations per second (e.g., 1 rotation every 2 seconds)

    # Simulation loop
    while time < t_f:
        # Calculate acceleration
        ball.accel = Fg / m

        # Handle collision
        overlap = ball.pos.y - R - floor.pos.y
        if overlap > 0:  # Ball is not in contact with the disk
            ball.velocity = ball.velocity + ball.accel * dt
        else:  # Collision with the disk
            ball.velocity.y = -e * ball.velocity.y

        # Update position
        ball.pos = ball.pos + ball.velocity * dt

        # Rotate the disk around the Z-axis
        angle = rotation_speed * time
        floor.up = vector(cos(angle), sin(angle), 0)  # Change the orientation around Z-axis

        # Manage simulation speed
        rate(frequency)

        # Update time
        time += dt

# Call the function with gravitational acceleration, restitution coefficient, and initial velocity
bouncing_ball_restitution(g=9.8, e=0.8, vy=0)
