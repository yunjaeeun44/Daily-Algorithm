import sys
from collections import deque
input = sys.stdin.readline
dq = deque([])

N = int(input())
for _ in range(N):
    command = list(input().split())
    if command[0] == "push_front":
        dq.appendleft(int(command[1]))
    elif command[0] == "push_back":
        dq.append(int(command[1]))
    elif command[0] == "pop_front":
        if len(dq) != 0:
            print(dq.popleft())
        else:
            print(-1)
    elif command[0] == "pop_back":
        if len(dq) != 0:
            print(dq.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(dq))
    elif command[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(dq) != 0:
            print(dq[0])
        else:
            print(-1)
    elif command[0] == "back":
        if len(dq) != 0:
            print(dq[-1])
        else:
            print(-1)