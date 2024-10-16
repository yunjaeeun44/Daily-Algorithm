from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for dun in list(permutations(dungeons, len(dungeons))):
        score = k
        tmp = 0
        for a, b in dun:
            if score >= a:
                tmp += 1
                score -= b
            else:
                break
        answer = max(answer, tmp)
                  
    return answer