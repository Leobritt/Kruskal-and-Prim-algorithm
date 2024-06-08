class UnionFind:
    def __init__(self, vertices): 
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if vertex != self.parent[vertex]:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def kruskal(graph):
    minimum_spanning_tree = []  
    edges = [(weight, u, v) for u in graph for v, weight in graph[u]]
    edges.sort()

    vertices = set(v for u in graph for v, _ in graph[u])  
    uf = UnionFind(vertices)

    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            minimum_spanning_tree.append((u, v, weight))
            uf.union(u, v)

    return minimum_spanning_tree

graph = {
    'Aberdeen': [('Edinburgh', 120), ('Fort William', 147), ('Glasgow', 142), ('Inverness', 104), ('Perth', 81)],
    'Edinburgh': [('Aberdeen', 120), ('Fort William', 132), ('Glasgow', 42), ('Inverness', 157), ('Perth', 45)],
    'Fort William': [('Aberdeen', 147), ('Edinburgh', 132), ('Glasgow', 102), ('Inverness', 66), ('Perth', 105)],
    'Glasgow': [('Aberdeen', 142), ('Edinburgh', 42), ('Fort William', 102), ('Inverness', 168), ('Perth', 61)],
    'Inverness': [('Aberdeen', 104), ('Edinburgh', 157), ('Fort William', 66), ('Glasgow', 168), ('Perth', 112)],
    'Perth': [('Aberdeen', 81), ('Edinburgh', 45), ('Fort William', 105), ('Glasgow', 61), ('Inverness', 112)]
}

minimum_spanning_tree = kruskal(graph)
print("Árvore Geradora Mínima:")
print(minimum_spanning_tree)
