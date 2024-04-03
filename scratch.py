from kill_team.board.base import BaseBoard

base_board = BaseBoard()
base_board.render_board()
base_board.board[1000:2000, 1000:2000] = 10


