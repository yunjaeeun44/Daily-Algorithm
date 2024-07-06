N = int(input())
isEnd = 0

q = []
q.append((N, 0))
prev = []
prev.append([N])
visit = set([N])

while (isEnd == 0):
    num, count = q.pop(0) # count = N이 num이 되기까지 연산 횟수
    li = prev.pop(0)
    if(num == 1):
        isEnd = 1
        print(count)
        for i in li:
            print(i ,end=' ')
        break
    if(num%3 == 0):
        if (num/3 not in visit):
            q.append((num//3,count+1))
            prev.append(li.copy()+[num//3])
            visit.add(num//3)
    if(num%2 == 0):
        if (num/2 not in visit):
            q.append((num//2, count+1))
            prev.append(li.copy()+[num//2])
            visit.add(num//2)
    if (num-1 not in visit):
        q.append((num-1, count+1))
        prev.append(li.copy()+[num-1])
        visit.add(num-1)