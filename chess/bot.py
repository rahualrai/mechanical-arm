class ChessBoard:


    def __init__(self):
        self.board = [['.' for _ in range(8)] for _ in range(8)]
        self.turn = 'white'  # initializing the turn to white (white starts first)
        self.move_log = [] # moves log in PGN form
        
        # setting up the pieces for the starting position, uppercased pieces are white and lowercased pices are black
        self.board[7] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        self.board[6] = ['P' for _ in range(8)]
        self.board[1] = ['p' for _ in range(8)]
        self.board[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']


    def get_input(self, player):
        """prompt the player for their move input and return it as a tuple of start and end positions."""
        print(f"{player}'s turn.")
        while True:
            move_input = input("Enter your move in the format 'start_pos end_pos': ")
            try:
                start_pos, end_pos = move_input.split()
                # convert the positions to coordinates on the board
                start_pos = (8-int(start_pos[1]), ord(start_pos[0])-ord("A"))
                end_pos = (8-int(end_pos[1]), ord(end_pos[0])-ord("A"))
                return start_pos, end_pos
            except:
                print("Invalid input. Please try again. (example: B2 B4)")
    
    # def get_input(self, player):
    #     """prompt the player for their move input in PGN format and return it as a tuple of start and end positions."""
    #     print(f"{player}'s turn.")
    #     while True:
    #         move_input = input("Enter your move in PGN format: ")
    #         try:
    #             if move_input[-1] == '+':
    #                 move_input = move_input[:-1]
    #             start_pos, end_pos = move_input.split('-')
    #             start_col, start_row = ord(start_pos[0])-97, int(start_pos[1])-1
    #             end_col, end_row = ord(end_pos[0])-97, int(end_pos[1])-1
    #             return (start_row, start_col), (end_row, end_col)
    #         except:
    #             print("Invalid input. Please try again. (example: e2-e4)")


    def move(self):
        move = self.get_input(board.turn)
        print(move)
        self.board[move[1][0]][move[1][1]] = self.board[move[0][0]][move[0][1]]
        self.board[move[0][0]][move[0][1]] = "."
        
    
    def __str__(self):
        """return a string representation of the board."""
        board_str = "\n"
        for i in range(8):
            board_str += str(8-i) + "   " + " ".join(self.board[i]) + "\n"
        board_str += "\n    A B C D E F G H\n"
        
        return board_str
    





board = ChessBoard()
print(board)
board.move()
print(board)
