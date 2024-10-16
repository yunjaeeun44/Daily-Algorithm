from itertools import permutations

def solution(numbers):
    numbers = list(numbers)
    numSet = set()
    for i in range(len(numbers)):
        numSet |= set(map(int, map("".join, permutations(numbers, i+1))))
    
    numSet -= set([0, 1])
    for i in range(2, int(max(numSet)**0.5)+1):
        numSet -= set(range(i*2, max(numSet)+1, i))
        
    return len(numSet)