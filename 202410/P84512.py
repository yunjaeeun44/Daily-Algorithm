from itertools import permutations

def solution(word):
    words = []
    alphabet = ['A', 'E', 'I', 'O', 'U', '']
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                for d in alphabet:
                    for e in alphabet:
                        tmp = a+b+c+d+e
                        if tmp not in words:
                            words.append(tmp)
            
    words.sort()
    return words.index(word)