import sys
input = sys.stdin.readline

def BFS(i, j, visited):
    tmp = [[i, j]]
    visited[i][j] = 1
    while(tmp):
        now = tmp.pop()
        for x in range(4):
            nexty = now[0] + dy[x]
            nextx = now[1] + dx[x]
            if 0 <= nexty < N and 0 <= nextx < M:
                if ices[nexty][nextx] != 0 and visited[nexty][nextx] == 0:
                    tmp.append([nexty, nextx])
                    visited[nexty][nextx] = 1

def  check():
    visited = [[0]*M for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(M):
            if ices[i][j] != 0 and visited[i][j] == 0:
                BFS(i, j, visited)
                answer += 1
    return answer

def  melt(ices):
    newIces = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ices[i][j] != 0:
                meltNum = 0
                for x in range(4):
                    nexty = i + dy[x]
                    nextx = j + dx[x]
                    if ices[nexty][nextx] == 0:
                        meltNum += 1
                newIces[i][j] = ices[i][j] - meltNum if ices[i][j] - meltNum >= 0 else 0
    return newIces         

N, M = map(int, input().split())
ices = []
for _ in range(N):
    ices.append(list(map(int, input().split())))

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
year = 0
while (True):
    if check() == 1:
        ices = melt(ices)
        year += 1
    elif check() == 0: #모두 녹았을 때 덩어리 개수는 무조건 0이다.
        print(0)
        break
    else:
        print(year)
        break