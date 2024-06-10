number = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
result = 0
word = input()
for i in range(len(word)):
    for j in number:
        if word[i] in j:
            result += number.index(j)+3
print(result)            