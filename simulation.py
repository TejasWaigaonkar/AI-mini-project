from astar import find_path

MAP = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
]
STARTS = [(0, 0), (6, 0), (4, 2)]
EXIT = (0, 6)
FIRE = (2, 3)



def simulate():
    grid = [row[:] for row in MAP]
    agents = STARTS[:]
    visited_paths = set(STARTS)

    frames = [(grid, agents[:], 'Initial positions: agents plan routes using A*.', visited_paths.copy())]
    replans = 0

    for tick in range(1, 25):
        if tick == 3:
            grid[FIRE[0]][FIRE[1]] = 2
            frames.append((
                [row[:] for row in grid],
                agents[:],
                'Fire appeared! Agents replan safe routes.',
                visited_paths.copy()
            ))
            replans += sum(pos != EXIT for pos in agents)

        next_positions = []

        for pos in agents:
            if pos == EXIT:
                next_positions.append(pos)
                continue

            path = find_path(grid, pos, EXIT)
            next_positions.append(path[1] if len(path) > 1 else pos)

        agents = next_positions
        visited_paths.update(agents)

        frames.append((
            [row[:] for row in grid],
            agents[:],
            f'Time step {tick}: agents move toward the exit.',
            visited_paths.copy()
        ))

        if all(pos == EXIT for pos in agents):
            break

    return frames, replans

