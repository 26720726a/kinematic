"""
LEVEL 4 - 가장 가까운 점

[문제]
로봇의 위치가 원점 (0, 0)이다.
N개의 점 (x, y)가 주어질 때 원점에서 가장 가까운 점의 번호와
거리를 출력하시오.

점 번호는 1부터 시작하며,
거리는 소수점 둘째 자리까지 출력한다.

[예제 입력]
4
3 4
1 1
5 2
2 2

[예제 출력]
2 1.41
"""

import math

N = int(input())

min_distance = float("inf")
min_index = -1

for i in range(N):
    x, y = map(float, input().split())

    distance = math.sqrt(x**2 + y**2)

    if distance < min_distance:
        min_distance = distance
        min_index = i

print(min_index + 1, f"{min_distance:.2f}")
