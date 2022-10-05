from collections import deque
import copy
# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    count = 1
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        #print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
    return count


def solution(n, wires):
    answer = -1
    graph = []
    abc = []
    for i in range(n + 1):
        graph.append([])

    for i in wires:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
        
    for i in wires:
        temp = copy.deepcopy(graph)
        #print(temp)
        temp[i[0]].remove(i[1])
        temp[i[1]].remove(i[0])
        visited = [False] * (n + 1)
        v1 = bfs(temp, i[0], visited)
        visited = [False] * (n + 1)
        v2 = bfs(temp, i[1], visited)
        abc.append(abs(v2 - v1))
        answer = min(abc)
    return answer

print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))