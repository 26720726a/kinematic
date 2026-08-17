import math
import sys

# ==============================
# Matrix Multiplication
# ==============================

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

                result[i][j] += (
                    A[i][k] * B[k][j]
                )

    return result

# ==============================
# Modified DH Matrix 
# ==============================
def dh_modified(theta, d, a, alpha):
    ct = math.cos(theta)
    st = math.sin(theta)
    ca = math.cos(alpha)
    sa = math.sin(alpha)
    return [
        [ct,     -st,     0,   a],
        [st*ca,   ct*ca, -sa, -sa*d],
        [st*sa,   ct*sa,  ca,  ca*d],
        [0,       0,      0,   1]
    ]

data=sys.stdin.read().split()

n=int(data[0])
T = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]   # 단위행렬
link=[]
for i in range(n):
    alpha=math.radians(float(data[4*i+1]))
    a=float(data[4*i+2])
    theta=math.radians(float(data[4*i+3]))
    d=float(data[4*i+4])
    link=dh_modified(theta,d,a,alpha)
    T=matrix_multiply(T,link)

print(f"{T[0][3]:.4f} {T[1][3]:.4f} {T[2][3]:.4f}")
