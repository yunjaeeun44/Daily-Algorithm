def solution(n, computers):
    visited = [0 for i in range(n)]
    cnt = 0
    for i in range(n):
        if visited[i] == 0:
            tmp = [i]
            while tmp:
                now = tmp.pop()
                visited[now] = 1
                for comi in range(n):
                    if computers[now][comi] == 1 and visited[comi] == 0:
                        tmp.append(comi)
            cnt += 1
    return cnt