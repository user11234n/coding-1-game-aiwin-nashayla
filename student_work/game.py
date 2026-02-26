# Write your game here
import curses
game_data = { 
'width':10,
'height':10,
{'truck': "\1F69A",
'toilet': "\1F6BD",
'rollercoaster': "\1F3A2"}
    # Store board dimensions, player/enemy positions, score, energy, collectibles, and icons
}

 
    # Print the board and all game elements using curses
def draw_board(screen):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)
    screen.refresh()
    screen.getkey()  # pause so player can see board

curses.wrapper(draw_board)

# Good Luck!