def solution(quiz):
    quiz_answer = []
    for tmp in quiz:
        math, equal = tmp.split(' = ')
        if " + " in math:
            a, b = map(int, math.split(' + '))
        elif " - " in math:
            a, b = map(int, math.split(' - '))
            b = -b
            
        if a + b == int(equal):
            quiz_answer.append("O")
        else:
            quiz_answer.append("X") 
        
    return quiz_answer


def solution1(quiz):
    quiz_answer = []
    for tmp in quiz:
        math, equal = tmp.split(' = ')
        a, opperand, b = math.split()
        if opperand == "+":
            math_answer = int(a) + int(b)
        elif opperand == "-":
            math_answer = int(a) - int(b)
            
        if math_answer == int(equal):
            quiz_answer.append("O")
        else:
            quiz_answer.append("X") 
        
    return quiz_answer