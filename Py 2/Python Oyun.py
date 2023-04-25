def create_board(boardSize, player1Pieces=[], player2Pieces=[]):
    board = []
    columName = "   "
    for i in range(boardSize):
        columName += chr(ord('A') + i) + "   "
    board.append([columName])

    for i in range(boardSize):
        board.append([" "] + ["-"] * (boardSize * 4 + 1))
        row = "|"
        for j in range(boardSize):
            if str(i + 1) + chr(ord('A') + j) in player1Pieces:
                row += " " + player1 + " |"
            elif str(i + 1) + chr(ord('A') + j) in player2Pieces:
                row += " " + player2 + " |"
            else:
                row += "   |"
        board.append([str(i + 1)] + [row])
    return board


def print_board(board):
    for row in board:
        print("".join(row))
    print("".join(board[1]))
    print("".join(board[0]))


# only vertical and horizontal moves
def is_valid_move(piece, new_position, allPieces):
    if new_position in allPieces:
        return False
    else:
        if piece[0] == new_position[0]:
            # check if there is a piece between them
            if piece[1] < new_position[1]:
                for i in range(ord(piece[1]), ord(new_position[1])):
                    if str(piece[0]) + chr(i + 1) in allPieces:
                        return False
            else:
                for i in range(ord(new_position[1]), ord(piece[1])):
                    if str(piece[0]) + chr(i) in allPieces:
                        return False
            return True
        elif piece[1] == new_position[1]:
            # check if there is a piece between them
            if piece[0] < new_position[0]:
                for i in range(int(piece[0]), int(new_position[0])):
                    if str(i + 1) + new_position[1] in allPieces:
                        return False
            else:
                for i in range(int(new_position[0]), int(piece[0])):
                    if str(i) + piece[1] in allPieces:
                        return False
            return True
        else:
            return False


# move piece
def move_piece(piece, player1Pieces, player2Pieces, turn):
    newPosition = input("Oyuncu "+str(counter % 2 + 1) + " lütfen hareket ettirmek istediğiniz kendi taşınızın hedef konumunu giriniz: ").upper()
    if turn == 1:
        if is_valid_move(piece, newPosition, player1Pieces + player2Pieces):
            player1Pieces.remove(piece)
            player1Pieces.append(newPosition)
            return True
        return False
    else:
        if is_valid_move(piece, newPosition, player1Pieces + player2Pieces):
            player2Pieces.remove(piece)
            player2Pieces.append(newPosition)
            return True
        return False


# check pieces if cant move remove it
def check_pieces(attackedPlayer, defendedPlayer, boardSize):
    for piece in defendedPlayer:
        if str(int(piece[0]) + 1) + piece[1] in attackedPlayer and str(int(piece[0]) - 1) + piece[1] in attackedPlayer:
            defendedPlayer.remove(piece)
            print(piece + "Konumundaki taş kilitlendi ve dışarı çıkarıldı")
            break
        if piece[0] + chr(ord(piece[1]) + 1) in attackedPlayer and piece[0] + chr(ord(piece[1]) - 1) in attackedPlayer:
            defendedPlayer.remove(piece)
            print(piece + "Konumundaki taş kilitlendi ve dışarı çıkarıldı")
            break
        if piece == "1A":
            if "2A" in attackedPlayer and "1B" in attackedPlayer:
                defendedPlayer.remove(piece)
                print(piece + "Konumundaki taş kilitlendi ve dışarı çıkarıldı")
                break
        elif piece == "1" + chr(ord('A') + (boardSize - 1)):
            if "2" + chr(ord('A') + (boardSize - 1)) in attackedPlayer and "1" + chr(
                    ord('A') + (boardSize - 2)) in attackedPlayer:
                defendedPlayer.remove(piece)
                print(piece + "Konumundaki taş kilitlendi ve dışarı çıkarıldı")
                break
        elif piece == str(boardSize) + "A":
            if str(boardSize - 1) + "A" in attackedPlayer and str(boardSize) + "B" in attackedPlayer:
                defendedPlayer.remove(piece)
                print(piece + "Konumundaki taş kilitlendi ve dışarı çıkarıldı")
                break
        elif piece == str(boardSize) + chr(ord('A') + (boardSize - 1)):
            if str(boardSize) + chr(ord('A') + (boardSize - 2)) in attackedPlayer and str(boardSize - 1) + chr(
                    ord('A') + (boardSize - 1)) in attackedPlayer:
                defendedPlayer.remove(piece)
                print(piece + "Konumundaki taş kilitlendi ve dışarı çıkarıldı")
                break


# Get board size from user

replayGame = True
while (True):
    if replayGame == False:
        break

    boardSize = int(input("Oyun alanının satır/sütun sayısını giriniz(4-8):"))
    if boardSize < 4 or boardSize > 8:
        print("Geçersiz bir değer girdiniz.")
        continue
    player1 = input("1. oyuncuyu temsil etmek için bir karakter giriniz: ")
    player2 = input("2. oyuncuyu temsil etmek için bir karakter giriniz: ")

    player1Pieces = []
    player2Pieces = []
    for i in range(boardSize):
        # append player 1 pieces
        player1Pieces.append(str(1) + chr(ord('A') + i))
        # append player 2 pieces
        player2Pieces.append(str(boardSize) + chr(ord('A') + i))

    board = create_board(boardSize, player1Pieces, player2Pieces)
    print_board(board)
    counter = 0

    while (True):
        piece = input("Oyuncu "+str(counter % 2 + 1) + " lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu giriniz:").upper()
        if counter % 2 == 0:

            if piece in player1Pieces:
                if not move_piece(piece, player1Pieces, player2Pieces, 1):
                    print("Geçersiz hamle")
                    continue
                check_pieces(player1Pieces, player2Pieces, boardSize)
                check_pieces(player2Pieces, player1Pieces, boardSize)
            else:
                print("Geçersiz taş")
                continue
        else:
            if piece in player2Pieces:
                if not move_piece(piece, player1Pieces, player2Pieces, 2):
                    print("Geçersiz hamle")
                    continue
                check_pieces(player2Pieces, player1Pieces, boardSize)
                check_pieces(player1Pieces, player2Pieces, boardSize)
            else:
                print("Geçersiz taş")
                continue

        board = create_board(boardSize, player1Pieces, player2Pieces)
        print_board(board)
        counter += 1
        if len(player1Pieces) == 1:
            print("İkinci oyuncu oyunu kazandı.")
            break

        elif len(player2Pieces) == 1:
            print("Birinci oyuncu oyunu kazandı.")
            break
    while (True):
        replayGame = input("Tekrar oynamak ister misiniz? [e/h]: ")

        if replayGame == "e":
            replayGame = True
            break
        elif replayGame == "h":
            replayGame = False
            break
        else:
            print("Geçersiz bir değer girdiniz.")
            continue


