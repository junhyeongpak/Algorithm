import sys
sys.setrecursionlimit(1000000) # 회귀를 100만번했다
# 그러므로 최대 회귀계수를 100만으로 설정한당 ㅎㅎ
input = sys.stdin.readline

# 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 유니온 수행
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

parent = [i for i in range(n + 1)]

for _ in range(m):
    a = list(map(int, input().split()))
    if a[0] == 0:
        union_parent(parent, a[1], a[2])
    else:
        if find_parent(parent, a[1]) == find_parent(parent, a[2]):
            print("YES")
        else:
            print("NO")