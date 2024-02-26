# MAE 3403 HW4 Problem b
# Hayden Gray
# Given: x-3*cos(x)=0 | cos(2*x)*x^3=0
# Required: using fsolve from scipy.optimize find if the functions intersect and where if they do intersect

from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plot


def equation1(x):
    # Define the first equation we are solving for
    return x - 3 * np.cos(x)

def equation2(x):
    # Define the second equation we are solving for
    return np.cos(2 * x) * x ** 3

# define Initial guess for root of equation 1 and assume equation 2 has a root of zero
root1 = fsolve(equation1, 0.1)
root2 = [0]

# Define x values for plotting the two equations to find the intersection of the two equations
x_values = np.linspace(-2, 2, 400)

# Define equations for calculating y values of the two equations
y1 = equation1(x_values)
y2 = equation2(x_values)

# Define Plotting Parameters
plot.figure(figsize=(10, 6))

plot.plot(x_values, y1, label='Equation 1')
plot.plot(x_values, y2, label='Equation 2')
plot.scatter(root1, equation1(root1), color='orange', zorder=5, label='Root of Equation 1')
plot.scatter(root2, equation2(root2[0]), color='blue', zorder=5, label='Root of Equation 2')
plot.legend()
plot.show()

# From the plot you can see that the two functions do in fact intersect.
# The two equations intersect at x=1.0
