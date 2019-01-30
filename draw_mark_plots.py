import numpy as np
import matplotlib.pyplot as plt
from one_base_mark import *

value_range = np.linspace(-5, 5, num=1000)

# Compute the marks for the quadratic mode
simple_normal = [compute_mark_from_zero_quadratic(v, quadratic_factor=-0.5) for v in value_range]
simple_important = [compute_mark_from_zero_quadratic(v) for v in value_range]
simple_super_important = [compute_mark_from_zero_quadratic(v, quadratic_factor=-2.0) for v in value_range]

# Compute for bandwidth 0.4
bandWidth = 10
q_factor = compute_quad_factor_bandwidth(bandWidth)
width_normal = [compute_mark_from_zero_quadratic(v, quadratic_factor=q_factor) for v in value_range]

# Compute the linear mode
linear = [compute_mark_from_zero_linear(v) for v in value_range]

# Plot the results
plt.plot(value_range, simple_normal, label="Simple normal")
plt.plot(value_range, simple_important, label="Simple Important")
plt.plot(value_range, simple_super_important, label="Simple Super Important")
plt.plot(value_range, width_normal, label="Width normal w=0.4")
plt.plot(value_range, linear, label="linear")

plt.legend()
plt.grid()
plt.show()
