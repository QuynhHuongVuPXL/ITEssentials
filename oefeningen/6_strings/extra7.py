def controleer_productcode(productcode):
    while len(productcode) != 8:
        print("Lengte moet 8 zijn")
        return False

    while not productcode[0] in "lLrR":
        print("Beginletter is niet ok")
        return False

    while not productcode[-2:] == "bo" and not productcode[-2:] == "on":
        print("Eindletters zijn niet ok")
        return False

    return True

def main():
    productcode = str(input("Geef een geldige productcode: "))

    while not controleer_productcode(productcode):
        productcode = str(input("Geef een geldige productcode: "))

    print(f"{productcode} is inderdaad een geldige productcode")

if __name__ == '__main__':
    main()

# productcode = "L12345nn"
#
# print(productcode[-2:])