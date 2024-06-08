import heapq

def prim(graph):
    min_span_tree = []
    visited = set()
    start_vertex = list(graph.keys())[0]
    visited.add(start_vertex)
    edges = [(cost, start_vertex, to_vertex) for to_vertex, cost in graph[start_vertex]]
    heapq.heapify(edges)
    
    while edges:
        cost, from_vertex, to_vertex = heapq.heappop(edges)
        if to_vertex not in visited:
            visited.add(to_vertex)
            min_span_tree.append((from_vertex, to_vertex, cost))
            for next_to_vertex, next_cost in graph[to_vertex]:
                if next_to_vertex not in visited:
                    heapq.heappush(edges, (next_cost, to_vertex, next_to_vertex))
    return min_span_tree

# Exemplo de uso
graph = {
    'Aberdeen': [('Edinburgh', 120), ('Fort William', 147), ('Glasgow', 142), ('Inverness', 104), ('Perth', 81)],
    'Edinburgh': [('Aberdeen', 120), ('Fort William', 132), ('Glasgow', 42), ('Inverness', 157), ('Perth', 45)],
    'Fort William': [('Aberdeen', 147), ('Edinburgh', 132), ('Glasgow', 102), ('Inverness', 66), ('Perth', 105)],
    'Glasgow': [('Aberdeen', 142), ('Edinburgh', 42), ('Fort William', 102), ('Inverness', 168), ('Perth', 61)],
    'Inverness': [('Aberdeen', 104), ('Edinburgh', 157), ('Fort William', 66), ('Glasgow', 168), ('Perth', 112)],
    'Perth': [('Aberdeen', 81), ('Edinburgh', 45), ('Fort William', 105), ('Glasgow', 61), ('Inverness', 112)]
}

print("Árvore de spanning mínima (Prim):", prim(graph)) 