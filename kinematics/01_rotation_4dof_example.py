# 문제: 4-DOF 로봇팔의 최종 방향
#
#θ1 = 30°
#θ2 = -45°
#θ3 = 60°
#θ4 = 15°

#direction = [1, 0]
import math

def rotation_2d(theta):

    c = math.cos(theta)
    s = math.sin(theta)

    R = [
        [c, -s],
        [s,  c]
    ]

    return R


def matrix_vector_multiply(A, v):

    result = []

    for i in range(len(A)):

        value = 0

        for j in range(len(v)):
            value += A[i][j] * v[j]

        result.append(value)

    return result


degrees=[30,-45,60,15]
new_point = [1, 0]
Rs=[]

for i in degrees:
    radians = math.radians(i)  # 라디안 변환 된 행렬
    Rs=rotation_2d(radians)  # 회전 행렬로 값 변환 
    new_point=matrix_vector_multiply(Rs, new_point)

print(new_point)

