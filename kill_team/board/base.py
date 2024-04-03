import numpy as np
from matplotlib import pyplot as plt

UNITS_PER_INCH = 100


class BaseBoard:
    def __init__(self, board_height: int = 30, board_width: int = 22):
        self.board = np.zeros((board_height * UNITS_PER_INCH,
                               board_width * UNITS_PER_INCH))

        fig, ax = plt.subplots()
        self.ax = ax
        self.fig = fig

    def render_board(self):
        im = self.ax.imshow(self.board)
