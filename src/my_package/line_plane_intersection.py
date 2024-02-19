
# Define the equations for the line
x_equation = lambda t: 1741.5593993137145 + (-0.0003320294304289967 * t)
y_equation = lambda t: 9000.000000000007 + (0.9999999999999953 * t)
z_equation = lambda t: 6907.421515901685 + (-0.002394062028697528 * t)

# Define the parameters of the plane
plane_point = (1740.934101, 14799, 6896.186)
plane_normal = (0.0004812788134277012, 1, -0.0037210960361140242)

# Calculate the intersection point by solving for t
t = ((plane_point[0] - x_equation(0)) * plane_normal[0] +
     (plane_point[1] - y_equation(0)) * plane_normal[1] +
     (plane_point[2] - z_equation(0)) * plane_normal[2]) / (
         plane_normal[0] * (x_equation(1) - x_equation(0)) +
         plane_normal[1] * (y_equation(1) - y_equation(0)) +
         plane_normal[2] * (z_equation(1) - z_equation(0)))

x_intersection = x_equation(0) + t * (x_equation(1) - x_equation(0))
y_intersection = y_equation(0) + t * (y_equation(1) - y_equation(0))
z_intersection = z_equation(0) + t * (z_equation(1) - z_equation(0))

# Print the intersection point
print(f"Intersection Point: ({x_intersection}, {y_intersection}, {z_intersection})")
