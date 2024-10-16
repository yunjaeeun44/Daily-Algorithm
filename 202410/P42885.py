from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    cnt = 0
    while people:
        if len(people) > 1:
            if people[0] + people[-1] <= limit:
                cnt += 1
                people.popleft()
                people.pop()
            else:
                people.pop()
                cnt += 1
        else:
            people.pop()
            cnt += 1
    return cnt