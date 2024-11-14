vertrekuur = int(input("geef vertrekuur: "))
vertrekminuut = int(input("geef vertrekminuten "))
duur = int(input("geef de duur in minuten: "))

totaal_vertrek_minuten = vertrekuur * 60 + vertrekminuut
totaal_aankomst_minuten = totaal_vertrek_minuten + duur

aankomstuur = (totaal_aankomst_minuten // 60) % 24
aankomstminuten = totaal_aankomst_minuten % 60

print(f"je komt aan om {aankomstuur}:{aankomstminuten}u")