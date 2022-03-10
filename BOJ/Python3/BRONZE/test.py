stack = 1
result = 0

word = 'ooxooox'

for w in word:
    if w == 'o':
        result += stack
        stack += 1
    else: # w == 'x'
        stack = 1

print(result)