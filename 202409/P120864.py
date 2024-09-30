def solution(my_string):
    tmp = ''.join(i if i.isdigit() else ' 'for i in my_string)
    return sum(map(int, tmp.split()))