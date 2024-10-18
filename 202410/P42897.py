def solution(money):
    dp1 = [money[0], max(money[0], money[1])] #마지막은 무조건 먹지 않는다.
    for i in range(2, len(money)-1):
        dp1.append(max(dp1[i-2]+money[i], dp1[i-1]))

    dp2 = [0, money[1], max(money[1], money[2])] #0번째는 무조건 먹지 않는다.
    for i in range(3, len(money)): 
        dp2.append(max(dp2[i-2]+money[i], dp2[i-1]))
    
    return max(max(dp1), max(dp2))