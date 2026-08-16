import sys
import math


def transform_x(theta, x, y, z):
    c = math.cos(theta)
    s = math.sin(theta)
    return [
        [1, 0,  0, x],
        [0, c, -s, c*y - s*z],
        [0, s,  c, s*y + c*z],
        [0, 0,  0, 1]
    ]

def transform_y(theta, x, y, z):
    c = math.cos(theta)
    s = math.sin(theta)
    return [
        [ c, 0, s,  c*x + s*z],
        [ 0, 1, 0,  y],
        [-s, 0, c, -s*x + c*z],
        [ 0, 0, 0,  1]
    ]

def transform_z(theta, x, y, z):
    c = math.cos(theta)
    s = math.sin(theta)
    return [
        [c, -s, 0, c*x - s*y],
        [s,  c, 0, s*x + c*y],
        [0,  0, 1, z],
        [0,  0, 0, 1]
    ]

def matrix_multiply(A, B):
    result = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                result[i][j] += A[i][k] * B[k][j]
    return result


AXIS_VEC = {'x': [1, 0, 0], 'y': [0, 1, 0], 'z': [0, 0, 1]}


def forward_all(joints):
    """각 관절 직전의 좌표계를 전부 저장하며 FK 수행"""
    T = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    frames = [T]
    for axis, func, theta, dx, dy, dz in joints:
        T = matrix_multiply(T, func(theta, dx, dy, dz))
        frames.append(T)
    return frames


def cross(a, b):
    """3차원 외적"""
    return [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]


def position_jacobian(joints, frames):
    """위치 자코비안 (3 x n)"""
    p_ee = [frames[-1][r][3] for r in range(3)]
    n = len(joints)
    J = [[0.0]*n for _ in range(3)]
    for i in range(n):
        axis = joints[i][0]
        F = frames[i]
        a = AXIS_VEC[axis]
        # z_i: 관절 i 회전축 (베이스 기준)
        z_i = [F[r][0]*a[0] + F[r][1]*a[1] + F[r][2]*a[2] for r in range(3)]
        # p_i: 관절 i 위치
        p_i = [F[r][3] for r in range(3)]
        # 위치 기여 = z_i x (p_ee - p_i)
        lin = cross(z_i, [p_ee[r] - p_i[r] for r in range(3)])
        for r in range(3):
            J[r][i] = lin[r]
    return J


def transpose(M):
    return [[M[r][c] for r in range(len(M))] for c in range(len(M[0]))]


def inverse_3x3(M):
    """3x3 역행렬 (여인수 방식). 특이하면 None"""
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]

    det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    if abs(det) < 1e-12:
        return None

    # 여인수
    A =  (e*i - f*h); B = -(d*i - f*g); C =  (d*h - e*g)
    D = -(b*i - c*h); E =  (a*i - c*g); F = -(a*h - b*g)
    G =  (b*f - c*e); H = -(a*f - c*d); I =  (a*e - b*d)

    # 수반행렬(여인수의 전치) / det
    return [
        [A/det, D/det, G/det],
        [B/det, E/det, H/det],
        [C/det, F/det, I/det]
    ]


def pseudo_inverse(J):
    """J+ = J^T (J J^T)^-1. 특이하면 None"""
    Jt = transpose(J)                       # n x 3
    JJt = matrix_multiply(J, Jt)            # 3 x 3
    JJt_inv = inverse_3x3(JJt)
    if JJt_inv is None:
        return None
    return matrix_multiply(Jt, JJt_inv)     # n x 3


def mat_vec(M, v):
    return [sum(M[r][c]*v[c] for c in range(len(v))) for r in range(len(M))]


def main():
    data = sys.stdin.read().split()

    Ls = [float(data[i]) for i in range(6)]
    tx, ty, tz = float(data[6]), float(data[7]), float(data[8])
    ts = [math.radians(float(data[i+9])) for i in range(6)]

    for _ in range(100):
        joints = [
            ('z', transform_z, ts[0], 0,     0, Ls[0]),
            ('y', transform_y, ts[1], Ls[1], 0, 0),
            ('y', transform_y, ts[2], Ls[2], 0, 0),
            ('x', transform_x, ts[3], Ls[3], 0, 0),
            ('y', transform_y, ts[4], Ls[4], 0, 0),
            ('x', transform_x, ts[5], Ls[5], 0, 0),
        ]

        frames = forward_all(joints)
        T = frames[-1]

        ex = tx - T[0][3]
        ey = ty - T[1][3]
        ez = tz - T[2][3]
        e = [ex, ey, ez]

        if math.sqrt(ex**2 + ey**2 + ez**2) < 1e-6:
            f_t = [math.atan2(math.sin(a), math.cos(a)) for a in ts]
            print(' '.join(f'{math.degrees(v):.4f}' for v in f_t))
            return

        J = position_jacobian(joints, frames)

        Jplus = pseudo_inverse(J)
        if Jplus is None:
            print('Singular')
            return

        dtheta = mat_vec(Jplus, e)
        for i in range(6):
            ts[i] += dtheta[i]

    print('Fail')


main()
