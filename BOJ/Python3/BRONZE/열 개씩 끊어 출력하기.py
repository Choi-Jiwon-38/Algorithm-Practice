# 백준 온라인 11721번

word = input()

slicedWord = []

while True:
    answer, word = word[0:10], word[10:]
    slicedWord.append(answer)
    if len(word) <= 10:
        slicedWord.append(word)
        break

for sw in slicedWord:
    print(sw)