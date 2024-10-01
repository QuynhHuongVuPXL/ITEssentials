VAST_BEDRAG = 10
BTW = 1.21

belgische_gesprekken = int(input("Geef het aantal Belgische gesprekken: "))
aantal_minuten_naar_buitenland = int(input("Geef het aantal minuten dat je naar het buitenland telefoneerde: "))

telefoongesprek_binnen_belgie = 0.12 * belgische_gesprekken
telefoongesprek_naar_buitenland = 0.50 * aantal_minuten_naar_buitenland

totaal_excl_btw = (VAST_BEDRAG + telefoongesprek_binnen_belgie + telefoongesprek_naar_buitenland)

totaal_incl_btw = totaal_excl_btw * BTW

print("Te betalen = " + str(totaal_incl_btw) + " euro")
