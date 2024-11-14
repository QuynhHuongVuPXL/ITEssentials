aantal_rijen = int(input("Geef het aanral rijen in "))
for i in range(1, aantal_rijen + 1):
    print(str(i) + ":", end=" ")
    for j in range(1,i):
        som = i * j
        print(som, end=" ")
    print()
