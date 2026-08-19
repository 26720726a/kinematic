"""
LEVEL 13 - 최소 분산 구간 찾기

[문제]
N개의 센서 값과 구간 길이 K가 주어진다.
연속된 K개 데이터 중 분산이 가장 작은 구간의 시작 위치를 출력하시오.

분산:
각 값과 평균의 차이 제곱의 평균

시작 위치는 1부터 시작한다.
분산이 같으면 더 앞의 구간을 출력한다.

[예제 입력]
6 3
1 2 3 10 10 10

[예제 출력]
4
"""

N, K = map(int, input().split())
data = list(map(float, input().split()))

best_index = 0
best_variance = float("inf")

for start in range(N - K + 1):
    window = data[start:start + K]

    avg = sum(window) / K

    variance = 0

    for value in window:
        variance += (value - avg) ** 2

    variance /= K

    if variance < best_variance:
        best_variance = variance
        best_index = start

print(best_index + 1)
