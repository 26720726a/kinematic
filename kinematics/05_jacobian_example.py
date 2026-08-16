import math
import sys


def jacobian(L1, L2, theta1, theta2):
    J11 = -L1 * math.sin(theta1) - L2 * math.sin(theta1 + theta2)
    J12 = -L2 * math.sin(theta1 + theta2)
    J21 = L1 * math.cos(theta1) + L2 * math.cos(theta1 + theta2)
    J22 = L2 * math.cos(theta1 + theta2)
    return [[J11, J12], [J21, J22]]


def end_effector_velocity(J, theta1_dot, theta2_dot):
    x_dot = J[0][0] * theta1_dot + J[0][1] * theta2_dot
    y_dot = J[1][0] * theta1_dot + J[1][1] * theta2_dot
    return x_dot, y_dot


def determinant_2x2(J):
    return J[0][0] * J[1][1] - J[0][1] * J[1][0]


def main():
    data = sys.stdin.read().split()

    L1 = float(data[0])
    L2 = float(data[1])

    t1 = math.radians(float(data[2]))
    t2 = math.radians(float(data[3]))

    v1 = float(data[4])
    v2 = float(data[5])

    J = jacobian(L1, L2, t1, t2)
    det_J = determinant_2x2(J)

    # 1행: 특이점 판정
    if abs(det_J) < 1e-9:
        print('Singular')
        return

    print(f'{det_J:.4f}')

    # 2행: 손끝 속도
    x_dot, y_dot = end_effector_velocity(J, v1, v2)
    print(f'{x_dot:.4f} {y_dot:.4f}')

    # 3행: 속력 + 안전 검사
    speed = math.sqrt(x_dot**2 + y_dot**2)
    if speed > 2.0:
        print(f'{speed:.4f} DANGER')
    else:
        print(f'{speed:.4f}')


main()