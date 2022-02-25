num = int(input())

dp = [0] * 9
dp[1] = 9
for i in range(2, num + 1):
    dp[i] = dp[i - 1] * 2 - 1


print(dp[num])