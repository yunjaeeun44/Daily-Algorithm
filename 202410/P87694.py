from collections import deque

#테두리가 겹치는 것을 보안하기 위해 maps 두배로 늘리기
def solution(rectangle, characterX, characterY, itemX, itemY):
    maps = [['x'] * 102 for _ in range(102)]
    for x1_, y1_, x2_, y2_ in rectangle:
        x1, y1, x2, y2 = 2*x1_, 2*y1_, 2*x2_, 2*y2_
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                if (i == y1 or i == y2) and maps[i][j] != -1:
                    maps[i][j] = 0
                elif (j == x1 or j == x2) and maps[i][j] != -1:
                    maps[i][j] = 0
                else:
                    maps[i][j] = -1
    
    xi = [0, 0, 1, -1]
    yi = [1, -1, 0, 0]
    bfs = deque([(characterY*2, characterX*2)])
    maps[characterY*2][characterX*2] = 1
    
    while (bfs):
        for i in range(len(bfs)):
            now = bfs.popleft()
            for i in range(4):
                nexty = now[0]+yi[i]
                nextx = now[1]+xi[i]
                if 0<=nexty<102 and 0<=nextx<102 and maps[nexty][nextx]==0:
                    bfs.append((nexty, nextx))
                    maps[nexty][nextx] = maps[now[0]][now[1]] + 1
                    if (itemY*2,itemX*2) == (nexty, nextx):
                        return maps[nexty][nextx] //2        
    return 0