# imports

import random
import constants


# state variables

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"x:{self.x}, y:{self.y}"

class Ship:
    def __init__(self, shipClass, hitPoints, letter):
        self.shipClass = shipClass
        self.hitPoints = hitPoints
        self.letter = letter
        self.position = []
    
    def __str__(self):
        return f"{self.shipClass}"

playerShips = []
playerHealth = 17

botShips = []
botHealth = 17


# functions

def create_board(size):
     """Create a new game board."""
     return [[constants.EMPTY_SPACE for _ in range(size)] for _ in range(size)]

def print_board(board):
    """Print the game board"""
    for row in board: 
        print(" ".join(row))

def print_boards(bot_board, player_board):
    """Print the game board"""
    print("")
    print("  A B C D E F G H I J")
    print("  *******************")

    row_num=0
    for row in bot_board: 
        print(row_num, " ".join(row))
        row_num+=1

    print("  -------------------")
    
    row_num=0
    for row in player_board: 
        print(row_num, " ".join(row))
        row_num+=1

def print_ships(ships):
    for ship in ships:
        print(ship.shipClass)
        for i in range(len(ship.position)):
            print(ship.position[i])

def place_ships(board):
    """Place a ship on the board"""
    # iterate through all ships in botShips
    for ship in botShips:
        # before placing ships ensure there is room for the ship after choosing the random coordinate
        room = False
        while room == False:
            # choose random coordinate
            x = random.randint(0, constants.BOARD_SIZE - 1)
            y = random.randint(0, constants.BOARD_SIZE - 1)

            # is there room for the ship below the coordinate?
            if x + ship.hitPoints - 1 < constants.BOARD_SIZE:
                tempX = x
                for i in range(ship.hitPoints):
                    # check if there's an existing ship here
                    if board[tempX][y] == constants.EMPTY_SPACE:
                        room = True
                    else:
                        room = False
                        break
                    tempX+=1
                if room == True:
                    tempX = x
                    # place ship
                    for i in range(ship.hitPoints):
                        board[tempX][y] = ship.letter
                        ship.position.append(Coordinate(tempX, y))
                        tempX+=1

            # is there room for the ship to the left of the coordinate?
            elif y - ship.hitPoints - 1 >= 0:
                tempY = y
                for i in range(ship.hitPoints):
                    if board[x][y] == constants.EMPTY_SPACE:
                        room = True
                    else:
                        room = False
                        break
                    tempY-=1
                if room == True:
                    tempY = y
                    for i in range(ship.hitPoints):
                        board[x][tempY] = ship.letter
                        ship.position.append(Coordinate(x, tempY))
                        tempY-=1

            # is there room for the ship above the coordinate?
            elif x - ship.hitPoints - 1 >= 0:
                tempX = x
                for i in range(ship.hitPoints):
                    if board[tempX][y] == constants.EMPTY_SPACE:
                        room = True
                    else:
                        room = False
                        break
                    tempX-=1
                if room == True:
                    tempX = x
                    for i in range(ship.hitPoints):
                        board[tempX][y] = ship.letter
                        ship.position.append(Coordinate(tempX, y))
                        tempX-=1

            # is there room for the ship to the right of the coordinate?
            elif y + ship.hitPoints - 1 < constants.BOARD_SIZE:
                tempY = y
                for i in range(ship.hitPoints):
                    if board[x][tempY] == constants.EMPTY_SPACE:
                        room = True
                    else:
                        room = False
                        break
                    y+=1
                if room == True:
                    tempY = y
                    for i in range(ship.hitPoints):
                        board[x][tempY] = ship.letter
                        ship.position.append(Coordinate(x, tempY))
                        tempY+=1

def createShips():
    playerShips.append(Ship("Carrier", 5, "A"))
    playerShips.append(Ship("Battleship", 4, "B"))
    playerShips.append(Ship("Cruiser", 3, "C"))
    playerShips.append(Ship("Submarine", 3, "S"))
    playerShips.append(Ship("Destroyer", 2, "D"))
    botShips.append(Ship("Carrier", 5, "A"))
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

    # declare bot board
    bot_board = create_board(constants.BOARD_SIZE)
    print("bot board created")

    # declare player board
    player_board = create_board(constants.BOARD_SIZE)
    guess_board = create_board(constants.BOARD_SIZE)
    print("player board created")

    # randomly generate bot ship positions
    place_ships(bot_board)
    print("randomly generated bot ship locations")
    print_ships(botShips)

    # bot chooses ship locations


    #print_board(bot_board)
    print_boards(bot_board, player_board)

main()