def main():
    tekst = "zonder zo'n beep in"
    tekst_tT = tekst.upper().find("T")

    if tekst_tT == -1:
        resultaat = "De gegeven tekst bevat geen t of T."
    elif len(tekst) % 2 == 0:
        resultaat = tekst[:tekst_tT + 1] + tekst[tekst_tT + 1:].lower()
    elif len(tekst) % 2 != 0:
        resultaat = tekst[:tekst_tT + 1] + tekst[tekst_tT + 1:].upper()

    print(resultaat)


if __name__ == '__main__':
    main()
