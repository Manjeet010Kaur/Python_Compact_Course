
"""The checkers game with 2 players should be created. No requirements for the graphical 
interface. Each move should be listed information about the player and the status of the board. 
Before each move player should be suggested or to move or to finish the game. 
After game finished general information about the game should be summarized and showed."""

import time


class Player:
   
    def __init__(self, name, color):
        self.name = name
        self.color = color             
        self.moves = 0                 
        self.captured = 0              
        self.result = "Not finished"
        self.time_spent = 0.0          

class Checker:

    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.is_king = False

    def symbol(self):
        return self.color.upper() if self.is_king else self.color

    def directions(self):
        if self.is_king:
            return [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        if self.color == "b":
            return [(1, -1), (1, 1)]
        return [(-1, -1), (-1, 1)]

    def move_to(self, row, col):
        self.row = row
        self.col = col

    def promote_if_needed(self, board_size):
        if not self.is_king:
            if (self.color == "b" and self.row == board_size - 1) or (
                self.color == "w" and self.row == 0
            ):
                self.is_king = True
                return True
        return False


class Board:

    def __init__(self):
        self.size = 8
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.setup()

    def setup(self):
        for row in range(3):
            for col in range(self.size):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = Checker("b", row, col)

        for row in range(5, 8):
            for col in range(self.size):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = Checker("w", row, col)

    def inside(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size

    def show(self):
        print("\n       0  1  2  3  4  5  6  7")
        print("     +------------------------+")
        for row in range(self.size):
            cells = []
            for col in range(self.size):
                piece = self.grid[row][col]
                if piece is not None:
                    cells.append(piece.symbol())
                elif (row + col) % 2 == 1:
                    cells.append(".")  # Empty playable square
                else:
                    cells.append(" ")  # Light square
            print(f"  {row}  | " + "  ".join(cells) + " |")
        print("     +------------------------+")
        print("b = Black, w = White, B/W = King, . = empty dark square")

    def pieces(self, color):
        return [
            piece
            for row in self.grid
            for piece in row
            if piece is not None and piece.color == color
        ]

    def count_pieces(self, color):
        return len(self.pieces(color))

    def simple_moves(self, piece):
        moves = []
        for dr, dc in piece.directions():
            new_row = piece.row + dr
            new_col = piece.col + dc
            if self.inside(new_row, new_col) and self.grid[new_row][new_col] is None:
                moves.append((piece.row, piece.col, new_row, new_col))
        return moves

    def captures(self, piece):
        moves = []
        for dr, dc in piece.directions():
            middle_row = piece.row + dr
            middle_col = piece.col + dc
            end_row = piece.row + 2 * dr
            end_col = piece.col + 2 * dc

            if not self.inside(end_row, end_col):
                continue

            middle_piece = self.grid[middle_row][middle_col]
            if (
                middle_piece is not None
                and middle_piece.color != piece.color
                and self.grid[end_row][end_col] is None
            ):
                moves.append((piece.row, piece.col, end_row, end_col))
        return moves

    def legal_moves(self, color):
        # Capturing is compulsory if any piece can capture.
        all_captures = []
        for piece in self.pieces(color):
            all_captures.extend(self.captures(piece))
        if all_captures:
            return all_captures

        all_moves = []
        for piece in self.pieces(color):
            all_moves.extend(self.simple_moves(piece))
        return all_moves

    def make_move(self, move):
        """Apply a validated move. Return (piece, captured, promoted)."""
        start_row, start_col, end_row, end_col = move
        piece = self.grid[start_row][start_col]
        self.grid[start_row][start_col] = None

        captured = False
        if abs(end_row - start_row) == 2:
            middle_row = (start_row + end_row) // 2
            middle_col = (start_col + end_col) // 2
            self.grid[middle_row][middle_col] = None
            captured = True

        self.grid[end_row][end_col] = piece
        piece.move_to(end_row, end_col)
        promoted = piece.promote_if_needed(self.size)
        return piece, captured, promoted


class Game:

    def __init__(self):
        self.board = Board()
        self.players = []
        self.current_player = 0
        self.total_moves = 0
        self.reason = ""
        self.start_time = None

    def setup_players(self):
        print("=== WELCOME TO CHECKERS ===")
        name1 = input("Enter Player 1 name (Black): ").strip() or "Player 1"
        name2 = input("Enter Player 2 name (White): ").strip() or "Player 2"
        self.players = [Player(name1, "b"), Player(name2, "w")]
        print("\nRules: Black starts. Move diagonally on dark squares.")
        print("Captures are compulsory; a second capture must be completed.")
        print("Reach the far end to become a King (B or W).")

    def ask_for_move(self, valid_moves):
        print("\nAvailable moves (start_row start_col end_row end_col):")
        for move in valid_moves:
            print(" ", *move)

        while True:
            entry = input("Enter 4 numbers (or 'back' to see the menu): ").strip()
            if entry.lower() == "back":
                return None

            try:
                numbers = tuple(int(number) for number in entry.split())
            except ValueError:
                print("Please enter numbers, e.g. 2 1 3 0")
                continue

            if numbers in valid_moves:
                return numbers
            print("Invalid move. Choose one of the available moves above.")

    def play_turn(self, player):
        moves = self.board.legal_moves(player.color)
        if any(abs(move[2] - move[0]) == 2 for move in moves):
            print("A capture is available, so you MUST capture.")

        first_move = self.ask_for_move(moves)
        if first_move is None:
            return False  # Return to the Move/Finish menu

        move = first_move
        while True:
            piece, captured, promoted = self.board.make_move(move)
            if captured:
                player.captured += 1

            print(f"\n{player.name} moved: {move}")
            if captured:
                print("Opponent checker captured!")
            if promoted:
                print("Your checker became a KING!")
            self.board.show()
            print(
                f"Pieces remaining: Black={self.board.count_pieces('b')}, "
                f"White={self.board.count_pieces('w')}"
            )

            # In American checkers, promotion ends the turn.
            if not captured or promoted:
                break

            more_captures = self.board.captures(piece)
            if not more_captures:
                break

            print("You must continue capturing with the SAME checker!")
            # The player cannot cancel a compulsory multi-jump.
            while True:
                next_move = self.ask_for_move(more_captures)
                if next_move is not None:
                    move = next_move
                    break
                print("You must finish the capture sequence first.")

        player.moves += 1
        self.total_moves += 1
        return True

    def start(self):
        self.setup_players()
        self.start_time = time.monotonic()

        while True:
            player = self.players[self.current_player]
            opponent = self.players[1 - self.current_player]

            if not self.board.legal_moves(player.color):
                player.result = "Lost"
                opponent.result = "Won"
                self.reason = f"{player.name} has no legal moves."
                break

            print("\n" + "=" * 42)
            self.board.show()
            print(f"Turn: {player.name} ({'Black' if player.color == 'b' else 'White'})")
            print(f"Turns played: {player.moves} | Pieces captured: {player.captured}")
            print("1. Make a move")
            print("2. Finish the game")

            turn_start = time.monotonic()
            choice = input("Choose 1 or 2: ").strip()
            if choice == "2":
                player.time_spent += time.monotonic() - turn_start
                for person in self.players:
                    person.result = "Stopped early"
                self.reason = f"{player.name} chose to finish the game."
                break
            if choice != "1":
                player.time_spent += time.monotonic() - turn_start
                print("Invalid choice. Please enter 1 or 2.")
                continue

            completed = self.play_turn(player)
            player.time_spent += time.monotonic() - turn_start
            if not completed:
                continue

            if not self.board.legal_moves(opponent.color):
                player.result = "Won"
                opponent.result = "Lost"
                self.reason = f"{opponent.name} has no legal moves."
                break

            self.current_player = 1 - self.current_player

        self.show_summary()

    def show_summary(self):
        duration = time.monotonic() - self.start_time
        print("\n" + "=" * 42)
        print("            GAME SUMMARY")
        print("=" * 42)
        print("Reason:", self.reason)
        print("Total completed turns:", self.total_moves)
        print(f"Total game time: {duration:.1f} seconds")
        for player in self.players:
            color_name = "Black" if player.color == "b" else "White"
            print(f"\nPlayer: {player.name} ({color_name})")
            print("  Result:", player.result)
            print("  Turns played:", player.moves)
            print("  Pieces captured:", player.captured)
            print("  Pieces remaining:", self.board.count_pieces(player.color))
            print(f"  Time spent on turns: {player.time_spent:.1f} seconds")
        print("\nThank you for playing!")


if __name__ == "__main__":
    game = Game()
    game.start()
