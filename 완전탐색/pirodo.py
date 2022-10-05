from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    random_list = [i for i in range(len(dungeons))]
    
    per_list = permutations(random_list)

    for item in per_list:
        temp = k
        temp_count = 0
        for i in item:
            if dungeons[i][0] > temp:
                break
            else:
                temp -= dungeons[i][1]
                temp_count += 1
        if temp_count > answer:
            answer = temp_count
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))