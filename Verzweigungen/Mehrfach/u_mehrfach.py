# Eingabe
print("Geben Sie ihr Bruttogehalt in Euro ein")
a = input()

# Eingabe in Zahl umwandeln
brutto = float(a)

# Berechnung des Steuersatzes
if brutto > 4000:
    steuersatz = 0.26
elif brutto > 2500:
    steuersatz = 0.22
else:
    steuersatz = 0.18

# Berechnung des Steuerbetrages
steuerbetrag = brutto * steuersatz

# Ausgabe
print("Ihr Steuergehalt ist:", steuerbetrag)
