# # oef 1
# tekst = "dit is een regel tekst"
# print(len(tekst))


# # oef 2
# def main():
#     string = str(input("Geef een string: "))
#     for i in range(0, len(string)):
#         if string[i] in "aeiou":
#             print(f"klinker: {string[i]}, op positie {i}")
#
#
# if __name__ == '__main__':
#     main()

# # oef 3
# def main():
#     korste_woord = ""
#     woord1 = "computer"
#     woord2 = "potpu"
#
#     if len(woord1) > len(woord2):
#         korste_woord = woord2
#     else:
#         korste_woord = woord1
#
#     for i in range(0, len(korste_woord)):
#         if woord1[i] == woord2[i]:
#             print("Het karakter", woord1[i], "komt voor in beide woorden op positie", str(i))
#
#
# if __name__ == '__main__':
#     main()

# # oef 4
# def main():
#     spreuk = "   aBRAcaDAbra   "
#     print("geen spaties:", spreuk.strip(" "))
#     print("in hoofdletters:", spreuk.upper())
#     print("in kleine letters:", spreuk.lower())
#
# if __name__ == '__main__':
#     main()

# # oef 5
# def main():
#     naam = "vu"
#     voornaam = "catharina"
#
#     # resultaat = C. Vu
#
#     eerste_letter = voornaam[0].upper()
#     hoofdletter = naam[0].upper() + naam[1:]
#
#     print(f"{eerste_letter}. {hoofdletter}")
#
#
# if __name__ == '__main__':
#     main()

# # oef 6
# def main():
#     naam = "Hans"
#     lengte_naam = len(naam)
#
#     if lengte_naam % 2 != 0:
#         middelste_index = lengte_naam // 2
#         nieuwe_string  = naam[middelste_index].upper()
#     else:
#         middelste_index1 = lengte_naam // 2 - 1
#         middelste_index2 = lengte_naam // 2
#         nieuwe_string = naam[middelste_index1].upper() + naam[middelste_index2].upper()
#
#     print(naam)
#     print(nieuwe_string)
#
#
# if __name__ == '__main__':
#     main()

# # oef 7
# def main():
#     string = "Barefoot on the grass,# listening to our favorite song"
#     hashtag = string.find("#")
#
#     nieuwe_string = string[hashtag + 2:]
#     print(nieuwe_string)
#
#
# if __name__ == '__main__':
#     main()

# # oef 8
# def main():
#     spreuk = "abracadabra"
#     spreuk_o = spreuk.replace("a", "o")
#     print(spreuk_o)
#
#     aantal_o = 0
#     for letter in spreuk_o:
#         if letter == "o":
#             aantal_o += 1
#     print(aantal_o)
#
#     print(spreuk_o.count("o"))
#
#
# if __name__ == '__main__':
#     main()

# # oef 9
# def main():
#     quote = "The quick brown fox jumps over de lazy cat."
#     nieuwe_quote = quote.replace("d", "th").replace("cat", "dog")
#     print(nieuwe_quote)
#
#
# if __name__ == '__main__':
#     main()

# oef 10

def vervorm_string(string):
    # nieuwe_string = ""
    # for teken in string:
    #     if 33 <= ord(teken) <= 64:
    #         nieuwe_string += " "
    #     else:
    #         nieuwe_string += teken
    # print(nieuwe_string)

    for letter in string:
        if ord(letter) < 97 or ord(letter) > 122:
            string = string.replace(letter, " ")
    print(string)


def main():
    string = "ph@t l00t"

    vervorm_string(string)


if __name__ == '__main__':
    main()
