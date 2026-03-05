# Write your game here
import curses
game_data = { 
    'width':10,
    'height':10,
    'player': {"x": 0, "y": 0},
    'game_elements': {'truck': "\U0001F69A",
    'toilet': "\U0001F6BD",
    'rollercoaster': "\U0001F3A2",
    'demon kitty': "\U0001F638"},
    # Store board dimensions, player/enemy positions, score, energy, collectibles, and icons
}

    # Print the board and all game elements using curses
for y in range(game_data['height']):
    row = ""
    for x in range(game_data['width']):
        if x == game_data['player']['x'] and y == game_data['player']['y']:
            row += game_data['game_elements']['demon kitty']
def move_player(key):
    x = game_data['player']['x']
    y = game_data['player']['y']
    new_x, new_y = x, y
    key = key.lower()
    if key == "w" and y > 0:
        new_y -= 1
    elif key == "s" and y < game_data['height'] - 1:
        new_y += 1    
    else:
        return

def draw_board(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)
def welcome_screen():
    print("Welcome to the personality quiz! Please answer honestly")

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    draw_board(stdscr)

    while True:
        print("hello")
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key:
            if key.lower() == "q":
                break

            move_player(key)
            draw_board(stdscr)
curses.wrapper(main)


# print(game_data['game_elements']['toilet'])

# Good Luck!