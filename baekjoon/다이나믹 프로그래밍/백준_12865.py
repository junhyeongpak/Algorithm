# 냅색 알고리즘
n, k = map(int, input().split())

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
graph = [[0, 0]]

# 입력받기
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 0 - 1 배낭문제

for i in range(1, n + 1):
    weight = graph[i][0]
    value = graph[i][1]
    for j in range(1, k + 1):
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])
            
print(dp[n][k]) 