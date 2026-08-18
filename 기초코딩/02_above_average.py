"""
LEVEL 2 - 평균보다 큰 값의 개수

[문제]
N개의 실수가 주어진다.
전체 데이터의 평균보다 큰 데이터의 개수를 출력하시오.

[예제 입력]
5
10 20 30 40 50

[예제 출력]
2
"""

N = int(input())
numbers = list(map(float, input().split()))

average = sum(numbers) / N

count = 0

for number in numbers:
    if number > average:
        count += 1

print(count)
