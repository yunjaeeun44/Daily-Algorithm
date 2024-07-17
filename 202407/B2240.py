import sys
input = sys.stdin.readline

T, W = map(int, input().split())
jadu = [0] + [int(input()) for _ in range(T)]
DP = [[0]*(W+1) for _ in range(T+1)]

#0번 움직였을 때
for t in range(1, T+1):
    plus = 1 if jadu[t] == 1 else 0
    DP[t][0] = DP[t-1][0] + plus

#1번 이상 움직였을 때
for t in range(1, T+1):
    for w in range(1, W+1):
        if w % 2 == 1: #2번에 위치
            plus = 1 if jadu[t] == 2 else 0
        else: #1번에 위치
            plus = 1 if jadu[t] == 1 else 0
        DP[t][w] = max(DP[t-1][w-1], DP[t-1][w]) + plus

print(max(DP[T]))