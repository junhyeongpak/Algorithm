
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    i = int(input())
    # i x i 배열 선언
    graph = [[0 for _ in range(i)] for _ in range(i)]
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    # 시작 노드와 종료 노드가 같을 때 0출력
    if start_x == end_x and start_y == end_y:
        print(0)
    else:
        queue = deque()
        queue.append((start_x, start_y))
        while queue:
            x, y = queue.popleft()
            for a in range(8):
                nx = x + dx[a]
                ny = y + dy[a]
                # 공간을 벗어난 경우
                if nx < 0 or nx >= i or ny < 0 or ny >= i:
                    continue
                # 한번도 진입하지 않고 그 값이 출발 위치가 아닐경우
                if graph[nx][ny] == 0 and not (nx == start_x and ny == start_y):
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
            

        print(graph[end_x][end_y])
    
    