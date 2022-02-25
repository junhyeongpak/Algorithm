num = int(input())

for i in range(num):
    a, b = map(int, input().split())
    num = a**b
    print(num % 10)