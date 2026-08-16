#2dof말단 
import sys
import math

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

data = sys.stdin.read().split()

for i in range(4):
    data[i]=float(data[i])

data[0] = math.radians(data[0])
data[1] = math.radians(data[1])

point1=transform_z(data[0],data[2],0,0)
point2=transform_z(data[1],data[3],0,0)

final=matrix_multiply(point1,point2)

print(f"{final[0][3]:.4f}, {final[1][3]:.4f}")

