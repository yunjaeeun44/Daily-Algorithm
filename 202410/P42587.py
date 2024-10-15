def solution(priorities, location):
    stack = [[priorities[i], i] for i in range(len(priorities))]
    
    cnt = 0
    while stack:
        now = stack.pop(0)
        m = max(stack)[0] if len(stack) > 0 else 0
        if now[0] < m:
            stack.append(now)
        else:
            cnt += 1
            if now[1] == location:
                return cnt