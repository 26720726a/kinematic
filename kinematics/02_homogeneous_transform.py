import math


# ==============================
# 4x4 Matrix Multiplication
# ==============================
#  크기가 같은 행렬 곱셈 
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


# ==============================
# Homogeneous Transformation
# X,Y,Z rotation + Translation
# ==============================
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

# ==============================
# Transformation Inverse 역행렬
# ==============================

def transform_inverse(T):

    # Rotation
    R = [
        [T[0][0], T[0][1], T[0][2]],
        [T[1][0], T[1][1], T[1][2]],
        [T[2][0], T[2][1], T[2][2]]
    ]

    # Translation
    p = [
        T[0][3],
        T[1][3],
        T[2][3]
    ]

    # R transpose
    RT = [
        [R[0][0], R[1][0], R[2][0]],
        [R[0][1], R[1][1], R[2][1]],
        [R[0][2], R[1][2], R[2][2]]
    ]

    # -R^T p
    new_p = []

    for i in range(3):

        value = 0

        for j in range(3):
            value += RT[i][j] * p[j]

        new_p.append(-value)

    return [
        [RT[0][0], RT[0][1], RT[0][2], new_p[0]],
        [RT[1][0], RT[1][1], RT[1][2], new_p[1]],
        [RT[2][0], RT[2][1], RT[2][2], new_p[2]],
        [0, 0, 0, 1]
    ]


# ==============================
# Example
# ==============================

T01 = transform_z(
    math.radians(30),
    1,
    0,
    0
)

T12 = transform_z(
    math.radians(45),
    1,
    0,
    0
)

T02 = matrix_multiply(T01, T12)

for row in T02:
    print(row)