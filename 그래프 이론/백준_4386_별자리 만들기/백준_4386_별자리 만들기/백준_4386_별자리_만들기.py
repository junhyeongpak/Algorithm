import sys
import math
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
graph = [0] * (n)
for i in range(n):
    a, b = map(float, input().split())
    graph[i] = [a, b, i]
gra = []
for i in range(len(graph) - 1):
    a = graph[i]
    for j in range(i + 1, len(graph)):
        b = graph[j]
        dis = math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
        gra.append((dis, a[2], b[2]))

gra.sort()

parent = [i for i in range(n + 1)]
result = 0
for g in gra:
    cost, a, b = g
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print('{:.2f}'.format(result))