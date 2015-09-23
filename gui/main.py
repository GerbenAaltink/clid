import curses

from time import sleep
from components.grid import Grid


def test_dict():

    data = []

    for x in range(0,50):
        data.append({
            'column_1': 'A{}'.format(x),
            'column_2': 'B{}'.format(x),
            'column_3': 'C{}'.format(x),
            'column_4': 'D{}'.format(x)
        })

    return data

def handle_user_input(stdscr, input_string):

    pass


def main(stdscr):

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(10, curses.COLOR_RED, curses.COLOR_WHITE)

    stdscr.nodelay(False)
    stdscr.leaveok(True)
    stdscr.clear()
    stdscr.refresh()
    curses.delay_output(1)

    key_buffer = []

    y, x = stdscr.getmaxyx()
    grid = Grid(stdscr, y - 20, x - 20, 10, 10, test_dict())

    while True:

        try:

            try:
                key = stdscr.getkey()

            except:
                key = None

            if key == '\n':

                handle_user_input(stdscr, ''.join(key_buffer))

                key_buffer = []

                continue

            if key == 'q':
                break

            y, x = stdscr.getmaxyx()
            grid.update( y - 20, x - 20, key)

            if key is not None:
                key_buffer.append(key)
            else:
                sleep(0.1)

        except KeyboardInterrupt:
            pass

curses.wrapper(main)