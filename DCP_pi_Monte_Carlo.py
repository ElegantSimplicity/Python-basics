""" DCP_pi_Monte_Carlo.py
This problem was asked by Google.

The area of a circle is defined as πr^2.
Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.

The following code is done by Bard
https://g.co/bard/share/3163346d5522 
"""

import random

# Define the radius of the circle
r = 1

# Define the number of points to generate
N = 1000

# Generate random points in the square
points = []
for _ in range(N):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    points.append((x, y))

# Count the number of points that fall inside the circle
hits = 0
for point in points:
    if point[0] ** 2 + point[1] ** 2 <= r ** 2:
        hits += 1

# Calculate the estimated value of π
pi = 4 * hits / N

# Print the estimated value of π
print("Estimated value of π:", pi)

import matplotlib.pyplot as plt

# Plot the points
plt.scatter([point[0] for point in points], [point[1] for point in points], c=['blue' if point[0] ** 2 + point[1] ** 2 > r ** 2 else 'red' for point in points])

# Add a circle
plt.Circle((0, 0), r, fill=False, color='black')

# Add a title and labels
plt.title("Monte Carlo Simulation for Estimating π")
plt.xlabel("x")
plt.ylabel("y")

# Show the plot
plt.show()
