
import shelve

def szukam_slowa():
    for slowo in vocabulary:
        if litery in slowo:
            print(slowo, " - ", vocabulary[slowo])

def wypisz_caly_slownik():
    print("\nSŁOWNIK\n===========")
    for slowo in vocabulary:
        print(slowo, " - ", vocabulary[slowo])
    print("===========")

vocabulary = shelve.open('MFD')

# vocabulary["implicitly"] = "domyślnie"
# vocabulary["fractional part"] = "część ułamkowa"
# vocabulary["efficient"] = "wydajny"
# vocabulary["distinguish"] = "rozróżniać"

wypisz_caly_slownik()


while True:
    litery = input("\nwprowadź pierwsze litery: \n")
    if litery == "quit":
        break
    else:
        szukam_slowa()

vocabulary.close()