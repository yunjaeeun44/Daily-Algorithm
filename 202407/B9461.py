import sys
input = sys.stdin.readline

T = int(input())
P = [0, 1, 1, 1, 2]

for _ in range(T):
    N = int(input())
    if len(P) <= N:
        for i in range(len(P), N+1):
            P.append(P[i-1] + P[i-5])
    print(P[N])