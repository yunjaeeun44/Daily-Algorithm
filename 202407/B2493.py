import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
answer = [0] * (N)
stk = []

for i in range(N-1, -1, -1):
    while stk and towers[i] >= stk[-1][1]:
        answer[stk.pop()[0]] = i+1# 수신하는 탑 번호 기록
    stk.append((i, towers[i]))

print(*answer)