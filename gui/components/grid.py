import curses
import math


def log(message):
    from datetime import datetime
    with open("/tmp/grid.txt", "a") as f:
        f.write(str(datetime.now()) + "  -  " + str(message) + "\n")



class Grid:

    def __init__(self, main, height, width, offset_x, offset_y, data):

        # BY DEFAULT
        curses.init_pair(10, curses.COLOR_WHITE, curses.COLOR_RED)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        # INSTANCE
        self.main = main
        self.window = curses.newwin(height, width, offset_y, offset_x)
        self.width = width
        self.height = height
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.data = data
        self.columns = self.data[0].keys() if len(self.data) else {}
        self.column_count = len(self.columns)
        self.column_width = int(math.floor(self.width / self.column_count)) - 1
        self.column_row = 0
        self.index = 0
        self.row_padding = 1    # Count of rows not to be used for e.g. column bar / status bar (tested!)
        self.refresh()

    def update(self, height, width, key):

        self.height = height
        self.width = width
        self.column_width = int(math.floor(self.width / self.column_count)) - 1

        if key == 'KEY_DOWN':
            self.scroll_down()
        elif key == 'KEY_UP':
            self.scroll_up()

        self.refresh()

    def scroll_down(self):
        self.index = min(len(self.data) - self.height + self.row_padding, self.index + 1)

    def scroll_up(self):
        self.index = max(0, self.index - 1)

    def refresh(self):
        self.update_columns()
        self.update_rows()
        self.window.refresh()

    def update_cell(self, row_index, column_index, text, color_pair=1):

        start = self.column_width * column_index
        content = text.ljust(self.column_width, ' ')

        self.window.addstr(row_index, start, content, curses.color_pair(color_pair))

    def update_row(self, row_index, data, color_pair=1):
        for column_index in range(0, self.column_count):
            self.update_cell(row_index, column_index, data[column_index], color_pair)

    def update_columns(self):
        self.update_row(0, self.columns, 10)

    def update_rows(self):
        for x in range(0, self.height - self.row_padding):
            self.update_row(x + 1, self.data[x + self.index].values())