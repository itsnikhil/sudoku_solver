from __future__ import print_function
import os
#file = open("output.txt","w")

# function to print the board on to a file.
# returns a string variable with the board info
def printFileBoard(board):
    string = ""
    string = string + "*********************\n"
    for x in range(0, 9):
        if x == 3 or x == 6:
            string = string + "*********************\n"
        for y in range(0, 9):
            if y == 3 or y == 6:
                string = string + " * "
            string = string + str(board[x][y]) + " "
        string = string + "\n"
    string = string + "*********************\n"
    return string

# function to print the board on to the console
def printBoard(board):
    print("*********************")
    for x in range(0, 9):
        if x == 3 or x == 6:
            print("*********************")
        for y in range(0, 9):
            if y == 3 or y == 6:
                print("*", end=" ")
            print(board[x][y], end=" ")
        print()
    print("*********************")
    
# function to check if the board is full or not
# returns true if it is full and false if it isn't
# it works on the fact that if it finds at least one 
# zero in the board it returns false
def isFull(board):
    for x in range(0, 9):
        for y in range (0, 9):
            if board[x][y] == 0:
                return False
    return True
    
# function to find all of the possible numbers
# which can be put at the specifies location by
# checking the horizontal and vertical and the 
# three by three square in which the numbers are
# housed
def possibleEntries(board, i, j):
    
    possibilityArray = {}
    
    for x in range (1, 10):
        possibilityArray[x] = 0
    
    #For horizontal entries
    for y in range (0, 9):
        if not board[i][y] == 0: 
            possibilityArray[board[i][y]] = 1
     
    #For vertical entries
    for x in range (0, 9):
        if not board[x][j] == 0: 
            possibilityArray[board[x][j]] = 1
            
    #For squares of three x three
    k = 0
    l = 0
    if i >= 0 and i <= 2:
        k = 0
    elif i >= 3 and i <= 5:
        k = 3
    else:
        k = 6
    if j >= 0 and j <= 2:
        l = 0
    elif j >= 3 and j <= 5:
        l = 3
    else:
        l = 6
    for x in range (k, k + 3):
        for y in range (l, l + 3):
            if not board[x][y] == 0:
                possibilityArray[board[x][y]] = 1          
    
    for x in range (1, 10):
        if possibilityArray[x] == 0:
            possibilityArray[x] = x
        else:
            possibilityArray[x] = 0
    
    return possibilityArray

# recursive function which solved the board and 
# prints it. 
def sudokuSolver(board):
    
    i = 0
    j = 0
    
    possiblities = {}
    
    # if board is full, there is no need to solve it any further
    if isFull(board):
        print("Board Solved Successfully!")
        printBoard(board)
        return
    else:
        # find the first vacant spot
        for x in range (0, 9):
            for y in range (0, 9):
                if board[x][y] == 0:
                    i = x
                    j = y
                    break
            else:
                continue
            break
        
        # get all the possibilities for i,j
        possiblities = possibleEntries(board, i, j)
        
        # go through all the possibilities and call the the function
        # again and again
        for x in range (1, 10):
            if not possiblities[x] == 0:
                board[i][j] = possiblities[x]
                #file.write(printFileBoard(board))
                sudokuSolver(board)
        # backtrack
        board[i][j] = 0

def main():
    SudokuBoard = [[0 for x in range(9)] for x in range(9)] 
    SudokuBoard[0][0] = os.system('python TrainAndTest.py slice_img_1_1.png')
    SudokuBoard[0][1] = os.system('python TrainAndTest.py slice_img_1_2.png')
    SudokuBoard[0][2] = os.system('python TrainAndTest.py slice_img_1_3.png')
    SudokuBoard[0][3] = os.system('python TrainAndTest.py slice_img_1_4.png')
    SudokuBoard[0][4] = os.system('python TrainAndTest.py slice_img_1_5.png')
    SudokuBoard[0][5] = os.system('python TrainAndTest.py slice_img_1_6.png')
    SudokuBoard[0][6] = os.system('python TrainAndTest.py slice_img_1_7.png')
    SudokuBoard[0][7] = os.system('python TrainAndTest.py slice_img_1_8.png')
    SudokuBoard[0][8] = os.system('python TrainAndTest.py slice_img_1_9.png')
    SudokuBoard[1][0] = os.system('python TrainAndTest.py slice_img_2_1.png')
    SudokuBoard[1][1] = os.system('python TrainAndTest.py slice_img_2_2.png')
    SudokuBoard[1][2] = os.system('python TrainAndTest.py slice_img_2_3.png')
    SudokuBoard[1][3] = os.system('python TrainAndTest.py slice_img_2_4.png')
    SudokuBoard[1][4] = os.system('python TrainAndTest.py slice_img_2_5.png')
    SudokuBoard[1][5] = os.system('python TrainAndTest.py slice_img_2_6.png')
    SudokuBoard[1][6] = os.system('python TrainAndTest.py slice_img_2_7.png')
    SudokuBoard[1][7] = os.system('python TrainAndTest.py slice_img_2_8.png')
    SudokuBoard[1][8] = os.system('python TrainAndTest.py slice_img_2_9.png')
    SudokuBoard[2][0] = os.system('python TrainAndTest.py slice_img_3_1.png')
    SudokuBoard[2][1] = os.system('python TrainAndTest.py slice_img_3_2.png')
    SudokuBoard[2][2] = os.system('python TrainAndTest.py slice_img_3_3.png')
    SudokuBoard[2][3] = os.system('python TrainAndTest.py slice_img_3_4.png')
    SudokuBoard[2][4] = os.system('python TrainAndTest.py slice_img_3_5.png')
    SudokuBoard[2][5] = os.system('python TrainAndTest.py slice_img_3_6.png')
    SudokuBoard[2][6] = os.system('python TrainAndTest.py slice_img_3_7.png')
    SudokuBoard[2][7] = os.system('python TrainAndTest.py slice_img_3_8.png')
    SudokuBoard[2][8] = os.system('python TrainAndTest.py slice_img_3_9.png')
    SudokuBoard[3][0] = os.system('python TrainAndTest.py slice_img_4_1.png')
    SudokuBoard[3][1] = os.system('python TrainAndTest.py slice_img_4_2.png')
    SudokuBoard[3][2] = os.system('python TrainAndTest.py slice_img_4_3.png')
    SudokuBoard[3][3] = os.system('python TrainAndTest.py slice_img_4_4.png')
    SudokuBoard[3][4] = os.system('python TrainAndTest.py slice_img_4_5.png')
    SudokuBoard[3][5] = os.system('python TrainAndTest.py slice_img_4_6.png')
    SudokuBoard[3][6] = os.system('python TrainAndTest.py slice_img_4_7.png')
    SudokuBoard[3][7] = os.system('python TrainAndTest.py slice_img_4_8.png')
    SudokuBoard[3][8] = os.system('python TrainAndTest.py slice_img_4_9.png')
    SudokuBoard[4][0] = os.system('python TrainAndTest.py slice_img_5_1.png')
    SudokuBoard[4][1] = os.system('python TrainAndTest.py slice_img_5_2.png')
    SudokuBoard[4][2] = os.system('python TrainAndTest.py slice_img_5_3.png')
    SudokuBoard[4][3] = os.system('python TrainAndTest.py slice_img_5_4.png')
    SudokuBoard[4][4] = os.system('python TrainAndTest.py slice_img_5_5.png')
    SudokuBoard[4][5] = os.system('python TrainAndTest.py slice_img_5_6.png')
    SudokuBoard[4][6] = os.system('python TrainAndTest.py slice_img_5_7.png')
    SudokuBoard[4][7] = os.system('python TrainAndTest.py slice_img_5_8.png')
    SudokuBoard[4][8] = os.system('python TrainAndTest.py slice_img_5_9.png')
    SudokuBoard[5][0] = os.system('python TrainAndTest.py slice_img_6_1.png')
    SudokuBoard[5][1] = os.system('python TrainAndTest.py slice_img_6_2.png')
    SudokuBoard[5][2] = os.system('python TrainAndTest.py slice_img_6_3.png')
    SudokuBoard[5][3] = os.system('python TrainAndTest.py slice_img_6_4.png')
    SudokuBoard[5][4] = os.system('python TrainAndTest.py slice_img_6_5.png')
    SudokuBoard[5][5] = os.system('python TrainAndTest.py slice_img_6_6.png')
    SudokuBoard[5][6] = os.system('python TrainAndTest.py slice_img_6_7.png')
    SudokuBoard[5][7] = os.system('python TrainAndTest.py slice_img_6_8.png')
    SudokuBoard[5][8] = os.system('python TrainAndTest.py slice_img_6_9.png')
    SudokuBoard[6][0] = os.system('python TrainAndTest.py slice_img_7_1.png')
    SudokuBoard[6][1] = os.system('python TrainAndTest.py slice_img_7_2.png')
    SudokuBoard[6][2] = os.system('python TrainAndTest.py slice_img_7_3.png')
    SudokuBoard[6][3] = os.system('python TrainAndTest.py slice_img_7_4.png')
    SudokuBoard[6][4] = os.system('python TrainAndTest.py slice_img_7_5.png')
    SudokuBoard[6][5] = os.system('python TrainAndTest.py slice_img_7_6.png')
    SudokuBoard[6][6] = os.system('python TrainAndTest.py slice_img_7_7.png')
    SudokuBoard[6][7] = os.system('python TrainAndTest.py slice_img_7_8.png')
    SudokuBoard[6][8] = os.system('python TrainAndTest.py slice_img_7_9.png')
    SudokuBoard[7][0] = os.system('python TrainAndTest.py slice_img_8_1.png')
    SudokuBoard[7][1] = os.system('python TrainAndTest.py slice_img_8_2.png')
    SudokuBoard[7][2] = os.system('python TrainAndTest.py slice_img_8_3.png')
    SudokuBoard[7][3] = os.system('python TrainAndTest.py slice_img_8_4.png')
    SudokuBoard[7][4] = os.system('python TrainAndTest.py slice_img_8_5.png')
    SudokuBoard[7][5] = os.system('python TrainAndTest.py slice_img_8_6.png')
    SudokuBoard[7][6] = os.system('python TrainAndTest.py slice_img_8_7.png')
    SudokuBoard[7][7] = os.system('python TrainAndTest.py slice_img_8_8.png')
    SudokuBoard[7][8] = os.system('python TrainAndTest.py slice_img_8_9.png')
    SudokuBoard[8][0] = os.system('python TrainAndTest.py slice_img_9_1.png')
    SudokuBoard[8][1] = os.system('python TrainAndTest.py slice_img_9_2.png')
    SudokuBoard[8][2] = os.system('python TrainAndTest.py slice_img_9_3.png')
    SudokuBoard[8][3] = os.system('python TrainAndTest.py slice_img_9_4.png')
    SudokuBoard[8][4] = os.system('python TrainAndTest.py slice_img_9_5.png')
    SudokuBoard[8][5] = os.system('python TrainAndTest.py slice_img_9_6.png')
    SudokuBoard[8][6] = os.system('python TrainAndTest.py slice_img_9_7.png')
    SudokuBoard[8][7] = os.system('python TrainAndTest.py slice_img_9_8.png')
    SudokuBoard[8][8] = os.system('python TrainAndTest.py slice_img_9_9.png')
    printBoard(SudokuBoard)
    #sudokuSolver(SudokuBoard)
    #file.close()
    
if __name__ == "__main__":
    main()