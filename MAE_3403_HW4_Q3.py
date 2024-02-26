# MAE 3403 HW4 Problem b
# Hayden Gray
"""Given: [ 3 1 -1] [x1]      [2]
          [ 1 4 1]  [x2]  =  [12]
          [ 2 1 2]  [x3]     [10]

          [1 -10 2 4]    [x1]   [2]
          [3  1  4 12]   [x2]   [12]
          [9  2  3  4]   [x3] = [21]
          [-1 2  7  3]   [x4]   [37]                     """

# Required: solve the given matrix problems using scipy and numpy and provide a nice output

import numpy as np
from scipy.linalg import solve

# Define the first matrix
a1 = np.array([[3, 1, -1], [1, 4, 1], [2, 1, 2]])
b1 = np.array([2, 12, 10])
# Employ the solve module to solve for x on the first matrix
x1 = solve(a1, b1)

# Define output for the first solution
print("Solution for the first Matrix:")
print(x1)

# Define the second matrix
a2 = np.array([[1, -10, 2, 4], [3, 1, 4, 12], [9, 2, 3, 4], [-1, 2, 7, 3]])
b2 = np.array([2, 12, 21, 37])
# Employ the solve module to solve for x on the second matrix
x2 = solve(a2, b2)

# Define output for the second solution
print("Solution for the second Matrix:")
print(x2)
