import sys
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

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    result = 0
    edges = []
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))
    for i in edges:
        a, b = i
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += 1
    print(result)