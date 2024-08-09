import sys
input = sys.stdin.readline

N = int(input())
building = []
for _ in range(N):
    building.append(int(input()))
    
    
answer = 0
stk = []
for now in building:
    while stk and stk[-1] <= now:
        stk.pop()
    answer += len(stk)
    stk.append(now)
    
print(answer)