from vpython import *

def multi_particles_on_rotating_disk(g, rotation_speed, ball_mass, num_particles_per_layer, num_layers):
    # Set up the scene
    scene = canvas()
    scene.caption = (
        "Rotate the camera by dragging with the right mouse button.\n"
        "To zoom, drag with left+right mouse buttons or use the mouse pad.\n"
        "Touch screen: pinch/extend to zoom, swipe or two-finger rotate."
    )

    # Create the rotating disk (representing the ground or reference plane)
    floor = cylinder(pos=vector(0, -8, 0), axis=vector(0, 0.01, 0), radius=100, color=color.blue)

    # Time parameters
    time = 0
    dt = 0.001
    t_f = 10  # simulate for 10 seconds
    frequency = 1/dt

    # Angular velocity vector of the disk (about the y-axis)
    rotation_speed_vec = vector(0, rotation_speed, 0)

    # Gravity vector
    g_vec = vector(0, -g, 0)

    # Parameters for layering
    # Assume top is smaller radius and each layer moves upward
    top_radius = 20
    bottom_radius = floor.radius
    height_per_layer = 5  # vertical spacing between layers
    radius_step = (bottom_radius - top_radius) / (num_layers - 1)

    particles = []
    for layer in range(num_layers):
        # Compute the radius for this layer
        current_radius = bottom_radius - layer * radius_step
        # Compute the vertical position for this layer
        y_pos = layer * height_per_layer

        for i in range(num_particles_per_layer):
            angle = 2 * pi * i / num_particles_per_layer
            x_pos = current_radius * cos(angle)
            z_pos = current_radius * sin(angle)

            # Create the particle
            particle = sphere(pos=vector(x_pos, y_pos, z_pos), radius=1, color=color.red)

            # Initial tangential velocity: v = ω × r
            r_vector = particle.pos - floor.pos
            tan_vel = cross(rotation_speed_vec, r_vector)

            # Add a vertical upward velocity component to get them started
            tan_vel += vector(0,10,0)

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

            # Lift force equal to -Fg to cancel gravity (just for demonstration)
            Flift = -Fg

            # Net force
            Fnet = Fc + Fg + Flift

            # Update motion
            accel = Fnet / ball_mass
            particle.velocity = particle.velocity + accel * dt
            particle.pos = particle.pos + particle.velocity * dt

        # Manage simulation speed
        rate(frequency)
        time += dt

def user_input(): 
    global omega, ball_mass, num_particles_per_layer, num_layers
    omega = float(input("What is the wind speed/rotation speed of your tornado? "))
    ball_mass = float(input("What is the mass of your air particle? "))
    num_particles_per_layer = int(input("How many air particles per layer would you like? "))
    num_layers = int(input("How many layers would you like? "))

def print_stats(accel, vel, v_mag, pos):
    print(f"Acceleration Vector: {accel} m/s^2")
    print(f"Velocity Magnitude: {v_mag} m/s")
    print(f"Velocity Vector: {vel} m/s")
    print(f"Ball Position: {pos} m")
    print("----------------------------------------------------")

# Example call with parameters
multi_particles_on_rotating_disk(g=9.8, rotation_speed=2, ball_mass=0.001, num_particles_per_layer=10, num_layers=5)
