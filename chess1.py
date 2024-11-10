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
        if self.x == new_x and abs(self.y - new_y) in [1,2] and self.y == 2:
            return True
        elif self.x == new_x and abs(self.y - new_y) == 1:
            return True
        else:
            return False


class Knight(Piece):
    pass


class Bishop(Piece):
    pass


class Rook(Piece):
    pass


class Queen(Piece):
    pass


class King(Piece):
    pass


class Board:
    pass
