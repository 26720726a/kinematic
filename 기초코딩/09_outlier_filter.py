"""
LEVEL 9 - 센서 데이터 이상치 제거

[문제]
로봇 센서에서 N개의 측정값을 얻었다.

1. 전체 평균을 계산한다.
2. 각 데이터와 전체 평균의 차이가 T보다 큰 값은 이상치로 제거한다.
3. 남은 데이터의 평균을 출력한다.

[예제 입력]
5 30
10 12 11 13 100

[예제 출력]
11.50
"""

N, T = map(float, input().split())
N = int(N)

data = list(map(float, input().split()))

average = sum(data) / N

filtered = []

for value in data:
    difference = abs(value - average)

    if difference <= T:
        filtered.append(value)

new_average = sum(filtered) / len(filtered)

print(f"{new_average:.2f}")
