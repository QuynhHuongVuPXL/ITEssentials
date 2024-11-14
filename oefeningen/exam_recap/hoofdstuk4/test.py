# num = 1
# while num <= 5:
#     print(num)
#     num += 1
#
# totaal = 0
# teller = 0
# while teller < 5:
#     totaal += int(input("Enter getal" + str(teller)))
#     teller += 1
# print(totaal)

# totaal = 0
# teller = 0
# getal = int(input("Geef een getal"))
# while getal != 0:
#     totaal += getal
#     teller += 1
#     getal = int(input("Geef een getal"))
#
# gemiddelde = totaal / teller
# print("totaal", totaal)
# print("gemiddelde", gemiddelde)

# totaal = 0
# for index in range(1, 6):
#     getal = int(input("Geef getal " + str(index) + ": "))
#     totaal += getal
# print(totaal)

# for i in range(3):
#     for j in range(3):
#         print(i, i)

# for i in range(3):
#     print("De buitenste loop begint met i =", i)
#     for j in range(3):
#         print("De binnenste loop begint met j =", j)
#         print("(i,j) = (" + str(i) + "," + str(j) + ")")
#         print("De binnenste loop eindigt met j =", j)
#     print("De buitenste loop eindigt met i =", i )

# for i in range(4):
#     for j in range(i + 1, 4):
#         print("(" + str(i) + "," + str(j) + ")")
#
# # opgave 4.14
# grootste_getal = 0
# deelbaar_door_drie = 0
#
# for i in range(1,11):
#     getal = int(input(f"Geef getal {i} in: "))
#     if getal > grootste_getal:
#         grootste_getal = getal
#     if getal % 3 == 0:
#         deelbaar_door_drie += 1
#
# print("Het grootste getal is:", grootste_getal)
# print("Het aantal deelbaar door drie is:", deelbaar_door_drie)


for i in range(1,11):
    getal = int(input(f"Geef getal {i} in: "))
