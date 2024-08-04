S = list(input())

zero = 0
one = 0
before = None
for i in range(len(S)):
    if before != S[i]:
        if S[i] == '1':
            one += 1
        else:
            zero += 1
    before = S[i]  
    
print(min(zero, one))