"""
LEVEL 16 - 연결된 자유 공간 개수

[문제]
N x M 격자가 주어진다.

0 : 자유 공간
1 : 장애물

상하좌우로 연결된 0들의 집합을 하나의 영역이라고 할 때,
전체 자유 공간 영역의 개수를 출력하시오.

[예제 입력]
4 5
0 0 1 0 0
0 1 1 0 1
1 1 0 0 1
0 0 1 1 0

[예제 출력]
4
"""

N, M = map(int, input().split())

grid = []

for _ in range(N):
    grid.append(list(map(int, input().split())))

visited = [
    [False] * M
    for _ in range(N)
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = True

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

        dfs(nx, ny)


count = 0

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0 and not visited[i][j]:
            dfs(i, j)
            count += 1

print(count)
