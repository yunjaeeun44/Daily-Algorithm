import math

def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    
    day = 0
    answer = []
    for i in days:
        if day < i:
            answer.append(1)
            day = i
        elif day >= i:
            answer[-1] += 1
    return answer