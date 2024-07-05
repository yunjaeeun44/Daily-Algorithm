from collections import deque

def DFS(V): #재귀
    visited[V] = 1
    print(V, end = " ")
    
    for i in graph[V]:
        if not visited[i]:
            DFS(i)
    
def BFS(V):
    queue = deque([V])
    visited[V] = 1
    
    while(queue):
        v = queue.popleft()
        print(v, end=" ")
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
         
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()       

visited = [0] * (N+1)
DFS(V)
print()

visited = [0] * (N+1)
BFS(V)
print()
