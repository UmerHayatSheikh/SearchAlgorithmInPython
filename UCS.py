from util import *

def UCS(graph, weights, start, goal, directed=True):
    print(start, goal)
    queue = [(0,start)]
    visited = []
    parent = {start: start}
    while queue:
        cost,first = queue.pop(0)
        visited.append(first)
        print(first)
        if goal == first:
            return (1, findPath(goal, parent))
        for i in graph[first]:
            if i not in visited:
                parent[i] = first
                queue.append((cost+weights[(first,i)],i))
        queue.sort()

    return (0, "Path does not found")

