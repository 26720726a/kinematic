import math


# ==============================
# 2-Link Jacobian
# ==============================

def jacobian(
    L1,
    L2,
    theta1,
    theta2
):

    J11 = (-L1 * math.sin(theta1)-L2 * math.sin(theta1 + theta2))

    J12 = (-L2 * math.sin(theta1 + theta2))

    J21 = (L1 * math.cos(theta1)+L2 * math.cos(theta1 + theta2))

    J22 = (L2 * math.cos(theta1 + theta2))

    # [x/t1 x/t2],
    # [y/t1 y/t2]

    return [
        [J11, J12],
        [J21, J22]
    ]


# ==============================
# End-Effector Velocity
# ==============================

def end_effector_velocity(
    J,
    theta1_dot,
    theta2_dot
):

    x_dot = (J[0][0] * theta1_dot+J[0][1] * theta2_dot)

    y_dot = (J[1][0] * theta1_dot+J[1][1] * theta2_dot)

    return x_dot, y_dot


# ==============================
# Determinant
# ==============================

def determinant_2x2(J):
    return (J[0][0] * J[1][1]-J[0][1] * J[1][0])


# ==============================
# Example
# ==============================

L1 = 1.0
L2 = 1.0

theta1 = math.radians(30)
theta2 = math.radians(45)

theta1_dot = 0.1
theta2_dot = 0.2

J = jacobian(
    L1,
    L2,
    theta1,
    theta2
)

x_dot, y_dot = end_effector_velocity(
    J,
    theta1_dot,
    theta2_dot
)

det_J = determinant_2x2(J)

print("Jacobian")

for row in J:
    print(row)

print("x_dot =", x_dot)
print("y_dot =", y_dot)

print("det(J) =", det_J)

if abs(det_J) < 1e-9:
    print("Singular configuration")
else:
    print("Non-singular configuration")