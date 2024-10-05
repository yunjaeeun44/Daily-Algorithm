def solution(polynomial):
    polynomial = (' '+ polynomial).replace(" x", " 1x")
    
    xnum = 0
    num = 0
    for i in polynomial.split(" + "):
        if i[-1] == 'x':
            xnum += int(i[:-1])
        else:
            num += int(i)
            
    answer = ''
    if xnum == 1:
        answer += 'x'
    elif xnum > 1:
        answer += str(xnum)+"x"
    if xnum and num:
        answer += " + "
    if num > 0:
        answer += str(num)
    return answer