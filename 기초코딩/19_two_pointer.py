"""
LEVEL 19 - 연속 구간 합

[문제]
모든 값이 양수인 N개의 센서 데이터가 주어진다.
연속된 일부 구간의 합이 정확히 S가 되는 구간의 개수를 출력하시오.

[예제 입력]
6 5
1 2 3 2 1 5

[예제 출력]
3

설명:
2+3
3+2
5
"""

N, S = map(int, input().split())

data = list(map(int, input().split()))

left = 0
current_sum = 0
count = 0

for right in range(N):
    current_sum += data[right]

    while current_sum > S and left <= right:
        current_sum -= data[left]
        left += 1

    if current_sum == S:
        count += 1

print(count)
