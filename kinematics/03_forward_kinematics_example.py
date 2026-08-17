import sys
import math

# transform_x, transform_y, transform_z, matrix_multiply는 그대로
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

    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = [
        [0 for _ in range(cols_B)]
        for _ in range(rows_A)
    ]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):

                result[i][j] += A[i][k] * B[k][j]

    return result

def rotation_to_euler(T):
    """회전행렬(T의 3x3)에서 roll, pitch, yaw 추출 (ZYX 오일러)"""
    r00 = T[0][0]
    r10 = T[1][0]
    r20 = T[2][0]
    r21 = T[2][1]
    r22 = T[2][2]

    pitch = math.atan2(-r20, math.sqrt(r00**2 + r10**2))
    roll  = math.atan2(r21, r22)
    yaw   = math.atan2(r10, r00)

    return roll, pitch, yaw

data = sys.stdin.read().split()

for i in range(12):
    data[i] = float(data[i])

for i in range(6):
    data[i] = math.radians(data[i])

# 관절 정의: (변환함수, 각도, x이동, y이동, z이동)
joints = [
    (transform_z, data[0], 0,       0, data[6]),   # 관절1: z회전, z방향 d1
    (transform_y, data[1], data[7], 0, 0),          # 관절2: y회전, x방향 L2
    (transform_y, data[2], data[8], 0, 0),          # 관절3
    (transform_x, data[3], data[9], 0, 0),          # 관절4
    (transform_y, data[4], data[10], 0, 0),         # 관절5
    (transform_x, data[5], data[11], 0, 0),         # 관절6
]

# 단위행렬에서 시작해 오른쪽으로 이어붙이기
T = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

for func, theta, x, y, z in joints:
    T = matrix_multiply(T, func(theta, x, y, z))

roll, pitch, yaw = rotation_to_euler(T)
print(f"{T[0][3]:.4f} {T[1][3]:.4f} {T[2][3]:.4f}")           # 위치
print(f"{math.degrees(roll):.4f} {math.degrees(pitch):.4f} {math.degrees(yaw):.4f}")  # 자세
