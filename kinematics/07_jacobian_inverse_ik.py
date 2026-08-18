# ============================================================
# 07_jacobian_inverse_ik.py
#
# 2-Link Planar Robot - Jacobian Inverse Kinematics
#
# 목표:
#   목표 손끝 좌표 (target_x, target_y)가 주어졌을 때
#   Jacobian의 역행렬(Pseudo-Inverse)을 이용하여
#   theta1, theta2를 반복적으로 수정한다.
#
# 핵심 공식:
#
#   error = target_position - current_position
#
#   dq = J^+ @ error
#
#   q_new = q_old + alpha * dq
#
#   J^+ : Jacobian Pseudo-Inverse
#
# ============================================================

import math
import numpy as np


# ------------------------------------------------------------
# Forward Kinematics
# 현재 관절각을 이용하여 End-Effector 위치 계산
# ------------------------------------------------------------
def forward_kinematics(L1, L2, theta1, theta2):

    x = (
        L1 * math.cos(theta1)
        + L2 * math.cos(theta1 + theta2)
    )

    y = (
        L1 * math.sin(theta1)
        + L2 * math.sin(theta1 + theta2)
    )

    return np.array([x, y])


# ------------------------------------------------------------
# Jacobian 계산
#
# [x_dot]   [J11 J12] [theta1_dot]
# [y_dot] = [J21 J22] [theta2_dot]
# ------------------------------------------------------------
def jacobian(L1, L2, theta1, theta2):

    J11 = (
        -L1 * math.sin(theta1)
        - L2 * math.sin(theta1 + theta2)
    )

    J12 = -L2 * math.sin(theta1 + theta2)

    J21 = (
        L1 * math.cos(theta1)
        + L2 * math.cos(theta1 + theta2)
    )

    J22 = L2 * math.cos(theta1 + theta2)

    J = np.array([
        [J11, J12],
        [J21, J22]
    ])

    return J


# ------------------------------------------------------------
# Jacobian 기반 Inverse Kinematics
# ------------------------------------------------------------
def jacobian_inverse_ik(
    L1,
    L2,
    target_x,
    target_y,
    theta1,
    theta2,
    alpha=0.1,
    tolerance=0.001,
    max_iterations=1000
):

    # 목표 위치
    target = np.array([
        target_x,
        target_y
    ])

    for i in range(max_iterations):

        # ----------------------------------------------------
        # 1. 현재 End-Effector 위치 계산
        # ----------------------------------------------------
        current_position = forward_kinematics(
            L1,
            L2,
            theta1,
            theta2
        )

        # ----------------------------------------------------
        # 2. 목표 위치와 현재 위치의 오차 계산
        #
        # error = 목표 위치 - 현재 위치
        # ----------------------------------------------------
        error = target - current_position


        # ----------------------------------------------------
        # 3. 오차의 크기 계산
        # ----------------------------------------------------
        error_norm = np.linalg.norm(error)


        # ----------------------------------------------------
        # 4. 목표 위치에 충분히 가까워졌으면 종료
        # ----------------------------------------------------
        if error_norm < tolerance:

            print("목표 위치에 도달했습니다.")
            print("반복 횟수:", i)

            break


        # ----------------------------------------------------
        # 5. 현재 관절각에서 Jacobian 계산
        # ----------------------------------------------------
        J = jacobian(
            L1,
            L2,
            theta1,
            theta2
        )


        # ----------------------------------------------------
        # 6. Jacobian Pseudo-Inverse 계산
        #
        # 일반 inverse:
        # J_inv = np.linalg.inv(J)
        #
        # 하지만 특이점 근처에서는 inverse 계산이 불안정하므로
        # pseudo-inverse를 사용하는 것이 더 안전하다.
        # ----------------------------------------------------
        J_pinv = np.linalg.pinv(J)


        # ----------------------------------------------------
        # 7. 필요한 관절각 변화량 계산
        #
        # dq = J^+ * error
        #
        # dq[0] = theta1 변화량
        # dq[1] = theta2 변화량
        # ----------------------------------------------------
        dq = J_pinv @ error


        # ----------------------------------------------------
        # 8. 관절각 업데이트
        #
        # alpha:
        # 한 번에 얼마나 움직일지 결정하는 비율
        # 너무 크면 발산할 수 있다.
        # ----------------------------------------------------
        theta1 = theta1 + alpha * dq[0]
        theta2 = theta2 + alpha * dq[1]


    else:

        print("최대 반복 횟수까지 목표에 도달하지 못했습니다.")


    # --------------------------------------------------------
    # 최종 End-Effector 위치
    # --------------------------------------------------------
    final_position = forward_kinematics(
        L1,
        L2,
        theta1,
        theta2
    )


    return theta1, theta2, final_position


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # 로봇 링크 길이
    # --------------------------------------------------------
    L1 = 1.0
    L2 = 1.0


    # --------------------------------------------------------
    # 목표 End-Effector 위치
    #
    # 시험에서 목표 좌표가 바뀌면
    # 여기만 수정하면 된다.
    # --------------------------------------------------------
    target_x = 1.0
    target_y = 1.0


    # --------------------------------------------------------
    # 초기 관절각
    #
    # Degree → Radian 변환
    # --------------------------------------------------------
    theta1 = math.radians(20)
    theta2 = math.radians(20)


    # --------------------------------------------------------
    # Jacobian IK 실행
    # --------------------------------------------------------
    theta1, theta2, final_position = jacobian_inverse_ik(
        L1,
        L2,
        target_x,
        target_y,
        theta1,
        theta2
    )


    # --------------------------------------------------------
    # 결과 출력
    # --------------------------------------------------------
    print()

    print("===== 결과 =====")

    print(
        "theta1:",
        math.degrees(theta1),
        "degree"
    )

    print(
        "theta2:",
        math.degrees(theta2),
        "degree"
    )

    print(
        "End-Effector Position:",
        final_position
    )

    print(
        "Target Position:",
        [target_x, target_y]
    )
