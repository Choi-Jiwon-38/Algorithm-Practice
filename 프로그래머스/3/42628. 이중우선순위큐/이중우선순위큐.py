import heapq

def solution(operations):
    max_heap = []
    min_heap = []
    
    num_dict = dict()
    q_len = 0
    
    for operation in operations:
        cmd, str_num = operation.split(" ")
        
        if cmd == 'I':
            q_len += 1
            num = int(str_num)
            
            if str_num in num_dict:
                num_dict[str_num] += 1
            else:
                num_dict[str_num] = 1
            
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
            
        elif cmd == 'D':
            if str_num == '1':
                while max_heap and str(-max_heap[0]) in num_dict and num_dict[str(-max_heap[0])] == 0:
                    heapq.heappop(max_heap)
                
                if q_len:
                    num_dict[str(-heapq.heappop(max_heap))] -= 1
                    
                    q_len -= 1
                    
            elif str_num == '-1':
                while min_heap and str(min_heap[0]) in num_dict and num_dict[str(min_heap[0])] == 0:
                    heapq.heappop(min_heap)
                
                if q_len:            
                    num_dict[str(heapq.heappop(min_heap))] -= 1
                    q_len -= 1
                    
    survived = []

    
    for key in num_dict.keys():
        if num_dict[key] > 0:
            survived.append(int(key))
    
    survived.sort()
    
    return [survived[-1], survived[0]] if q_len else [0, 0]