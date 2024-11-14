# # vraag 1
# # invoer stopt als ingegeven getal negatief is of als er 9 getallen ingegeven zijn:
# teller = 1
# maximum_getallen = 9
# getal = int(input("Geef getal: "))
#
# while getal >= 0 and teller < maximum_getallen:
#     teller += 1
#
#     getal = int(input("Geef getal: "))
#
# print(teller)

# # vraag 2
# teller = 2
# som = 0
# while teller < 5:
#     som += teller
#     teller +=1
#     print(som)
# gemiddelde = som / teller
# print(gemiddelde)


# vraag 3
# # wat wordt er afgedrukt
# i = 0
# while i < 10:
#     if i % 2 == 0:
#         print(i, end=" ")
#         i = i + 1
# ## als je 1 deelt door 2 heb je rest 1 en niet rest 0, dus je komt niet binnen de lus
# ## die komt nooit in de if en wordt nooit opgeroepen
# ## dus je kan oneindige loop hebben

# # vraag 4
# # wat wordt er afgedrukt
# i = 0
# while i > 10:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i = i + 1
# # als i = 0, gaat hij nooit in de while loop dus print hij nooit iets

# # vraag 5
# # wat is de output
# for teller in range(100, 10, -10):
#     if teller == 50:
#         teller = teller + 1
#     print(teller, end=" ")

# # vraag 6
# wat is de waarde van i en j na afloop van het programma
# i = 0
# j = 0
# while i < 10:
#     i += 1
# j += 1
# print(i, j)

# # vraag 7
# # hoeveel forloops heb je nodig om onderstaande output te bekomen
# # antwoord is 3
# for i in range(1, 4):
#     print("Titel " + str(i))
#     for j in range(1, 4):
#         for k in range(1, 6):
#             print(str(j) + "." + str(k), end=" ")
#         print()

# # # vraag 8
# # hoe vaak wordt het woord output afgedrukt
# teller1 = 1
# while teller1 <= 10:
#     teller2 = 1
#     while teller2 <= 20:
#         print("output")
#         teller2 += 1
#     teller1 += 1
# # antwoord is 200

# # vraag 9
meubel = "tafel"
for i in meubel:
    print(i, end=" ")
    # i = i + 1
    if i == "a":
        meubel = "stoel"
    print("klaar", end=" ")
