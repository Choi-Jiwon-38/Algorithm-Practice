def solution(park, routes):
    maps = []
    curr_pos = [None, None]
    
    n = len(park)
    m = len(park[0])
    
    for y in range(n):
        maps.append([])
        for x in range(m):
            if park[y][x] == 'S':
                curr_pos[0] = y
                curr_pos[1] = x
                
            maps[y].append(park[y][x])
    
    for route in routes:
        pos, dist_str = route.split(" ")
        dist = int(dist_str)
        
        if pos == 'N':
            # 주어진 방향으로 이동할 때 공원 벗어나는지
            if curr_pos[0] - dist < 0:
                continue
            
            # 주어진 방향으로 이동 중 장애물을 만나는지
            flag = False
            
            for i in range(curr_pos[0], curr_pos[0] - dist - 1, -1):
                if maps[i][curr_pos[1]] == 'X':
                    flag = True
                    break
            
            if flag: 
                continue
            
            # 이동 가능
            curr_pos[0] -= dist
            
        elif pos == 'S':
            # 주어진 방향으로 이동할 때 공원 벗어나는지
            if curr_pos[0] + dist >= n:
                continue
            
            # 주어진 방향으로 이동 중 장애물을 만나는지
            flag = False
            
            for i in range(curr_pos[0], curr_pos[0] + dist + 1):
                if maps[i][curr_pos[1]] == 'X':
                    flag = True
                    break
            
            if flag: 
                continue
            
            # 이동 가능
            curr_pos[0] += dist
            
        elif pos == 'W':
            # 주어진 방향으로 이동할 때 공원 벗어나는지
            if curr_pos[1] - dist < 0:
                continue
            
            # 주어진 방향으로 이동 중 장애물을 만나는지
            flag = False
            
            for i in range(curr_pos[1], curr_pos[1] - dist - 1, -1):
                if maps[curr_pos[0]][i] == 'X':
                    flag = True
                    break
            
            if flag: 
                continue
            
            # 이동 가능
            curr_pos[1] -= dist
        elif pos == 'E':
            # 주어진 방향으로 이동할 때 공원 벗어나는지
            if curr_pos[1] + dist >= m:
                continue
            
            # 주어진 방향으로 이동 중 장애물을 만나는지
            flag = False
            
            for i in range(curr_pos[1], curr_pos[1] + dist + 1):
                if maps[curr_pos[0]][i] == 'X':
                    flag = True
                    break
            
            if flag: 
                continue
            
            # 이동 가능
            curr_pos[1] += dist
            
    return curr_pos