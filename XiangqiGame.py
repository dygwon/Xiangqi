# Author: Daniel Gwon
# Date: 3/4/2020
# Description:


# Implementation Notes:
# 1. Game
#       game won?
#       in bounds?
#       has a piece?
#       right player's piece?
# 2. Board
#       only holds pieces
# 3. Piece
#       move valid for type of Piece?
#       move valid given placement of other Pieces on board?


class XiangqiGame:
    """
    Creates a game of Xiangqi
    """

    def __init__(self):
        """
        init the game
        """
        self._game_state = 'UNFINISHED'         # 'UNFINISHED', 'RED_WON', 'BLACK_WON'
        self._red_in_check = False
        self._black_in_check = False
        self._turn = 'red'                      # red starts
        self._board = Board()

    def get_game_state(self):
        """
        gives the current game state
        :return: str ('UNFINISHED', 'RED_WON', or 'BLACK_WON')
        """
        return self._game_state

    def _set_game_state(self, state):
        """
        update the game state
        :param state: str
        :return: n/a
        """
        self._game_state = state

    def _update_check(self, player, state):
        """
        sets player to state
        :param player: str ('red' or 'black')
        :param state: bool
        :return: n/a
        """
        if player == 'red':
            self._red_in_check = state
        else:
            self._black_in_check = state

    def is_in_check(self, player):
        """
        tells if given player is in check
        :param player: str ('red' or 'black')
        :return: bool
        """
        if player == 'red':
            return self._red_in_check
        return self._black_in_check

    def _update_turn(self):
        """
        updates whose turn it is
        :return: n/a
        """
        if self._turn == 'red':
            self._turn = 'black'
        else:
            self._turn = 'red'

    def _pos_to_ints(self, start, to):
        """
        converts pos in str to list indices
        :param start str
        :param to: str
        :return: [int row_s, int col_s, int row_t, int col_t]
        """
        row_s = int(start[1])
        col_s = int(start[0])
        row_t = int(to[1])
        col_t = int(to[0])
        return [row_s, col_s, row_t, col_t]


    def _has_a_piece(self, r, c):
        """
        True if piece at position, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        if self._board.get_piece(r, c) == '':
            return False
        return True

    def _is_player_piece(self, r, c):
        """
        True if right piece, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        if self._board.get_piece(r, c).get_player() != self._turn:
            return False
        return True

    def _is_in_bounds(self, r, c):
        """
        True if in bounds, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        if r < 0 or r > 9:          # row out of bounds
            return False
        elif c < 0 or c > 8:        # col out of bounds
            return False
        return True

    def make_move(self, start, to):
        """
        moves a piece from start position to to position
        :param start: str
        :param to: str
        :return: bool
        """

        # convert start and to to board indices
        pos = self._pos_to_ints(start, to)

        # is game over?
        if self.get_game_state != 'UNFINISHED':
            return False

        # start in bounds?
        if not self._is_in_bounds(pos[0], pos[1]):
            return False

        # to in bounds?
        if not self._is_in_bounds(pos[2], pos[3]):
            return False

        # piece at to?
        if not self._has_a_piece(pos[0], pos[1]):
            return False

        # right player's piece?
        if not self._is_player_piece(pos[0], pos[1]):
            return False

        # make the move
        result = self._board.make_move(pos[0], pos[1], pos[2], pos[3])

        # update player's turn
        self._update_turn()

        # update game state
        # TODO update the game state after making a move

        return result


class Board:
    """
    Creates a Xiangqi board
    """

    def __init__(self):
        """
        init the board
        """

        # initial board
        self._board = [['' for _ in range(9)] for _ in range(10)]   # 10 rows x 9 cols

        # set up the board
        self._board[0][4] = gen_b = General('black', 0, 4, self._board)
        self._board[0][3] = adv_b_1 = Advisor('black', 0, 3, self._board)
        self._board[0][5] = adv_b_2 = Advisor('black', 0, 5, self._board)
        self._board[0][2] = ele_b_1 = Elephant('black', 0, 2, self._board)
        self._board[0][6] = ele_b_2 = Elephant('black', 0, 6, self._board)
        self._board[0][1] = hor_b_1 = Horse('black', 0, 1, self._board)
        self._board[0][7] = hor_b_2 = Horse('black', 0, 7, self._board)
        self._board[0][0] = cha_b_1 = Chariot('black', 0, 0, self._board)
        self._board[0][8] = cha_b_2 = Chariot('black', 0, 8, self._board)
        self._board[2][1] = can_b_1 = Cannon('black', 2, 1, self._board)
        self._board[2][7] = can_b_2 = Cannon('black', 2, 7, self._board)
        self._board[3][0] = sol_b_1 = Soldier('black', 3, 0, self._board)
        self._board[3][2] = sol_b_2 = Soldier('black', 3, 2, self._board)
        self._board[3][4] = sol_b_3 = Soldier('black', 3, 4, self._board)
        self._board[3][6] = sol_b_4 = Soldier('black', 3, 6, self._board)
        self._board[3][8] = sol_b_5 = Soldier('black', 3, 8, self._board)
        self._board[9][4] = gen_r = General('red', 9, 4, self._board)
        self._board[9][3] = adv_r_1 = Advisor('red', 9, 3, self._board)
        self._board[9][5] = adv_r_2 = Advisor('red', 9, 5, self._board)
        self._board[9][2] = ele_r_1 = Elephant('red', 9, 2, self._board)
        self._board[9][6] = ele_r_2 = Elephant('red', 9, 6, self._board)
        self._board[9][1] = hor_r_1 = Horse('red', 9, 1, self._board)
        self._board[9][7] = hor_r_2 = Horse('red', 9, 7, self._board)
        self._board[9][0] = cha_r_1 = Chariot('red', 9, 0, self._board)
        self._board[9][8] = cha_r_2 = Chariot('red', 9, 8, self._board)
        self._board[7][1] = can_r_1 = Cannon('red', 7, 1, self._board)
        self._board[7][7] = can_r_2 = Cannon('red', 7, 7, self._board)
        self._board[6][0] = sol_r_1 = Soldier('red', 6, 0, self._board)
        self._board[6][2] = sol_r_2 = Soldier('red', 6, 2, self._board)
        self._board[6][4] = sol_r_3 = Soldier('red', 6, 4, self._board)
        self._board[6][6] = sol_r_4 = Soldier('red', 6, 6, self._board)
        self._board[6][8] = sol_r_5 = Soldier('red', 6, 8, self._board)

    def make_move(self, row_s, col_s, row_t, col_t):
        """
        takes piece in the _s position to the _t position
        :param row_s: int
        :param col_s: int
        :param row_t: int
        :param col_t: int
        :return: n/a
        """

        # XiangqiGame will check if move has piece, and if piece belongs to correct player
        self._board[row_s][col_s].make_move(row_t, col_t)

    def get_piece(self, r, c):
        """
        gives the piece at the specified row and col
        :param r: int
        :param c: int
        :return: '' or Piece
        """
        return self._board[r][c]

    def get_board(self):
        """
        gives the board
        :return: [[]]
        """
        return self._board

    def print_board(self):
        """
        prints the board
        :return: n/a
        """
        for i in range(len(self._board)-1, -1, -1):
            print(self._board[i])


class Piece:
    """
    Creates a Xiangqi piece on the board
    """

    def __init__(self, player, r, c, board):
        """
        init the Piece
        :param player: str ('red' or 'black')
        :param r: int
        :param c: int
        :param board: Board
        """
        self._player = player
        self._row = r
        self._col = c
        self._board = board

    def get_player(self):
        """
        gives the owner of the Piece
        :return: str ('red' or 'black')
        """
        return self._player

    def get_row(self):
        """
        gives the row of the Piece
        :return: int
        """
        return self._row

    def get_col(self):
        """
        gives the col of the Piece
        :return: int
        """
        return self._col

    def is_orthogonal(self, r, c):
        """
        True if move is orthogonal, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        if self.get_row() == r or self.get_col() == c:
            return True
        return False


class General(Piece):
    """
    Creates a General Piece
    """

    def __init__(self, player, r, c, board):
        """
        init the General
        :param player: str ('red' or 'black')
        :param r: int
        :param c: int
        :param board: Board
        """

        # inherits from Piece
        super().__init__(player, r, c, board)

    def _ax_from_gen(self, r, c):
        """
        True if new pos across from General, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        # red General
        if r <= 2:
            if self._board[9][c] is General or self._board[8][c] is General or self._board[9][c] is General:
                return True
        # black General
        elif self._board[0][c] is General or self._board[1][c] is General or self._board[2][c] is General:
                return True
        return False

    def _one_orthogonal(self, r, c):
        """
        True if move is one space orthogonally, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """

        # calculate magnitude of change in pos
        mag_r = abs(self.get_row()-r)
        mag_c = abs(self.get_col()-c)

        # change in r and c can't be greater than one point
        if mag_r > 1 and mag_c > 1:
            return False
        if mag_r == 1 or mag_c == 1 and self.is_orthogonal(r, c):
            return True
        return False

    def make_move(self, r, c):
        """
        moves the General to the given position
        :param r: int
        :param c: int
        :return: bool
        """
        # TODO check if move is valid
        # 1. no across from other General
        # 2. single space orthogonally
        # 3. castle only
        # 4. not in check following move
        # else return False
        # is_valid method?


class Advisor(Piece):
    """
    Creates an Advisor Piece
    """

    def __init__(self, player, r, c, board):
        """
        init the Advisor
        :param player: str ('red' or 'black')
        :param r: int
        :param c: int
        :param board: Board
        """

        # inherits from Piece
        super().__init__(player, r, c, board)

    def make_move(self, r, c):
        """
        moves the Advisor to the given position
        :param r: int
        :param c: int
        :return:
        """
        # TODO check if move is valid
        # 1. single space diagonal
        # 2. castle only
        # is_valid method?



class Elephant(Piece):
    """
    Creates an Elephant Piece
    """

    def __init__(self, player, r, c, board):
        """
        init the Elephant
        :param player: str ('red' or 'black')
        :param r: int
        :param c: int
        :param board: Board
        """

        # inherit from Piece
        super().__init__(player, r, c, board)

    def make_move(self, r, c):
        """
        moves the Elephant to the given position
        :param r: int
        :param c: int
        :return:
        """
        # TODO check if move is valid
        # 1. two points diagonally
        # 2. can't cross river
        # is_valid method?


class Horse(Piece):
    """
    Creates a Horse Piece
    """

    def __init__(self, player, r, c, board):
        """
        init the Horse
        :param player: str ('red' or 'black')
        :param r: int
        :param c: int
        :param board: Board
        """

        # inherit from Piece
        super().__init__(player, r, c, board)

    def make_move(self, r, c):
        """
        moves the Horse to the given position
        :param r: int
        :param c: int
        :return:
        """
        # TODO check if move is valid
        # 1. one point orthogonally, one point diagonally
        # 2. can be blocked
        # is_valid method?


class Chariot(Piece):
    """
    Creates a Chariot Piece
    """

    def __init__(self, player, r, c, board):
        """
        init the Chariot
        :param player: str ('red' or 'black')
        :param r: int
        :param c: int
        :param board: Board
        """

        # inherit from Piece
        super().__init__(player, r, c, board)

    def make_move(self, r, c):
        """
        moves the Chariot to the given position
        :param r: int
        :param c: int
        :return:
        """

        # TODO check if move is valid
        # 1. any point orthogonally
        # is_valid method?

        if r == self._row and c > self._col:        # move right
            for i in range(self._col, c):

        elif r == self._row and c < self._col:      # move left

        elif r < self._row and c == self._col:      # move forward
            for (i in range())
        elif r > self._row and c == self._col:      # move backward



class Cannon(Piece):
    """
    Creates a Cannon Piece
    """

    def __init__(self, player, r, c, board):
        """
        init the Cannon
        :param player: str ('red' or 'black')
        :param r: int
        :param c: int
        :param board: Board
        """

        # inherit from Piece
        super().__init__(player, r, c, board)

    def make_move(self, r, c):
        """
        moves the Cannon to the given position
        :param r: int
        :param c: int
        :return:
        """
        # TODO check if move is valid
        # 1. any point orthogonally
        # 2. needs screen to capture


class Soldier(Piece):
    """
    Creates a Soldier Piece
    """

    def __init__(self, player, r, c, board):
        """
        init the Soldier
        :param player: str ('red' or 'black')
        :param r: int
        :param c: int
        :param board: Board
        """

        # inherit from Piece
        super().__init__(player, r, c, board)

    def make_move(self, r, c):
        """
        moves the Soldier to the given position
        :param r: int
        :param c: int
        :return:
        """

        # TODO check if move is valid
        # 1. one point forward
        # 2. one point horizontal after crossing river
        # 4. never back
        # is_valid method?

        if self._player == 'black':
            if r > 4:                   # before crossing river
                if r == self._row - 1:  # vertical move
                    self._row = r
                else:
                    return False
            else:                       # after crossing river
                if r == self._row - 1:
                    self._row = r
                elif c == self._col + 1 or c == self._col - 1:      # horizontal moves
                    self._col = c
                else:
                    return False
        else:                           # self._player == 'red'
            if r < 5:                   # before crossing river
                if r == self._row + 1:  # vertical move
                    self._row = r
                else:
                    return False
            else:                       # after crossing river
                if r == self._row + 1:
                    self._row = r
                elif c == self._col + 1 or c == self._col - 1:      # horizontal moves
                    self._col = c
                else:
                    return False
