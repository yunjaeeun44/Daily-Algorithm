def solution(array):
    return sum(str(i).count('7') for i in array)

def solution1(array):
    return str(array).count('7')