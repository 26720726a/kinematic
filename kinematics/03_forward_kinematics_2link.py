import math


# ==============================
# 2-Link Forward Kinematics
# ==============================

def forward_kinematics(L1, L2, theta1, theta2):

    x = (
        L1 * math.cos(theta1)
        + L2 * math.cos(theta1 + theta2)
    )

    y = (
        L1 * math.sin(theta1)
        + L2 * math.sin(theta1 + theta2)
    )

    phi = theta1 + theta2

    return x, y, phi


# ==============================
# Example
# ==============================

L1 = 1.0
L2 = 1.0

theta1 = math.radians(30)
theta2 = math.radians(60)

x, y, phi = forward_kinematics(
    L1,
    L2,
    theta1,
    theta2
)

print(f"x = {x:.6f}")
print(f"y = {y:.6f}")

print(
    f"orientation = "
    f"{math.degrees(phi):.6f} degree"
)