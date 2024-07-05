import sys
input = sys.stdin.readline

def BFS(i, j):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    village = len(villages) + 1
    tmp = [[i, j]]
    villageNum = 1
    mapList[i][j] = 0
    while(tmp):
        y, x = tmp.pop()
        for i in range(4):
            nextY, nextX = y+dy[i], x+dx[i]
            if 0 <= nextY < N and 0 <= nextX < N:
                if mapList[nextY][nextX] == 1:
                    tmp.append([nextY, nextX])
                    mapList[nextY][nextX] = 0
                    villageNum += 1
    villages.append(villageNum)

N = int(input())
mapList = []
for _ in range(N):
    mapList.append(list(map(int, input().rstrip())))

villages = []
for i in range(N):
    for j in range(N):
        if mapList[i][j] == 1:
            BFS(i, j)

villages.sort()
print(len(villages))
for v in villages:
    print(v)