n = int(input())
li = list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
dp[1] = li[0]

for i in range(2, n + 1):
    # 현재 값이 음수인 경우
    if li[i - 1] < 0:
        dp[i] = dp[i - 1]
        #print(dp[i])
    # 현재 값이 양수인 경우
    else:
        if li[i - 2] >= 0:
            li[i - 1] = li[i - 2] + li[i - 1]
            #print(li[i-1])
        else:
            pass
        dp[i] = max(li[i - 1], dp[i - 1])
        #print(dp[i])
print(dp[n - 1])
         
        
