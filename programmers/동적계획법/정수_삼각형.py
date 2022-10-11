def solution(triangle):
    answer = 0
    n = len(triangle[-1])
    table = [[] for i in range(n)]
    table[n-1] = triangle[-1]
    
    for i in range(n - 1, 0, -1):
        for j in range(i):
            table[i - 1].append(max(table[i][j] + triangle[i - 1][j], table[i][j+1] + triangle[i - 1][j]))
        
    answer = table[0][0]
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))