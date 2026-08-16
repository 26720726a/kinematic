import math


# ==============================
# 2D Rotation Matrix
# ==============================

def rotation_2d(theta):

    c = math.cos(theta)
    s = math.sin(theta)

    R = [
        [c, -s],
        [s,  c]
    ]
    print(R)

    return R


# ==============================
# X-axis Rotation Matrix
# ==============================

def rotation_x(theta):

    c = math.cos(theta)
    s = math.sin(theta)

    R = [
        [1, 0, 0],
        [0, c, -s],
        [0, s,  c]
    ]

    return R


# ==============================
# Y-axis Rotation Matrix
# ==============================

def rotation_y(theta):

    c = math.cos(theta)
    s = math.sin(theta)

    R = [
        [ c, 0, s],
        [ 0, 1, 0],
        [-s, 0, c]
    ]

    return R


# ==============================
# Z-axis Rotation Matrix
# ==============================

def rotation_z(theta):

    c = math.cos(theta)
    s = math.sin(theta)

    R = [
        [c, -s, 0],
        [s,  c, 0],
        [0,  0, 1]
    ]

    return R


# ==============================
# Matrix × Vector
# ==============================
# 행렬 A 와 v 곱하기 
def matrix_vector_multiply(A, v):

    result = []

    for i in range(len(A)):

        value = 0

        for j in range(len(v)):
            value += A[i][j] * v[j]

        result.append(value)

    return result


# ==============================
# Example
# ==============================
# (1,0)을 원점 기준으로 90 도 회전 
theta = math.radians(90)

R = rotation_2d(theta)

point = [1, 0]

new_point = matrix_vector_multiply(R, point)

print(new_point)