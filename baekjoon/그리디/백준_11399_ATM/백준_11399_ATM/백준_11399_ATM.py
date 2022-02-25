num = int(input())

list_a = list(map(int, input().split()))

list_a.sort()

res = 0
for i in range(num):
    res += sum(list_a[0:i+1])

print(res)