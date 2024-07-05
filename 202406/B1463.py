from collections import deque

#DP 방식
N = int(input())
DP = [0]* (N+1)
for i in range(2, N+1):
    DP[i] = DP[i-1] + 1
    if i % 2 == 0:
        DP[i] = min(DP[i], DP[i//2] + 1)
    if i % 3 == 0:
        DP[i] = min(DP[i], DP[i//3] + 1)
print(DP[N])

#BFS로 푼 방식
N = int(input())
visited = []
tmp = deque([N])
answer = 0
while(True):
    for _ in range(len(tmp)):
        now = tmp.popleft()
        if now == 1:
            print(answer)
            exit()
        if now % 3 == 0:
            if (now//3) not in visited:
                tmp.append(now//3)
                visited.append(now//3)
        if now % 2 == 0:
            if (now//2) not in visited:
                tmp.append(now//2)
                visited.append(now//2)
        if now-1 not in visited:
            tmp.append(now - 1)
            visited.append(now-1)
    answer += 1