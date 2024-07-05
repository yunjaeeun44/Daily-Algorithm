T = int(input())
L = [0, 1, 2, 4]
for _ in range(T):
    N = int(input())
    if len(L)-1 < N:
        for i in range(len(L), N+1):
            L.append(L[i-3] + L[i-2] + L[i-1])
        print(L[N])
    else:
        print(L[N])
    