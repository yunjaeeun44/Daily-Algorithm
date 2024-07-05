import sys
imput = sys.stdin.readline

def BFS(y, x, height, visited):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    tmp = [[y, x]]
    visited[y][x] = 1
    while tmp:
        now = tmp.pop()
        for i in range(4):
            nexti = now[0]+dy[i]
            nextj = now[1]+dx[i]
            if 0 <= nexti < N and 0 <= nextj < N:
                if mapList[nexti][nextj] > height and visited[nexti][nextj] == 0:
                    tmp.append([nexti, nextj])
                    visited[nexti][nextj] = 1

N = int(input())
mapList = []
heightSet = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    mapList.append(tmp)
    heightSet = heightSet + tmp
heightSet = list(set(heightSet))

visited = []
answers = []
for height in heightSet:
    visited = [[0]*N for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(N):
            if mapList[i][j] > height and visited[i][j] == 0:
                BFS(i, j, height, visited)
                answer += 1
    answers.append(answer)
    
answers.sort(reverse=True)
if (answers[0] == 0): 
    print(1) #비가 안 내릴 때가 가장 많은 경우 답은 1이다.
else:
    print(answers[0])
