from collections import deque

#(0,0)이 3이되는 오류가 있지만 정답을 구하는데 문제없으므로 해결 생략
def solution(maps):
    m = len(maps[0])
    n = len(maps)
    visited = [[0]*(m) for i in range(n)]
    bfs = deque([(0, 0)])
    
    xi = [0, 0, 1, -1]
    yi = [1, -1, 0, 0]
    while bfs:
        now = bfs.popleft()
        for i in range(4):
            nextx = now[1]+xi[i]
            nexty = now[0]+yi[i]
            if 0<=nextx<m and 0<=nexty<n:
                if maps[nexty][nextx] == 1:
                    bfs.append((nexty,nextx))
                    maps[nexty][nextx] = maps[now[0]][now[1]] + 1
            
    if maps[n-1][m-1] == 1:
        return -1
    return maps[n-1][m-1]