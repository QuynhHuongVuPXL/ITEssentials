# def is_dubbelwoord(woord):
#     # dehelft = int(len(woord) / 2)
#     # eerste_woord = woord[:dehelft]
#     # tweede_woord = woord[dehelft::]
#     # for letter in eerste_woord:
#     #     if letter in tweede_woord:
#     #         return True
#     #     else:
#     #         return False
#
#     # lijst = []
#     # i = 0
#     # while i < len(woord) - 1:
#     #     if woord[i] not in lijst:
#     #         index1 = woord.find(woord[i], i + 1)
#     #         if index1 == 1:
#     #             return False
#     #         else:
#     #             index2 = woord.find(woord[i], index1 + 1)
#     #             if index2 != -1:
#     #                 return False
#     #         lijst.append(woord)
#     #     i = i + 1
#     # if woord(len(woord) - 1) not in lijst:
#     #     return True
#
#
#     lijst1 = []
#     lijst2 = []
#     dehelft = int(len(woord)) / 2
#     eerste_woord = woord[:dehelft]
#     tweede_woord = woord[dehelft::]
#     for letter in eerste_woord:
#         if letter not in lijst1:
#             lijst1.append(letter)
#         else:
#             lijst2.append(letter)
#
# def main():
#     woord = str(input("Geef een woord: "))
#     result = is_dubbelwoord(woord)
#     print(result)
#
#
# if __name__ == '__main__':
#     main()


def is_dubbelwoord(woord):
    # Controleer of het woord een even aantal letters heeft
    if len(woord) % 2 != 0:
        return False

    # Splits het woord in twee helften
    dehelft = len(woord) // 2
    eerste_helft = list(woord[:dehelft])
    tweede_helft = list(woord[dehelft:])

    # Controleer of elke letter in de eerste helft voorkomt in de tweede helft
    for letter in eerste_helft:
        if letter in tweede_helft:
            tweede_helft.remove(letter)  # Verwijder de letter uit de tweede helft
        else:
            return False

    # Als de tweede helft leeg is, is het een dubbelwoord
    return len(tweede_helft) == 0

# Test de functie
print(is_dubbelwoord("couscous"))  # True
print(is_dubbelwoord("groeiregio"))  # True
print(is_dubbelwoord("abcabc"))  # True
print(is_dubbelwoord("test"))  # False
print(is_dubbelwoord("dubbel"))  # False
