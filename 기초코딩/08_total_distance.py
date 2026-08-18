"""
LEVEL 8 - 로봇 전체 이동 거리

[문제]
로봇이 순서대로 방문한 N개의 좌표가 주어진다.
로봇이 이동한 전체 Euclidean Distance를 계산하시오.

[예제 입력]
4
0 0
3 4
3 8
6 8

[예제 출력]
12.00
"""

import math

N = int(input())

points = []

for _ in range(N):
    x, y = map(float, input().split())
    points.append([x, y])

total_distance = 0

for i in range(N - 1):
    x1 = points[i][0]
    y1 = points[i][1]

    x2 = points[i + 1][0]
    y2 = points[i + 1][1]

    dx = x2 - x1
    dy = y2 - y1

    distance = math.sqrt(dx**2 + dy**2)
    total_distance += distance

print(f"{total_distance:.2f}")
