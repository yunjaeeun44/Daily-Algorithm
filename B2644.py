from collections import deque
import sys
input = sys.stdin.readline

def BFS(A, B):
    answer = 1
    tmp = deque([A])
    visited = [0 for _ in range(N+1)]
    while tmp:
        for _ in range(len(tmp)):
            now = tmp.popleft()
            for i in graph[now]:
                if visited[i] == 0:
                    tmp.append(i)
                    visited[i] = 1
                if i == B:
                    return answer;
        answer += 1
    return -1
    
def DFS(v, num):
    visited[v] = 1
    if v == B:
        global answer
        answer = num
    else:
        for i in graph[v]:
            if visited[i] == 0:
                DFS(i, num+1)
    

N = int(input())
graph = [[] for _ in range(N+1)]
A, B = map(int, input().split())
M = int(input())

for _ in range(M):
    x, y = map(int, input().split()) #부모 , 자식
    graph[x].append(y)
    graph[y].append(x)

#print(BFS(A, B))

visited = [0 for _ in range(N+1)]
answer = -1
DFS(A, 0)
print(answer)