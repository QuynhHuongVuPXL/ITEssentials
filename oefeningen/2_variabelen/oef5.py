temperatuur_in_fahrenheit = float(input("Geef de temperatuur in graden Fahrenheit in: "))
fahrenheit_naar_celsius = (temperatuur_in_fahrenheit - 32) / 1.8
print("Het aantal graden Celsius afgerond op 1 cijfer na komma is: " + str(round(fahrenheit_naar_celsius, 1)))
