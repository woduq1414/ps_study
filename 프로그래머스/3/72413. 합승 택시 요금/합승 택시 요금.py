def solution(n, s, a, b, fares):
    
    graph = [[] for _ in range(n + 1)]
    dist = [[10**12] * (n + 1) for _ in range(n+1)]
    
    for fare in fares:
        graph[fare[0]].append([fare[1], fare[2]])
        graph[fare[1]].append([fare[0], fare[2]])

        dist[fare[0]][fare[1]] = fare[2]
        dist[fare[1]][fare[0]] = fare[2]
    
    
    for i in range(1, n+1):
        dist[i][i] = 0
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
    cost_list = []
    
    for i in range(1, n + 1):
        cost_list.append(dist[s][i] + dist[i][a] + dist[i][b])
    answer = min(cost_list)
    
    
    return answer