"""
LEVEL 12 - 방향을 가진 로봇 시뮬레이션

[문제]
로봇은 (0, 0)에서 시작하고 처음에는 북쪽을 바라본다.

명령은 다음과 같다.
F : 현재 방향으로 1칸 전진
L : 왼쪽으로 90도 회전
R : 오른쪽으로 90도 회전

모든 명령 수행 후 최종 x, y, 방향을 출력하시오.

방향 출력:
N, E, S, W

[예제 입력]
7
FFRFFLF

[예제 출력]
2 3 N
"""

N = int(input())
commands = input().strip()

# 북 동 남 서
directions = ["N", "E", "S", "W"]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x = 0
y = 0
direction = 0

for command in commands:
    if command == "L":
        direction = (direction - 1) % 4

    elif command == "R":
        direction = (direction + 1) % 4

    elif command == "F":
        x += dx[direction]
        y += dy[direction]

print(x, y, directions[direction])
