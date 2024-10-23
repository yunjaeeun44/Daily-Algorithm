import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    
    N = int(input())
    answer = 1
    exp = ((N+1)*N)//2 #얻은 경험지
    left = 1 #최소 레벨
    right = 1000000000 #최대 레벨
    
    while (left+1 != right):
        tmplevel = (left+right)//2
        tmpExp = (tmplevel-1)*tmplevel
        #tmplevel이 되기 위한 최소 경험치 = tmpExp
        if tmpExp < exp:
            left = tmplevel
            answer = tmplevel
            
        elif tmpExp > exp:
            right = tmplevel
        else:
            answer = tmplevel
            break
    
    print(answer)