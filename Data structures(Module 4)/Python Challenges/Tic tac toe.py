#Tic tac toe of Two player tic tac toe game in python

''' We will make the bard using Dict
    keys=location 
    initially will be empty space
    value will change while play'''
the_board={7:' ',8:' ',9:' ',
           4:' ',5:' ',6:' ',
           1:' ',2:' ',3:' '}
board_keys=[]
for key in the_board:
    board_keys.append(key)
def printboard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['1']+'|'+board['2']+'|'+board['3'])

def game():

    turn='X'
    count=0

    for i in range(10):
        printboard(the_board)
        print("Its your turn,",turn,".move to which place?")

        move=input()

        if the_board[move]==' ':
            the_board[move]=turn
            count+=1
        else:
            print("That place is already filled.\nMove to which place")
            continue

        if count>=5:
            if the_board['7']==the_board['8']==the_board['9'] !=' ':
                printboard(the_board)
                print("\nGame over\n")
                print("****"+turn+"won.****")
                break
            elif the_board['4']==the_board['5']==the_board['6'] !=' ':
                printboard(the_board)
                print("\nGame over\n")
                print("****"+turn+"won.****")
                break
            elif the_board['1']==the_board['2']==the_board['3'] !=' ':
                printboard(the_board)
                print("\nGame over\n")
                print("****"+turn+"won.****")
                break
            elif the_board['1']==the_board['4']==the_board['7'] !=' ':
                printboard(the_board)
                print("\nGame over\n")
                print("****"+turn+"won.****")
                break
            elif the_board['2']==the_board['5']==the_board['8'] !=' ':
                printboard(the_board)
                print("\nGame over\n")
                print("****"+turn+"won.****")
                break
            elif the_board['3']==the_board['6']==the_board['9'] !=' ':
                printboard(the_board)
                print("\nGame over\n")
                print("****"+turn+"won.****")
                break
            elif the_board['7']==the_board['5']==the_board['3'] !=' ':
                printboard(the_board)
                print("\nGame over\n")
                print("****"+turn+"won.****")
                break
            elif the_board['1']==the_board['5']==the_board['9'] !=' ':
                printboard(the_board)
                print("\nGame over\n")
                print("****"+turn+"won.****")
                break

        if count==9:
            print("\nGame over\n")
            print("Its a tie")

        if turn=='X':
            turn='O'

    restart=(input("Do you want to play again?(Y/N)"))
    if restart=='Y'or restart=='y':
        for key in board_keys:
            the_board[key]=""

        game()

if __name__=="__main__":
    game()
#end