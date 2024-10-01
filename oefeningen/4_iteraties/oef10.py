# # pyramide normaal
# hoogte = int(input("Geef de hoogte van de driehoek in: "))
#
# for i in range(0, hoogte, 1):
#     for j in range(i + 1):
#         print("@", end=" ")
#     print()

# # pyramide inverted
hoogte = int(input("Geef de hoogte van de driehoek in: "))

for i in range(hoogte, 0, -1):
    for j in range(i):
        print("@", end=" ")
    print()
