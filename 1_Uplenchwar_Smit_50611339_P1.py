def BFS_DFS(n, m, s, t, edges):
    
    # Please write your algorithm here:
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = []
    for i in range(0,n+1):
        visited.append(False)
    queue = [s]
    
    #We will mark the source node as visted
    visited[s] = True
    
    result = "no"
    
    while queue:
        node = queue.pop(0)
        # We will write the base case i.e. if the popped node is t(destination) or not
        if node==t:
            result = "yes"
            return result
        
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    # .................................
    return result


def read_input():
    n, m = map(int, input().split())
    s, t = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, m, s, t, edges


if __name__ == "__main__":
    n, m, s, t, edges = read_input()
    result = BFS_DFS(n, m, s, t, edges)
    print(result)
