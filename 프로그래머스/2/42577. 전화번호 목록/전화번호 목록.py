def solution(phone_book):
    # O(nlogn)
    phone_book.sort()
    
    answer = True
    
    l = len(phone_book)
    
    # O(n^2)
    for i in range(l - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
                
    
    return answer