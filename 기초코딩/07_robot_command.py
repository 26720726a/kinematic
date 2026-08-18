"""
LEVEL 7 - 로봇 명령 처리

[문제]
로봇은 (0, 0)에서 시작한다.

U : y + 1
D : y - 1
L : x - 1
R : x + 1

N개의 명령을 수행한 후,
최종 위치 x y 와 원점까지의 맨해튼 거리 |x| + |y| 를 출력하시오.

[예제 입력]
6
UURRDL

[예제 출력]
1 1
2
"""

N = int(input())
commands = input().strip()

x = 0
y = 0

for command in commands:
    if command == "U":
        y += 1
    elif command == "D":
        y -= 1
    elif command == "L":
        x -= 1
    elif command == "R":
        x += 1

distance = abs(x) + abs(y)

print(x, y)
print(distance)
