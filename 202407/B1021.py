import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
dq = deque([i for i in range(1, N+1)])
locs = list(map(int, input().split()))
answer = 0

for loc in locs:
    if dq.index(loc) <= len(dq)//2:
        while(dq[0] != loc):
            dq.append(dq.popleft())
            answer += 1
        dq.popleft()
    else:
        while(dq[0] != loc):
            dq.appendleft(dq.pop())
            answer += 1
        dq.popleft()
print(answer)