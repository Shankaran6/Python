import numpy as np

# ---- INPUTS ----
AB = float(input("Enter length AB: "))
BC = float(input("Enter length BC: "))
CD = float(input("Enter length CD: "))
AD = float(input("Enter length AD: "))

theta_A = float(input("Enter angle BAD (deg): "))
omega_AB = float(input("Enter angular velocity of AB (rad/s): "))

# ---- CONVERT ----
theta_A = np.radians(theta_A)

# ---- POINTS ----
A = np.array([0.0, 0.0])
D = np.array([AD, 0.0])

# Position of B
B = np.array([
    AB * np.cos(theta_A),
    AB * np.sin(theta_A)
])

# ---- FIND POINT C (circle intersection) ----
# From B and D
d = np.linalg.norm(D - B)

# Check feasibility
if d > (BC + CD) or d < abs(BC - CD):
    raise ValueError("Invalid geometry: links cannot form a closed chain.")

# Unit vector from B to D
e = (D - B) / d

# Distance from B to midpoint of intersection
x = (BC**2 - CD**2 + d**2) / (2*d)

# Height of triangle
h = np.sqrt(BC**2 - x**2)

# Perpendicular direction
perp = np.array([-e[1], e[0]])

# Two possible solutions → choose upper one
C = B + x*e + h*perp

# ---- VELOCITY OF B ----
v_B = omega_AB * np.array([
    -AB * np.sin(theta_A),
     AB * np.cos(theta_A)
])

# ---- SOLVE omega_BC ----
r_CB = C - B
r_CD = C - D

def perp_vec(v):
    return np.array([-v[1], v[0]])

# Constraint: v_C ⟂ CD
num = -np.dot(v_B, r_CD)
den = np.dot(perp_vec(r_CB), r_CD)

omega_BC = num / den

# ---- MIDPOINT VELOCITY ----
M = (B + C) / 2
r_MB = M - B

v_M = v_B + omega_BC * perp_vec(r_MB)

# ---- OUTPUT ----
print("\n--- Results ---")
print(f"Point C: {C}")
print(f"Angular velocity of BC: {omega_BC:.5f} rad/s")

speed_M = np.linalg.norm(v_M)
print(f"Velocity of midpoint magnitude: {speed_M:.5f}")
print(f"Velocity vector of midpoint: {v_M}")