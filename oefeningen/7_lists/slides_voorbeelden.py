# fruitlist = ["appel", "banaan", "kers", "mango"]
# # print("Aantal elementen in fruitlist:", len(fruitlist))
# # for element in fruitlist:
# #     print(element)
# #     fruitlist[0] = "appelsien" # mutable
# # print(fruitlist[2])
# # print(fruitlist[0])
#
# fruitlist2 = ["peer", "kiwi"]  # je kan aan de lijst optellen
# # resultaat = fruitlist + fruitlist2 # kan overschrijven of een nieuwe maken en dan + doen
# fruitlist.append(fruitlist2)  # kan ook appenden, dan geef je nieuwe lijst = sublist
# fruitlist[len(fruitlist):1] = ["appelsientje"]  # deze plak je op het einde
#
# fruitlist.insert(0, "komkommer")  # insert methode
# fruitlist.insert(2, "komkommer")  # insert methode voorbeeld voor remove
# fruitlist.insert(4, "komkommer")  # insert methode voorbeeld voor remove
#
# fruitlist.remove("komkommer")  # daar waar het de eerste keer voorkomt, gaat het weghalen
# # remove als het niet in de list staat => dan krijg je error
#
# # index = fruitlist.index("komkommer", 2)  # geeft de index van de eerst voorkomende element
# # kan ook  ene start positie ingeven, begint pas te zoeken bij positie 2
#
# aantal_komkommer = fruitlist.count("komkommer")  # telt hoeveel keer element voorkomt in de lijst
# print(fruitlist)
# print(aantal_komkommer)
# # print(index)
#
# # numberlist = [314, 315, 642, 246, 129, 999]
# # for number in numberlist:
# #     print(number)
# # print(number[3])
#
# # # STRINGS ZIJN IMMUTABLE: kan je niet veranderen
# # # LIST ZIJN MUTABLE: kan je wel veranderen
# # naam = "aaaaaaaaaa"
# # print(naam)
# # naam = naam[:5] + "b" + naam[6:]
# # print(naam)

# def wijziglijst(mijn_list, index):
#     if index >= 0 and index < len(mijn_list):
#         mijn_list[index] = "FRUIT"
#
#
# def main():
#     fruitlijst = ["apple", "banana", "komkommer", "kiwi"]
#     te_wijzigen = 2
#     wijziglijst(fruitlijst, te_wijzigen)
#     print(fruitlijst)
#
# if __name__ == '__main__':
#     main()

def main():
    lijst = [
        ["X", "O", "X", "A"],
        [" ", " ", "O", "A"],
        [" ", " ", " ", "A"]
    ]

    print(len(lijst)) # hoeveel elementen in de lijst zitten
    print(len(lijst[0]))

    for rij in range(3):
        for kolom in range(3):
            # print("rij: " + str(rij) + " kolom: " + str(kolom) + " |", end=" ")
            print(lijst[rij][kolom], end=" ")
        print()


if __name__ == '__main__':
    main()
