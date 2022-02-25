import sys
import copy
from collections import deque
input = sys.stdin.readline

def topology_sort(k):
    result = copy.deepcopy(time)
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(result[k])


num = int(input())
for _ in range(num):
    n, m = map(int, input().split())
    time = [0]
    time = time + list(map(int, input().split()))
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    a = int(input())
    topology_sort(a)