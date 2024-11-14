def main():
    alle_cijfers = []
    for i in range(1, 6):
        student_cijfers = []
        print(f"Geef de punten voor student {i}")
        for j in range(1, 5):
            cijfer = int(input(f"Vak {j}: "))
            student_cijfers.append(cijfer)
        alle_cijfers.append(student_cijfers)

    for i in range(4):
        laagste_score = alle_cijfers[0][i]
        laagste_student = 1
        totale_score = 0

        for j in range(5):
            score = alle_cijfers[j][i]
            totale_score += score
            if score < laagste_score:
                laagste_score = score
                laagste_student = j + 1

        gemiddelde_score = totale_score / 5

        print("Vak {} Gemiddelde score: {:5.1f}   Laagste score: {:2}   behaald door student: {:2}".format(
            i + 1, gemiddelde_score, laagste_score, laagste_student))


if __name__ == '__main__':
    main()
