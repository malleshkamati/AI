import math

# Initialize the board
board = [' ' for _ in range(9)]

# printing the board
def print_board(board):
    for i in range(0, 9, 3):
        print('|'.join(board[i:i+3]))

# Function to check if a player has won the game.
def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    # Check if the player occupies all positions in any of the win conditions.
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

# Function to check if the board is full (no available moves left).
def is_full(board):
    return ' ' not in board  

# Function to get a list of available moves (indices of empty spaces).
def get_available_moves(board):
    
    return [i for i, spot in enumerate(board) if spot == ' ']

# Alpha-beta pruning algorithm for AI to choose the best move.
def alpha_beta_pruning(board, depth, is_maximizing, alpha, beta):
    
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        # Maximize the score for AI's move ('O').
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            score = alpha_beta_pruning(board, depth + 1, False, alpha, beta)
            # Undo the move (backtrack).
            board[move] = ' '
            best_score = max(score, best_score)  # Keep track of the best score.
            alpha = max(alpha, best_score)  
            if beta <= alpha:  # Prune the branch if beta is less than or equal to alpha.
                break
        return best_score
    else:
        # Minimize the score for human's move ('X').
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            score = alpha_beta_pruning(board, depth + 1, True, alpha, beta)
            board[move] = ' '  # Undo the move (backtrack).
            best_score = min(score, best_score)  # Keep track of the best score.
            beta = min(beta, best_score) 
            if beta <= alpha:  # Prune the branch if beta is less than or equal to alpha.
                break
        return best_score

# Function to determine the best move for AI using alpha-beta pruning.
def get_best_move(board):
    best_score = -math.inf  # Start with the worst possible score.
    best_move = None  # Store the best move's index.
    alpha = -math.inf  
    beta = math.inf  
    
    # Iterate over all available moves.
    for move in get_available_moves(board):
        board[move] = 'O'  # Try AI's move.
        score = alpha_beta_pruning(board, 0, False, alpha, beta)  # Call the pruning function.
        board[move] = ' '  # Undo the move (backtrack).
        if score > best_score:
            best_score = score  
            best_move = move  
    return best_move  # Return the best move index.

# Main function to play the Tic-Tac-Toe game.
def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board(board)  # Display the initial empty board.

    # Game loop continues until there is a winner or a tie.
    while True:
        # Human's turn.
        print("Your turn")    

        human_move = int(input("Enter your move (0-8): "))  

        # Ensure the move is valid (within bounds).
        while human_move >= 9 or board[human_move] != ' ':
            print("Invalid move. Try again.")
            human_move = int(input("Enter your move (0-8): "))
        
        board[human_move] = 'X'  
        print_board(board)  # Print the updated board.

        # Check if the human has won.
        if check_win(board, 'X'):
            print("You win!")
            break

        # Check if the board is full, indicating a tie.
        if is_full(board):
            print("It's a tie!")
            break

        # AI's turn.
        print("AI is making a move...")
        ai_move = get_best_move(board) 
        board[ai_move] = 'O'  # Place 'O' on the board for the AI's move.
        print_board(board) 

      
        if check_win(board, 'O'):
            print("AI wins!")
            break
   
        if is_full(board):
            print("It's a tie!")
            break

# Entry point for the program.
if __name__ == "__main__":
    play_game()  # Start the game.
