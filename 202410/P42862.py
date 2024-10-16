def solution(n, lost, reserve):
    lost2 = sorted(list(set(lost) - set(reserve)))
    reserve2 = sorted(list(set(reserve) - set(lost)))
    
    answer = n - len(lost2)
    for i in lost2:
        if i-1 in reserve2:
            reserve2.remove(i-1)
            answer+=1
        elif i+1 in reserve2:
            reserve2.remove(i+1)
            answer+=1

    return answer