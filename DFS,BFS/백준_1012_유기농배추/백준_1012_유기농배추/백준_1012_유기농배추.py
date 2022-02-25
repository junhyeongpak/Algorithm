import sys
# 파이썬 재귀 깊이를 설정(기본적으로 파이썬은 1000회가 제한)
sys.setrecursionlimit(15000)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        return False
    graph[x][y] = 0

    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True


case = int(sys.stdin.readline())
for i in range(case):
    result = 0

    n, m, s = map(int, sys.stdin.readline().split())
    graph = [[0 for a in range(m)] for b in range(n)]
    for j in range(s):
        q, w = map(int, sys.stdin.readline().split())
        graph[q][w] = 1

    for o in range(n):
        for k in range(m):
            if dfs(o, k) == True:
                result += 1
    print(result)

