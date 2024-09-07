N, M = map(int, input().split())
NList = [i for i in range(1, N+1)]

def backtracking(tmp):
    if len(tmp) == M:
        print(*tmp)
        return 
    
    for i in NList:
        if i not in tmp and len(tmp) != M:
            tmp.append(i)
            backtracking(tmp)
            tmp.pop()

backtracking([])