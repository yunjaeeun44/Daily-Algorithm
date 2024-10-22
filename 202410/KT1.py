def same(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return i
        
        
def solution(arr1, arr2):
    exam = []
    for i in range(len(arr1)):
        exam.append([arr1[i], arr2[i]])
    exam.sort()
    print(exam)
    print()
    
    answer = []
    answer.append([exam[0][0][0], exam[0][0], exam[0][1]])
    for i in range(1, len(exam)):        
        if answer[-1][-1] == exam[i][1]:            #정답이 같으면
            num = same(answer[-1][1], exam[i][0])
            answer[-1][1] = answer[-1][1][0:num]    #최대값 겹치는 부분만큼 줄이기
        else:                                       #정답이 다르면
            num = same(answer[-1][1], exam[i][0])
            if num > 0:                             #이전 암기법에 겹치는 부분만큼 늘리기
                answer[-1][0] = answer[-1][1][0:num+1]

            min_ = exam[i][0][0:num+1]              #최소값도 겹치는 부분만큼 늘리기
            max_ = exam[i][0]                       #최대값 자기자신
            answer.append([min_, max_, exam[i][1]])
    
    print("answer=> ", answer)
    tmp = 0
    for min, max, num in answer:
        tmp += len(min)
    print(tmp)
    return tmp

solution(
    ['abcd?', 'abcdef?', 'bbab?', 'bbabab?', 'cacabc?', 'cacsdc?', 'cacsz?'],
    [2, 2, 3, 1, 5, 4, 3])