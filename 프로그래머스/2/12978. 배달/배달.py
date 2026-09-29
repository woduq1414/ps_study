import heapq
from collections import defaultdict

def solution(N, road, K):
    heap = []
    
    answer = 0
    
    graph = defaultdict(list)
    for r in road:
        graph[r[0]].append([r[1], r[2]])
        graph[r[1]].append([r[0], r[2]])
        

    dist = [10**12] * (N + 1)
    
    
    dist[1] = 0
    heapq.heappush(heap, [0, 1])
    
    while heap:
        cost, cur = heapq.heappop(heap)
        print(cost,cur)
        
        if cost > dist[cur]:
            continue
        
        for next_node in graph[cur]:
            if cost + next_node[1] < dist[next_node[0]]:
                dist[next_node[0]] = cost + next_node[1]
                heapq.heappush(heap, [cost + next_node[1], next_node[0]])
    
    
    return len([
        x for x in dist if x <= K
    ])
    

