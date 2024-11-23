alpha = input()
answer = []
for i in alpha:
    if i.isupper():
        answer.append(i.lower())
    else:
        answer.append(i.upper())

for i in answer:
    print(i, end='')