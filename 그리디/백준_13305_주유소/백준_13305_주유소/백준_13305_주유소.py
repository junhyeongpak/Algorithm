import sys

num = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

result = 0
min_price = price[0] # 제일 중요한 아이디어 
# 최소값으로 둔 다음에 더 큰 값이 나오기 전까지 
# 최소값을 유지하면서 계산을 할 수 있도록 함

for i in range(num - 1):
    if min_price <= price[i]:
        result += min_price * distance[i]
    else:
        min_price = price[i]
        result += min_price * distance[i]

print(result)