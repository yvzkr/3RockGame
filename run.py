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

    board = [["___", "___", "___"],
             ["___", "___", "___"],
             ["___", "___", "___"]]

    print("\n" * 5)

    show_board(board)

    sira=1
    while True:
        if sira % 2 == 0:
            isaret = player1_symbol.center(3)
        else:
            isaret = player2_symbol.center(3)

        print("İŞARET: {}\n".format(isaret))

        x = input("yukarıdan aşağıya [1, 2, 3]: ".ljust(30))
        if x == "q":
            break
        y = input("soldan sağa [1, 2, 3]: ".ljust(30))
        if y == "q":
            break

        x=int(x)-1
        y=int(y)-1

        if board[x][y]=="___":
            board[x][y]=isaret
            if isaret==player1_symbol.center(3):
                player1_durum+=[[x,y]]
            elif isaret == player2_symbol.center(3):
                player2_durum += [[x, y]]
            sira+=1
        else:
            print(f"{x+1},{y+1} konumu dolu")

        show_board(board)


        for i in winning_criteria:
            o = [z for z in i if z in player2_durum]
            x = [z for z in i if z in player1_durum]
            if len(o) == len(i):
                print(f"{player2_symbol} KAZANDI!")
                quit()
            if len(x) == len(i):
                print(f"{player1_symbol} KAZANDI!")
                quit()

        print(f"Son durumlar\n {player1_symbol} durumu: {player1_durum} \n {player2_symbol} durumu: {player2_durum}")

def show_board(board_item):
    for i in board_item:
        print("\t".expandtabs(30), *i, end="\n" * 2)



player1=input("ilk oyuncu hangi simgeyi istiyor:")
player2=input("İkinci oyuncu hangi simgeyi istiyor:")

start(player1,player2)