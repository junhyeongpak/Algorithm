import sys

num = int(sys.stdin.readline())
time = []

for i in range(num):
    start, end = map(int, sys.stdin.readline().split())
    time.append((start, end))
 
time = sorted(time, key=lambda time : (time[1],time[0]))


last = 0
result = 0
for i in time:
    if i[0] >= last:
        result += 1
        last = i[1]
print(result)