import sys
input = sys.stdin.readline

computersNum = int(input())
num = int(input())

computers = [[] for _ in range(computersNum+1)]
for _ in range(num):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)
    
def BFS():
    visited = [0] * (computersNum+1)
    tmp = [1]
    visited[1] = 1
    while(tmp):
        now = tmp.pop()
        for i in computers[now]:
            if visited[i] == 0:
                tmp.append(i)
                visited[i] = 1
    print(sum(visited) - 1)

BFS()