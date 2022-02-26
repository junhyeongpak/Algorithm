n, k =map(int, input().split())

d = [[0 for j in range(201)] for i in range(201)]

for i in range(1, 201):
    d[i][1] = 1

for i in range(1, 201):
    d[1][i] = i

for i in range(2, 201):
    for j in range(2, 201):
        d[i][j] = d[i][j - 1] + d[i - 1][j]

print(d[n][k] % 1000000000)