# In this file I will create a minesweeper game

# steps to do this

# I will need to create the game board
# Then I will need to randomly populate the board with a set of mines
# Then I will need to populate numbers within that board such that 
# if a mine is present in an ajacent square the number will reflect it
# if there are no mines that is a blank space when the user select all blank spaces and 
# number square will be revealed
# if the mine is uncovered its game over
# if all squares are uncovered and all mines are covered the player wins


import random
import os

random_number = random.randint(1, 10)

rows = 9
cols = 9 
mines = 10

board = [[0 for i in range(0,rows)] for j in range(0,cols)]
proxyBoard = [[0 for i in range(0,rows)] for j in range(0,cols)]

board_coordinates = [(x, y) for x in range(0,cols) for y in range(0, rows)]
mine_coordinates = random.sample(board_coordinates, mines)
# mine_coordinates = [(0,0),(1,0),(5,5),(0,8),(8,8),]

# print(mine_coordinates)

for i in mine_coordinates:
    mineY= i[0]
    mineX=i[1]
    if(i[0]>=0 and i[0]<8):
        board[mineY+1][mineX]+=1   
    if(i[0]>=0 and i[0]<8 and i[1]<8):
     board[mineY+1][mineX+1]+=1
    if(i[0]>=0 and i[0]<=8 and i[1]<8):
         board[mineY][mineX+1]+=1
    if(i[0]>=1 and i[0]<=8 and i[1]<8):
        board[mineY-1][mineX+1]+=1
    if(i[1]>0 and i[1]<=8):
        board[mineY-1][mineX]+=1   
    if(i[1]>0 and i[1]<=8 and i[0]>0):
        board[mineY-1][mineX-1]+=1   
    if(i[1]>0 and i[1]<=8 ):
        board[mineY][mineX-1]+=1   
    if(i[1]>0 and i[1]<=8 and i[0]<8  ):
        board[mineY+1][mineX-1]+=1   

for i in mine_coordinates:
    mineY= i[0]
    mineX=i[1]
    board[mineY][mineX]='*'

gameOver = False

while gameOver == False:

    os.system("clear")
    print('MINESWEEPER')
    print('-----------------------------------------------------------------------')
    print('\n'.join(['  '.join([str(cell) for cell in row]) for row in proxyBoard]))
    print('-----------------------------------------------------------------------')
    print("Tile move selection")
    moveTileRow = int(input('which row ?'))-1
    if(moveTileRow<0 or moveTileRow>9):
        print('invalid selection choose row value between 1-9')
        continue
    moveTileCol = int(input('which col ?'))-1
    if(moveTileCol<0 or moveTileCol>9):
        print('invalid selection choose column value between 1-9')
        continue


    if( board[moveTileRow][moveTileCol] == '*'):
        os.system("clear")
        print('GAME OVER')
        print('-----------------------------------------------------------------------')
        print('\n'.join(['  '.join([str(cell) for cell in row]) for row in board]))
        gameOver=True

    def floodfill(board, moveTileRow, moveTileCol):
         if( board[moveTileRow][moveTileCol] == 0):
            board[moveTileRow][moveTileCol] = '/'
            proxyBoard[moveTileRow][moveTileCol] = board[moveTileRow][moveTileCol]
            if moveTileRow > 0:
                floodfill(board,moveTileRow-1,moveTileCol)
            if moveTileRow < len(board[moveTileCol]) :
                floodfill(board,moveTileRow+1,moveTileCol)
            if moveTileCol > 0:
                floodfill(board,moveTileRow,moveTileCol-1)
            if moveTileCol < len(board) - 1:
                floodfill(board,moveTileRow,moveTileCol+1)

    if( board[moveTileRow][moveTileCol] == 0):
        floodfill(board, moveTileRow, moveTileCol)

    proxyBoard[moveTileRow][moveTileCol] = board[moveTileRow][moveTileCol]

   
