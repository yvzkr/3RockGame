"""
    oyuncuların sadece 3 taş hakkı var ve bunlar tahtanın içinde döndürüyorlar

"""

winning_criteria = [[[0, 0], [1, 0], [2, 0]],
                    [[0, 1], [1, 1], [2, 1]],
                    [[0, 2], [1, 2], [2, 2]],
                    [[0, 0], [0, 1], [0, 2]],
                    [[1, 0], [1, 1], [1, 2]],
                    [[2, 0], [2, 1], [2, 2]],
                    [[0, 0], [1, 1], [2, 2]],
                    [[0, 2], [1, 1], [2, 0]]]


def start(player1_symbol, player2_symbol):
    player1_durum = []
    player2_durum = []
    # oyuncuların taşları
    player1_rocks = [player1_symbol, player1_symbol, player1_symbol]
    player2_rocks = [player2_symbol, player2_symbol, player2_symbol]
    # oyunu oynayacağımız tahta
    board = [["___", "___", "___"],
             ["___", "___", "___"],
             ["___", "___", "___"]]

    print("\n" * 5)

    show_board(board)

    sira = 1
    while player2_rocks or player1_rocks:
        isaret = select_sign(sira, player1_symbol, player2_symbol)
        x, y = enter_location()

        if board_control(board,x,y):
            board[x][y] = isaret
            if isaret == player1_symbol.center(3):
                player1_durum += [[x, y]]
                player1_rocks.pop()
            elif isaret == player2_symbol.center(3):
                player2_durum += [[x, y]]
                player2_rocks.pop()
            sira += 1
        else:
            print(f"{x + 1},{y + 1} konumu dolu")

        show_board(board)

        who_winner = winner(player1_durum, player2_durum)

        printWinner(who_winner, player1_symbol, player2_symbol)

        print(f"Son durumlar\n {player1_symbol} durumu: {player1_durum} \n {player2_symbol} durumu: {player2_durum}")

    print("Taşlar Bitti")
    # taşları oynatma blogu
    while True:
        show_board(board)
        isaret = select_sign(sira, player1_symbol, player2_symbol)
        print("İŞARET: {}\n Oynatmak istediğiniz taşın konumu giriniz".format(isaret))
        x_now, y_now = enter_location()

        while board[x_now][y_now] != isaret:
            if board[x_now][y_now] != isaret:
                print("Kendi taşınızı seçiniz!!")

            print("İŞARET: {}\n Oynatmak istediğiniz taşın konumu giriniz".format(isaret))

            x_now, y_now = enter_location()

        print("İŞARET: {}\n Nereye?".format(isaret))
        x_next, y_next = enter_location()

        # tahtadaki yeri boş iseboard_control(board,x,y)
        #if board[x_next][y_next] == "___":
        if board_control(board,x_next,y_next):
            # yerine yerleştiriyoruz
            board[x_next][y_next] = isaret
            # tahtadaki eski yeri siliyoruz
            board[x_now][y_now] = "___"
            # kim oynamış ise onun durumuna ekliyoruz
            if isaret == player1_symbol.center(3):
                player1_durum += [[x_next, y_next]]
                player1_durum.remove([x_now, y_now])
            elif isaret == player2_symbol.center(3):
                player2_durum += [[x_next, y_next]]
                player2_durum.remove([x_now, y_now])
            sira += 1
            # print(f"Son durumlar\n {player1_symbol} durumu: {player1_durum} \n {player2_symbol} durumu: {player2_durum}")
        else:
            print(f"{x_next + 1},{y_next + 1} konumu dolu")

        who_winner = winner(player1_durum, player2_durum)

        printWinner(who_winner, player1_symbol, player2_symbol)

        print(f"Son durumlar\n {player1_symbol} durumu: {player1_durum} \n {player2_symbol} durumu: {player2_durum}")


def board_control(board,x,y):
    return board[x][y] == "___"

def winner(player1_status, player2_status):
    for i in winning_criteria:
        x = [z for z in i if z in player1_status]
        o = [z for z in i if z in player2_status]
        if len(o) == len(i):
            return 2
        if len(x) == len(i):
            return 1
    return 0


def select_sign(tour, player1_symbol, player2_symbol):
    if tour % 2 == 0:
        symbol = player1_symbol.center(3)
    else:
        symbol = player2_symbol.center(3)
    print("İŞARET: {}\n".format(symbol))
    return symbol


def printWinner(player, player1_symbol, player2_symbol):
    if player == 1:
        print(f"{player1_symbol} KAZANDI!")
        quit()
    elif player == 2:
        print(f"{player2_symbol} KAZANDI!")
        quit()


# tahtanın son durumunu gösterme
def show_board(board_item):
    for i in board_item:
        print("\t".expandtabs(30), *i, end="\n" * 2)


def enter_location():
    x = input("Yukarıdan aşağıya [1, 2, 3]: ".ljust(30))
    if x == "q":
        quit()
    y = input("Soldan sağa [1, 2, 3]: ".ljust(30))
    if y == "q":
        quit()
    return int(x) - 1, int(y) - 1


# main blogu

player1 = input("ilk oyuncu hangi simgeyi istiyor:")
player2 = input("İkinci oyuncu hangi simgeyi istiyor:")

while player1 == player2:
    player2 = input("Simgeler farklı olmalıdır. Player 2 yeniden giriniz:")

start(player1, player2)
