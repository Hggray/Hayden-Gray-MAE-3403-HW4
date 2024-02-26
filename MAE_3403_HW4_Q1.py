# MAE 3403 HW4 Problem a
# Hayden Gray
# Given: P(x<1|N(0,1)): Probability x<1 given a normal distribution with mu=0 and theta=1
# P(x>mu+2*theta|N(175, 3))
# Required: Using Scipy stats and matplotlib.pyplot produce nicely formatted graphs for the problem above
import numpy as np
import matplotlib.pyplot as plot
from scipy.stats import norm

# Set up definition for
# x values of the first distribution in order to calculate y values
x1 = np.linspace(-5, 5, 1000)
y1 = norm.pdf(x1, 0, 1)

# Now that ranges are defined calculate the probability of the value being less than 1
probability1 = norm.cdf(1, 0, 1)

# x values of the second distribution in order to calculate y values
x2 = np.linspace(160, 190, 1000)
y2 = norm.pdf(x2, 175, 3)

# Now that ranges are defined calculate the probability that value is greater than the critical value of mu+2*theta
critical = 175 + 2 * 3
probability2 = 1 - norm.cdf(critical, 175, 3)

# Define plot size
plot.figure(figsize=(12, 6))

# Plot for N(0, 1)
plot.subplot(1, 2, 1)
plot.plot(x1, y1, label='N(0, 1)')
plot.fill_between(x1, y1, where=(x1 < 1), alpha=0.3)
plot.title(f'N(0,1) - Area for P(x < 1): {probability1}')
plot.legend()

# Plot for N(175, 3)
plot.subplot(1, 2, 2)
plot.plot(x2, y2, label='N(175, 3)', color='red')
plot.fill_between(x2, y2, where=(x2 > critical), alpha=0.3, color='red')
plot.title(f'N(175, 3) - Area for P(x > mu + 2*theta): {probability2:.4f}')
plot.legend()

plot.tight_layout()
plot.show()
