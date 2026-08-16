import sys
import math


def inverse_kinematics(x, y, L1, L2):

    # 코사인 법칙: D = cos(theta2)
    D = (x * x + y * y - L1 * L1 - L2 * L2) / (2 * L1 * L2)

    # 도달 가능성 검사
    if D < -1.0 or D > 1.0:
        return None

    # 부동소수점 보정 (1.00000000002 같은 값 클램핑)
    D = max(-1.0, min(1.0, D))

    # 해 1 (elbow down)
    sin_theta2_1 = math.sqrt(max(0.0, 1 - D * D))
    theta2_1 = math.atan2(sin_theta2_1, D)
    theta1_1 = (
        math.atan2(y, x)
        - math.atan2(
            L2 * math.sin(theta2_1),
            L1 + L2 * math.cos(theta2_1)
        )
    )

    # 해 2 (elbow up)
    sin_theta2_2 = -math.sqrt(max(0.0, 1 - D * D))
    theta2_2 = math.atan2(sin_theta2_2, D)
    theta1_2 = (
        math.atan2(y, x)
        - math.atan2(
            L2 * math.sin(theta2_2),
            L1 + L2 * math.cos(theta2_2)
        )
    )

    return (
        (theta1_1, theta2_1),
        (theta1_2, theta2_2)
    )


data = sys.stdin.read().split()

L1 = float(data[0])
L2 = float(data[1])

x = float(data[2])
y = float(data[3])

final = inverse_kinematics(x, y, L1, L2)

if final is not None:
    for theta1, theta2 in final:
        print(f"{math.degrees(theta1):.4f} {math.degrees(theta2):.4f}")
else:
    print("Fail")