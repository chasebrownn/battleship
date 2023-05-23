# imports
import random

# state variables

class Ship:
    def __init__(self, shipClass, hitPoints, letter):
        self.shipClass = shipClass
        self.hitPoints = hitPoints
        self.letter = letter
        self.position = []

playerShips = []
playerHealth = 17

botShips = []
botHealth = 17

board_size = 10
empty_space = 'O'
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
    for ship in botShips:
        room = False
        while room == False:
            x = random.randint(0, board_size - 1)
            y = random.randint(0, board_size - 1)

            if x + ship.hitPoints - 1 < board_size:
                tempX = x
                for i in range(ship.hitPoints):
                    if board[tempX][y] == empty_space:
                        room = True
                    else:
                        room = False
                        break
                    tempX+=1
                if room == True:
                    tempX = x
                    for i in range(ship.hitPoints):
                        board[tempX][y] = ship.letter
                        tempX+=1

            elif y - ship.hitPoints - 1 >= 0:
                tempY = y
                for i in range(ship.hitPoints):
                    if board[x][y] == empty_space:
                        room = True
                    else:
                        room = False
                        break
                    tempY-=1
                if room == True:
                    tempY = y
                    for i in range(ship.hitPoints):
                        board[x][tempY] = ship.letter
                        tempY-=1

            elif x - ship.hitPoints - 1 >= 0:
                tempX = x
                for i in range(ship.hitPoints):
                    if board[tempX][y] == empty_space:
                        room = True
                    else:
                        room = False
                        break
                    tempX-=1
                if room == True:
                    tempX = x
                    for i in range(ship.hitPoints):
                        board[tempX][y] = ship.letter
                        tempX-=1

            elif y + ship.hitPoints - 1 < board_size:
                tempY = y
                for i in range(ship.hitPoints):
                    if board[x][tempY] == empty_space:
                        room = True
                    else:
                        room = False
                        break
                    y+=1
                if room == True:
                    tempY = y
                    for i in range(ship.hitPoints):
                        board[x][tempY] = ship.letter
                        tempY+=1

def createShips():
    playerShips.append(Ship("Carrier", 5, "C"))
    playerShips.append(Ship("Battleship", 4, "B"))
    playerShips.append(Ship("Cruiser", 3, "C"))
    playerShips.append(Ship("Submarine", 3, "S"))
    playerShips.append(Ship("Destroyer", 2, "D"))
    botShips.append(Ship("Carrier", 5, "C"))
    botShips.append(Ship("Battleship", 4, "B"))
    botShips.append(Ship("Cruiser", 3, "C"))
    botShips.append(Ship("Submarine", 3, "S"))
    botShips.append(Ship("Destroyer", 2, "D"))

def main():
    print("Welcome to Battleship!")
    print("***********************")

    # declare ships
    createShips()
    print("Ships created")

    # declare board
    bot_board = create_board(board_size)
    print("board created")

    # declare bot instance
    place_ships(bot_board)

    # bot chooses ship locations

    # for testing, we'll just place one ship

    print_board(bot_board)

main()