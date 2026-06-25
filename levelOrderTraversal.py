from collections import deque
graph={
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = set()
queue = deque(['A'])

while queue:
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=' ')
        visited.add(vertex)
        queue.extend(graph[vertex])