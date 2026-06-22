import numpy as np
import matplotlib.pyplot as plt

# Domain
x = np.linspace(-1, 1, 5000)
x = np.linspace(-0.5, 0.5, 5000)
x = np.linspace(-0.2, 0.2, 5000)
x = np.linspace(-0.1, 0.1, 5000)

# Systems
f = x**2
g = x**2 + 0.001 * np.sin(100 * x)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x, f, label="f(x) = x²")
plt.plot(x, g, label="g(x) = x² + 0.001 sin(100x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("EX-001: Structural Similarity Under Perturbation")
plt.legend()
plt.grid(True)

plt.show()