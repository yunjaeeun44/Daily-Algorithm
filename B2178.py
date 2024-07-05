from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input().rstrip())))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

tmp = deque([[0, 0]])
while(tmp):
    now = tmp.popleft()
    for i in range(4):
        y, x = now[0]+dy[i], now[1]+dx[i]
        if 0 <= y < N and 0 <= x < M:
            if  maze[y][x] == 1:
                maze[y][x] = maze[now[0]][now[1]] + 1
                tmp.append([y, x])

print(maze[N-1][M-1])