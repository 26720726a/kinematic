"""
LEVEL 1 - 배열의 합

[문제]
N개의 정수가 주어질 때 모든 정수의 합을 출력하시오.

[입력]
첫째 줄: N
둘째 줄: N개의 정수

[예제 입력]
5
1 2 3 4 5

[예제 출력]
15
"""

N = int(input())
numbers = list(map(int, input().split()))

total = 0

for number in numbers:
    total += number

print(total)
