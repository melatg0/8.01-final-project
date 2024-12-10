from vpython import *

def ball_on_rotating_disk(g, rotation_speed, ball_mass):
    # Set up the scene
    scene = canvas()
    scene.caption = (
        "Rotate the camera by dragging with the right mouse button.\n"
        "To zoom, drag with left+right mouse buttons or use the mouse pad.\n"
        "Touch screen: pinch/extend to zoom, swipe or two-finger rotate."
    )

    # Create the rotating disk    ########### Do not rotate it at first
    floor = cylinder(pos=vector(0, -8, 0), axis=vector(0, 0.01, 0), radius=10, color=color.blue)

    # Create the ball and set its initial position
    ball = sphere(pos=vector(floor.radius, -7, 0), radius = 1, color=color.red, make_trail=True)

    # Time parameters
    time = 0
    dt = 0.001
    t_f = 100
    frequency = 1/dt ###### frequency = 1/dt  change the frequency based on dt

    # Initial velocity

    rotation_speed_vec = vec(0, rotation_speed, 0) #### do not confuse the disk and the ball rotational speed
    # tan_vel= cross(rotation_speed_vec, FILL IN HERE)  ########### TODO Calculate here the initial tangential velocity
                                 ###### draw vectors to figure out which vectors to multiply
    ball.velocity = tan_vel ############### Here we force to have only tangential initial velocity . If you want
         ##### once you get the circular motion try to add a vector with a vertical component and see what happens!

    ############ TODO calculate here  centripetal force (CHECK SIGN!)

    # Fc = FILL IN
    # Fnet = Fc    ############ IF you want after add gravity and  lift (in the vertical, y direction)


    # Simulation loop
    #while time < 2*dt:  # small time interval used for debugging
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

        # Calculating centripetal force requires tangential velocity; Assuming the ball
        # is traveling at the same rotational speed as the disk, we can convert
        # the ball's rotation speed into its tangential velocity:
        '''tan_velocity = floor.radius * rotation_speed # tangential velocity is in theta-hat dir.
        ball.velocity = vector(0, tan_velocity, 0) # ****will likely need to be changed
        Fc = -ball_mass * ((tan_velocity) ** 2)/floor.radius # radial force
        Fcx = vector(Fc * cos(angle), 0, 0)
        Fcy = vector(0, Fc * sin(angle), 0)
        Fnet = Fg + Fcx + Fcy'''

        #STEP 1 calculate acceleration. Find v and pos after dt EXPLAIN WHY IN THE PRESENTATION!


        ball.accel = Fnet/ball_mass
        ball.velocity = ball.velocity + ball.accel*dt
        ball.pos = ball.pos + ball.velocity*dt

        #STEP 2 calculate force with new velocity

        Fc = ball_mass * cross(ball.velocity, rotation_speed_vec) ######## CHECK SIGN
        #Fc = -ball_mass * mag(ball.velocity)**2/floor.radius * ball.pos/mag(ball.pos)
        #print(ball.pos)
        #print(ball.velocity )
        #print(Fc)
        Fnet = Fc


        # Manage simulation speed
        rate(frequency)

        # Update time
        time += dt

# Call the function with gravitational acceleration and rotation speed
ball_on_rotating_disk(g=9.8, rotation_speed= 2 * pi / 2, ball_mass=0.1) # TODO change mass to be something smaller
