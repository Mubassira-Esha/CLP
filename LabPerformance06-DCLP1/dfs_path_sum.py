def dfs(grid, x, y, visited, current_sum, target, path):
    rows, cols = len(grid), len(grid[0])
    if current_sum > target:
        return False
    if current_sum == target:
        return True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
            visited[nx][ny] = True
            path.append((nx, ny))
            if dfs(grid, nx, ny, visited, current_sum + grid[nx][ny], target, path):
                return True
            path.pop()
            visited[nx][ny] = False
    return False

def find_path_with_sum(grid, target):
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            path = [(i, j)]
            visited[i][j] = True
            if dfs(grid, i, j, visited, grid[i][j], target, path):
                print("Path found")
                print("DFS Traversal Order:", path)
                return
    print("Path not found")

if __name__ == "__main__":
    n, m = map(int, input("Enter grid size (rows cols): ").split())
    grid = []
    print("Enter the grid values row by row:")
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    target = int(input("Enter target value: "))
    find_path_with_sum(grid, target)
