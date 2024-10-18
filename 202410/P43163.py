from collections import deque

def check(now, word):
    cnt = 0
    for i in range(len(now)):
        if now[i] != word[i]:
                cnt += 1
    if cnt == 1:
        return True
    return False

def solution(begin, target, words):
    visited = {}
    for word in words:
        visited[word] = 0
    
    bfs = [begin]
    visited[begin] = 1
    while bfs:
        now = bfs.pop()
        for word in words:
            if visited[word] == 0 and check(now, word):
                bfs.append(word)
                visited[word] = visited[now]+1
                if word == target:
                    return visited[word] - 1

    return 0