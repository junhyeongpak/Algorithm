import sys

k, n = map(int, input().split())

arr = []
for i in range(k):
    arr.append(int(sys.stdin.readline().rstrip()))

start = 1
end = max(arr)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in arr:
        count += i // mid 
    if count < n:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)