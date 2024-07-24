import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    nums = input().rstrip()[1:-1]
    if n != 0:
        nums = deque(list(map(int, nums.split(','))))
    else:
        nums = deque([])
        
    isR = False
    isError = False
    for i in p:
        if i == 'R':
            isR = not isR
        if i == 'D':
            if len(nums) == 0:
                isError = True
                break
            if isR:
                nums.pop()
            else:
                nums.popleft();
    
    if isError:
        print("error")
    else:
        if isR:
            nums.reverse()
        print(f"[{','.join(map(str, nums))}]")