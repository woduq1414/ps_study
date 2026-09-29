from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[] for _ in range(n + 1)]
    dist = [-1 for _ in range(n + 1)]
    
    queue = deque()
    
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
    
    queue.append(destination)
    dist[destination] = 0

    while queue:
        
        
        node = queue.popleft()
    
        
        for near_node in graph[node]:
        
            if dist[near_node] == -1:
                dist[near_node] = dist[node] + 1
                queue.append(near_node)
        
    
    return [
        dist[x] for x in sources
    ]