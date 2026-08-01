from collections import deque

def solution(tickets):

    a = dict()
    ticket = dict()
    answer = []
    
    for s, e in tickets:
        if s+e in ticket:
            ticket[s+e] += 1
        else:
            ticket[s+e] = 1

        if s in a:
            a[s].append(e)
        else:
            a[s] = [e]
            
    def dfs(curr, path, airport, tickets):
        if sum(tickets.values()) == 0:
            answer.append(path)
            return True
        
        if curr not in a:
            return False
        
        for dest in a[curr]:
            if tickets[curr+dest] > 0:
                tickets[curr+dest] -= 1
                dfs(dest, path + [dest], a, tickets)
                tickets[curr+dest] += 1
    
    dfs('ICN', ['ICN'], a, ticket)
    answer.sort()
    
    return answer[0]