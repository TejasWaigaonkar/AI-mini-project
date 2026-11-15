import heapq


def find_path(grid, start, goal):
    """A* search on a grid. 0 = free, 1 = wall, 2 = fire."""
    rows, cols = len(grid), len(grid[0])
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    queue = [(heuristic(start, goal), 0, start)]
    previous = {start: None}
    best = {start: 0}
    while queue:
        _, cost, current = heapq.heappop(queue)
        if cost != best[current]:
            continue
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = previous[current]
            return path[::-1]
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nxt = (current[0] + dr, current[1] + dc)
            r, c = nxt
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0:
                new_cost = cost + 1
                if new_cost < best.get(nxt, float('inf')):
                    best[nxt] = new_cost
                    previous[nxt] = current
                    heapq.heappush(queue, (new_cost + heuristic(nxt, goal), new_cost, nxt))
    return []
