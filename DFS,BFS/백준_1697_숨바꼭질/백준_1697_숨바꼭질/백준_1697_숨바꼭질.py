h, m = map(int, input().split())
time = int(input())
a = time // 60
b = time % 60

h = h + a
m = m + b


if 60 <= m:
    m = m - 60
    h += 1
    if h >= 24:
        h = h % 24
else:
    if h >= 24:
        h = h % 24


print(h, m)