import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split(" "))

memo = {}
memo[1] = a % c

def f(b):
    if b in memo:
        return memo[b]
    
    b1 = b // 2
    result = 1
    
    if b % 2 == 0:
        result = (f(b1) * f(b1)) % c          
    else:
        result = (((f(b1) * f(b1)) % c) * a) % c
    
    memo[b] = result
    return memo[b]

f(b)
print(memo[b])