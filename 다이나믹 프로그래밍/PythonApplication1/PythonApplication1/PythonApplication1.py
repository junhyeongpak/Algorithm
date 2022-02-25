a, b, c = map(int, input().split())

if a == b and b == c:
    result = 10000 + (a * 1000)
    print(result)
elif a == b or b == c or a == c:
    li = [a, b, c]
    if li.count(a) == 2:
        result = 1000 + (a * 100)
    elif li.count(b) == 2:
        result = 1000 + (b * 1000)
    print(result)
else:
    li = [a,b,c]
    m = max(li)
    result = m * 100
    print(result)