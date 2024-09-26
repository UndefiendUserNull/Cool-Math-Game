import curses


def main(stdscr):
    stdscr.clear()  # Clear the screen
    stdscr.addstr(0, 0, "Welcome to the Curses Example!")  # Add text at position (0,0)
    stdscr.addstr(1, 0, "Press any key to continue...")  # Add another line of text
    stdscr.refresh()  # Refresh the screen to show the text
    stdscr.getch()  # Wait for a key press


curses.wrapper(main)  # Initialize and run the main function
