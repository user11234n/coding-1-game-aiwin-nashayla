import curses
import locale  # Set locale for emoji support
locale.setlocale(locale.LC_ALL, '')

MAZE = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 'P', 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 'E', 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

WALL, PATH, EXIT = 1, 0, 2
MAZE_HEIGHT, MAZE_WIDTH = len(MAZE), len(MAZE[0])

def find_pos(char):
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if MAZE[y][x] == char: return y, x
    return None, None

def draw_maze(stdscr, player_char, py, px, ey, ex, moves):
    stdscr.clear()
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            cell = MAZE[y][x]
            if cell == WALL: stdscr.addch(y, x, '#')
            elif cell == EXIT: stdscr.addch(y, x, '.')
            else: stdscr.addch(y, x, ' ')
    
    stdscr.addstr(MAZE_HEIGHT + 1, 0, f"Moves: {moves}")
    try:
        stdscr.addstr(ey, ex, '!')  # Enemy
        stdscr.addstr(py, px, player_char)
    except curses.error: pass
    stdscr.refresh()

def quiz(stdscr):
    questions = {
        "How did your story start?": ["You won a game.", "You were born.", "You died."],
        "What was your goal?": ["An adventure.", "To have fun.", "Morality."],
        "Who stopped you?": ["Your friends.", "Nobody (You chose to).", "Everyone."],
        "How long did you live?": ["84 years.", "You didn't.", "30 years."],
        "What did you enjoy?": ["Everything.", "Nothing.", "Getting what you wanted."]
    }
    keys = list(questions.keys())
    answers = []
    q_idx, sel = 0, 0
    cat = "\U0001F63A"

    while q_idx < len(keys):
        q = keys[q_idx]
        opts = questions[q]
        stdscr.clear()
        stdscr.addstr(0, 0, q, curses.A_BOLD)
        for i, opt in enumerate(opts):
            if i == sel:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(i + 2, 4, opt)
                stdscr.attroff(curses.A_REVERSE)
                stdscr.addstr(i + 2, 0, cat) 
            else:
                stdscr.addstr(i + 2, 4, opt)
        stdscr.refresh()
        
        k = stdscr.getch()
        if k in [curses.KEY_UP, ord('w')] and sel > 0: sel -= 1
        elif k in [curses.KEY_DOWN, ord('s')] and sel < len(opts) - 1: sel += 1
        elif k in [ord(' '), 10, curses.KEY_ENTER]:
            answers.append(opts[sel])
            q_idx += 1
            sel = 0
        elif k == ord('q'): return None
    return answers

def evaluate_results(answers):
    
    first_ans = answers[0]
    if "won" in first_ans: return "\U0001F3A2"  # Rollercoaster
    if "born" in first_ans: return "\U0001F69A"  # Truck
    if "died" in first_ans: return "\U0001F31F"  # Star
    return "\U0001F437"  # Pig default

def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)
    
    # 1. Run Quiz
    results = quiz(stdscr)
    if not results: return
    player_char = evaluate_results(results)

    # 2. Maze
    p_y, p_x = find_pos('P')
    e_y, e_x = find_pos('E')
    move_count = 0
    stdscr.nodelay(1)
    stdscr.timeout(100)  
    while True:
        draw_maze(stdscr, player_char, p_y, p_x, e_y, e_x, move_count)
        key = stdscr.getch()
        
        if key == ord('q'): break
        
        ny, nx = p_y, p_x
        if key == curses.KEY_UP: ny -= 1
        elif key == curses.KEY_DOWN: ny += 1
        elif key == curses.KEY_LEFT: nx -= 1
        elif key == curses.KEY_RIGHT: nx += 1

        
        if (ny, nx) != (p_y, p_x):
            if 0 <= ny < MAZE_HEIGHT and 0 <= nx < MAZE_WIDTH:
                if MAZE[ny][nx] != WALL:
                    p_y, p_x = ny, nx
                    move_count += 1
                    if MAZE[p_y][p_x] == EXIT: break

            
            if abs(p_y - e_y) > abs(p_x - e_x):
                my = 1 if p_y > e_y else -1
                if MAZE[e_y + my][e_x] != WALL: e_y += my
            else:
                mx = 1 if p_x > e_x else -1
                if MAZE[e_y][e_x + mx] != WALL: e_x += mx
            
            if p_y == e_y and p_x == e_x: break

    
    stdscr.nodelay(0)
    stdscr.clear()
    msg = "You Win!" if MAZE[p_y][p_x] == EXIT else "Game Over!"
    stdscr.addstr(0, 0, f"{msg}\nTotal Moves: {move_count}\nPress 'q' to quit.")
    while stdscr.getch() != ord('q'): pass

if __name__ == "__main__":
    curses.wrapper(main)
