
import time
import streamlit as st
from simulation import simulate, EXIT

st.set_page_config(page_title='AI Evacuation Planner', layout='centered')

st.title('Dynamic Multi-Agent Evacuation Planner')
st.write('Mini project: A* heuristic search + dynamic replanning during fire.')

st.caption('Legend: ⬜ Free  ⬛ Wall  🔥 Fire  🟦 Agent  🟩 Exit  🔵 Path')


def draw(grid, agents, visited_paths):
    lines = []

    for r, row in enumerate(grid):
        line = ''

        for c, cell in enumerate(row):
            point = (r, c)

            if point == EXIT:
                symbol = '🟩'

            elif cell == 1:
                symbol = '⬛'

            elif cell == 2:
                symbol = '🔥'

            elif point in agents and point != EXIT:
                symbol = '🟦'

            elif point in visited_paths:
                symbol = '🔵'

            else:
                symbol = '⬜'

            line += symbol

        lines.append(line)

    return '\n'.join(lines)


# Run simulation
frames, replans = simulate()

map_box = st.empty()
message = st.empty()
summary = st.empty()


if st.button('▶ Start Simulation'):

    for grid, agents, description, visited_paths in frames:

        map_box.markdown(
            '<div style="font-size:27px;line-height:1.5;'
            'white-space:pre;font-family:monospace">'
            + draw(grid, agents, visited_paths)
            + '</div>',
            unsafe_allow_html=True
        )

        message.info(description)
        time.sleep(0.35)

    evacuated = sum(pos == EXIT for pos in frames[-1][1])

    summary.success(
        f'Evacuated: {evacuated}/3 | '
        f'Fire-triggered replanning events: {replans} | '
        f'Steps: {len(frames)-2}'
    )

else:
    grid, agents, description, visited_paths = frames[0]

    map_box.markdown(
        '<div style="font-size:27px;line-height:1.5;'
        'white-space:pre;font-family:monospace">'
        + draw(grid, agents, visited_paths)
        + '</div>',
        unsafe_allow_html=True
    )

    message.info('Click Start Simulation to begin.')
