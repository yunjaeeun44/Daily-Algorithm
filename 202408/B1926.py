import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
paint = 0

def BFS(y, x):
    iy = [0, 0, 1, -1]
    ix = [1, -1, 0, 0]
    tmp = deque([[y, x]])
    paper[y][x] = 0
    num = 1
    
    while(tmp):
        nowy, nowx = tmp.popleft()
        for i in range(4):
            if 0 <= nowy+iy[i] < N and 0 <= nowx+ix[i] < M:
                if paper[nowy+iy[i]][nowx+ix[i]] == 1:
                    tmp.append([nowy+iy[i], nowx+ix[i]])
                    paper[nowy+iy[i]][nowx+ix[i]] = 0
                    num += 1
    return num

for i in range(N):
    for j in range(M):
        if paper[i][j] == 1:
            cnt += 1
            paint = max(paint, BFS(i, j))

print(cnt)
print(paint)