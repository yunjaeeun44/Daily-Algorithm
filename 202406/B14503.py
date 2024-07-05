import sys
input = sys.stdin.readline

def isNearClean(nowy, nowx):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    for i in range(4):
        if rooms[nowy+dy[i]][nowx+dx[i]] == 0:
            if [nowy+dy[i], nowx+dx[i]] not in visited:
                return False    
    return True
    
    
N, M = map(int, input().split())
r, c, d = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]
visited = []
backway = [[1, 0], [0, -1], [-1, 0], [0, 1]]

nowy, nowx, nowWay = r, c, d
while True:
    if [nowy, nowx] not in visited:
        visited.append([nowy, nowx])
    if isNearClean(nowy, nowx):
        if rooms[nowy+backway[d][0]][nowx+backway[d][1]] == 0:
            nowy += backway[d][0]
            nowx += backway[d][1]
            continue
        else:
            print(len(visited))
            exit()
    else:
        d = d-1 if 0<d<4 else 3
        if rooms[nowy-backway[d][0]][nowx-backway[d][1]] == 0:
            if [nowy-backway[d][0], nowx-backway[d][1]] not in visited:
                nowy -= backway[d][0]
                nowx -= backway[d][1]
                continue
        