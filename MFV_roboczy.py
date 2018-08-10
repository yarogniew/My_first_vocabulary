import shelve

def init(): # otwarcie bazy danych
    global vocabulary
    try:
        vocabulary = shelve.open('MFD_roboczy')
    except:
        print("Błąd krytyczny! Baza danych nie została otwarta!")


def wypisz_caly_slownik():
    print("\nS Ł O W N I K\n=============")
    i = 1
    for slowo in sorted(vocabulary.keys()):
        print(f"{i:2}|  {slowo} - {vocabulary[slowo]}")
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



# główny program

init()

# wpisywanie nowego słowa, update

nowy_wpis_lub_update()


vocabulary.close()