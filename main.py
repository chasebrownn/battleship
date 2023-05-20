from random import randint

create_board = []
for x in range(5):
    create_board.append(("O") * 5)

def display_board(create_board):
    for row in create_board:
        print((" ".join(row)))

print("Welcome to Battleship!")
display_board(create_board)



