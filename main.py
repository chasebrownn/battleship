# state variables
board_size = 10
empty_space = 'O'
ship_space ='S'
hit_space = 'X'

class Ship:
    def __init__(self, shipClass, hitPoints):
        self.shipClass = shipClass
        self.hitPoints = hitPoints
        self.position = []

playerShips = []
botShips = []

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

def createShips():
    playerShips.append(Ship("Carrier", 5))
    playerShips.append(Ship("Battleship", 4))
    playerShips.append(Ship("Cruiser", 3))
    playerShips.append(Ship("Submarine", 3))
    playerShips.append(Ship("Destroyer", 2))
    botShips.append(Ship("Carrier", 5))
    botShips.append(Ship("Battleship", 4))
    botShips.append(Ship("Cruiser", 3))
    botShips.append(Ship("Submarine", 3))
    botShips.append(Ship("Destroyer", 2))

def main():
    print("Welcome to Battleship!")

    createShips()

    # declare ships
    # declare board
    board = create_board(board_size)
    # declare bot instance
    # bot chooses ship locations

    # for testing, we'll just place one ship
    place_ship(board, ship_space)

    print_board(board)

main()