import math


# ==============================
# 2-Link Inverse Kinematics
# ==============================

def inverse_kinematics(x, y, L1, L2):

    # --------------------------------
    # cos(theta2)
    # --------------------------------
    # 코사인 법칙 사용 ( D = 코사인 세타 값)
    D = (x * x+ y * y- L1 * L1- L2 * L2) / (2 * L1 * L2)

    # --------------------------------
    # Reachability Check
    # --------------------------------

    if D < -1.0 or D > 1.0:
        return None

    # Floating point 보정
    # 1.00000000002 같은 값이 나올경우 오차 제거 과정 
    D = max(-1.0, min(1.0, D))


    # ==============================
    # Solution 1
    # 해 1
    # ==============================

    sin_theta2_1 = math.sqrt(max(0.0, 1 - D * D))

    theta2_1 = math.atan2(sin_theta2_1,D)

    theta1_1 = (
        math.atan2(y, x)
        -
        math.atan2(
            L2 * math.sin(theta2_1),
            L1 + L2 * math.cos(theta2_1)
        )
    )


    # ==============================
    # Solution 2
    # 해 2
    # ==============================

    sin_theta2_2 = -math.sqrt(max(0.0, 1 - D * D))

    theta2_2 = math.atan2(sin_theta2_2,D)

    theta1_2 = (
        math.atan2(y, x)
        -
        math.atan2(
            L2 * math.sin(theta2_2),
            L1 + L2 * math.cos(theta2_2)
        )
    )


    return (
        (theta1_1, theta2_1),
        (theta1_2, theta2_2)
    )


# ==============================
# Example
# ==============================

L1 = 1.0
L2 = 1.0

x = 1.0
y = 1.0

solutions = inverse_kinematics(
    x,
    y,
    L1,
    L2
)

if solutions is None:

    print("Unreachable")

else:

    for i, solution in enumerate(
        solutions,
        start=1
    ):

        theta1, theta2 = solution

        print(f"Solution {i}")

        print(
            "theta1 =",
            math.degrees(theta1)
        )

        print(
            "theta2 =",
            math.degrees(theta2)
        )