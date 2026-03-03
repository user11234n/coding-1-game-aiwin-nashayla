# Write your game here
import curses
game_data = { 
    'width':10,
    'height':10,
    'player': {"x": 0, "y": 0},
    'game_elements': {'truck': "\U0001F69A",
    'toilet': "\U0001F6BD",
    'rollercoaster': "\U0001F3A2"},
    # Store board dimensions, player/enemy positions, score, energy, collectibles, and icons
}

    # Print the board and all game elements using curses
def draw_board(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)
    screen.refresh()
    screen.getkey()  # pause so player can see board
def welcome_screen():
    print("Welcome to the personality quiz! Please answer honestly")
def move_player(key):
    x = game_data['player']['x']
    y = game_data['player']['y']
    new_x, new_y = x, y
    key = key.lower()
# curses.wrapper(draw_board)

print(game_data['game_elements']['toilet'])

# Good Luck!