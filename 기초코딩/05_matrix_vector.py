"""
LEVEL 5 - 행렬 × 벡터

[문제]
3x3 행렬 A와 3x1 벡터 x가 주어진다.
y = A x 를 계산하여 출력하시오.

[예제 입력]
1 2 3
4 5 6
7 8 9
1 2 3

[예제 출력]
14 32 50
"""

A = []

for _ in range(3):
    row = list(map(int, input().split()))
    A.append(row)

x = list(map(int, input().split()))

result = []

for i in range(3):
    value = 0

    for j in range(3):
        value += A[i][j] * x[j]

    result.append(value)

print(*result)
