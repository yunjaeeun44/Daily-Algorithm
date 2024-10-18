from collections import deque

def solution(numbers, target):
    bfs = deque([0])
    for number in numbers:
        for _ in range(len(bfs)):
            now = bfs.popleft()
            bfs.append(now+number)
            bfs.append(now-number)
    
    return bfs.count(target)