def least(a, b):
    A, B = a, b
    
    while (b != 0):
        r = a % b
        a = b
        b = r
        
    gcd = a
    
    return A * B // gcd
    

def solution(arr):
    answer = 1
    
    prev = arr[0]

    for i in range(1, len(arr)):  
        print(prev, arr[i])
        prev = least(prev, arr[i])
        
    return prev
    


