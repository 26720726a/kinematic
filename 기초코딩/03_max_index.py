"""
LEVEL 3 - 최댓값과 위치 찾기

[문제]
N개의 정수가 주어진다.
가장 큰 값과 그 값이 처음 등장한 위치를 출력하시오.
위치는 1부터 시작한다.

[예제 입력]
6
3 7 2 9 9 5

[예제 출력]
9 4
"""

N = int(input())
numbers = list(map(int, input().split()))

max_value = numbers[0]
max_index = 0

for i in range(N):
    if numbers[i] > max_value:
        max_value = numbers[i]
        max_index = i

print(max_value, max_index + 1)
