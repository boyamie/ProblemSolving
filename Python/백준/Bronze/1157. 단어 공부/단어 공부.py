word = list(input().upper())
what_word = list(set(word))
count_word = []

for i in what_word:
    count = word.count(i)
    count_word.append(count)

if count_word.count(max(count_word))>=2:
    print('?')
else:
    print(what_word[count_word.index(max(count_word))])