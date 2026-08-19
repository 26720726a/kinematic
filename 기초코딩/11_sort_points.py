"""
LEVEL 11 - 거리 기준 좌표 정렬

[문제]
N개의 점 (x, y)가 주어진다.
각 점의 원점으로부터의 거리 제곱 x^2 + y^2 를 기준으로 오름차순 정렬하시오.

거리 제곱이 같다면 x가 작은 점,
x도 같다면 y가 작은 점을 먼저 출력한다.

[예제 입력]
5
1 2
0 1
2 0
-1 0
1 1

[예제 출력]
-1 0
0 1
1 1
1 2
2 0
"""

N = int(input())

points = []

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort(
    key=lambda p: (
        p[0]**2 + p[1]**2,
        p[0],
        p[1]
    )
)

for x, y in points:
    print(x, y)
