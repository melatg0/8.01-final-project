from vpython import *

def ball_on_rotating_disk(g, rotation_speed, ball_mass):
    # Set up the scene
    scene = canvas()
    scene.caption = (
        "Rotate the camera by dragging with the right mouse button.\n"
        "To zoom, drag with left+right mouse buttons or use the mouse pad.\n"
        "Touch screen: pinch/extend to zoom, swipe or two-finger rotate."
    )

    # Create the rotating disk
    floor = cylinder(pos=vector(0, -8, 0), axis=vector(0, 0.01, 0), radius=10, color=color.blue)

    # Create the ball and set its initial position
    ball = sphere(pos=vector(floor.radius, -7, 0), radius=1, color=color.red, make_trail=True)

    # Time parameters
    time = 0
    dt = 0.01
    t_f = 100
    frequency = 100

    # Simulation loop
    while time < t_f:
        # Rotate the disk about its center of mass (COM)
        angle = rotation_speed * dt  # Incremental rotation angle
        floor.rotate(angle=angle, axis=vector(0, 1, 0), origin=floor.pos)

        # Update the ball's position to stay on the disk
        # Calculate the new position of the ball based on the rotation
        #x_new = floor.radius * cos(rotation_speed * time)
        #z_new = floor.radius * sin(rotation_speed * time)
        #ball.pos = vector(x_new, ball.pos.y, z_new)  # Update ball's position

        # Update ball's position based on the net force acting upon it;
        # We are defining net force to be centripetal force + gravity

        Fg = vector(0, 0, -ball_mass*g)
        # Calculating centripetal force requires tangential velocity; Assuming the ball
        # is traveling at the same rotational speed as the disk, we can convert
        # the ball's rotation speed into its tangential velocity:
        '''tan_velocity = floor.radius * rotation_speed # tangential velocity is in theta-hat dir.
        ball.velocity = vector(0, tan_velocity, 0) # ****will likely need to be changed
        Fc = -ball_mass * ((tan_velocity) ** 2)/floor.radius # radial force
        Fcx = vector(Fc * cos(angle), 0, 0)
        Fcy = vector(0, Fc * sin(angle), 0)
        Fnet = Fg + Fcx + Fcy'''
        rotation_speed_vec = vec(0, 0, rotation_speed)
        ball.velocity = cross(rotation_speed_vec, ball.axis)
        Fc = ball_mass * cross(ball.velocity, rotation_speed_vec)
        Fnet = Fc+Fg

        ball.accel = Fnet/ball_mass

        ball.velocity = ball.velocity + ball.accel*dt
        ball.pos = ball.pos + ball.velocity*dt


        # Manage simulation speed
        rate(frequency)

        # Update time
        time += dt

# Call the function with gravitational acceleration and rotation speed
ball_on_rotating_disk(g=9.8, rotation_speed=2 * pi / 2, ball_mass=0.1) # change mass to be something smaller



