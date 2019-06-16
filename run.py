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
    #oyuncuların taşları
    player1_rocks = [player1_symbol,player1_symbol,player1_symbol]
    player2_rocks = [player2_symbol,player2_symbol,player2_symbol]
    #oyunu oynayacağımız tahta
    board = [["___", "___", "___"],
             ["___", "___", "___"],
             ["___", "___", "___"]]
    print("\n" * 5)

    show_board(board)

    sira=1
    while player2_rocks or player1_rocks:
        """if sira % 2 == 0:
            isaret = player1_symbol.center(3)
        else:
            isaret = player2_symbol.center(3)"""

        isaret = select_sign(sira, player1_symbol, player2_symbol)



        """x = input("Yukarıdan aşağıya [1, 2, 3]: ".ljust(30))
        if x == "q":
            break
        y = input("Soldan sağa [1, 2, 3]: ".ljust(30))
        if y == "q":
            break
        x=int(x)-1
        y=int(y)-1"""
        x , y = enter_location()



        if board[x][y]=="___":
            board[x][y]=isaret
            if isaret==player1_symbol.center(3):
                player1_durum+=[[x,y]]
                player1_rocks.pop()
            elif isaret == player2_symbol.center(3):
                player2_durum += [[x, y]]
                player2_rocks.pop()
            sira+=1
        else:
            print(f"{x+1},{y+1} konumu dolu")

        show_board(board)

        for i in winning_criteria:
            x = [z for z in i if z in player1_durum]
            o = [z for z in i if z in player2_durum]

            if len(o) == len(i):
                print(f"{player2_symbol} KAZANDI!")
                quit()
            if len(x) == len(i):
                print(f"{player1_symbol} KAZANDI!")
                quit()

        print(f"Son durumlar\n {player1_symbol} durumu: {player1_durum} \n {player2_symbol} durumu: {player2_durum}")


    print("Taşlar Bitti")
    #taşları oynatma blogu
    while True:

        show_board(board)

        isaret = select_sign(sira,player1_symbol,player2_symbol)

        print("İŞARET: {}\n Oynatmak istediğiniz taşın konumu giriniz".format(isaret))

        x_now, y_now = enter_location()
        """x_now = input("Yukarıdan aşağıya [1, 2, 3]: ".ljust(30))
        if x == "q":
            break
        y_now = input("Soldan sağa [1, 2, 3]: ".ljust(30))
        if y == "q":
            break
        x_now = int(x_now) - 1
        y_now = int(y_now) - 1"""


        while board[x_now][y_now] != isaret:
            if board[x_now][y_now] != isaret:
                print("Kendi taşınızı seçiniz!!")

            print("İŞARET: {}\n Oynatmak istediğiniz taşın konumu giriniz".format(isaret))

            x_now, y_now = enter_location()
            """x_now = input("Yukarıdan aşağıya [1, 2, 3]: ".ljust(30))
            if x == "q":
                break
            x_now=int(x_now)-1
            y_now = input("Soldan sağa [1, 2, 3]: ".ljust(30))
            if y == "q":
                break
            y_now=int(y_now)-1"""



        print("İŞARET: {}\n Nereye?".format(isaret))

        x_next, y_next = enter_location()

        """x_next = input("Yukarıdan aşağıya [1, 2, 3]: ".ljust(30))
        if x_next == "q":
            break
        x_next=int(x_next)-1
        y_next = input("Soldan sağa [1, 2, 3]: ".ljust(30))
        if y_next == "q":
            break
        y_next=int(y_next)-1"""

        #tahtadaki yeri boş ise
        if board[x_next][y_next]=="___":
            #yerine yerleştiriyoruz
            board[x_next][y_next]=isaret
            #tahtadaki eski yeri siliyoruz
            board[x_now][y_now]="___"
            #kim oynamış ise onun durumuna ekliyoruz
            if isaret==player1_symbol.center(3):
                player1_durum+=[[x_next,y_next]]
                player1_durum.remove([x_now,y_now])
            elif isaret == player2_symbol.center(3):
                player2_durum += [[x_next, y_next]]
                player2_durum.remove([x_now,y_now])
            sira+=1
            #print(f"Son durumlar\n {player1_symbol} durumu: {player1_durum} \n {player2_symbol} durumu: {player2_durum}")
        else:
            print(f"{x_next+1},{y_next+1} konumu dolu")

        for i in winning_criteria:
            x = [z for z in i if z in player1_durum]
            o = [z for z in i if z in player2_durum]
            if len(o) == len(i):
                print(f"{player2_symbol} KAZANDI!")
                quit()
            if len(x) == len(i):
                print(f"{player1_symbol} KAZANDI!")
                quit()

        print(f"Son durumlar\n {player1_symbol} durumu: {player1_durum} \n {player2_symbol} durumu: {player2_durum}")

def select_sign(tour,player1_symbol,player2_symbol):
    if tour % 2 == 0:
        symbol = player1_symbol.center(3)
    else:
        symbol = player2_symbol.center(3)
    print("İŞARET: {}\n".format(symbol))
    return symbol

#tahtanın son durumunu gösterme
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
    return  int(x) - 1 , int(y) - 1




player1=input("ilk oyuncu hangi simgeyi istiyor:")
player2=input("İkinci oyuncu hangi simgeyi istiyor:")

while player1==player2:
    player2=input("Simgeler farklı olmalıdır. Player 2 yeniden giriniz:")


start(player1,player2)