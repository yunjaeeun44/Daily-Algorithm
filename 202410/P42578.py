def solution(clothes):
    clothesHash = {}
    for cloth in clothes:
        if clothesHash.get(cloth[1]) == None:
            clothesHash[cloth[1]] = 1
        else:
            clothesHash[cloth[1]] += 1
    
    answer = 1
    for i in clothesHash.values():
        answer = answer*(i+1)
    return answer-1
