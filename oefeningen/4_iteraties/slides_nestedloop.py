# # oefening 4.19
# for i in range(1, 6):
#     for j in range(1, 11):
#         print(i * j, end=" ")
#     print()

# # oefening 4.20
# for i in range(5, 2, -1):
#     for j in range(2, 6, 2):
#         print(i, " ", j)

# # oefening 4.21 zonder geneste loop
# for i in range(1, 6):
#     print(i * "a ")

# oefening 4.21 met geneste loop
for i in range(1, 6):
    for j in range(1, i + 1):
        print("a", end=" ")
    print()
