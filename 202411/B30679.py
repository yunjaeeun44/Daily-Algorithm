import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

def check(i):
    now = [i, 0, 1] #0: 위, 1:오른쪽, 2:아래, 3:왼쪽
    visited = [[[False, False, False, False] for j in range(M)] for i in range(N)]
    #visited를 방문한 곳만 넣는 방식이 아닌 좌표에 boolean 방식으로 표시
    while(1):
        if (now[0]<0 or now[0]>=N or now[1]<0 or now[1]>=M):
            return 0
        if visited[now[0]][now[1]][now[2]] == True:
            return 1
        
        visited[now[0]][now[1]][now[2]] = True
        tmp = MAP[now[0]][now[1]]
        if now[2] == 0:
            now[0] -= tmp
        elif now[2] == 1:
            now[1] += tmp
        elif now[2] == 2:
            now[0] += tmp
        elif now[2] == 3:
            now[1] -= tmp
        now[2] = (now[2]+1)%4

answer = []
for i in range(N):
    if check(i):
        answer.append(i+1)

print(len(answer))
if len(answer):
    print(*answer)