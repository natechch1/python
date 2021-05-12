import curses

def c_main(stdscr: 'curses._CursesWindow') -> int:
    while True:
        stdscr
        #stdscr.addstr(0, 0, "Hello World!")
        char = stdscr.get_wch()
        break
    return 0

def main() -> int:
    return curses.wrapper(c_main)

if __name__ == '__main__':
    exit(main())