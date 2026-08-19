"""
LEVEL 15 - 센서 데이터 큐 처리

[문제]
센서 데이터가 시간 순서대로 들어온다.

A x : 값 x를 큐 뒤에 추가
R   : 가장 오래된 값을 제거
Q   : 현재 큐의 맨 앞 값을 출력

Q 시 큐가 비어 있으면 EMPTY 출력.
R 시 큐가 비어 있으면 아무 작업도 하지 않는다.

[예제 입력]
7
A 10
A 20
Q
R
Q
R
Q

[예제 출력]
10
20
EMPTY
"""

from collections import deque

N = int(input())

queue = deque()

for _ in range(N):
    command = input().split()

    if command[0] == "A":
        queue.append(int(command[1]))

    elif command[0] == "R":
        if queue:
            queue.popleft()

    elif command[0] == "Q":
        if queue:
            print(queue[0])
        else:
            print("EMPTY")
