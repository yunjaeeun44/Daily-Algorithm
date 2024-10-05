def solution(my_str, n):
    answer = []
    while my_str:
        answer.append(my_str[0:n])
        my_str = my_str[n:]
    return answer

def solution1(my_str, n):
    answer = [my_str[i:i+n] for i in range(0, len(my_str), n)]
    return answer