
# http://uoo.univ.szczecin.pl/~jakubs/py/py14.html


import shelve

def init(): # otwarcie bazy danych
    global vocabulary
    try:
        vocabulary = shelve.open('MFV')
    except:
        print("Błąd krytyczny! Baza danych nie została otwarta!")

    # print("Inicjalizacja udana. Baza danych została otwarta.")


def wyswietl_menu():
    global poz_menu
    menu = "1 - wyświetlenie słownika, 2 - szukanie, 3 - edycja, 4 - kasowanie, 9 - wyjście"
    print("=" * len(menu))
    print(menu)
    print("=" * len(menu))
    poz_menu = input("Wpisz nr menu: ")


def szukam_slowa():
    for slowo in vocabulary:
        if litery in slowo:
            print(slowo, " - ", vocabulary[slowo])

def wypisz_caly_slownik():
    print("\nS Ł O W N I K\n=============")
    i = 1
    for slowo in sorted(vocabulary.keys()):
        print(f"{i:2}|  {slowo}  -  {vocabulary[slowo]}")
        i += 1
    # print("="*20)

def nowy_wpis_lub_update():
    while True:
        wypisz_caly_slownik()
        wpis = input("\n\tWprowadź słowo - tłumaczenie ('menu' - wyjście): ")
        wpis_splited = wpis.split("-")
        slowo_ang = wpis_splited[0].strip()  # usuwanie białych znaków
        if slowo_ang.upper() == "MENU":
            break
        elif len(wpis_splited) == 1:  # sprawdzanie czy jest tłumaczenie
            continue
        else:
            tlumaczenie = wpis_splited[1].strip()
        # print(slowo_ang + "|" + tlumaczenie)

        if slowo_ang in vocabulary:
            kontynuacja = input(f"\tSłowo {slowo_ang} jest już w słowniku, nadpisać? t/n   ")
            if kontynuacja == "t":
                vocabulary[slowo_ang] = tlumaczenie
                print(slowo_ang + "-" + vocabulary[slowo_ang])
            else:
                break
        else:  # jeśli nowy wpis
            vocabulary[slowo_ang] = tlumaczenie
            print(slowo_ang + "-" + vocabulary[slowo_ang])

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
                # print("\nKoniec usuwania")
                break
            elif kontynuacja == "t":
                continue
            else:
                print("\n\tWpisałeś złą literę, kontynuuję usuwanie")
                continue
        else:
            print("Nie ma takiego wyrazu, spróbuj jeszcze raz")

# ========= PROGRAM ===========

init()

vocabulary["dupa"] = "osiemdziesiąt siedem dup"
vocabulary["koniec"] = "coś tam, coś tam"


print("\n'menu' - powrót do menu głównego")

wyswietl_menu()
while True:
    if poz_menu == "MENU":  # menu
        wyswietl_menu()

    if poz_menu == "1":  # słownik
        wypisz_caly_slownik()

    if poz_menu == "2":  # szukanie wyrazu
        while True:
            litery = input("      Wpisz fragment słowa ('menu' - wyjście): ")
            if litery.upper() == "MENU":
                break
            else:
                szukam_slowa()

    if poz_menu == "3":  # wprowadzanie słów i tłumaczenia
        nowy_wpis_lub_update()

    if poz_menu == "4":
        usuwanie_wyrazu()

    if poz_menu == "9":
        break

    poz_menu = "MENU"  # żeby menu wyświetlane w pętli było raz
vocabulary.close()