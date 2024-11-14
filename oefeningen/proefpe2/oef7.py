def bepaal_hoogste_resultaat(punten):
    # # antwoord A
    # hoogste = 0
    # for vak in range(len(punten)):
    #     for student in range(len(punten[vak])):
    #         if punten[vak][student] > hoogste:
    #             hoogste = punten[vak][student]
    # return hoogste

    # # antwoord B
    # hoogste = max(punten[0])
    # for vak in range(1, len(punten)):
    #     hoogste_in_test = max(punten[vak])
    #     if hoogste_in_test > hoogste:
    #         hoogste = hoogste_in_test
    # return hoogste

    # antwoord C
    hoogste_per_vak = []
    for vak_list in punten:
        hoogste_per_vak.append(max(vak_list))
    return max(hoogste_per_vak)

def main():
    punten = [[12, 17, 5, 13, 2, 17],
              [6, 15, 15, 10, 9, 12],
              [5, 4, 17, 19, 12, 1],
              [6, 7, 11, 17, 18, 13]]
    print("Hoogste resultaat:", bepaal_hoogste_resultaat(punten))

if __name__ == '__main__':
    main()

