from vpython import *

def multi_particles_on_rotating_disk(g, rotation_speed, ball_mass, num_particles=10):
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
    t_f = 100  # simulate for 10 seconds
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
        particle = sphere(pos=vector(x_pos, -8, z_pos), radius=1, color=color.red, make_trail=True)

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
            Fnet = Fc + Fg + Flift

            # Update motion
            accel = Fnet / ball_mass
            particle.velocity = particle.velocity + accel * dt
            particle.pos = particle.pos + particle.velocity * dt

        # Manage simulation speed
        rate(frequency)
        time += dt

# Parameters chosen:
# g = 9.8 m/s²
# rotation_speed = 0.5 rad/s (about 50 m/s at 100 m radius)
# ball_mass = 0.001 kg (1 gram of air)
# num_particles = 10 (adjust this as desired)
multi_particles_on_rotating_disk(g=9.8, rotation_speed=0.5, ball_mass=0.001, num_particles=10)
