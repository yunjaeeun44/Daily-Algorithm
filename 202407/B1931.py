import sys
input = sys.stdin.readline

N = int(input())
meeting = []
for _ in range(N):
    meeting.append(list(map(int, input().split())))
meeting.sort(key = lambda x: x[0]) 
meeting.sort(key = lambda x: x[1]) #일찍 끝나는 순서

count = 0
tmpEnd = 0
for i in range(N):
    if tmpEnd <= meeting[i][0]:
        tmpEnd = meeting[i][1]
        count += 1
print(count)