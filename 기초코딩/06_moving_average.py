"""
LEVEL 6 - 이동 평균

[문제]
로봇에서 측정한 N개의 센서 데이터가 주어진다.
연속된 K개 값의 평균인 Moving Average를 계산하여 출력하시오.

각 평균은 소수점 둘째 자리까지 출력한다.

[예제 입력]
6 3
1 2 3 4 5 6

[예제 출력]
2.00 3.00 4.00 5.00
"""

N, K = map(int, input().split())
data = list(map(float, input().split()))

result = []

for i in range(N - K + 1):
    total = 0

    for j in range(i, i + K):
        total += data[j]

    average = total / K
    result.append(average)

print(*[f"{value:.2f}" for value in result])
