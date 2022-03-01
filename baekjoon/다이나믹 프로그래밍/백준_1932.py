n = int(input())

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
graph = [[0, 0]]

for _ in range(n):
    graph.append([0] + list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i][j] = graph[i][j]
        re = max(dp[i - 1][j - 1], dp[i - 1][j])
        dp[i][j] += re


result = max(dp[n])
print(result)