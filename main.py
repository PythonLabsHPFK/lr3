class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        # Перевірка рядків
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return True

        # Перевірка стовпців
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return True

        # Перевірка діагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True

        return False

    def check_draw(self):
        for row in self.board:
            if " " in row:
                return False
        return True


# Приклад використання класу TicTacToe
game = TicTacToe()

while not game.check_win() and not game.check_draw():
    game.print_board()
    row = int(input("Enter row (0, 1, or 2): "))
    col = int(input("Enter column (0, 1, or 2): "))

    if game.make_move(row, col):
        game.switch_player()
    else:
        print("Invalid move. Try again.")

game.print_board()

if game.check_win():
    print(f"Player {game.current_player} wins!")
else:
    print("It's a draw!")
