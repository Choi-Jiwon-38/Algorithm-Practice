import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dic = {}
    
    for _ in range(n):        
        val, key = input().rstrip().split(" ")

        if not key in dic:
            dic[key] = []
        
        dic[key].append(val)
    
    answer = 1    
    values = dic.values()
    
    for value in values:
        answer *= len(value) + 1
    
    print(answer - 1)
