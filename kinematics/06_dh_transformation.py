import math


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
# Classic DH Matrix 
# ==============================

def dh_classic(
    theta, # 관절각
    d, # 오프셋
    a, #링크 길이 
    alpha # 비틀림 
):

    ct = math.cos(theta)
    st = math.sin(theta)

    ca = math.cos(alpha)
    sa = math.sin(alpha)

    return [
        [ct,-st * ca,st * sa,a * ct],
        [st,ct * ca,-ct * sa,a * st],
        [0,sa,ca,d],
        [0,0,0,1]
    ]

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
