bedrag_in_centen = int(input("Geef het bedrag in centen in: "))

twee_euro = bedrag_in_centen // 200
rest = bedrag_in_centen % 200

een_euro = rest // 100
rest = rest % 100

vijftig_cent = rest // 50
rest = rest % 50

twintig_cent = rest // 20
rest = rest % 20

tien_cent = rest // 10
rest = rest % 10

vijf_cent = rest // 5
rest = rest % 5

twee_cent = rest // 2
rest = rest % 2

een_cent = rest // 1
rest = rest % 1

print(f"{twee_euro} van 2 EUR")
print(f"{een_euro} van 1 EUR")
print(f"{vijftig_cent} van 50 CENT")
print(f"{twintig_cent} van 20 CENT")
print(f"{tien_cent} van 10 CENT")
print(f"{vijf_cent} van 5 CENT")
print(f"{twee_cent} van 2 CENT")
print(f"{een_cent} van 1 CENT")

