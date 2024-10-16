def solution(answers):
    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    for i in range(len(answers)):
        scores[0] += 1 if answers[i] == A[i%len(A)] else 0
        scores[1] += 1 if answers[i] == B[i%len(B)] else 0
        scores[2] += 1 if answers[i] == C[i%len(C)] else 0
    
    highScore = max(scores)
    answer = []
    for i in range(len(scores)):
        if scores[i] == highScore:
            answer.append(i+1)
    
    return answer