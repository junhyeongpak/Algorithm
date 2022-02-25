import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

n = int(input())
h_card = list(map(int, input().split()))

h_card.sort()

test_n = int(input())
test_card = list(map(int, input().split()))

for i in test_card:
    r = binary_search(h_card, i, 0, n -1)
    if r == True:
        print(1, end = ' ')
    else:
        print(0, end = ' ')