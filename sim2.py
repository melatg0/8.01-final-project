from vpython import *

def multi_particles_on_rotating_disk(g, rotation_speed, ball_mass, num_particles):
    # Set up the scene
    scene = canvas()
    scene.caption = (
        "Rotate the camera by dragging with the right mouse button.\n"
        "To zoom, drag with left+right mouse buttons or use the mouse pad.\n"
        "Touch screen: pinch/extend to zoom, swipe or two-finger rotate."
    )

    # Create the rotating disk
    floor = cylinder(pos=vector(0, -8, 0), axis=vector(0, 0.01, 0), radius=100, color=color.blue)

    # Time parameters
    time = 0
    dt = 0.001
    t_f = 10  # simulate for 10 seconds TODO: change back to 100 seconds
    frequency = 1/dt

    # Angular velocity vector of the disk (about the y-axis)
    rotation_speed_vec = vector(0, rotation_speed, 0)

    # Gravity vector
    g_vec = vector(0, -g, 0)

    # Number of particles
    # We'll spread them evenly around the circle
    particles = []
    for i in range(num_particles):
        angle = 2 * pi * i / num_particles
        x_pos = floor.radius * cos(angle)
        z_pos = floor.radius * sin(angle)
        # Each particle will be placed at a different position around the circumference
        # at the same vertical level (-8 on y-axis)
        particle = sphere(pos=vector(x_pos, 0, z_pos), radius=1, color=color.red)#, make_trail=True)

        # Initial tangential velocity: v = ω × r
        r_vector = particle.pos - floor.pos
        tan_vel = cross(rotation_speed_vec, r_vector)

        # Add a vertical upward velocity component
        tan_vel += vector(0,10,0) # Initial upward "kick"

        particle.velocity = tan_vel
        
        # Store particle data
        particles.append(particle)

    while time < t_f:
        # Rotate the disk about its center
        angle = rotation_speed * dt
        floor.rotate(angle=angle, axis=vector(0,1,0), origin=floor.pos)

        for particle in particles:
            # Update forces and motion for each particle

            # Recompute radius vector each iteration
            r_vector = particle.pos - floor.pos
            r_mag = mag(r_vector)
            r_hat = r_vector / r_mag

            # Particle speed and velocity magnitude
            v_mag = mag(particle.velocity)

            # Centripetal force
            Fc = -ball_mass * (v_mag**2 / r_mag) * r_hat

            # Gravity force
            Fg = ball_mass * g_vec

            # Lift force equal to -Fg to cancel gravity
            Flift = -Fg

            # Net force
            Fnet = Fc + Fg + Flift # Fg and Flift cancels out

            # Update motion
            accel = Fnet / ball_mass
            particle.velocity = particle.velocity + accel * dt
            particle.pos = particle.pos + particle.velocity * dt

            # Print motion statistics in terminal
            if abs(time - round(time)) < 1e-9:
                print_stats(accel, particle.velocity, v_mag, particle.pos)

        # Manage simulation speed
        rate(frequency)
        time += dt

def user_input(): 
    global omega, ball_mass, num_particles
    omega = float(input("What is the wind speed/rotation speed of your tornado? "))
    ball_mass = float(input("What is the mass of your air particle? "))
    num_particles = int(input("How many air particles per layer would you like? "))


def print_stats(accel, vel, v_mag, pos):
    print(f"Acceleration Vector: {accel} m/s^2")
    print(f"Velocity Magnitude: {v_mag} m/s")
    print(f"Velocity Vector: {vel} m/s")
    print(f"Ball Position: {pos} m")
    print("----------------------------------------------------")

# Parameters chosen:
# g = 9.8 m/s²
# rotation_speed = 0.5 rad/s (about 50 m/s at 100 m radius) --> can vary!
# ball_mass = 0.001 kg (1 gram of air)
# num_particles = 10 (adjust this as desired)

# version for testing
multi_particles_on_rotating_disk(g=9.8, rotation_speed=2, ball_mass=0.001, num_particles=10)

# version with user input
# user_input()
# multi_particles_on_rotating_disk(9.8, omega, ball_mass, num_particles)

