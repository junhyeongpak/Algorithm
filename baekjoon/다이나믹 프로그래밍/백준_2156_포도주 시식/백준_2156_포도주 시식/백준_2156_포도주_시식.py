import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = int(input())

if n >= 3:    
    dp[2] = dp[2] + dp[1]
    dp[3] = max(dp[1] + dp[3], dp[2] + dp[3] - dp[1])
elif n == 2:
    dp[2] = dp[2] + dp[2]
else:
    pass

if n >=4 :
    for i in range(4, n + 1):
        dp[i] = max(dp[i - 2] + dp[i], dp[i - 1] + dp[i])
        print(dp[i])
else:
    pass

print(dp)