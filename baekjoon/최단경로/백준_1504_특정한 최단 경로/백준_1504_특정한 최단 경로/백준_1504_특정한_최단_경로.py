import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())
def dijstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijstra(1)
v1_dist = distance[v1]
v2_dist = distance[v2]

distance = [INF] * (n + 1)

dijstra(v1)
v1tov2 = distance[v2]

distance = [INF] * (n + 1)
dijstra(n)
v1_dis = distance[v1]
v2_dis = distance[v2]

result = min(v1_dist + v1tov2 + v2_dis, v2_dist + v1tov2 + v1_dis)
if result >= INF:
    print(-1)
else:
    print(result)