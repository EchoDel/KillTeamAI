import numpy as np
from matplotlib import pyplot as plt

from kill_team.operatives.base import BaseTeam

UNITS_PER_INCH = 100


class BaseBoard:
    def __init__(self, team_1: BaseTeam, team_2: BaseTeam,
                 board_height: int = 30, board_width: int = 22):
        self.board = np.zeros((board_width * UNITS_PER_INCH,
                               board_height * UNITS_PER_INCH))

        fig, ax = plt.subplots()
        self.ax = ax
        self.fig = fig
        self.team_1 = team_1
        self.team_2 = team_2

    def render_board(self):
        im = self.ax.imshow(self.board)
