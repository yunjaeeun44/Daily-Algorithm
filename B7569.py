from collections import deque

M, N, H = map(int, input().split())
tomatos = []
tmp = deque([])

for i in range(H):
    box = []
    for j in range(N):
        line = list(map(int, input().split()))
        box.append(line)
        for k in range(M):
            if line[k] == 1:
                tmp.append([i, j, k])
    tomatos.append(box)
  
di = [0, 0, 1, -1, 0, 0]
dj = [1, -1, 0, 0, 0, 0]
dk = [0, 0, 0, 0, 1, -1]
              
answer = 0
while(tmp):
    for _ in range(len(tmp)):
        i, j, k = tmp.popleft()
        now = tomatos[i][j][k]
        for d in range(6):
            if 0 <= i+di[d] < H and 0 <= j+dj[d] < N and 0 <= k+dk[d] < M:
                if tomatos[i+di[d]][j+dj[d]][k+dk[d]] == 0:
                    tomatos[i+di[d]][j+dj[d]][k+dk[d]] = now + 1
                    tmp.append([i+di[d], j+dj[d], k+dk[d]])
    answer += 1

answerFlag = True
for i in range(H):
    for j in range(N):
        if 0 in tomatos[i][j]:
            answerFlag = False

if answerFlag == True:
    print(answer-1)
else:
    print(-1)