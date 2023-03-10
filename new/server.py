import socket

board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
                bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                       bo[2] == le and bo[5] == le and bo[8] == le) or (
                       bo[3] == le and bo[6] == le and bo[9] == le) or (
                       bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def play_game(conn):
    board = [' ' for x in range(10)]
    conn.sendall(b'Welcome to Tic Tac Toe!\n')
    conn.sendall(bytes(printBoard(board), 'utf-8'))
    player_turn = 'X'
    while not(isBoardFull(board)):
        if isWinner(board, 'O'):
            conn.sendall(b'Sorry, O\'s won this time!\n')
            break
        elif isWinner(board, 'X'):
            conn.sendall(b'X\'s won this time! Good Job!\n')
            break
        elif player_turn == 'X':
            conn.sendall(b"Please select a position to place an 'X' (1-9): ")
            player_move = int(conn.recv(1024).strip())
            if spaceIsFree(board, player_move):
                insertLetter(board, 'X', player_move)
                conn.sendall(bytes(printBoard(board), 'utf-8'))
                player_turn = 'O'
            else:
                conn.sendall(b'Sorry, this space is occupied!\n')
        elif player_turn == 'O':
            move = compMove(board)
            insertLetter(board, 'O', move)
            conn.sendall(b'Computer placed an \'O\' in position ' + str(move) + ': ')
            conn.sendall(bytes(printBoard(board), 'utf-8'))
            player_turn = 'X'
    if isBoardFull(board):
        conn.sendall(b'Tie Game!\n')
    conn.close()



def main():
    host = '127.0.0.1'
    port = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print('Waiting for connections...')
        while True:
            conn, addr = s.accept()
            print('Connected by', addr)
            play_game(conn)

if __name__ == '__main__':
    main()
