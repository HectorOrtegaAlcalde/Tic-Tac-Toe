#-------------------------------------------------------------------------------
# Name:        Tic-Tac-Toe
# Purpose:
#
# Author:      Hector
#
# Created:     24/07/2022
# Copyright:   (c) Hector 2022
# Licence:
#-------------------------------------------------------------------------------

def win(seq, char):
    i = 0
    win = False
    for i in range(3):
        if all(cell == char for cell in seq[i]) or \
        seq[0][i] == seq[1][i] == seq[2][i] == char:
            win = True
    if seq[0][0] == seq[1][1] == seq[2][2] == char or \
    seq[0][2] == seq[1][1] == seq[2][0] == char:
        win = True
    return win



print("---------")
for i in range(3):
    print("| " + " " + " " + " " + " " + " " + " |")
print("---------")

grid_seq = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

turn = 0
while True:
    if turn == 9:
        print("Draw")
        break
    else:
        while True:
            try:
                num_f, num_c = input().split(" ")
                num_f = int(num_f)
                num_c = int(num_c)
            except TypeError:
                print("You should enter numbers!")
                continue
            else:
                if num_c <= 0 or num_c > 3 or num_f <= 0 or num_f > 3:
                    print("Coordinates should be from 1 to 3!")
                    continue
                else:
                    if grid_seq[num_f - 1][num_c - 1] != " ":
                        print("This cell is occupied! Choose another one!")
                        continue
                    else:
                        break
        if turn % 2 == 0:
            grid_seq[num_f - 1][num_c - 1] = "X"
        else:
            grid_seq[num_f - 1][num_c - 1] = "O"

        print("---------")
        for i in range(len(grid_seq)):
            print("|", end = " ")
            for j in range(len(grid_seq[i])):
                    print(grid_seq[i][j], end = " ")
            print("|")
        print("---------")

        if turn % 2 == 0:
            if win(grid_seq, "X"):
                print("X wins")
                break
            else:
                turn += 1
                continue
        else:
            if win(grid_seq, "O"):
                print("O wins")
                break
            else:
                turn += 1
                continue
