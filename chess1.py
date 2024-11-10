class Piece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def __repr__(self):
        return f'{self.__class__.__name__}({self.color}, {self.x}, {self.y})'


class Pawn(Piece):
    def move_forward(self, new_x, new_y):
        if self.x == new_x and abs(self.y - new_y) in [1, 2] and self.y == 1:
            return True
        elif self.x == new_x and abs(self.y - new_y) == 1:
            return True
        else:
            return False


class Knight(Piece):
    def move_in_L_shape(self, new_x, new_y):
        if abs(self.x - new_x) == 2 and abs(self.y - new_y) == 1:
            return True
        elif abs(self.x - new_x) == 1 and abs(self.y - new_y) == 2:
            return True
        else:
            return False


class Bishop(Piece):
    def move_diagonal(self, new_x, new_y):
        if abs(self.x - new_x) == abs(self.y - new_y):
            return True
        else:
            return False


class Rook(Piece):
    def move_straight(self, new_x, new_y):
        if self.x == new_x or self.y == new_y:
            return True
        else:
            return False


class Queen(Piece):
    def move_any(self, new_x, new_y):
        if self.x == new_x or self.y == new_y or abs(self.x - new_x) == abs(self.y - new_y):
            return True
        else:
            return False


class King(Piece):
    def move_one_square(self, new_x, new_y):
        if abs(self.x - new_x) <= 1 and abs(self.y - new_y) <= 1:
            return True
        else:
            return False


class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]

    def place_piece(self, piece, x, y):
        if self.grid[y][x] is None:
            self.grid[y][x] = piece
            piece.x, piece.y = x, y
        else:
            print(f"Position ({x}, {y}) is already occupied.")

    def remove_piece(self, x, y):
        if self.grid[y][x] is not None:
            self.grid[y][x] = None
        else:
            print(f"Position ({x}, {y}) is already empty.")

    def get_piece_at_position(self, x, y):
        return self.grid[y][x]

    def get_all_pieces(self):
        return [piece for row in self.grid for piece in row if piece is not None]

    def is_valid_move(self, piece, new_x, new_y):
        if not (0 <= new_x < 8 and 0 <= new_y < 8):
            return False

        if self.grid[new_y][new_x] is not None and self.grid[new_y][new_x].color == piece.color:
            return False

        if isinstance(piece, Pawn):
            return piece.move_forward(new_x, new_y)
        elif isinstance(piece, Knight):
            return piece.move_in_L_shape(new_x, new_y)
        elif isinstance(piece, Bishop):
            return piece.move_diagonal(new_x, new_y)
        elif isinstance(piece, Rook):
            return piece.move_straight(new_x, new_y)
        elif isinstance(piece, Queen):
            return piece.move_any(new_x, new_y)
        elif isinstance(piece, King):
            return piece.move_one_square(new_x, new_y)
        else:
            return False


def main():
    board = Board()

    white_pawn = Pawn("White", 1, 1)
    black_knight = Knight("Black", 1, 7)
    white_bishop = Bishop("White", 2, 0)
    black_rook = Rook("Black", 0, 7)
    white_queen = Queen("White", 3, 0)
    black_king = King("Black", 4, 7)

    board.place_piece(white_pawn, 1, 1)
    board.place_piece(black_knight, 1, 7)
    board.place_piece(white_bishop, 2, 0)
    board.place_piece(black_rook, 0, 7)
    board.place_piece(white_queen, 3, 0)
    board.place_piece(black_king, 4, 7)

    print("All pieces on the board:")
    for piece in board.get_all_pieces():
        print(piece)

    print("\nTest moves:")
    print(f"Can we move white pawn on 1,3? {board.is_valid_move(white_pawn, 1, 3)}")
    print(f"Can we move white pawn on 2,2? {board.is_valid_move(white_pawn, 2, 2)}")
    print(f"Can we move black_knight on 2,5? {board.is_valid_move(black_knight, 2, 5)}")
    print(f"Can we move white bishop on 5,3? {board.is_valid_move(white_bishop, 5, 3)}")
    print(f"Can we move black rook on 0,5? {board.is_valid_move(black_rook, 0, 5)}")
    print(f"Can we move white queen on 5,5? {board.is_valid_move(white_queen, 5, 5)}")
    print(f"Can we move black king on 6,5? {board.is_valid_move(black_king, 6, 5)}")

    board.remove_piece(1, 1)
    print("\nAfter removing white pawn:")
    for piece in board.get_all_pieces():
        print(piece)


if __name__ == '__main__':
    main()
