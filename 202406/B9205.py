import sys
from collections import deque
input = sys.stdin.readline

def BFS(visited):
    tmp = deque([[housex, housey]])
    while(tmp):
        nowx, nowy = tmp.popleft()
        if abs(festivalx - nowx) + abs(festivaly - nowy) <= 1000:
            print("happy")
            return
        for i in range(N):
            if visited[i] == 0:
                nextx, nexty = convList[i]
                if abs(nowx - nextx) + abs(nowy - nexty) <= 1000:
                    tmp.append([nextx, nexty])
                    visited[i] = 1
    print("sad")
    return

T = int(input())
for _ in range(T):
    N = int(input())
    housex, housey = map(int, input().split())
    convList = []
    for i in range(N):
        convx, convy = map(int, input().split())
        convList.append([convx, convy])
    festivalx, festivaly = map(int, input().split())
    visited = [0] * (N+1) #편의점 방문 확인
    BFS(visited)
