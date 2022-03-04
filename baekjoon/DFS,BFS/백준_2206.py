from collections import deque
import sys

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y, crush, graph, visited):
    queue = deque()
    queue.append((start_x, start_y, crush))
    visited[start_x][start_y][crush] = 1
    while queue:
        x, y, c = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][c]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽을 안부수고 이동
            if graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                queue.append((nx, ny, c))
                visited[nx][ny][c] = visited[x][y][c] + 1
            if graph[nx][ny] == 1 and c == 0:
                queue.append((nx, ny, c + 1))
                visited[nx][ny][c + 1] = visited[x][y][c] + 1
    return -1
    
print(bfs(0, 0, 0, graph, visited))