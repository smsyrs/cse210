#Author: Samantha Jenkins

def main():
    print("Hello, This is a simple game of tic-tac-toe. One player is the x's and the other is the o's. Good luck, Have Fun!")
    game_play = True
    game_board = [[1, 2, 3],[4,5,6],[7,8,9]]
    turn_counter =0
    while game_play == True:
        print_game_board(game_board)
        #Even numbers starting at zero are x's
        if turn_counter % 2 == 0:
            placement = int(input("x's turn to choose a square (1-9): "))
            turn_counter+=1
            game_board=update_list(game_board,placement,"x")
        #odd numbers starting at one are o's
        else:
            placement = int(input("o's turn to choose a square (1-9): "))
            turn_counter+=1
            game_board=update_list(game_board,placement,"o")
        #determines if there was a winning play during that turn
        if turn_counter >=5:
            game_play=validate(game_board, turn_counter)

        

def print_game_board(list):
    for number in list:
        print(number)

def update_list(list, placement, player):
    #determines what column to place the move by using modulo 3 and using the remainder
    if placement %3 == 0:
        column = 2
    elif placement %3 == 1:
        column = 0
    else:
        column = 1
    
    #determines what row to place the move by the value of the choice
    if placement < 4:
        row = 0
    elif placement >3 and placement <7:
        row = 1
    else:
        row = 2
    #set row and column = to the player
    list[row][column] = player
    return list


def validate(list, turn):
    players = ["x", "o"]
    for letter in players:
        for row in range(len(list)):
            #checks hortizonally
            if list[row][0] == letter and list[row][1] == letter and list[row][2] ==letter:
                print(f"Congrats! Player {letter} has won.")
                return False
            #checks vertically
            for column in range(len(list[row])):
                if list[0][column] == letter and list[1][column]==letter and list[2][column]==letter:
                    print(f"Congrats! Player {letter} has won.")
                    return False
    #checks diagonally
    if list[0][0] == letter and list[1][1] == letter and list[2][2] == letter:
        print(f"Congrats! Player {letter} has won.")
        return False
    elif list[0][2] == letter and list[1][1] == letter and list[2][0] == letter:
        print(f"Congrats! Player {letter} has won.")
        return False

    #checks for draw
    if turn <9:
        return True
    else:
        print_game_board(list)
        print("No one wins. It's a draw!")
        return False

if __name__ == "__main__":
    main()