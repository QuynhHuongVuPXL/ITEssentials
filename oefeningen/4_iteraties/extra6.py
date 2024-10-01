# lengte = 6
# hoogte = 4
#
# for i in range(hoogte):
#     for j in range(lengte):
#         print("*", end=" ")
#     print()

# extra
lengte = 6
hoogte = 4

for i in range(1, hoogte + 1):
    for j in range(1, lengte + 1):
        if i == 1 or i == hoogte or j == 1 or j == lengte:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
