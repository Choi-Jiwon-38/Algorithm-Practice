import heapq

def solution(operations):
    max_heap = []
    min_heap = []
    
    num_dict = dict()
    
    for operation in operations:
        cmd, str_num = operation.split(" ")
        num = int(str_num)
        
        if cmd == 'I':
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
            
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
        elif cmd == 'D':
            if num == 1:
                while max_heap and num_dict[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                
                if max_heap:
                    num_dict[-heapq.heappop(max_heap)] -= 1
                
            elif num == -1:
                while min_heap and num_dict[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                
                if min_heap:
                    num_dict[heapq.heappop(min_heap)] -= 1
    
    if sum(num_dict.values()) == 0:
        return [0, 0]
    
    answers = []
    
    for key in num_dict.keys():
        if num_dict[key] != 0:
            answers.append(key)
    
    return [max(answers), min(answers)]