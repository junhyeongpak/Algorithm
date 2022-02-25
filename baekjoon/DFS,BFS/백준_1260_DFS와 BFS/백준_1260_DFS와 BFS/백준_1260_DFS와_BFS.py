from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

vertex, edge, s = map(int, input().split())

# 2차원 리스트는 이렇게 선언합니다.
graph = [[] for i in range(vertex + 1)]

for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(vertex + 1):
    graph[i].sort()

visited = [False] * (vertex + 1)
dfs(graph, s, visited)
visited = [False] * (vertex + 1)
print()
bfs(graph, s, visited)