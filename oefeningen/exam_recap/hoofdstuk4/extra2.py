naam = str(input("Geef de naam van de student in: "))
while naam != "xx" and naam != "XX":
    percentage = int(input("Geef het percentage van student " + str(naam) + " in: "))

    while percentage > 100:
        print("Fout! Het getal mag maximum 100 zijn!")
        percentage = int(input("Geef het percentage van student " + str(naam) + " in: "))

    while percentage < 0:
        print("Fout! Het getal moet minstens 0 zijn!")
        percentage = int(input("Geef het percentage van student " + str(naam) + " in: "))

    if percentage < 60:
        graad = "onvoldoende"
    elif percentage < 70:
        graad = "voldoende"
    elif percentage < 80:
        graad = "onderscheiding"
    elif percentage < 85:
        graad = "grote onderscheiding"
    elif percentage >= 85:
        graad = "grootste onderschieidng"

    print("De graad van student " + str(naam) + " is " + str(graad))

    naam = str(input("Geef de naam van de student in: "))

