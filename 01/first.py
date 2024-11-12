vek = input("Zadej věk: ")

try:
    vek = int(vek)

    if vek > 12 and vek < 20:
        print("Jsi teenager")
    else:
        print("Nejsi teenager")
except:
    print("Neplatná hodnota")


# TODO: make new function
