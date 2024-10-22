import sys
import math
input = sys.stdin.readline

def solution():
    n = int(input())
    calls = {}
    for _ in range(n):
        time, name = input().split()
        hour, minutes = map(int, time.split(':'))
        if calls.get(name) == None:
            calls[name] = hour*60 + minutes
        else:
            calls[name] += hour*60 + minutes
    
    for name, minutes in calls.items():
        money = 0
        if minutes >= 100:
            money = (math.ceil((minutes-100) / 50) * 3) + 10
        else:
            money = 10
        calls[name] = money
    
    answer = sorted(list(calls.items()), key=lambda x: (-x[1], x[0]))
    for name, money in answer:
        print(name, money)
    
    return 0

solution()