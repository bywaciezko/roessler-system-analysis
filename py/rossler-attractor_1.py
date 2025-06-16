import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MaxNLocator, FormatStrFormatter

# Parameters
a = 0.2
b = 0.2
c = 5.25


# Rössler system
def rossler(t, state):
    x, y, z = state
    return [-y - z, x + a * y, b + z * (x - c)]


# Define the total simulation time and the time step
total_time = 5000
dt = 0.001
t_span = np.arange(0, total_time, dt)

# Define the transient time duration (e.g., discard the first 100 time units)
transient_time = total_time / 2

# Find the index corresponding to the transient time
transient_idx = int(transient_time / dt)

# integrate
initial_state = [0.1, 0, 0]
sol = solve_ivp(rossler, [t_span[0], t_span[-1]], initial_state, t_eval=t_span)

# discard transient
t = sol.t[transient_idx:]
x, y, z = (
    sol.y[0, transient_idx:],
    sol.y[1, transient_idx:],
    sol.y[2, transient_idx:],
)

# --- Poincaré Section Calculation ---
x_section = []
y_section = []
z_section = []

# Iterate through the trajectory to find intersections with x=0, y<0
for i in range(1, len(x)):
    # Check for a crossing of the x=0 plane
    # and ensure y < 0 for the specific section
    if (x[i - 1] < 0 and x[i] >= 0) or (x[i - 1] > 0 and x[i] <= 0):
        if y[i] < 0:  # Ensure y is negative
            # Use linear interpolation to find the exact crossing point if needed,
            # but for visualization, simply taking the current point is often sufficient.
            x_section.append(x[i])
            y_section.append(y[i])
            z_section.append(z[i])

# --- Plotting ---
fig = plt.figure(figsize=(10, 8))  # Adjusted figure size for a single plot

# Create a single 3D subplot
ax = fig.add_subplot(111, projection="3d")  # Changed to 111 for a single plot

# Plot the Rössler attractor
ax.plot(x, y, z, color="gray", linewidth=0.5, alpha=0.6)

# Plot the identified section points
ax.scatter(
    x_section,
    y_section,
    z_section,
    color="red",
    s=20,
)

# Draw the plane x=0 for better visualization (optional)
y_plane = np.linspace(min(y) - 3, max(y), 100)
z_plane = np.linspace(-3, 4, 100)
Y_plane, Z_plane = np.meshgrid(y_plane, z_plane)
X_plane = np.zeros_like(Y_plane)

# Mask out the region where y >= 0
mask = Y_plane >= 0
X_plane_masked = np.copy(X_plane)
Y_plane_masked = np.copy(Y_plane)
Z_plane_masked = np.copy(Z_plane)

X_plane_masked[mask] = np.nan
Y_plane_masked[mask] = np.nan
Z_plane_masked[mask] = np.nan

# Plot the semi-transparent plane
ax.plot_surface(
    X_plane_masked,
    Y_plane_masked,
    Z_plane_masked,
    alpha=0.1,
    color="blue",
    rstride=100,
    cstride=100,
)


# Set plot titles and labels
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.view_init(elev=25, azim=250)
# Format axis ticks
ax.xaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax.yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax.zaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax.xaxis.set_major_locator(MaxNLocator(5))
ax.yaxis.set_major_locator(MaxNLocator(5))
ax.zaxis.set_major_locator(MaxNLocator(5))

ax.set_zlim(-4, 20)
ax.set_ylim(-15, 10)
plt.tight_layout()
plt.savefig("../images/section_with_points.png", bbox_inches="tight", dpi=500)
plt.show()
