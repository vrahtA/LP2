from heapq import heappush, heappop
def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = [(0, start)]
    g_score = {start: 0}
    f_score = {start: abs(goal[0] - start[0]) + abs(goal[1] - start[1])}
    came_from = {}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while open_list:
        _, current = heappop(open_list)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        for dx, dy in directions:
            next_pos = (current[0] + dx, current[1] + dy)
            
            if 0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols and grid[next_pos[0]][next_pos[1]] == 0:
                tentative_g_score = g_score[current] + 1
                
                if next_pos not in g_score or tentative_g_score < g_score[next_pos]:
                    came_from[next_pos] = current
                    g_score[next_pos] = tentative_g_score
                    f_score[next_pos] = tentative_g_score + abs(goal[0] - next_pos[0]) + abs(goal[1] - next_pos[1])
                    heappush(open_list, (f_score[next_pos], next_pos))
    return []
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    start = (0, 0)
    goal = (2, 3)
    path = astar(grid, start, goal)
    print("Path:", path)
