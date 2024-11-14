def bepaal_inschrijfgeld(code_student, inschrijfgeld):
    inschrijfgeld = 600
    if code_student == 3:
        inschrijfgeld *= 1.10
    elif code_student == 4 or code_student == 5:
        inschrijfgeld *= 1.30
    elif code_student == 6 or code_student == 7:
        inschrijfgeld *= 1.40
    else:
        inschrijfgeld += 45

    return int(inschrijfgeld)

def main():

    code_student = int(input("Geef code student in: "))
    inschrijfgeld = bepaal_inschrijfgeld(code_student, 600)
    print("Het inschrijfgeld voor een student met code", code_student, "is gelijk aan", inschrijfgeld)

if __name__ == '__main__':
    main()