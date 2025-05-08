import random
from collections import deque

# Directions: Down, Up, Right, Left
directions = [(1, 0, "Down"), (-1, 0, "Up"), (0, 1, "Right"), (0, -1, "Left")]

class Node:
    def __init__(self, x, y, level, path):
        self.x = x
        self.y = y
        self.level = level
        self.path = path  # path stores the steps taken to reach this node

def generate_grid(n, obstacle_ratio=0.3):
    grid = [[1 if random.random() > obstacle_ratio else 0 for _ in range(n)] for _ in range(n)]
    return grid

def print_grid(grid):
    print("Generated Grid (1=free, 0=obstacle):")
    for row in grid:
        print(" ".join(map(str, row)))
    print()

def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n

def bfs(grid, start, goal):
    n = len(grid)
    visited = [[False]*n for _ in range(n)]
    queue = deque()
    queue.append(Node(start[0], start[1], 0, []))
    visited[start[0]][start[1]] = True

    while queue:
        current = queue.popleft()

        if (current.x, current.y) == goal:
            print("Goal found")
            print("Number of moves required =", current.level)
            for move in current.path:
                print(f"Moving {move[0]} -> {move[1]}")
            return

        for dx, dy, dir in directions:
            new_x, new_y = current.x + dx, current.y + dy
            if is_valid(new_x, new_y, n) and not visited[new_x][new_y] and grid[new_x][new_y] == 1:
                visited[new_x][new_y] = True
                new_path = current.path + [(dir, (new_x, new_y))]
                queue.append(Node(new_x, new_y, current.level + 1, new_path))

    print("Goal cannot be reached from starting block.")

if __name__ == "__main__":
    N = int(input("Enter grid size (N): "))
    grid = generate_grid(N)
    print_grid(grid)

    sx, sy = map(int, input("Enter Start X Y (0-indexed): ").split())
    gx, gy = map(int, input("Enter Goal X Y (0-indexed): ").split())

    if grid[sx][sy] == 0 or grid[gx][gy] == 0:
        print("Invalid Start or Goal (on obstacle). Exiting.")
    else:
        bfs(grid, (sx, sy), (gx, gy))
