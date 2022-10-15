def solution(money):
    answer = 0
    result = [[0, 0] for i in range(len(money) + 1)]

    n = len(money)
    if n == 3:
        return max(money)
    if n == 4:
        return max(money[0]+money[2], money[1]+money[3])
    else:
        temp_a = money[:n - 1] 
        temp_b = money[1:]

        result[3][0] = money[0]
        result[3][1] = money[n - 1]
        result[4][0] = max(money[0] + money[2], money[1])
        result[4][1] = max(money[n - 3] + money[n - 1], money[n - 1])

        for i in range(5, n + 1):
            result[i][0] = max(result[i - 2][0] + temp_a[i - 2], result[i - 1][0])
            result[i][1] = max(result[i - 2][1] + temp_b[n - i], result[i - 1][1])
        
        answer = max(result[n][0], result[n][1])
        return answer

print(solution([1, 2, 300, 1, 5]))
