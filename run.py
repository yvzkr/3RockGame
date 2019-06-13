def start():
    x_durum =[]
    o_durum = []

    tahta = [["___", "___", "___"],
             ["___", "___", "___"],
             ["___", "___", "___"]]
    print("\n" * 5)
    kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
                         [[0, 1], [1, 1], [2, 1]],
                         [[0, 2], [1, 2], [2, 2]],
                         [[0, 0], [0, 1], [0, 2]],
                         [[1, 0], [1, 1], [1, 2]],
                         [[2, 0], [2, 1], [2, 2]],
                         [[0, 0], [1, 1], [2, 2]],
                         [[0, 2], [1, 1], [2, 0]]]
    #print(tahta)

    show_board(tahta)

    sira=1
    while True:
        print("X durumu:",x_durum,"\n Y durumu: ", o_durum,"\n")
        if sira % 2 == 0:
            isaret = "X".center(3)
        else:
            isaret = "O".center(3)

        print("İŞARET: {}\n".format(isaret))

        x = input("yukarıdan aşağıya [1, 2, 3]: ".ljust(30))
        if x == "q":
            break
        y = input("soldan sağa [1, 2, 3]: ".ljust(30))
        if y == "q":
            break


        x=int(x)-1
        y=int(y)-1


        if tahta[x][y]=="___":
            tahta[x][y]=isaret
            if isaret=="X".center(3):
                x_durum+=[[x,y]]
            elif isaret == "O".center(3):
                o_durum += [[x, y]]
            sira+=1
        else:
            print(f"{0},{1} konumu dolu",x,y)

        show_board(tahta)


        for i in kazanma_ölçütleri:
            o = [z for z in i if z in o_durum]
            x = [z for z in i if z in x_durum]
            if len(o) == len(i):
                print("O KAZANDI!")
                quit()
            if len(x) == len(i):
                print("X KAZANDI!")
                quit()

        print(f"\n son durumlar\n x durumu {x_durum} \n o durumu: {o_durum}")

def show_board(board_item):
    for i in board_item:
        print("\t".expandtabs(30), *i, end="\n" * 2)


start()