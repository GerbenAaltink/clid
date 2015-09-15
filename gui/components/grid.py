import curses
import math




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
        self.update_columns()
        self.refresh()

    def refresh(self):
        self.update_columns()
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