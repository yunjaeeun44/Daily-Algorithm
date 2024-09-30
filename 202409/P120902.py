def solution(my_string):
    answer = 0
    tmp = ''
    opperand = '+'
    my_string += '+' #마지막 숫자도 연산되도록 수정
    for i in my_string:
        if i.isdigit():
            tmp += i
        elif i == '+' or i == '-':
            if opperand == '+':
                answer += int(tmp)
            elif opperand == '-':
                answer -= int(tmp)
            opperand = i
            tmp = ''
            
    return answer

def solution1(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))