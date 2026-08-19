"""
LEVEL 20 - 최소 비용 이동

[문제]
로봇이 0번 위치에서 N-1번 위치까지 이동한다.

한 번에 1칸 또는 2칸 이동할 수 있다.
i번 위치에 도착하면 cost[i]의 비용이 발생한다.

0번 위치의 비용도 포함한다.

N-1번 위치까지 가는 최소 총 비용을 출력하시오.

[예제 입력]
5
1 100 1 1 1

[예제 출력]
3

예시 경로:
0 -> 2 -> 4
비용 = 1 + 1 + 1 = 3
"""

N = int(input())

cost = list(map(int, input().split()))

if N == 1:
    print(cost[0])

else:
    dp = [0] * N

    dp[0] = cost[0]
    dp[1] = cost[0] + cost[1]

    for i in range(2, N):
        dp[i] = min(
            dp[i - 1],
            dp[i - 2]
        ) + cost[i]

    print(dp[N - 1])
