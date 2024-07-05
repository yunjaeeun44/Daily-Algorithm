from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001
tmp = deque([N])

while tmp:
    now = tmp.popleft()
    if now == K:
        print(visited[now])
        exit()
    for nx in (now-1, now+1, now*2):
        if 0 <= nx <= 100000 and visited[nx]== 0:
            tmp.append(nx)
            visited[nx] = visited[now]+1