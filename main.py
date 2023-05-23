# state variables
board_size = 10
empty_space = 'O'
ship_space ='S'
hit_space = 'X'


# functions
def create_board(size):
     """Create a new game board."""
     return [[empty_space for _ in range(size)] for _ in range(size)]

def print_board(board):
    """Print the game board"""
    for row in board: 
        print(" ".join(row))

def place_ship(board, ship):
    """Place a ship on the board"""
    # for now, we'll just place the ship at a random location
    import random
    x = random.randint(0, board_size - 1)
    y = random.randint(0, board_size - 1)
    board[x][y] = ship_space

def main():
    print("Welcome to Battleship!")

    # declare ships
    # declare board
    board = create_board(board_size)
    # declare bot instance
    # bot chooses ship locations

    # for testing, we'll just place one ship
    place_ship(board, ship_space)

    print_board(board)

main()