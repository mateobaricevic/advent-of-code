from collections import defaultdict

with open('2019/day_6/input.txt', 'r') as input_file:
    orbits = input_file.read().splitlines()
    orbits = [orbit.split(')') for orbit in orbits]
    # print(orbits)

graph = defaultdict(list)
for orbit in orbits:
    graph[orbit[0]].append(orbit[1])
    graph[orbit[1]].append(orbit[0])

# print(graph)

def breadth_first_search(graph, start, goal):
    explored = []
    queue = [[start]]
    
    if start == goal:
        print('Same start and goal node.')
        return 0
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in explored:
            neighbours = graph[node]
            
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                
                if neighbour == goal:
                    print(f'Shortest path from {start} to {goal}: {new_path}')
                    return len(new_path)
            
            explored.append(node)

    print(f"{start} and {goal} nodes aren't connected!")
    return -1

print(breadth_first_search(graph, 'YOU', 'SAN') - 3)