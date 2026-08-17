'''
문제: DH 파라미터 기반 순기구학

로봇팔이 DH 테이블로 주어진다. 각 관절의 DH 파라미터 (θ, d, a, α)를 이용해 말단(end-effector)의 위치를 구하라.

DH 규약: 각 관절의 변환행렬은 dh_matrix(θ, d, a, α)로 계산하고, 이를 관절 순서대로 곱하면 베이스→말단 변환이 된다.

T0n=T1⋅T2⋯Tn

입력 (표준입력)

n                          (관절 개수, 정수)
θ₁ d₁ a₁ α₁                (1번 관절의 DH 파라미터 4개)
θ₂ d₂ a₂ α₂                (2번 관절)
...
θₙ dₙ aₙ αₙ                (n번 관절)
θと α는 degree로 주어진다 (라디안 변환 필요)
d와 a는 길이 (변환 불필요)

출력
말단 위치를 소수점 넷째 자리까지:

x y z
'''
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

data= sys.stdin.read().split()

n=int(data[0])

thetas, ds, a, alpha=[] ,[], [], []
links=[]

for i in range(n):
    thetas.append(math.radians(float(data[4*i+1])))
    ds.append(float(data[4*i+2]))
    a.append(float(data[4*i+3]))
    alpha.append(math.radians(float(data[4*i+4])))
    links.append(dh_classic(thetas[i],ds[i],a[i],alpha[i]))

T = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]   # 단위행렬

for i in range(n):
    T=matrix_multiply(T,links[i])

print(f"{T[0][3]:.4f} {T[1][3]:.4f} {T[2][3]:.4f}")
