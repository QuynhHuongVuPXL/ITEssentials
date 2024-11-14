def bepaal_schrikkeljaar(jaar):
    if (jaar % 4 == 0 and  jaar % 100 != 0) or (jaar % 400 ==0):
        return True;
    else:
        return False;


def main():
    jaar = int(input("Geef het jaar in: "))

    schrikkeljaar = bepaal_schrikkeljaar(jaar)
    print("Is dit een schrikkeljaar? " + str(schrikkeljaar))

if __name__ == '__main__':
    main()