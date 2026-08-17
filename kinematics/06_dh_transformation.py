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


# ==============================
# Example: 3-Link Robot
# ==============================

theta1 = math.radians(30)
theta2 = math.radians(45)
theta3 = math.radians(20)

A1 = dh_matrix(theta1,0,1,0)

A2 = dh_matrix(theta2,0,1,0)

A3 = dh_matrix(theta3,0,1,0)

T02 = matrix_multiply(A1,A2)

T03 = matrix_multiply(T02,A3)

print("T03")

for row in T03:

    print(
        " ".join(
            f"{value:.6f}"
            for value in row
        )
    )


# ==============================
# End-Effector Position
# ==============================

x = T03[0][3]
y = T03[1][3]
z = T03[2][3]

print("x =", x)
print("y =", y)
print("z =", z)
