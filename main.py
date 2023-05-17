# state variables

class Ship:
    def __init__(self, shipClass, hitPoints):
        self.shipClass = shipClass
        self.hitPoints = hitPoints
        self.position = []

playerShips = []
botShips = []

# functions

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
    # declare bot instance
    # bot chooses ship locations

main()