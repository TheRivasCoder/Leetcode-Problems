n = 4
edges = [[0,1],[2,3],[1,2]]

def countComponents(n, edges):
    parents = [number for number in range(n)]
    
    def union(num1, num2):
        root1, root2 = find(num1), find(num2)
        if root1 != root2:
            parents[root2] = parents[root1]
    
    def find(number):
        if number != parents[number]:
            parents[number] = find(parents[number])
        return parents[number]
    
    for edge in edges:
        union(edge[0], edge[1])
        
        
    roots = set()
    for parent in parents:
        roots.add(find(parent))
    return len(roots)

print(countComponents(n,edges))