vertrekuur = int(input("geef vetrekuur: "))
vertrekminuten = int(input("geef vetrekminuten: "))
duur = int(input("geef de duur in minuten: "))

totale_vertrekminuten = vertrekuur * 60 + vertrekminuten
totaal_aankomstminuten = totale_vertrekminuten + duur

aankomstuur = (totaal_aankomstminuten // 60) % 24
aankomstminuten = totaal_aankomstminuten % 60

print(f"je komt aan om {aankomstuur}:{aankomstminuten}u")