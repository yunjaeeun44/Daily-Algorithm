def solution(arr):
    dp = {} #(i, j) = [최소, 최대]
    for step in range(0, len(arr), 2):
        for i in range(0, len(arr)-step, 2):
            j = i+step
            if step == 0:
                dp[(i, j)] = [int(arr[i]), int(arr[i])]
                
            else:
                maxCandidate, minCandidate = [], []    
                for k in range(i+1, j, 2):
                    if arr[k] == "+":
                        minCandidate.append(dp[(i, k-1)][0] + dp[(k+1, j)][0])
                        maxCandidate.append(dp[(i, k-1)][1] + dp[(k+1, j)][1])
                    elif arr[k] == "-":
                        minCandidate.append(dp[(i, k-1)][0] - dp[(k+1, j)][1])
                        maxCandidate.append(dp[(i, k-1)][1] - dp[(k+1, j)][0])
                dp[(i, j)] = [min(minCandidate), max(maxCandidate)]
            
    return dp[(0, len(arr)-1)][1]