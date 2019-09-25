rock = []
country = []

def collect_songs():
    song = "Укажите песню. "
    ask = "Введите p (рок) или k (кантри). Введите X для выхода. "

    while True:
        genre = input(ask)
        if genre == "X":
            break

        if genre == "p":
            rk = input(song)
            rock.append(rk)

        elif genre == ("k"):
            cy = input(song)
            country.append(cy)
        
        else:
            print("Неверно. ")
    print(rock)
    print(country)

collect_songs()