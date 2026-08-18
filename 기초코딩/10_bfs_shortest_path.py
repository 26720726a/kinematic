"""
LEVEL 10 - 격자 최단 경로 BFS

[문제]
N x M 크기의 맵이 주어진다.

0 : 이동 가능
1 : 장애물

로봇은 (0, 0)에서 시작하여 (N-1, M-1)까지 이동한다.
상하좌우로 한 칸씩 이동할 수 있다.

목표까지 필요한 최소 이동 횟수를 출력하시오.
갈 수 없다면 -1을 출력한다.

[예제 입력]
4 4
0 0 1 0
1 0 1 0
0 0 0 0
0 1 1 0

[예제 출력]
6
"""

from collections import deque

N, M = map(int, input().split())

grid = []

for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

# 시작점 또는 도착점이 장애물인 경우
if grid[0][0] == 1 or grid[N - 1][M - 1] == 1:
    print(-1)
else:
    visited = [
        [False] * M
        for _ in range(N)
    ]

    distance = [
        [-1] * M
        for _ in range(N)
    ]

    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()

    queue.append((0, 0))
    visited[0][0] = True
    distance[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N:
                continue

            if ny < 0 or ny >= M:
                continue

            if grid[nx][ny] == 1:
                continue

            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            distance[nx][ny] = distance[x][y] + 1

            queue.append((nx, ny))

    print(distance[N - 1][M - 1])
