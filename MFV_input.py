import shelve

vocabulary = shelve.open('MFD')

def wypisz_caly_slownik():
    print("\nSŁOWNIK\n===========")
    for slowo in vocabulary:
        print(slowo, " - ", vocabulary[slowo])
    print("===========")


wypisz_caly_slownik()

while True:
    slowo_ang = input("\n Wprowadź slowo angielskie: \n")

    if slowo_ang == "quit":
        break
    elif slowo_ang in vocabulary:
        print("Już kurwa to masz zjebie!")
    else:
        slowo_polskie = input("\n Wprowadź slowo polskie: \n")
        vocabulary[slowo_ang] = slowo_polskie

vocabulary.close()