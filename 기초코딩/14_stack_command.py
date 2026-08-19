"""
LEVEL 14 - 로봇 명령 Undo

[문제]
로봇 제어 명령이 순서대로 주어진다.

P x : 명령 x를 스택에 저장
U   : 가장 최근 명령 하나를 취소
Q   : 현재 가장 최근 명령 출력

Q에서 스택이 비어 있으면 EMPTY를 출력한다.

[예제 입력]
7
P MOVE
P LEFT
Q
U
Q
U
Q

[예제 출력]
LEFT
MOVE
EMPTY
"""

N = int(input())

stack = []

for _ in range(N):
    command = input().split()

    if command[0] == "P":
        stack.append(command[1])

    elif command[0] == "U":
        if stack:
            stack.pop()

    elif command[0] == "Q":
        if stack:
            print(stack[-1])
        else:
            print("EMPTY")
