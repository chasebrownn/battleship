# state variables

class Ship:
    def __init__(self, shipClass, hitPoints):
        self.shipClass = shipClass
        self.hitPoints = hitPoints
        self.position = []

playerShips = []
botShips = []

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

def place_ships(board):
    """Place a ship on the board"""
    # for now, we'll just place the ship at a random location
    # bot places carrier
    # bot places battleship
    # bot places cruiser
    # bot places submarine
    # bot places destroyer
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
    print("***********************")

    # declare ships
    createShips()
    print("Ships created")

    # declare board
    board = create_board(board_size)
    print("board created")

    # declare bot instance
    place_ships(board)

    # bot chooses ship locations

    # for testing, we'll just place one ship

    print_board(board)

main()