"""
LEVEL 18 - 구간 센서 합

[문제]
N개의 센서 값이 주어지고 Q개의 질의가 주어진다.

각 질의 l r 에 대해
l번째부터 r번째까지 센서 값의 합을 출력하시오.

인덱스는 1부터 시작한다.

[예제 입력]
5 3
10 20 30 40 50
1 3
2 5
4 4

[예제 출력]
60
140
40
"""

N, Q = map(int, input().split())

data = list(map(int, input().split()))

prefix = [0] * (N + 1)

for i in range(N):
    prefix[i + 1] = prefix[i] + data[i]

for _ in range(Q):
    l, r = map(int, input().split())

    result = prefix[r] - prefix[l - 1]

    print(result)
