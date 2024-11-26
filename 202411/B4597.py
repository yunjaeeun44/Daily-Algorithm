import sys
input = sys.stdin.readline

while(1):
    bitString = input().strip()
    if bitString == '#':
        exit()
        
    num = bitString[0:-1]
    bit = bitString[-1]
    tmp = ''
    if num.count('1') % 2 == 0: #짝수
        if bit == 'e': #짝수
            tmp = '0'
        else:
            tmp = '1'
    else: #홀수
        if bit == 'e': #짝수
            tmp = '1'
        else:
            tmp = '0'
    print(num+tmp)
