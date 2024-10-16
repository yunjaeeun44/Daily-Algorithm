def solution(brown, yellow):
    brownSet = set()
    for i in range(1, (brown+4)//4+1):
        brownSet.add(((brown+4)//2-i, i))
    
    for i in brownSet:
        if i[0] * i[1] == brown+yellow:
            return list(i)
    
    return 0