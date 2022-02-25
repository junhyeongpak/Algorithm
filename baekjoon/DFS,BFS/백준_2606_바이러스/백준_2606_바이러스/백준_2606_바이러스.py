global count
count = 0

def dfs(x, y):
    if x < 0 or x >= num or y < 0 or y >= num:
        return False
    if graph[x][y] == 0:
        return False
    graph[x][y] = 0

    # 함수내에서 글로벌 변수 선언할때는 선언 부터 해야함 global로
    global count
    count += 1
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True

graph = []
num = int(input())

for i in range(num):
    graph.append(list(map(int, input())))

result = 0
house_num = []
for i in range(num):
    for j in range(num):
        if dfs(i, j) == True:
            result += 1
            house_num.append(count)
            count = 0

house_num.sort()
print(result)
for i in house_num:
    print(i)