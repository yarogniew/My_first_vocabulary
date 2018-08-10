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
        print(f"{i:2}|  {slowo}  -  {vocabulary[slowo]}")
        i += 1
    # print("="*20)

def tlumaczenie_zapis():
    slowo_pol = input(f"Wpisz tłumaczenie słowa '{slowo_ang}': ")
    vocabulary[slowo_ang] = slowo_pol
    print(slowo_ang + " - " + slowo_pol)

# główny program

# init()

while True:
    wpis = input("      Wprowadź słowo angielskie ('menu' - wyjście): ")
    wpis_splited = wpis.split("-")
    print(wpis_splited)
    # if slowo_ang.upper() == "MENU":
    #     break
    # elif slowo_ang in vocabulary:
    #     kontynuacja = input(f"\tSłowo {slowo_ang} jest już w słowniku, zmienić tłumaczenie? t/n   ")
    #     if kontynuacja == "t":
    #         tlumaczenie_zapis()
    # else:
    #     tlumaczenie_zapis()


vocabulary.close()