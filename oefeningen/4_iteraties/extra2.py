naam = str(input("Geef de naam van de student in: "))

while naam != "xx" and naam != "XX":
    percentage = int(input(f"Geef de percentage van student {naam} in: "))

    while not percentage <= 100:
        print("Fout! Het getal mag maximum 100 zijn.")
        percentage = int(input(f"Geef de percentage van student {naam} in: "))

    while not percentage >= 0:
        print("Fout! Het getal moet minstens 0 zijn.")
        percentage = int(input(f"Geef de percentage van student {naam} in: "))

    if percentage < 60:
        graad = "onvoldoende"
    elif percentage < 70:
        graad = "voldoende"
    elif percentage < 80:
        graad = "onderscheiding"
    elif percentage < 85:
        graad = "grote onderscheiding"
    else:
        graad = "grootste onderscheiding"

    print(f"De graad van student {naam} is {graad}")

    naam = str(input("Geef de naam van de student in: "))
