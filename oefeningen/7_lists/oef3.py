def main():
    getallenlijst = []
    positieve_getallen = []
    # aantal_positieve_getallen = 0
    negatieve_getallen = []
    # aantal_negatieve_getallen = 0

    # strikt positief of negatief is de nul niet inbegrepen
    # als op examen vraagt voor positief getal dan is wel met 0

    for i in range(1, 6):
        getal = int(input(f"Geef een geheel getal {i} in: "))
        getallenlijst.append(getal)

    for getal in getallenlijst:
        if getal >= 0:
            positieve_getallen.append(getal)
            # aantal_positieve_getallen += 1
        else:
            negatieve_getallen.append(getal)
            # aantal_negatieve_getallen += 1

    # hoef geen variabel kan gewoon lengte van de list van positieve getal en negatieve getal

    print(str(len(positieve_getallen)) + " positieve getallen")
    print(positieve_getallen)
    for getal in positieve_getallen:
        print(getal, end=" ")
    print()
    print(str(len(negatieve_getallen)) + " negatieve getallen")
    if negatieve_getallen:
        kleinste_negatieve_getal = negatieve_getallen[0]
        for getal in negatieve_getallen:
            print(getal, end=" ")
            if getal < kleinste_negatieve_getal:
                kleinste_negatieve_getal = getal
        print()
        print(f"Het kleinste getal van de negatieve getallen is {kleinste_negatieve_getal}")
    else:
        print("Er zijn geen negatieve getallen.")

if __name__ == '__main__':
    main()
