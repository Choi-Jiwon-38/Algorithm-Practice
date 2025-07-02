ps = input()

stack = []
pairs = []

for i in range(len(ps)):
    if ps[i] == '(':
        stack.append(i)
    elif ps[i] == ')':
        start = stack.pop()
        pairs.append((start, i))

result = set()

def backtrack(depth, selected_pair_indexs):
    if selected_pair_indexs:
        to_remove = []

        for _idx in selected_pair_indexs:
            to_remove += pairs[_idx]
        
        new_chars = []

        for i in range(len(ps)):
            if i not in to_remove:
                new_chars.append(ps[i])
            
        new_str = ''.join(new_chars)
        result.add(new_str)
    
    for i in range(depth, len(pairs)):
        if i in selected_pair_indexs:
            continue
        selected_pair_indexs.append(i)
        backtrack(depth + 1, selected_pair_indexs)
        selected_pair_indexs.pop()

backtrack(0, [])

answer = sorted(list(result))

for a in answer:
    print(a)
