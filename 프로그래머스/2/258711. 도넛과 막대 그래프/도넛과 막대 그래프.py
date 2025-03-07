from collections import defaultdict

def solution(edges):
    answer = []
    
    enter_list = defaultdict(list)
    exit_list = defaultdict(list)
    
    for edge in edges:
        enter_list[edge[1]].append(edge[0])
        exit_list[edge[0]].append(edge[1])
        
    max_exit_degree = -1
    max_exit_degree_node = -1
    for node, exit_node_list in exit_list.items():
        degree = len(exit_node_list)
        if degree > max_exit_degree and len(enter_list[node]) == 0:
            max_exit_degree_node = node
            max_exit_degree = degree
            

    
    c1, c2, c3 = 0, 0, 0
    for node in exit_list[max_exit_degree_node]:
        if not exit_list[node]:
            c2 += 1
        else:
            new_node = node
            while True:
                new_exit_list = [x for x in exit_list[new_node] ]
                
                if len(new_exit_list) == 0:
                    c2 += 1
                    break
                
                new_node = new_exit_list[0]
                
                
                if len(new_exit_list) >= 2:
                    c3 += 1
                    break
                elif len(new_exit_list) == 0:
                    c2 += 1
                    break
                elif new_node == node:
                    c1 += 1
                    break
                
                
            
    answer = [
        max_exit_degree_node, c1,c2,c3
    ]
            
        
    return answer