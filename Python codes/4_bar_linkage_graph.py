import numpy as np
import matplotlib.pyplot as plt

# ---- INPUTS ----
AB = float(input("Enter AB: "))
BC = float(input("Enter BC: "))
CD = float(input("Enter CD: "))
AD = float(input("Enter AD: "))
omega_AB = float(input("Enter angular velocity of AB (rad/s): "))

# ---- STORAGE ----
angles = []
velocities = []

# ---- PERP FUNCTION ----
def perp(v):
    return np.array([-v[1], v[0]])

# ---- LOOP OVER INPUT ANGLE ----
for theta_deg in range(0, 361, 2):
    theta = np.radians(theta_deg)

    # Points
    A = np.array([0.0, 0.0])
    D = np.array([AD, 0.0])

    B = np.array([
        AB * np.cos(theta),
        AB * np.sin(theta)
    ])

    # Distance BD
    d = np.linalg.norm(D - B)

    # Skip invalid positions
    if d > (BC + CD) or d < abs(BC - CD):
        continue

    # Unit vector
    e = (D - B) / d

    # Geometry
    x = (BC**2 - CD**2 + d**2) / (2*d)
    h = np.sqrt(max(0, BC**2 - x**2))

    perp_dir = np.array([-e[1], e[0]])

    # Choose one configuration
    C = B + x*e + h*perp_dir

    # Velocity of B
    v_B = omega_AB * np.array([
        -AB * np.sin(theta),
         AB * np.cos(theta)
    ])

    # Solve omega_BC
    r_CB = C - B
    r_CD = C - D

    denom = np.dot(perp(r_CB), r_CD)
    if abs(denom) < 1e-6:
        continue

    omega_BC = -np.dot(v_B, r_CD) / denom

    # Velocity of C
    v_C = v_B + omega_BC * perp(r_CB)

    speed_C = np.linalg.norm(v_C)

    angles.append(theta_deg)
    velocities.append(speed_C)

# ---- PLOT ----
plt.figure()
plt.plot(angles, velocities)
plt.xlabel("Input Angle BAD (degrees)")
plt.ylabel("Velocity of Point C (cm $s^{-1}$)")
plt.title("Input Angle vs Velocity of Point C")
plt.grid()

plt.show()