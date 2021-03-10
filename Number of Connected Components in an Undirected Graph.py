n = 4
edges = [[0,1],[2,3],[1,2]]

def countComponents(n, edges):
    parents = [number for number in range(n)] #create list of nodes to record parent node for each edge
    
    def union(num1, num2): #union function recieves edge input and gives each node in edge the same parent node
        root1, root2 = find(num1), find(num2)
        if root1 != root2:
            parents[root2] = parents[root1]
    
    def find(number): #find function recieves node and changes its parent to the root parent of all other nodes with connected edges
        if number != parents[number]:
            parents[number] = find(parents[number])
        return parents[number]
    
    for edge in edges: #for every edge, find root parent group both nodes with that root parent node
        union(edge[0], edge[1])
        
        
    roots = set() #create root set to collect unique parent nodes
    for parent in parents: #reverse through parent nodes and place them in roots set
        roots.add(find(parent))
    return len(roots) #return number of unique parents (number of connected components)

print(countComponents(n,edges))