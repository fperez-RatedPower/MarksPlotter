import numpy as np
import matplotlib.pyplot as plt
from one_base_mark import *

value_range = np.linspace(-1, 1, num=1000)

# Compute the marks for the quadratic mode
quad_simple = [compute_mark_from_zero_quadratic(v) for v in value_range]
quad_plus_linear = [compute_mark_from_zero_quadratic(v, linear_factor=-1) for v in value_range]
quad_dampened = [compute_mark_from_zero_quadratic(v, quadratic_factor=-0.5) for v in value_range]

# Compute for bandwidth 0.4
q_factor = compute_quad_factor_bandwidth(0.4)
q_factor_linear = compute_quad_factor_bandwidth(0.4, linear_factor=-0.5)
quad_band = [compute_mark_from_zero_quadratic(v, quadratic_factor=q_factor) for v in value_range]
quad_band_linear = [compute_mark_from_zero_quadratic(v, quadratic_factor=q_factor_linear, linear_factor=-0.5)
                    for v in value_range]

# Compute the linear mode
linear = [compute_mark_from_zero_linear(v) for v in value_range]

# Plot the results
plt.plot(value_range, quad_simple, label="quad")
plt.plot(value_range, quad_plus_linear, label="quad linear")
plt.plot(value_range, quad_dampened, label="quad damp")
plt.plot(value_range, quad_band, label="quad band")
plt.plot(value_range, quad_band_linear, label="quad band lin")
plt.plot(value_range, linear, label="linear")

plt.legend()
plt.grid()
plt.show()
