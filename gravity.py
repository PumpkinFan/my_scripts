# simulating gravitational motion high above Earth's surface 
# motivation: recreate results from: https://sites.pitt.edu/~jdnorton/teaching/HPS_0410/chapters/general_relativity/index.html

# gravitational constant ("big G")
G = 6.67430e-11  # units: N * m^2 / kg^2
MASS_EARTH = 5.972e24  # units: kg
RADIUS_EARTH = 6371000  # units: m


def integrate_motion(x_init, total_time, dt=1e-6):
    current_time = 0
    current_x = x_init
    current_velocity = 0
    while current_time < total_time:
        acceleration = - (G * MASS_EARTH) / (current_x**2)
        current_velocity += acceleration * dt
        current_x += current_velocity * dt
        current_time += dt
        print(current_time)
    return current_x


if __name__ == "__main__":
    x0 = RADIUS_EARTH + 160934  # 100 miles above Earth (in meters)
    t = 18.3
    x0f = integrate_motion(x0, t)
    x1 = RADIUS_EARTH + 162544  # 101 miles above Earth (in meters)
    x1f = integrate_motion(x1, t)
    dist0 = abs(x0f - x0)
    dist1 = abs(x1f - x1)
    print(f"difference {dist0 - dist1}")
