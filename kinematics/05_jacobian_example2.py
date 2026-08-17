'''문제: 자코비안 기반 반복법 역기구학 (2링크)

링크 길이 L₁, L₂인 2링크 평면 로봇팔의 목표 위치 (x, y)가 주어질 때, 자코비안 반복법(뉴턴 방식) 으로 관절 각도를 구하라.

알고리즘 (이 순서로 구현)

초기 각도 θ = (θ₁⁰, θ₂⁰)에서 시작 (입력으로 주어짐)
현재 각도에서 FK로 손끝 위치 (xc, yc) 계산
오차 e = (x − xc, y − yc) 계산
‖e‖ = √(ex² + ey²) < 1e-6이면 수렴 → 종료
현재 각도에서 자코비안 J(2×2) 계산
det(J) 검사: |det(J)| < 1e-9이면 특이점 → Singular 출력 후 종료
Δθ = J⁻¹ · e 계산
θ ← θ + Δθ로 갱신, 2번으로
100회 반복해도 수렴 안 하면 Fail 출력
'''
import sys
import math

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
    data=sys.stdin.read().split()

    L1 = float(data[0])
    L2 = float(data[1])

    x = float(data[2])
    y = float(data[3])

    t1 = math.radians(float(data[4]))
    t2 = math.radians(float(data[5]))

    for i in range(100):
        x_i,y_i,phi_i = forward_kinematics(L1,L2,t1,t2) # 현재 위치 계산 
        #오차 계산 
        ex=x-x_i
        ey=y-y_i
        # 가까우면 종료 
        if ex**2 + ey**2 < 1e-6:
            # atan2를 이용해서 각도를 -180~180d으로 맞춤 
            n_t1 = math.atan2(math.sin(t1), math.cos(t1))
            n_t2 = math.atan2(math.sin(t2), math.cos(t2))
            print(f'{math.degrees(n_t1):.4f} {math.degrees(n_t2):.4f}')
            return
        else:
            J=jacobian(L1,L2,t1,t2)
            det_J=determinant_2x2(J)
            if abs(det_J) < 1e-9:
                print('Singular')
                return
            else:
                J_inv = [[ J[1][1] / det_J, -J[0][1] / det_J],[-J[1][0] / det_J,  J[0][0] / det_J]] # 역행렬 J 구하기
                dt1, dt2 = end_effector_velocity(J_inv, ex, ey) # J^-1*e
                t1=t1+dt1
                t2=t2+dt2
    print('Fail')

main()
