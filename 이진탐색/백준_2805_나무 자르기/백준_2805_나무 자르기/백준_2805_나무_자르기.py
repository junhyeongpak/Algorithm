import sys 

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

start = 0
end = 1000000000
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in arr:
        if i - mid > 0:
            count += i - mid
    if count >= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
