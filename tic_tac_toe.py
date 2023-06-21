import random

board=[' ']*10
computer='x'
human='o'


def display_board(board):
    print(f"{board[1]} | {board[2]}| {board[3]}\n"
         f"{board[4]} | {board[5]}| {board[6]}\n" 
         f"{board[7]} | {board[8]}| {board[9]}\n")
    print('*'*10)

def check_win():
    if board[1]==board[2]==board[3]and board[1]!=' ':
        return True
    elif board[4]==board[5]==board[6]and board[4]!=' ':
        return True
    elif board[7]==board[8]==board[9]and board[7]!=' ':
        return True
    elif board[1]==board[4]==board[7]and board[7]!=' ':
        return True
    elif board[2]==board[5]==board[8]and board[2]!=' ':
        return True
    elif board[3]==board[6]==board[9]and board[3]!=' ':
        return True
    elif board[1]==board[5]==board[9]and board[1]!=' ':
        return True
    elif board[7]==board[5]==board[3]and board[7]!=' ':
        return True
    else:
        return False


def check_draw():
    if board.count(' ') < 2:
        return True
    else:
        return False

def is_available(pos):
    return True if board[pos]==' ' else False




def insert(letter,pos):
    if is_available(pos):
        board[pos]=letter
        display_board(board)
        if check_win():
            if letter=='x':
                print("computer wins")
                exit()
            else:
                print("player wins")
                exit()
        if check_draw():
            print("!draw!")
            exit()
    else:
        if letter =='o':
            pos=int(input("!!!! re-enter a position"))
        else:
            pos=random.randint(1,9)
        insert(letter,pos)

def human_move(letter):
    pos=int(input("Enter the position to insert:"))
    insert(letter,pos)

def computer_move(letter):
    pos=random.randint(1,9)
    insert(letter,pos)
    







while not check_win():
    display_board(board)
    computer_move(computer)
    human_move(human)

