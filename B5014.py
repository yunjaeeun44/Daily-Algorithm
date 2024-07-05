from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [0] * 1000001

tmp = deque([S])
visited[S] = 1
while(tmp):
    now = tmp.popleft()
    if now == G:
        print(visited[now]-1)
        exit()
    for next in [now-D, now+U]:
        if 1 <= next <= F:
            if visited[next] == 0:
                visited[next] = visited[now]+1
                tmp.append(next)

print("use the stairs")      