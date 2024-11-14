def main():
    voorraad = [
        [45, 102, 19, 55, 0],
        [79, 47, 58, 22, 46],
        [109, 33, 112, 0, 0]
    ]
    kleuren = ["rood", "wit", "blauw", "oranje", "zwart"]
    maten = ["Small", "Medium", "Large"]

    print("Bijbstellen:")

    for i in range(len(voorraad)):
        totaal_per_maat = 0
        for aantal in voorraad[i]:
            totaal_per_maat += aantal

        bijbestellen = totaal_per_maat / 3
        print(f"Bijbestellen {maten[i]} als voorraad < {bijbestellen}")

        for j in range(len(voorraad[i])):
            if voorraad[i][j] < bijbestellen:
                print(f"{maten[i]} {kleuren[j]}")


if __name__ == '__main__':
    main()
