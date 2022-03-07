import sys
from queue import PriorityQueue
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    check = [0 for _ in range(n)]
    check[m] = 1
    count = 0
    while 1:
        if li[0] == max(li):
            count += 1
            if check[0] != 1:
                del li[0]
                del check[0]
            else:
                print(count)
                break
        else:
            li.append(li[0])
            check.append(check[0])
            del li[0]
            del check[0]
        