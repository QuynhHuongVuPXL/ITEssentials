#
#
# regel = "Dit is een regel tekst, de lengte van deze regel is {0:5<d}, de tweede string is {1:50.2f}"
# regel2 = 12/7
# lengte = len(regel)
# print(regel.format(lengte, regel2))

# lange_string = "Deze string bevat verschillende karakters"
# print(len(lange_string))
# for i in range(0, len(lange_string)):
#     print(lange_string[i], end="")


# print("*"+"   dit is een test   \n    ".strip()+"*")
# pxl_url = "www.pxl.be"
# print(pxl_url.strip("w.be"))

woord1 = "aaaaaaaaaapootaaaaaaaaa"
print(woord1.strip("a")) # haalt begin en einde a's weg
print(woord1.upper())