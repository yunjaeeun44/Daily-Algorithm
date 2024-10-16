def solution(number, k):
    number = list(number)
    answer = list(number[0])
    cnt = 0
    for i in range(1, len(number)):
        while (len(answer)>0 and int(answer[-1])<int(number[i]) and cnt<k):
            del answer[-1]
            cnt += 1
        answer.append(number[i])
    #k 남아있는 경우 빼기    
    for i in range(k-cnt):
        del answer[-1]
        
    return "".join(answer)