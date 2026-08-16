import math

# transform_x, transform_y, transform_z, matrix_multiply는
# 이미 만들어둔 것 그대로 사용

TRANSFORM = {'x': transform_x, 'y': transform_y, 'z': transform_z}
AXIS_VEC  = {'x': [1, 0, 0], 'y': [0, 1, 0], 'z': [0, 0, 1]}


def forward_all(joints, thetas):
    """각 관절이 회전하기 '직전'의 좌표계를 전부 저장하며 FK 수행"""
    T = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    frames = [T]
    for (axis, tx, ty, tz), th in zip(joints, thetas):
        T = matrix_multiply(T, TRANSFORM[axis](th, tx, ty, tz))
        frames.append(T)
    return frames


def cross(a, b):
    """3차원 외적"""
    return [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]


def geometric_jacobian(joints, thetas):
    """
    joints: [(축문자, tx, ty, tz), ...]  예: [('z',0,0,1), ('y',2,0,0), ...]
    thetas: [θ1, θ2, ...] (radian)
    반환: 6 x n 자코비안 (위 3행 = 선속도, 아래 3행 = 각속도)
    """
    frames = forward_all(joints, thetas)
    p_ee = [frames[-1][r][3] for r in range(3)]     # 말단 위치

    n = len(joints)
    J = [[0.0] * n for _ in range(6)]

    for i in range(n):
        F = frames[i]                                # 관절 i 직전 좌표계
        a = AXIS_VEC[joints[i][0]]
        # z_i: 관절 i의 회전축 (베이스 좌표계 기준)
        z_i = [F[r][0]*a[0] + F[r][1]*a[1] + F[r][2]*a[2] for r in range(3)]
        # p_i: 관절 i의 위치
        p_i = [F[r][3] for r in range(3)]
        # 선속도 기여 = z_i × (p_ee − p_i)
        lin = cross(z_i, [p_ee[r] - p_i[r] for r in range(3)])
        for r in range(3):
            J[r][i]     = lin[r]    # 위 3행: 위치
            J[r + 3][i] = z_i[r]    # 아래 3행: 자세
    return J