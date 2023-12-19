# from queue import PriorityQueue
from queue import PriorityQueue
import numpy as np

visited = set()
queue = PriorityQueue()
queue.put((0,      # Heat
           (0, 0), # node; row,col
           (0, 0), # direction row, direction col
           0       # length
           ))

fh = open("big.txt", 'r')
maze = np.array([list(map(int, [*line.strip()])) for line in fh.readlines()])

end = (len(maze) - 1, len(maze[0]) - 1) 

def bounds(node, maze):
    if 0 <= node[0] < len(maze) and 0 <= node[1] < len(maze[0]):
        return True
    return False

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
while queue:
    heat, node, direction, length = queue.get()
    
    if (node) == end:
        print(heat)
        break

    if (node, direction, length) in visited:
        continue

    visited.add((node, direction, length))
    
    # Move forward:
    # Length less than 3:
    if length < 3 and direction != (0, 0):
        new_node = (node[0] + direction[0], node[1] + direction[1])
        if bounds(new_node, maze):
            queue.put((heat + maze[new_node], (new_node), direction, length + 1))

    # Turn
    for ndr, ndc in directions:
        if (ndr, ndc) != direction and (ndr, ndc) != (-direction[0], -direction[1]):
            new_node = (node[0] + ndr, node[1] + ndc)
            if bounds(new_node, maze):
                queue.put((heat + maze[new_node], new_node, (ndr, ndc), 1))