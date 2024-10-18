def solution(routes):
    routes.sort(key = lambda x:x[1])
    cnt = 0
    camera = -30000
    for a, b in routes:
        if camera < a:
            cnt += 1
            camera = b
    
    return cnt