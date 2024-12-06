
dt = 0.0001

t=0
t_f = 10

# We know F = -mv^2/r for centripetal motion
# Modeling a tornado air particle and simplifying to only include gravity
# and sum F_c acting on it to keep it in tornado
# m approximated to 28.96 g/mol
# v approximately 50 m/s
# r approximately 20 m

m = 0.02896
v = 86
r = 20
x = 0

F_c = (-m*(v**2))/r

a_y = F_c/m # m/s

while t<t_f:
    v = v + a_y*dt
    x = x + v*dt

    t = t+dt

    print(f'This is velocity {v}, position {x}, and time {t}')