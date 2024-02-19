import sympy as sp

# Define the variables and parameters
t = sp.symbols('t')
line1 = {
    'x_equation': 1740.1674698770705 + -0.00041275919818083644*t,
    'y_equation': 9199.885845431521 + 0.9999951161667939*t,
    'z_equation': 6907.453730255026 + -0.002284165243153896*t,
}
line2 = {
    'x_equation': 1740.3639088583027 + -0.0003505546711384246*t,
    'y_equation': 9000.0 + 1.0*t,
    'z_equation': 6907.568884414786 + -0.002023615139355317*t,
}

# Calculate the direction vectors of the lines
vector1 = [line1['x_equation'].diff(t), line1['y_equation'].diff(t), line1['z_equation'].diff(t)]
vector2 = [line2['x_equation'].diff(t), line2['y_equation'].diff(t), line2['z_equation'].diff(t)]

# Calculate the dot product of the direction vectors
dot_product = sum(vector1[i] * vector2[i] for i in range(3))

# Calculate the magnitudes of the direction vectors
magnitude1 = sp.sqrt(sum(vector1[i]**2 for i in range(3)))
magnitude2 = sp.sqrt(sum(vector2[i]**2 for i in range(3)))

# Calculate the cosine of the angle between the lines
cosine_theta = dot_product / (magnitude1 * magnitude2)

# Calculate the angle in degrees
angle_degrees = sp.acos(cosine_theta) * 180 / sp.pi

# Print the angle in degrees without showing pi
angle_degrees_no_pi = angle_degrees.evalf()
print("Angle between the lines:", angle_degrees_no_pi)
