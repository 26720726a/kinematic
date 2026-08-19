"""
LEVEL 17 - 가장 가까운 충전소

[문제]
N x M 격자가 주어진다.

0 : 이동 가능
1 : 장애물
2 : 충전소

로봇은 시작 좌표 (sx, sy)에서 출발한다.
상하좌우로 이동할 수 있다.

가장 가까운 충전소까지의 최소 이동 횟수를 출력하시오.
충전소에 도달할 수 없다면 -1을 출력한다.

좌표는 0부터 시작한다.

[예제 입력]
5 5
0 0 0 1 2
1 1 0 1 0
0 0 0 0 0
0 1 1 1 0
2 0 0 0 0
2 2

[예제 출력]
4
"""

from collections import deque

N, M = map(int, input().split())

grid = []

for _ in range(N):
    grid.append(list(map(int, input().split())))

sx, sy = map(int, input().split())

distance = [
    [-1] * M
    for _ in range(N)
]

queue = deque()

queue.append((sx, sy))
distance[sx][sy] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = -1

while queue:
    x, y = queue.popleft()

    if grid[x][y] == 2:
        answer = distance[x][y]
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N:
            continue

        if ny < 0 or ny >= M:
            continue

        if grid[nx][ny] == 1:
            continue

        if distance[nx][ny] != -1:
            continue

        distance[nx][ny] = distance[x][y] + 1
        queue.append((nx, ny))

print(answer)
