import shelve

def init(): # otwarcie bazy danych
    global vocabulary
    try:
        vocabulary = shelve.open('MFD')
    except:
        print("Błąd krytyczny! Baza danych nie została otwarta!")


def wypisz_caly_slownik():
    print("\nS Ł O W N I K\n=============")
    i = 1
    for slowo in sorted(vocabulary.keys()):
        print(f"{i:2}|  {slowo}  -  {vocabulary[slowo]}")
        i += 1
    # print("="*20)

def usuwanie_wyrazu():
    while True:
        wypisz_caly_slownik()
        delWord = input("\n\tWpisz słowo do usunięcia: ")
        if delWord in vocabulary:
            tlumaczenie = vocabulary[delWord]
            del vocabulary[delWord]
            print(f"Usunięto: {delWord} - {tlumaczenie}")
            kontynuacja = input("\n\tUsunąć następny wyraz? t/n: ")
            if kontynuacja == "n":
                print("\nKONIEC PROGRAMU")
                break
            elif kontynuacja == "t":
                continue
            else:
                print("\n\tWpisałeś złą literę, kontynuuję usuwanie")
                continue
        else:
            print("Nie ma takiego wyrazu, spróbuj jeszcze raz")


# główny program

init()

vocabulary["dupa"] = "osiemdziesiąt siedem dup"
vocabulary["koniec"] = "coś tam, coś tam"


usuwanie_wyrazu()

# del vocabulary["dupa"]

vocabulary.close()